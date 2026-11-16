"""Build the first-meeting slides (playback, solution hypothesis, solution summary) on the Creatio slide template.

Usage: python build_first_meeting_slides.py <base.pptx> <out.pptx> <slides-fm.json | sample>
<base.pptx> = templates/TEMPLATE-Discovery-Slides-v0.1.pptx (its two slides carry the Creatio template frame).
<slides-fm.json> = format in workflows/FM-First-Meeting-Prep.md. "sample" builds a fictional example.
"""
import copy
import json
import os
import sys

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_hypothesis_slides import (  # noqa: E402  (shared Creatio styling and helpers)
    KEEP, ORANGE, TINT, INK, GREY, RULE, WHITE, strip, set_text, textbox, run, shape,
)

SAMPLE = {
    "playback_title": "What we heard from you",
    "playback_sub": "Tell us what we got wrong.",
    "playback_rows": [
        ["Where it gets hard", "Enterprise customer requests pass through email and four teams before anyone owns them", "Slow answers to your largest accounts", "C"],
        ["How it's handled now", "Spreadsheets and a ticketing tool that sales can't see", "No single view of an account's open issues", "C"],
        ["If nothing changes", "Renewals at risk when service issues stay open", "Revenue from your top accounts", "P"],
        ["Why now", "A new enterprise segment target for next year", "A date to work back from", "I"],
        ["Who decides", "The VP Enterprise Sales, with IT", "Who needs to see this next", "A"],
    ],
    "hyp_title": "How we'd approach it",
    "hyp_headline": "If every enterprise request had one owner and one record, account teams could answer within a day, not a week.",
    "hyp_parts": [
        ["One record per account", "Requests, issues and renewals in one place that sales and service both see", True],
        ["Requests routed and tracked", "Each request gets an owner, a due time and an alert before it's late", True],
        ["An AI assistant for account teams", "Summarises an account's open issues before every customer call", False],
    ],
    "hyp_confirm": [
        "Is a day the right target for a first answer?",
        "Which teams handle a request today?",
        "Who would own this change?",
    ],
    "summary_title": "Your solution at a glance",
    "summary_outcome": "One owner and one record for every enterprise request, answered within a day.",
    "summary_parts": [
        ["One record per account", "Requests, issues and renewals in one place", True],
        ["Requests routed and tracked", "An owner, a due time and an alert for each", True],
        ["Rules your team can change", "Limits and routing changed without a project", True],
        ["Account team dashboard", "Open issues and renewals at a glance", False],
        ["AI assistant for account teams", "A summary of open issues before every call", False],
        ["Works with your ticketing tool", "Issues flow in from the tool you have today", False],
    ],
}

RGB_SOFT = RGBColor(0xF4, 0xF5, 0xF7)
LABEL = {"C": "You told us", "P": "We understand", "I": "We understand", "A": "We think"}


def frame(slide, title, sub):
    strip(slide)
    names = {s.name: s for s in slide.shapes}
    set_text(names["Text 0"], title)
    set_text(names["TextBox 15"], sub)
    set_text(names["Text 50"], "")


def playback_slide(slide, d):
    frame(slide, d["playback_title"], d["playback_sub"])
    cols = (("", 0.5, 2.6), ("What we heard", 3.3, 5.5), ("Why it matters for you", 9.05, 3.8))
    for label, x, w in cols:
        if label:
            run(textbox(slide, f"Header {label}", x, 1.45, w, 0.3), label, 11, GREY)

    rows = d["playback_rows"][:5]
    top = 1.85
    row_h = min(1.0, 4.9 / max(len(rows), 1))
    for i, (topic, heard, why, tag) in enumerate(rows):
        y = top + i * row_h
        shape(slide, MSO_SHAPE.RECTANGLE, f"Row rule {i}", 0.5, y, 12.33, 0.01, fill=RULE)
        run(textbox(slide, f"Topic {i+1}", 0.5, y + 0.12, 2.6, row_h - 0.2), topic, 15, INK, bold=True)

        tf = textbox(slide, f"Heard {i+1}", 3.3, y + 0.1, 5.5, row_h - 0.15)
        tag = (tag or "A").strip().upper()[:1]
        run(tf, LABEL.get(tag, "We think"), 10, ORANGE if tag == "C" else GREY, bold=True)
        run(tf, f"“{heard}”" if tag == "C" else heard, 14, INK, first=False, space_before=2)

        run(textbox(slide, f"Why {i+1}", 9.05, y + 0.12, 3.8, row_h - 0.2), why, 14, GREY)
    shape(slide, MSO_SHAPE.RECTANGLE, "Row rule end", 0.5, top + len(rows) * row_h, 12.33, 0.01, fill=RULE)


