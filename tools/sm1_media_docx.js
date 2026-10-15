// Собирает docx «что скачать с ShkolaApp — аудио и видео» для Super Minds 1.
// Альбомный А4, одна таблица: галочка,
// урок со ссылкой на него в ShkolaApp, тип, подсказка «по какому заданию
// узнать» и имя файла для бакета classroom-media.
//   node tools/sm1_media_docx.js [выход.docx]
// Данные — tools/sm1_media.json:
//   { "rows": [ { "lesson": "Unit 6 · ДЗ 2", "link": "https://shkola.app/...",
//                 "kind": "видео" | "аудио", "what": "...", "hint": "...",
//                 "name": "sm1_u6_hw2_b3" } ] }
// Одна таблица — методист просила без разделов и без лишнего (15.10.2026).
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ExternalHyperlink,
  WidthType, ShadingType, AlignmentType, PageOrientation, HeadingLevel,
} = require('docx');

const DATA = JSON.parse(fs.readFileSync(path.join(__dirname, 'sm1_media.json'), 'utf8'));
const COLS = [420, 520, 3000, 1000, 6460, 3000];   // сумма 14400
const HEAD = ['✔', '№', 'Урок', 'Тип', 'Что это и где искать в ShkolaApp', 'Как назвать файл'];
const ICON = { 'видео': '🎬 видео', 'аудио': '🔊 аудио' };
const EXT  = { 'видео': '.mp4', 'аудио': '.mp3' };

function para(children, opts = {}) {
  return new Paragraph({
    spacing: { before: 20, after: 20 },
    alignment: opts.center ? AlignmentType.CENTER : AlignmentType.LEFT,
    children,
  });
}

function cell(children, i, opts = {}) {
  return new TableCell({
    width: { size: COLS[i], type: WidthType.DXA },
    shading: opts.head ? { type: ShadingType.CLEAR, color: 'auto', fill: 'E8EEF7' } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: Array.isArray(children[0]) ? children.map(c => para(c, opts)) : [para(children, opts)],
  });
}

const t = (text, o = {}) => new TextRun({ text, size: o.small ? 18 : 20, bold: !!o.bold, italics: !!o.it });

function lessonCell(r) {
  const lines = [[t(r.lesson, { bold: true })]];
  if (r.link) lines.push([new ExternalHyperlink({ link: r.link,
    children: [new TextRun({ text: r.link, style: 'Hyperlink', size: 16 })] })]);
  return lines;
}

function table(rows, startNo) {
  const trs = [new TableRow({ tableHeader: true,
    children: HEAD.map((h, i) => cell([t(h, { bold: true })], i, { head: true, center: i < 2 })) })];
  rows.forEach((r, k) => {
    const what = [[t(r.what)]];
    if (r.hint) what.push([t(r.hint, { small: true, it: true })]);
    trs.push(new TableRow({ children: [
      cell([t('☐')], 0, { center: true }),
      cell([t(String(startNo + k))], 1, { center: true }),
      cell(lessonCell(r), 2),
      cell([t(ICON[r.kind])], 3),
      cell(what, 4),
      cell([t(r.name + EXT[r.kind], { bold: true })], 5),
    ]}));
  });
  return new Table({ columnWidths: COLS, width: { size: 14400, type: WidthType.DXA }, rows: trs });
}

// «41 файл», а не «41 файлов»
function plural(n, one, few, many) {
  const a = Math.abs(n) % 100, b = a % 10;
  if (a > 10 && a < 20) return many;
  if (b > 1 && b < 5) return few;
  return b === 1 ? one : many;
}

const ROWS = DATA.rows;
const nVideo = ROWS.filter(r => r.kind === 'видео').length;
const nAudio = ROWS.filter(r => r.kind === 'аудио').length;
const P = (text, o = {}) => new Paragraph({ spacing: { after: 120 }, children: [t(text, o)] });

const kids = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({
    text: 'Super Minds 1 · аудио и видео — что скачать с ShkolaApp', bold: true, size: 32 })] }),
  P(`${ROWS.length} ${plural(ROWS.length, 'файл', 'файла', 'файлов')}: ${nVideo} видео и ${nAudio} аудио. `
    + 'Класть в бакет classroom-media, папка sm1/u<номер юнита>/ (Final Test — в sm1/u9/), '
    + 'имя — из последней колонки.'),
  table(ROWS, 1),
];

const doc = new Document({ sections: [{
  properties: { page: {
    size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE },
    margin: { top: 720, right: 720, bottom: 720, left: 720 },
  }},
  children: kids,
}]});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(process.argv[2] || 'SM1_аудио_видео.docx', b);
  console.log('готово,', ROWS.length, 'строк');
});
