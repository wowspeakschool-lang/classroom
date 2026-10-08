// Собирает docx «что скачать с ShkolaApp — аудио и видео» для Super Minds 1.
// Форма — как у файла SM3: альбомный А4, по таблице на раздел, галочка,
// урок со ссылкой на него в ShkolaApp, тип, подсказка «по какому заданию
// узнать» и имя файла для бакета classroom-media.
//   node tools/sm1_media_docx.js [выход.docx]
// Данные — tools/sm1_media.json:
//   { "sections": [ { "title": "Unit 6 · My house", "note": "...",
//       "rows": [ { "lesson": "ДЗ 2", "link": "https://shkola.app/...",
//                   "kind": "видео" | "аудио", "what": "...", "hint": "...",
//                   "name": "sm1_u6_hw2_b3" } ] } ] }
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ExternalHyperlink,
  WidthType, ShadingType, AlignmentType, PageOrientation, HeadingLevel,
} = require('docx');

const DATA = JSON.parse(fs.readFileSync(path.join(__dirname, 'sm1_media.json'), 'utf8'));
const COLS = [420, 520, 3000, 1000, 6460, 3000];   // сумма 14400
const HEAD = ['✔', '№', 'Урок', 'Тип',
              'Что это и по какому заданию узнать в ShkolaApp', 'Как назвать файл'];
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

const ALL = DATA.sections.flatMap(s => s.rows);
const nVideo = ALL.filter(r => r.kind === 'видео').length;
const nAudio = ALL.filter(r => r.kind === 'аудио').length;
const P = (text, o = {}) => new Paragraph({ spacing: { after: 120 }, children: [t(text, o)] });

const kids = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({
    text: 'Super Minds 1 · что скачать с ShkolaApp — аудио и видео', bold: true, size: 32 })] }),
  P(`Всего ${ALL.length} ${plural(ALL.length, 'файл', 'файла', 'файлов')}: ${nVideo} видео и ${nAudio} аудио. `
    + 'Это всё, чего не было в выгрузке. В уроках под них уже стоят пустые блоки, номера не сдвинутся.'),
  P('Куда класть: бакет classroom-media, папка sm1/u<номер юнита>/ — например sm1/u6/. '
    + 'Файлы Final Test — в папку sm1/u9/. Имя брать из последней колонки и не переименовывать: '
    + 'по нему я пойму, в какой блок вставить файл. Видео — .mp4, аудио — .mp3. '
    + 'Если вместо файла есть ссылка на YouTube — пришлите строкой «имя = ссылка». '
    + 'Когда зальёте, напишите — я пропишу ссылки в блоки.'),
  P('Ссылка в колонке «Урок» открывает этот урок в ShkolaApp. Курсивом — какое задание стоит '
    + 'там рядом с нужным файлом, чтобы не искать вслепую.', { it: true }),
];

let no = 1;
for (const s of DATA.sections) {
  if (!s.rows.length) continue;
  kids.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 80 },
    children: [new TextRun({ text: s.title, bold: true, size: 26 })] }));
  if (s.note) kids.push(P(s.note, { it: true }));
  kids.push(table(s.rows, no));
  no += s.rows.length;
}

const doc = new Document({ sections: [{
  properties: { page: {
    size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE },
    margin: { top: 720, right: 720, bottom: 720, left: 720 },
  }},
  children: kids,
}]});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(process.argv[2] || 'SM1_аудио_видео.docx', b);
  console.log('готово,', no - 1, 'строк');
});