def hypothesis_slide(slide, d):
    frame(slide, d["hyp_title"], "Our starting point. We'll refine it with you.")

    box = shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, "Headline", 0.5, 1.4, 12.33, 1.05, fill=TINT)
    box.adjustments[0] = 0.08
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.3)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    run(tf, d["hyp_headline"], 20, INK, bold=True, align=PP_ALIGN.LEFT)

    parts = d["hyp_parts"][:3]
    gap = 0.3
    w = (12.33 - gap * (len(parts) - 1)) / max(len(parts), 1)
    y, h = 2.75, 2.45
    for i, (title, how, today) in enumerate(parts):
        x = 0.5 + i * (w + gap)
        card = shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, f"Part {i+1}", x, y, w, h,
                     fill=RGB_SOFT, line=None)
        card.adjustments[0] = 0.06
        run(textbox(slide, f"Part {i+1} number", x + 0.25, y + 0.22, 0.6, 0.3), f"{i+1:02d}", 11, ORANGE, bold=True)
        run(textbox(slide, f"Part {i+1} title", x + 0.25, y + 0.5, w - 0.5, 0.75), title, 17, INK, bold=True)
        run(textbox(slide, f"Part {i+1} how", x + 0.25, y + 1.2, w - 0.5, 0.75), how, 13, GREY)

        chip = shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, f"Part {i+1} status", x + 0.25, y + h - 0.5, 2.3, 0.32,
                     fill=ORANGE if today else WHITE, line=None if today else RULE, line_w=1)
        chip.adjustments[0] = 0.5
        ctf = chip.text_frame
        ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = 0
        ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
        run(ctf, "You'll see this today" if today else "Next time", 10, WHITE if today else GREY,
            bold=True, align=PP_ALIGN.CENTER)

    confirm = d.get("hyp_confirm", [])[:3]
    if confirm:
        run(textbox(slide, "Confirm label", 0.5, 5.5, 12.33, 0.3), "To confirm with you", 12, ORANGE, bold=True)
        tf = textbox(slide, "Confirm list", 0.5, 5.85, 12.33, 1.0)
        for j, q in enumerate(confirm):
            run(tf, f"{j+1}.  {q}", 14, INK, first=(j == 0), space_before=0 if j == 0 else 4)


def add_frame_slide(prs, source):
    """New slide on the same layout, carrying the template's title, subtitle and page-number shapes."""
    slide = prs.slides.add_slide(source.slide_layout)
    for ph in list(slide.placeholders):
        ph._element.getparent().remove(ph._element)
    for sh in source.shapes:
        if sh.name in KEEP:
            slide.shapes._spTree.append(copy.deepcopy(sh._element))
    return slide


def summary_slide(slide, d):
    frame(slide, d.get("summary_title", "Your solution at a glance"), d["summary_outcome"])

    parts = d["summary_parts"][:6]
    cols = 4 if len(parts) == 4 else 3
    rows = (len(parts) + cols - 1) // cols
    gap = 0.25
    w = (12.33 - gap * (cols - 1)) / cols
    h = 2.15
    top = 1.5 if rows == 2 else 2.1
    for i, (title, what, shown) in enumerate(parts):
        x = 0.5 + (i % cols) * (w + gap)
        y = top + (i // cols) * (h + gap)
        card = shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, f"Part {i+1}", x, y, w, h, fill=RGB_SOFT)
        card.adjustments[0] = 0.06

        marker = shape(slide, MSO_SHAPE.OVAL, f"Part {i+1} number", x + 0.22, y + 0.2, 0.44, 0.44, fill=ORANGE)
        tf = marker.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        run(tf, str(i + 1), 14, WHITE, bold=True, align=PP_ALIGN.CENTER)

        run(textbox(slide, f"Part {i+1} status", x + 0.8, y + 0.28, w - 1.02, 0.3),
            "Shown today" if shown else "Not yet shown", 10, ORANGE if shown else GREY,
            bold=True, align=PP_ALIGN.RIGHT)
        run(textbox(slide, f"Part {i+1} title", x + 0.22, y + 0.76, w - 0.44, 0.6), title, 16, INK, bold=True)
        run(textbox(slide, f"Part {i+1} what", x + 0.22, y + 1.4, w - 0.44, 0.6), what, 13, GREY)

    y = top + rows * h + (rows - 1) * gap + 0.22
    run(textbox(slide, "Basis", 0.5, y, 12.33, 0.3),
        d.get("summary_note", "Based on what we know so far. We'll refine it with you."), 11, GREY)


def main(base, out, key):
    if key == "sample":
        d = SAMPLE
    else:
        with open(key, encoding="utf-8") as f:
            d = json.load(f)
    prs = Presentation(base)
    ids = prs.slides._sldIdLst
    for sid in list(ids)[:-2]:
        ids.remove(sid)
    playback_slide(prs.slides[0], d)
    hypothesis_slide(prs.slides[1], d)
    prs.slides[0].notes_slide.notes_text_frame.text = (
        "Open with: \"Before we show you anything, here's what we heard. Did we get this right?\" "
        "Let them correct it; every correction is now Confirmed. 'We understand' = from a partner or research; "
        "'We think' = our assumption. Ask about those.")
    prs.slides[1].notes_slide.notes_text_frame.text = (
        "Say: \"This is our starting point, not the answer.\" Then show the parts marked 'You'll see this today' "
        "in Creatio. Ask the 'To confirm' questions at the end. Notes and sources: 01-fm-prep.md in the deal folder.")
    if d.get("summary_parts"):
        slide = add_frame_slide(prs, prs.slides[1])
        summary_slide(slide, d)
        slide.notes_slide.notes_text_frame.text = (
            "Keep this ready; show it only if they want to know more. Ask out loud: 'Which of these would you want to go "
            "deeper on?' Write down the numbers they pick and who cares about each. Those are the next session's agenda. "
            "If they said yes at the closing question, skip this slide and go to next steps.")
    prs.save(out)


if __name__ == "__main__":
    main(*sys.argv[1:4])
