// Список «что скачать со Взнания»: node build_media.js media_sm2
//
// На «Взнания» нумерации блоков нашего редактора нет, поэтому файл узнаётся по
// заданию, которое идёт сразу после него. Данные — в media_<курс>.js.
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
        WidthType, ShadingType, PageOrientation } = require('docx');
const fs = require('fs');

const D = require(`./${process.argv[2]}`);
const OUT = `${__dirname}/${process.argv[2].replace(/^media_/, '')}_скачать_медиа.docx`.replace('sm2', 'SM2');

const W = 14400;
const HEAD = 'E8EEF7', ALT = 'F7F9FC', AUD = 'FFF4E5', VID = 'EAF4EA', NAME = 'F0ECF9';

function cell(text, width, opts = {}) {
  const runs = String(text).split('\n').map(t => new Paragraph({
    children: [new TextRun({ text: t, bold: !!opts.bold, size: opts.bold ? 20 : 19,
                             font: opts.mono ? 'Consolas' : undefined })],
    spacing: { before: 20, after: 20 }
  }));
  return new TableCell({
    children: runs,
    width: { size: width, type: WidthType.DXA },
    shading: opts.shade ? { type: ShadingType.CLEAR, fill: opts.shade, color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 }
  });
}

function table(cols, widths, rows) {
  const head = new TableRow({
    tableHeader: true,
    children: cols.map((c, i) => cell(c, widths[i], { bold: true, shade: HEAD }))
  });
  const body = rows.map((r, ri) => new TableRow({
    children: r.map((v, i) => cell(v.text, widths[i],
      { shade: v.shade || (ri % 2 ? ALT : undefined), mono: v.mono, bold: v.bold }))
  }));
  return new Table({ columnWidths: widths, rows: [head, ...body],
    width: { size: W, type: WidthType.DXA } });
}

const h1 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_1, spacing: { after: 160 } });
const h2 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_2, spacing: { before: 340, after: 140 } });
const p = (t, o = {}) => new Paragraph({
  children: [new TextRun({ text: t, size: 20, italics: !!o.i, bold: !!o.b })],
  spacing: { after: o.after == null ? 120 : o.after } });
const gap = () => new Paragraph({ text: '', spacing: { after: 160 } });

const all = [];
for (const [unit, rows] of D.units) for (const r of rows) all.push([unit, ...r]);
const nAud = all.filter(r => r[2] === 'аудио').length;
const nVid = all.length - nAud;

const C = ['✔', '№', 'Урок', 'Тип', 'Что это за файл — как он подписан у нас',
           'Узнать на «Взнания» по заданию, которое идёт сразу после', 'Как назвать файл'];
const COL = [420, 520, 1100, 800, 3600, 4360, 3600];

const children = [
  h1(D.title),
  p(`Всего файлов: ${all.length} — ${nVid} видео и ${nAud} аудио. Это ровно те места в уроках, ` +
    'где сейчас стоит пустой плеер: выгрузка «Взнания» медиафайлы не отдаёт.', { after: 100 }),
  p('Колонка «Узнать по заданию» нужна потому, что на «Взнания» нумерации блоков нашего редактора нет: ' +
    'откройте урок, найдите названное задание — нужный файл стоит прямо перед ним.', { after: 100 }),
  p('Видео обычно лежит ссылкой на YouTube — скачивать его не нужно, пришлите строку ' +
    '«имя_файла = ссылка». Аудио — файлом с тем же именем.', { after: 100 }),
  p(`Составлено ${new Date().toLocaleDateString('ru-RU')}.`, { i: true, after: 240 }),

  h2('Сколько по юнитам'),
  table(['Юнит', 'Видео', 'Аудио', 'Всего'], [5000, 2000, 2000, 5400],
    D.units.map(([u, rows]) => {
      const a = rows.filter(r => r[1] === 'аудио').length;
      return [{ text: u }, { text: String(rows.length - a) }, { text: String(a) },
              { text: String(rows.length) }];
    })),
  gap(),
];

let n = 0;
for (const [unit, rows] of D.units) {
  children.push(h2(unit));
  children.push(table(C, COL, rows.map(r => {
    const [lesson, kind, what, after, name] = r;
    n += 1;
    return [
      { text: '☐' },
      { text: String(n) },
      { text: lesson },
      { text: kind === 'аудио' ? '🔊 аудио' : '🎬 видео', shade: kind === 'аудио' ? AUD : VID },
      { text: what },
      { text: after },
      { text: name, mono: true, shade: NAME },
    ];
  })));
  children.push(gap());
}

children.push(h2('Что делать с файлами'));
children.push(p('• Имя файла говорит, куда его вставить: sm2_u6_hw2_b9 — курс, юнит 6, домашка 2, блок 9. ' +
  'Переименовывать вручную ничего больше не нужно, расширение любое (.mp3, .mp4).', { after: 60 }));
children.push(p('• Всё складывайте в одну папку на Диске — раскладывать по юнитам не нужно.', { after: 60 }));
children.push(p('• Для видео с YouTube файл не нужен: пришлите текстом строки вида ' +
  '«sm2_u6_hw2_b9 = https://youtu.be/…», по строке на видео.', { after: 60 }));
children.push(p('• Чего-то не найдётся — просто пропустите строку: вставлю то, что будет, ' +
  'остальное останется в списке на потом.', { after: 60 }));
children.push(p('• Если на «Взнания» в уроке есть аудио или видео, которого нет в этой таблице, — ' +
  'скажите, в каком уроке: значит, при переносе для него не завели блок, и я его добавлю.'));

const doc = new Document({
  styles: { default: {
    document: { run: { font: 'Calibri', size: 20 } },
    heading1: { run: { font: 'Calibri', size: 32, bold: true, color: '1F3864' } },
    heading2: { run: { font: 'Calibri', size: 24, bold: true, color: '2E5496' } } } },
  sections: [{
    properties: { page: { size: { orientation: PageOrientation.LANDSCAPE },
                          margin: { top: 720, bottom: 720, left: 720, right: 720 } } },
    children
  }]
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b);
  console.log(OUT, Math.round(b.length / 1024), 'КБ,', all.length, 'строк'); });
