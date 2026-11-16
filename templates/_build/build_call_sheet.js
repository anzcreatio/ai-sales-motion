const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, AlignmentType } = require("docx");

const ORANGE = "FF4013", INK = "17202B", GREY = "5F6B78", TINT = "FFF1EC", RULE = "D9DCE1";
const F = "Arial";
const W = 10466; // A4 width 11906 - 2*720 margins

const r = (text, o = {}) => new TextRun({ text, font: F, size: o.size || 22, bold: o.bold, italics: o.italics, color: o.color || INK });
const p = (runs, o = {}) => new Paragraph({ children: Array.isArray(runs) ? runs : [runs], spacing: { before: o.before || 0, after: o.after ?? 60, line: o.line || 264 }, indent: o.indent, alignment: o.align, border: o.border });
const h = (num, text) => p([r(num + "  ", { bold: true, color: ORANGE, size: 24 }), r(text, { bold: true, size: 24 })], { before: 160, after: 60 });
const rule = () => new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 1 } }, spacing: { before: 60, after: 60 } });

const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const thin = { style: BorderStyle.SINGLE, size: 4, color: RULE };
function table(rows, widths, opts = {}) {
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((cells, ri) => new TableRow({
      children: cells.map((c, ci) => new TableCell({
        width: { size: widths[ci], type: WidthType.DXA },
        margins: { top: 50, bottom: 50, left: 100, right: 100 },
        shading: opts.shade && opts.shade(ri, ci) ? { type: ShadingType.CLEAR, color: "auto", fill: opts.shade(ri, ci) } : undefined,
        borders: { top: thin, bottom: thin, left: none, right: none },
        children: [p(typeof c === "string" ? [r(c)] : c, { after: 0 })],
      })),
    })),
  });
}
const quote = (lines) => new Table({
  width: { size: W, type: WidthType.DXA }, columnWidths: [W],
  rows: [new TableRow({ children: [new TableCell({
    width: { size: W, type: WidthType.DXA },
    margins: { top: 90, bottom: 90, left: 160, right: 160 },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: TINT },
    borders: { top: none, bottom: none, left: none, right: none },
    children: lines,
  })] })],
});

const children = [
  p([r("Discovery call sheet", { bold: true, size: 36 })], { after: 20 }),
  p([r("For BDRs and AEs, when no solution consultant is on the call", { color: GREY })], { after: 80 }),
  p([r("Your job: ", { bold: true }), r("find a real pain and book 30 minutes with our solution team. "), r("Ask, listen, don't pitch.", { bold: true }), r(" The call is recorded, so you don't take notes: Claude reads the transcript. "), r("AEs: ", { bold: true }), r("no BDR call yet? Same six questions, before any slides.")], { after: 80 }),

  h("0", "Start"),
  p([r("“Mind if I record this so I don't miss anything? And just so I've got it right, what's your role in this?”")]),

  h("1", "Open"),
  p([r("Cold call", { bold: true, color: ORANGE })], { after: 40 }),
  quote([
    p([r("“Most [industry] leaders we talk to say one of three things keeps coming up:")], { after: 50 }),
    p([r("One, ", { bold: true }), r("getting the full picture of a customer means asking three different teams;")], { after: 40, indent: { left: 200 } }),
    p([r("two, ", { bold: true }), r("the business moves faster than the systems, so a new product or rule takes months to go live;")], { after: 40, indent: { left: 200 } }),
    p([r("three, ", { bold: true }), r("everyone's being asked to do something with AI, but most are still working out where it pays off, or their agents never got past the pilot.")], { after: 60, indent: { left: 200 } }),
    p([r("Which of those is closest to home for you?”", { bold: true })], { after: 0 }),
  ]),
  p([r("Then stop talking.", { italics: true, color: GREY, size: 18 })], { before: 40, after: 80 }),
  p([r("They contacted us", { bold: true, color: ORANGE })], { after: 40 }),
  p([r("“Thanks for reaching out. "), r("What prompted it?", { bold: true }), r("”")]),

  h("2", "Then ask, in this order"),
  table([
    [[r("1", { bold: true, color: ORANGE })], "“Where does that get hard today?”"],
    [[r("2", { bold: true, color: ORANGE })], "“How do you handle it now? What do you use, and what has to stay?”"],
    [[r("3", { bold: true, color: ORANGE })], "“What happens if nothing changes?”"],
    [[r("4", { bold: true, color: ORANGE })], "“Is fixing it on anyone's plan? By when, and why now?”"],
    [[r("5", { bold: true, color: ORANGE })], "“Who runs that day to day, and who'd sign off a fix?”"],
    [[r("6", { bold: true, color: ORANGE })], "“If AI could take one job off the team first, which would it be?”"],
  ], [500, W - 500]),

  h("3", "Book, only if you heard all three"),
  p([r("☐ A pain in their words      ☐ Who owns it      ☐ A timeframe", { bold: true })], { after: 60 }),
  p([r("“Let's get 30 minutes with our solution team. Who should be there, and when suits?”")]),
  p([r("Not all three? Send a thank-you email and leave it in nurture.", { color: GREY })], { after: 80 }),

  rule(),
  table([
    [[r("If they…", { bold: true, color: GREY, size: 18 })], [r("Say", { bold: true, color: GREY, size: 18 })]],
    ["say “all three”", "“If you could fix only one, which would it be?”"],
    ["say “none”", "“What's taking up most of your team's time right now?”"],
    ["describe a problem with no size", "“Roughly how many people does that hit, and how often?”"],
    ["go deep, or ask “can it do X?”", "“What would you want it to do? That's exactly what our specialist will dig into. Let's get them in the room.”"],
    ["ask about price", "“That depends on what we'd solve. The session will show you that first.”"],
  ], [3400, W - 3400]),

  p([r("Never: ", { bold: true, color: ORANGE }), r("pitch, demo, quote prices, name other customers or quote their numbers, promise what it will do, or criticise their current tools.")], { before: 120 }),
  p([r("After the call: ", { bold: true }), r("save the recording or transcript to the deal and tell the AE the booked time. Not recorded? Write 3 lines: their pain in their words · who's coming · when.")], { after: 0 }),
];

const doc = new Document({
  creator: "Creatio APAC presales",
  title: "Discovery call sheet v0.4",
  styles: { default: { document: { run: { font: F, size: 22, color: INK } } } },
  sections: [{ properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 720, bottom: 720, left: 720, right: 720 } } }, children }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(process.argv[2], b); console.log("written"); });
