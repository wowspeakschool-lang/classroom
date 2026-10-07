// Собирает docx со списком аудио и видео GG1, которых не было в выгрузке ShkolaApp.
// Форма та же, что у файла SM3: альбомный А4, по таблице на юнит, последняя
// колонка — имя файла для бакета classroom-media. Строки берутся из
// tools/gg1_media.json (его пишет tools/gg1_media_list.py по собранным урокам).
//   python3 tools/gg1_media_list.py && node tools/gg1_media_docx.js out.docx
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, ShadingType, AlignmentType, PageOrientation, HeadingLevel,
} = require('docx');

const COLS = [420, 520, 1100, 1000, 8160, 3200];   // сумма 14400
const HEAD = ['✔', '№', 'Урок', 'Тип',
              'Узнать в ShkolaApp по заданию (как оно подписано у нас)', 'Как назвать файл'];

const ROWS = JSON.parse(fs.readFileSync(path.join(__dirname, 'gg1_media.json'), 'utf8'));
const DATA = [];
for (const r of ROWS) {
  let g = DATA.find(([u]) => u === r.unit);
  if (!g) DATA.push(g = [r.unit, []]);
  g[1].push(r);
}

const ICON = { 'видео': '🎬 видео', 'аудио': '🔊 аудио' };
const EXT  = { 'видео': '.mp4', 'аудио': '.mp3' };

function cell(text, i, opts = {}) {
  return new TableCell({
    width: { size: COLS[i], type: WidthType.DXA },
    shading: opts.head
      ? { type: ShadingType.CLEAR, color: 'auto', fill: 'E8EEF7' }
      : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    children: [new Paragraph({
      spacing: { before: 20, after: 20 },
      alignment: opts.center ? AlignmentType.CENTER : AlignmentType.LEFT,
      children: [new TextRun({ text, bold: !!opts.head, size: opts.small ? 18 : 20 })],
    })],
  });
}

function table(rows, startNo) {
  const trs = [new TableRow({
    tableHeader: true,
    children: HEAD.map((h, i) => cell(h, i, { head: true })),
  })];
  rows.forEach((r, k) => {
    trs.push(new TableRow({ children: [
      cell('☐', 0, { center: true }),
      cell(String(startNo + k), 1, { center: true }),
      cell(r.lesson, 2),
      cell(ICON[r.kind], 3),
      cell(r.hint, 4, { small: true }),
      cell(r.name + EXT[r.kind], 5),
    ]}));
  });
  return new Table({
    columnWidths: COLS,
    width: { size: 14400, type: WidthType.DXA },
    rows: trs,
  });
}

function plural(n, one, few, many) {
  const a = Math.abs(n) % 100, b = a % 10;
  if (a > 10 && a < 20) return many;
  if (b > 1 && b < 5) return few;
  return b === 1 ? one : many;
}

const nVideo = ROWS.filter(r => r.kind === 'видео').length;
const nAudio = ROWS.filter(r => r.kind === 'аудио').length;

const kids = [
  new Paragraph({ heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text: 'Go Getter 1 · что скачать из ShkolaApp — аудио и видео', bold: true, size: 32 })] }),
  new Paragraph({ spacing: { after: 120 }, children: [new TextRun({
    text: `Всего ${ROWS.length} ${plural(ROWS.length, 'файл', 'файла', 'файлов')}: ${nVideo} видео и ${nAudio} аудио. `
        + 'Это всё, чего не было в выгрузке — в уроках под них уже стоят пустые блоки, номера не сдвинутся.',
    size: 20 })] }),
  new Paragraph({ spacing: { after: 120 }, children: [new TextRun({
    text: 'Куда класть: бакет classroom-media, папка gg1/u<номер юнита>/ (Unit 0 — gg1/u0/), у финального теста — gg1/ft/. '
        + 'Имя файла брать из последней колонки, не переименовывать: по нему я найду, в какой блок его вставить. '
        + 'Видео — .mp4, аудио — .mp3. Когда зальёте, напишите — я пропишу ссылки в блоки.', size: 20 })] }),
  new Paragraph({ spacing: { after: 240 }, children: [new TextRun({
    text: 'Колонка «узнать по заданию» — чтобы не искать файл вслепую: там написано, как называется этот блок '
        + 'у нас (обычно это инструкция из ShkolaApp) и какое задание стоит сразу после него.',
    size: 20, italics: true })] }),
];

let no = 1;
for (const [unit, rows] of DATA) {
  kids.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 80 },
    children: [new TextRun({ text: unit, bold: true, size: 26 })] }));
  kids.push(table(rows, no));
  no += rows.length;
}

const doc = new Document({
  sections: [{
    properties: { page: {
      size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE },
      margin: { top: 720, right: 720, bottom: 720, left: 720 },
    }},
    children: kids,
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync(process.argv[2] || 'GG1_аудио_видео.docx', b);
  console.log('готово,', no - 1, 'строк');
});
