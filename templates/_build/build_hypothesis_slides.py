"""Build the discovery hypothesis slides on the Creatio slide template.

Usage: python build_hypothesis_slides.py <base.pptx> <out.pptx> <template|gsb|deal.json>
<base.pptx> = templates/TEMPLATE-Discovery-Slides-v0.1.pptx, or any deck whose last two slides are ours
(the original Creatio template with slide 5 duplicated once also works). Earlier slides are dropped.
<deal.json> = a deal's W1 Output 8 and Output 4, with the same keys as DATA below; "steps" is a list of
[label, cost-or-null] pairs.
"""
import json
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

ORANGE = RGBColor(0xFF, 0x40, 0x13)
TINT = RGBColor(0xFF, 0xEC, 0xE6)
INK = RGBColor(0x0A, 0x0A, 0x0A)
GREY = RGBColor(0x66, 0x66, 0x66)
RULE = RGBColor(0xD9, 0xDC, 0xE1)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Montserrat"

DATA = {
    "template": {
        "h_title": "What we see at [organisations like yours]",
        "h_sub": "Which of these are true for you, and which one costs you most?",
        "hyps": [
            "[H1: restates the BDR trigger in our words, max 12 words]",
            "[H2: a pain or task they could say no to, max 12 words]",
            "[H3: a pain or task they could say no to, max 12 words]",
            "[H4: a pain or task they could say no to, max 12 words]",
            "[H5: the expansion hypothesis, owned by another team]",
        ],
        "h5_label": "Often linked: [the other team, e.g. hardship and financial crime]",
        "p_title": "How [a routine enquiry] works today",
        "p_sub": "Where does this break for you? Tell us what we got wrong.",
        "steps": [
            ("[Step 1]", None), ("[Step 2]", None), ("[Step 3]", None),
            ("[Step 4: likely break]", "[What it costs: max 6 words]"),
            ("[Step 5]", None),
            ("[Step 6: likely break]", "[What it costs: max 6 words]"),
            ("[Step 7]", None),
        ],
    },
    "gsb": {
        "h_title": "What we see at customer-owned banks like yours",
        "h_sub": "Which of these are true for you, and which one costs you most?",
        "hyps": [
            "Routine questions still reach agents because self-service can't finish them",
            "Writing up calls takes minutes agents would rather spend with customers",
            "Agents switch between several screens to see one customer",
            "AI pilots stall in risk and architecture review",
            "Hardship and scam cases slow down when passed between teams",
        ],
        "h5_label": "Often linked: hardship and financial crime teams",
        "p_title": "How a customer enquiry gets resolved today",
        "p_sub": "Where does this break for you? Tell us what we got wrong.",
        "steps": [
            ("Call or chat arrives", None),
            ("Routed by the IVR", None),
            ("Customer identified", None),
            ("Agent finds the customer across screens", "Several screens, one customer"),
            ("Agent resolves: routine, hardship or scam?", "Routine work reaches agents"),
            ("Notes and case written up", "Minutes of after-call work"),
            ("Follow-up", None),
            ("Closed", None),
        ],
    },
}

NOTES_H = (
    "Show this at minute 2, straight after introductions. Don't read the statements out.\n"
    "Say: \"Before we ask you anything, here's what we usually see at organisations like yours. "
    "Which of these are true for you, and which one costs you most?\"\n"
    "Let them react and rank. Write their exact words in block 1 (Pick) of the discovery card. "
    "A \"no\" is as useful as a \"yes\": ask what's different for them.\n"
    "Statements come from W1 Output 8: industry observations, max 12 words, no product names, no research trail."
)
NOTES_P = (
    "Show this after they've picked their top pain (card block 2, Break).\n"
    "Say: \"This is how we think it works today. Where does it break for you? What have we got wrong?\"\n"
    "Edit the steps live if they correct you; it shows we listen and gives us their vocabulary.\n"
    "Steps come from W1 Output 4: 6 to 9 steps in their likely terms. Mark 2 or 3 likely breaks in orange.\n"
    "Track A (AI Studio): use the same slide for the task: trigger, inputs, checks, actions, systems; "
    "use the orange note for what a person must approve."
)

KEEP = {"Text 0", "TextBox 15", "Text 50"}


def strip(slide):
    for sh in list(slide.shapes):
        if sh.name not in KEEP:
            sh._element.getparent().remove(sh._element)


def set_text(shape, text):
    p = shape.text_frame.paragraphs[0]
    p.runs[0].text = text
    for r in p.runs[1:]:
        r._r.getparent().remove(r._r)


