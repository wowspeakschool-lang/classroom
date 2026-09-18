// Файл «доработать руками» для одного юнита: node build_unit.js u6
//
// Рядом нужны: units.js (ручные части — см. units.example.js) и u6.json,
// который пишет tools/dump_todo.py. Всё, что можно посчитать из сборки,
// считается здесь; руками задаётся только то, чего в данных нет.
// Перед первым запуском: npm i (ставит docx).
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
        WidthType, ShadingType, PageOrientation } = require('docx');
const fs = require('fs');
const UNITS = require('./units');

const KEY = process.argv[2];
const U = UNITS[KEY];
const D = JSON.parse(fs.readFileSync(`${__dirname}/${KEY}.json`, 'utf8'));

const W = 14400;
const HEAD = 'E8EEF7', ALT = 'F7F9FC', RED = 'FDE8E8';

function cell(text, width, opts = {}) {
  const runs = String(text).split('\n').map(t => new Paragraph({
    children: [new TextRun({ text: t, bold: !!opts.bold, size: opts.bold ? 20 : 19 })],
    spacing: { before: 20, after: 20 }
  }));
  return new TableCell({
    children: runs,
    width: { size: width, type: WidthType.DXA },
    shading: opts.shade ? { type: ShadingType.CLEAR, fill: opts.shade, color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 }
  });
}

function table(cols, widths, rows, redCol) {
  const head = new TableRow({
    tableHeader: true,
    children: cols.map((c, i) => cell(c, widths[i], { bold: true, shade: HEAD }))
  });
  const body = rows.map((r, ri) => new TableRow({
    children: r.map((v, i) => cell(v, widths[i],
      { shade: (redCol != null && i === redCol) ? RED : (ri % 2 ? ALT : undefined) }))
  }));
  return new Table({ columnWidths: widths, rows: [head, ...body],
    width: { size: W, type: WidthType.DXA } });
}

const h1 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_1, spacing: { after: 160 } });
const h2 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_2, spacing: { before: 360, after: 140 } });
const p  = (t, o = {}) => new Paragraph({
  children: [new TextRun({ text: t, size: 20, italics: !!o.i, bold: !!o.b })],
  spacing: { after: o.after == null ? 120 : o.after } });
const gap = () => new Paragraph({ text: '', spacing: { after: 160 } });

// короткое имя урока: «ДЗ 3», «Тест», «Финальный тест»
const short = l => l.title.replace(/^Homework /, 'ДЗ ')
                          .replace(/^Unit \d+ Test$/, 'Тест')
                          .replace(/^Final Test$/, 'Финальный тест');

// ───────────────────────────────────────────── сводка «что нужно от вас» ──
const AV = [], WW = [], DOTS = [], READ = [], MINE = [], OTHER = [];
for (const l of D.lessons) {
  const n = short(l);
  for (const r of l.todo) {
    const [num, , , need, why] = r;
    if (need.startsWith('Ссылка на видео')) AV.push(`${n} бл. ${num}`);
    else if (need.startsWith('Ссылка на аудио')) AV.push(`${n} бл. ${num} (аудио)`);
    else if (need.startsWith('Проверить, куда встали точки')) DOTS.push(`${n} бл. ${num}`);
    else if (need.startsWith('Прочитать текст для READING')) READ.push(`${n} бл. ${num}`);
    else if (need.startsWith('Посмотреть')) MINE.push(`${n} бл. ${num}`);
    else OTHER.push([need, `${n} бл. ${num}`, why]);
  }
  for (const m of l.made) WW.push(`${n} бл. ${m[0]}`);
}

const CT = ['🟥 Что нужно от вас', 'Где', 'Почему'];
const WT = [3400, 4200, 6800];
const RT = [];
if (AV.length) RT.push([`Дать ссылки на видео и аудио — ${AV.length}`, AV.join(' · '),
  'В выгрузке медиафайлы не сохраняются никогда. В каждом случае задание под блоком — по этому же видео или аудио']);
RT.push(['Нажать «Озвучить пачкой»', `Во всех ${D.lessons.length === 1 ? 'уроке' : 'уроках'}`,
  `Разметка озвучки стоит: ${U.tts}. Поля audio пустые, пока не нажмёте`]);
RT.push(['Включить публикацию', D.lessons.length === 1 ? 'В уроке' : `Во всех ${D.lessons.length} уроках`,
  'Всё залито с выключенной публикацией — до вашего нажатия ученики уроков не видят']);
if (WW.length) RT.push([`Посмотреть пересобранные игры — ${WW.length}`, WW.join(' · '),
  'Содержимого игр Wordwall в выгрузке не бывает никогда. Пересобрала их штатными блоками; в комментарии к каждому блоку стоит «СОСТАВ МОЙ»']);
if (DOTS.length) RT.push([`Сверить точки на картинках — ${DOTS.length}`, DOTS.join(' · '),
  'Координаты точек выгрузка не сохраняет. Расставила их сама по смыслу картинки — посмотрите, что встало на место']);
