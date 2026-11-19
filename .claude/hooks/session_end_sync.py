"""SessionEnd hook: share the handover and push committed work, except after a demo build.

Option B (Renzo, 16 Nov 2026). What it does when a chat closes:
  1. Skips everything if the chat was a demo build (it ran sc-demo-plan's approval_pack.py start/log/check).
     Builds stay hands-off until Renzo has read the build report; the git-push deny rule exists for them.
  2. Commits ONLY CONTEXT-HANDOVER.md and CONTEXT-HANDOVER-LOG.md in the workspace, if they changed.
  3. Pushes the workspace and apac-sc-motion: commits that already exist only. Never stages anything else,
     so another chat's half-finished work stays local.
Never fails the session: every error goes to session-end-sync.log next to this file.
Dry run: set SYNC_DRY_RUN=1 to print the git commands instead of running them.
"""
import datetime
import json
import os
import re
import socket
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PLUGIN = os.path.join(ROOT, "apac-sc-motion")
LOG = os.path.join(HERE, "session-end-sync.log")
HANDOVER = ["CONTEXT-HANDOVER.md", "CONTEXT-HANDOVER-LOG.md"]
DRY = os.environ.get("SYNC_DRY_RUN") == "1"
# A build = a command Claude actually ran (a tool_use), not text it read: skill docs mention these commands too.
BUILD_MARK = re.compile(r"approval_pack\.py\\*[\"']?\s+(start|log|check)\b")


def log(msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    if DRY:
        print(line)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def git(args, cwd, change=False):
    if DRY and change:
        log(f"[dry] git {' '.join(args)}  (in {os.path.basename(cwd)})")
        return 0, ""
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, timeout=45)
    return p.returncode, (p.stdout + p.stderr).strip()


def was_build(transcript_path):
    if not transcript_path or not os.path.isfile(transcript_path):
        return False
    try:
        with open(transcript_path, encoding="utf-8", errors="ignore") as f:
            for line in f:
                if "approval_pack" not in line:
                    continue
                try:
                    content = (json.loads(line).get("message") or {}).get("content")
                except ValueError:
                    continue
                for item in content if isinstance(content, list) else []:
                    if isinstance(item, dict) and item.get("type") == "tool_use":
                        if BUILD_MARK.search(json.dumps(item.get("input") or {})):
                            return True
    except OSError:
        return False
    return False


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    sid = (data.get("session_id") or "?")[:8]
    if was_build(data.get("transcript_path")):
        log(f"session {sid}: demo build session, nothing committed or pushed")
        return
    if not os.path.isdir(os.path.join(ROOT, ".git")):
        log(f"session {sid}: {ROOT} is not a git repo, skipped")
        return

    rc, out = git(["status", "--porcelain", "--", *HANDOVER], ROOT)
    if rc == 0 and out:
        git(["add", "--", *HANDOVER], ROOT, change=True)
        msg = f"Handover update (end of session {sid}, {socket.gethostname()})"
        rc, out = git(["commit", "-q", "-m", msg, "--", *HANDOVER], ROOT, change=True)
        log(f"session {sid}: handover commit {'ok' if rc == 0 else 'FAILED: ' + out}")

    for name, path in (("workspace", ROOT), ("apac-sc-motion", PLUGIN)):
        if not os.path.isdir(os.path.join(path, ".git")):
            continue
        rc, ahead = git(["rev-list", "--count", "@{u}..HEAD"], path)
        if rc != 0 or ahead.strip() in ("", "0"):
            log(f"session {sid}: {name} nothing to push" + ("" if rc == 0 else f" ({ahead})"))
            continue
        rc, out = git(["push", "-q", "--follow-tags"], path, change=True)
        log(f"session {sid}: {name} push {'ok' if rc == 0 else 'FAILED: ' + out}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # never break the session
        log(f"error: {e!r}")
    sys.exit(0)