def textbox(slide, name, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def run(tf, text, size, color=INK, bold=False, first=True, align=None, space_before=0):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    if align is not None:
        p.alignment = align
    p.space_before = Pt(space_before)
    r = p.add_run()
    r.text = text
    r.font.name, r.font.size, r.font.bold = FONT, Pt(size), bold
    r.font.color.rgb = color
    return p


def shape(slide, kind, name, x, y, w, h, fill=None, line=None, line_w=1.0):
    s = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    s.name = name
    s.shadow.inherit = False
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(line_w)
    return s


def hypothesis_slide(slide, d):
    strip(slide)
    title, sub, num = (next(s for s in slide.shapes if s.name == n) for n in ("Text 0", "TextBox 15", "Text 50"))
    set_text(title, d["h_title"])
    set_text(sub, d["h_sub"])
    set_text(num, "")

    # column headers
    for label, x, w in (("True for you?", 10.05, 1.3), ("Costs most (rank)", 11.45, 1.4)):
        run(textbox(slide, f"Header {label}", x, 1.45, w, 0.3), label, 11, GREY, align=PP_ALIGN.CENTER)

    top, row_h = 1.85, 0.98
    for i, text in enumerate(d["hyps"]):
        y = top + i * row_h
        expansion = i == 4
        if i:
            line = shape(slide, MSO_SHAPE.RECTANGLE, f"Row rule {i}", 0.5, y - 0.04, 12.33, 0.01, fill=RULE)
        circle = shape(slide, MSO_SHAPE.OVAL, f"H{i+1} marker", 0.5, y + 0.2, 0.52, 0.52,
                       fill=None if expansion else ORANGE, line=ORANGE if expansion else None, line_w=2)
        tf = circle.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        run(tf, str(i + 1), 16, ORANGE if expansion else WHITE, bold=True, align=PP_ALIGN.CENTER)

        tf = textbox(slide, f"H{i+1} statement", 1.3, y + 0.06, 8.4, 0.8, anchor=MSO_ANCHOR.MIDDLE)
        if expansion:
            run(tf, d["h5_label"], 11, GREY)
            run(tf, text, 18, INK, first=False, space_before=2)
        else:
            run(tf, text, 18, INK)

        for col, x in (("true", 10.48), ("rank", 11.93)):
            shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, f"H{i+1} {col} box", x, y + 0.24, 0.44, 0.44,
                  fill=WHITE, line=RULE, line_w=1.25)

    slide.notes_slide.notes_text_frame.text = NOTES_H


def picture_slide(slide, d):
    strip(slide)
    title, sub, num = (next(s for s in slide.shapes if s.name == n) for n in ("Text 0", "TextBox 15", "Text 50"))
    set_text(title, d["p_title"])
    set_text(sub, d["p_sub"])
    set_text(num, "")

    steps = d["steps"]
    n = len(steps)
    left, width, gap = 0.5, 12.33, 0.3
    box_w = (width - gap * (n - 1)) / n
    box_y, box_h = 2.2, 1.85
    size = 14 if n <= 7 else 12

    for i, (label, cost) in enumerate(steps):
        x = left + i * (box_w + gap)
        breaks = cost is not None
        box = shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, f"Step {i+1}", x, box_y, box_w, box_h,
                    fill=TINT if breaks else RGBColor(0xF4, 0xF5, 0xF7), line=ORANGE if breaks else None, line_w=1.75)
        box.adjustments[0] = 0.08
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.1)
        tf.margin_top = Inches(0.12)
        tf.vertical_anchor = MSO_ANCHOR.TOP
        run(tf, f"{i+1:02d}", 10, ORANGE if breaks else GREY, bold=True, align=PP_ALIGN.LEFT)
        run(tf, label, size, INK, bold=breaks, first=False, align=PP_ALIGN.LEFT, space_before=4)

        if i < n - 1:
            shape(slide, MSO_SHAPE.ISOSCELES_TRIANGLE, f"Arrow {i+1}", x + box_w + gap / 2 - 0.07,
                  box_y + box_h / 2 - 0.08, 0.16, 0.14, fill=RULE).rotation = 90

        if breaks:
            run(textbox(slide, f"Break label {i+1}", x, box_y - 0.42, box_w, 0.3),
                "Breaks here?", 11, ORANGE, bold=True)
            run(textbox(slide, f"Cost {i+1}", x, box_y + box_h + 0.18, box_w, 0.9), cost, 12, INK)

    run(textbox(slide, "Legend", 0.5, 5.6, 12.3, 0.35),
        "Orange: where we expect it to break. Correct us; we'll change it as we talk.", 11, GREY)
    slide.notes_slide.notes_text_frame.text = NOTES_P


def load(key):
    if key.endswith(".json"):
        with open(key, encoding="utf-8") as f:
            d = json.load(f)
        d["steps"] = [tuple(s) for s in d["steps"]]
        return d
    return DATA[key]


def main(base, out, key):
    d = load(key)
    prs = Presentation(base)
    ids = prs.slides._sldIdLst
    for sid in list(ids)[:-2]:
        ids.remove(sid)
    hypothesis_slide(prs.slides[0], d)
    picture_slide(prs.slides[1], d)
    prs.save(out)


if __name__ == "__main__":
    main(*sys.argv[1:4])