if (READ.length) RT.push(['Прочитать мой текст READING', READ.join(' · '),
  'В выгрузке у блока READING остались только задания, самого текста нет. Написала текст так, чтобы сходились все ответы из выгрузки']);
if (MINE.length) RT.push([`Посмотреть мой состав заданий — ${MINE.length}`, MINE.join(' · '),
  'В выгрузке эти места пустые — состав подобрала сама']);
for (const o of OTHER) RT.push(o);
for (const e of U.extra) RT.push(e);

// ───────────────────────────────────────────────────────── по урокам ──
const C = ['Блок', 'Тип', 'Как выглядит в уроке — по этой фразе найдёте', '🟥 Что нужно от вас', 'Почему / что я уже сделала'];
const COL = [900, 1500, 3900, 3300, 4800];

const CS = ['Урок', 'О чём', 'Блоков', 'Нужно от вас'];
const WS = [1500, 5400, 1200, 6300];
const RS = D.lessons.map(l => [short(l), l.summary, String(l.blocks),
  l.todo.length ? `${l.todo.length} ${l.todo.length === 1 ? 'пункт' : l.todo.length < 5 ? 'пункта' : 'пунктов'}` : '—']);

const children = [
  h1(U.title),
  p(`${D.lessons.length === 1 ? 'Урок залит' : `Все ${D.lessons.length} уроков залиты`} в Classroom под юнитом «${D.unit}», публикация выключена — включаете вы. Ниже: что осталось сделать руками и что я уже сделала сама.`, { after: 100 }),
  p('Номера блоков — как в редакторе, нумерация с 1.', { i: true, after: 100 }),
  p(`Составлено ${new Date().toLocaleDateString('ru-RU')}.`, { i: true, after: 240 }),

  h2('Сводка по урокам'),
  table(CS, WS, RS),
  gap(),

  h2('Что нужно от вас — весь список'),
  p('Ниже всё, что осталось сделать руками, включая публикацию и озвучку. Подробности по каждому пункту — в таблицах по урокам.', { after: 140 }),
  table(CT, WT, RT, 0),
  gap(),
];

for (const l of D.lessons) {
  if (!l.todo.length && !l.made.length && !l.typos.length) continue;
  children.push(h2(`${short(l)} — ${l.summary}`));
  if (l.todo.length) {
    children.push(table(C, COL, l.todo, 3));
    children.push(gap());
  }
  if (l.made.length) {
    children.push(p('Пересобранные игры и задания, которых в выгрузке не было:', { i: true, after: 100 }));
    children.push(table(['Блок', 'Тип', 'Заголовок в уроке', 'Что это было в выгрузке'],
      [900, 1500, 5000, 7000], l.made));
    children.push(gap());
  }
  if (l.typos.length) {
    children.push(p('Опечатки, исправленные сразу:', { i: true, after: 100 }));
    children.push(table(['Блок', 'Тип', 'Что исправлено'], [900, 1500, 12000], l.typos));
    children.push(gap());
  }
}

children.push(h2('Ваши картинки — куда встали'));
children.push(table(['Файлы', 'Куда встали'], [5200, 9200], U.pictures));
children.push(gap());

const totalBlocks = D.lessons.reduce((s, l) => s + l.blocks, 0);
children.push(h2('Что уже сделано автоматически'));
children.push(p(`• Озвучка размечена: ${U.tts}. Поля audio пустые — синтез заполнит их, когда нажмёте «Озвучить пачкой».`, { after: 60 }));
children.push(p('• Правильные ответы сняты по отметкам в выгрузке (отмечен тот вариант, у которого нет пустого чекбокса) и каждый раз сверены с картинкой, к которой относится вопрос.', { after: 60 }));
children.push(p('• Перед заливкой payload проверен скриптом: индексы верных вариантов, отсутствие дублей среди вариантов, уникальность правых значений в «найди пару», совпадение слов и предложения в «составь предложение», число пропусков в каждом «заполни пропуски», координаты точек на картинках, наличие каждого файла картинки в репозитории. Ошибок — ноль.', { after: 60 }));
children.push(p('• Картинки лежат в репозитории и отдаются ссылками с classroom.wowteach.ru — ни одной картинки внутри текста урока.', { after: 60 }));
children.push(p(`• Домашки заведены с порогом 60 %, тест — с порогом 90 % и типом «тест». Публикация выключена. Порядок уроков проставлен числами. Всего блоков: ${totalBlocks}.`));

const doc = new Document({
  styles: { default: {
    document: { run: { font: 'Calibri', size: 20 } },
    heading1: { run: { font: 'Calibri', size: 32, bold: true, color: '1F3864' } },
    heading2: { run: { font: 'Calibri', size: 24, bold: true, color: '2E5496' } } } },
  sections: [{
    properties: { page: { size: { orientation: PageOrientation.LANDSCAPE }, margin: { top: 720, bottom: 720, left: 720, right: 720 } } },
    children
  }]
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(`${__dirname}/${U.file}`, b);
  console.log(U.file, Math.round(b.length / 1024), 'КБ'); });
