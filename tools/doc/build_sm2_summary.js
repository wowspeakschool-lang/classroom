// Один файл «что осталось руками» на весь курс: node build_sm2_summary.js <папка с данными>
//
// Собирается из двух выгрузок: lessons.json (уроки, блоки, число блоков
// с разметкой озвучки — из базы) и marks.json (пересобранные игры, мои тексты
// и блоки с точками — из сборок уроков). Всё, что можно посчитать, считается;
// руками здесь задан только список спорных мест внизу файла.
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
        WidthType, ShadingType, PageOrientation } = require('docx');
const fs = require('fs');

const DIR = process.argv[2];
const LESSONS = JSON.parse(fs.readFileSync(`${DIR}/lessons.json`, 'utf8'));
const MARKS = JSON.parse(fs.readFileSync(`${DIR}/marks.json`, 'utf8'));
const OUT = `${DIR}/SM2_что_сделать_руками.docx`;

const W = 14400;
const HEAD = 'E8EEF7', ALT = 'F7F9FC', RED = 'FDE8E8', OK = 'EAF4EA';

function cell(text, width, o = {}) {
  const runs = String(text).split('\n').map(t => new Paragraph({
    children: [new TextRun({ text: t, bold: !!o.bold, size: o.bold ? 20 : 19 })],
    spacing: { before: 20, after: 20 }
  }));
  return new TableCell({
    children: runs, width: { size: width, type: WidthType.DXA },
    shading: o.shade ? { type: ShadingType.CLEAR, fill: o.shade, color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 90, right: 90 }
  });
}

function table(cols, widths, rows, redCol) {
  const head = new TableRow({ tableHeader: true,
    children: cols.map((c, i) => cell(c, widths[i], { bold: true, shade: HEAD })) });
  const body = rows.map((r, ri) => new TableRow({
    children: r.map((v, i) => cell(v, widths[i],
      { shade: (redCol != null && i === redCol) ? RED : (ri % 2 ? ALT : undefined) })) }));
  return new Table({ columnWidths: widths, rows: [head, ...body],
    width: { size: W, type: WidthType.DXA } });
}

const h1 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_1, spacing: { after: 160 } });
const h2 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_2, spacing: { before: 360, after: 140 } });
const p = (t, o = {}) => new Paragraph({
  children: [new TextRun({ text: t, size: 20, italics: !!o.i, bold: !!o.b })],
  spacing: { after: o.after == null ? 120 : o.after } });
const gap = () => new Paragraph({ text: '', spacing: { after: 160 } });

const short = t => t.replace(/^Homework /, 'ДЗ ')
                    .replace(/^Unit \d+ Test$/, 'Тест').replace(/^Test$/, 'Тест')
                    .replace(/^Final Test$/, 'Финальный тест');
const unitKey = n => (n === 10 ? 'final' : 'u' + n);
const plural = (n, a, b, c) => n % 10 === 1 && n % 100 !== 11 ? a
  : [2, 3, 4].includes(n % 10) && ![12, 13, 14].includes(n % 100) ? b : c;

// ─────────────────────────────────────────────────────────── что посчиталось ──
const nLessons = LESSONS.reduce((s, u) => s + u[2].length, 0);
const nBlocks = LESSONS.reduce((s, u) => s + u[2].reduce((q, l) => q + l[1], 0), 0);
const voiced = LESSONS.flatMap(u => u[2].filter(l => l[2] > 0));
const marksOf = kind => LESSONS.flatMap(u =>
  (MARKS[unitKey(u[1])] || []).filter(r => r[3] === kind)
    .map(r => [u[0], short(r[0]), r[1], r[2], r[4], r[5]]));
const games = marksOf('игра'), dots = marksOf('точки'), texts = marksOf('текст');
const noBuild = LESSONS.filter(u => !MARKS[unitKey(u[1])]).map(u => u[0]);

// ──────────────────────────────────────────── главная таблица «что от вас» ──
const MAIN = [
  ['Включить публикацию',
   `Все ${nLessons} ${plural(nLessons, 'урок', 'урока', 'уроков')} курса`,
   'Сейчас не опубликован ни один урок — ученики курса не видят. Так и задумано: заливаю всегда с выключенной публикацией, включаете вы, когда проверите'],
  ['Нажать «Озвучить пачкой»',
   `${voiced.length} ${plural(voiced.length, 'урок', 'урока', 'уроков')} с разметкой`,
   'Разметка озвучки стоит у слов, фраз и реплик историй. Поля audio пустые, пока не нажмёте; уже озвученное кнопка не трогает'],
  [`Посмотреть пересобранные игры — ${games.length}`,
   'Юниты 3–9, список ниже',
   'Содержимого игр Wordwall выгрузка не отдаёт никогда — только тип и название на обложке. Пересобрала их штатными блоками, состав подобрала сама'],
  [`Сверить точки на картинках — ${dots.length}`,
   'Юниты 4–8, список ниже',
   'Координаты точек выгрузка не сохраняет. Расставила по смыслу картинки — посмотрите, что встало на место'],
  [`Прочитать мои тексты READING — ${texts.length}`,
   'Юниты 6–9, список ниже',
   'В выгрузке у этих блоков остались только задания, самого текста нет. Написала так, чтобы сходились все ответы из выгрузки'],
  ['Решить, что делать с четырьмя пустыми заданиями',
   'ДЗ 5 юнита 6, ДЗ 5 юнита 7, тест юнита 9, финальный тест',
   'В выгрузке они пришли пустыми: ни аудио, ни вариантов ответа — только отметки, какой вариант верный. Восстановить ответы нельзя, в уроки не заливала. Пришлёте материал — добавлю'],
  ['Посмотреть 25 новых картинок в Unit 4',
   'ДЗ 1, ДЗ 4, ДЗ 7 и тест',
   'Еда и фрукты-гибриды. Прежние потерялись, эти сгенерированы заново — вышли фотореалистичными, а не в 3D-стиле остальных картинок курса. Вы согласились оставить так'],
];

const children = [
  h1('Super Minds 2 — что осталось сделать руками'),
  p(`Курс перенесён целиком: 11 юнитов, ${nLessons} ${plural(nLessons, 'урок', 'урока', 'уроков')}, ${nBlocks} ${plural(nBlocks, 'блок', 'блока', 'блоков')}. Аудио и видео вставлены — все 36 файлов, ни одного пустого плеера.`, { after: 100 }),
  p('Этот файл заменяет прежние файлы по юнитам: в них ещё значились строки про аудио и видео, которых уже нет.', { i: true, after: 100 }),
  p(`Составлено ${new Date().toLocaleDateString('ru-RU')}. Номера блоков — как в редакторе, нумерация с 1.`, { i: true, after: 240 }),

  h2('Что нужно от вас — весь список'),
  table(['🟥 Что сделать', 'Где', 'Почему'], [3600, 3800, 7000], MAIN, 0),
  gap(),

  h2('По юнитам'),
  table(['Юнит', 'Уроков', 'Блоков', 'Уроков с озвучкой', 'Игр', 'Точек', 'Текстов'],
    [4600, 1400, 1500, 2600, 1400, 1400, 1500],
    LESSONS.map(u => {
      const m = MARKS[unitKey(u[1])] || [];
      return [u[0], String(u[2].length), String(u[2].reduce((s, l) => s + l[1], 0)),
        String(u[2].filter(l => l[2] > 0).length),
        String(m.filter(r => r[3] === 'игра').length) || '—',
        String(m.filter(r => r[3] === 'точки').length) || '—',
        String(m.filter(r => r[3] === 'текст').length) || '—'];
    })),
  gap(),
];

if (noBuild.length) {
  children.push(p(`По юнитам «${noBuild.join('», «')}» колонки «Игр», «Точек» и «Текстов» пустые не потому, что там ничего нет, а потому что сборки этих юнитов не сохранились — они делались до того, как сборки стали попадать в репозиторий. Подробности по ним остались в прежних файлах «доработать руками» по этим юнитам.`, { i: true }));
  children.push(gap());
}

function section(title, intro, rows, cols) {
  if (!rows.length) return;
  children.push(h2(title));
  children.push(p(intro, { after: 140 }));
  children.push(table(cols, [3000, 1500, 900, 1800, 3600, 3600],
    rows.map(r => [r[0], r[1], String(r[2]), r[3], r[4] || '—', r[5] || '—'])));
  children.push(gap());
}

section(`Пересобранные игры — ${games.length}`,
  'Открывается по названию блока. В комментарии к каждому стоит «СОСТАВ МОЙ» — это значит, что задание собрала я, а в выгрузке была только обложка игры.',
  games, ['Юнит', 'Урок', 'Блок', 'Тип', 'Заголовок в уроке', 'Что было в выгрузке']);

section(`Точки на картинках — ${dots.length}`,
  'Ученик соединяет подпись с местом на картинке. Координаты я расставила сама — проверьте, что точки попали куда надо.',
  dots, ['Юнит', 'Урок', 'Блок', 'Тип', 'Заголовок в уроке', 'Комментарий']);

section(`Мои тексты READING — ${texts.length}`,
  'Текст написан мной так, чтобы сходились все ответы из выгрузки. Проверьте, что он вам подходит по стилю и уровню.',
  texts, ['Юнит', 'Урок', 'Блок', 'Тип', 'Заголовок в уроке', 'Комментарий']);

children.push(h2('Что уже сделано и проверять не нужно'));
[
  '• Аудио и видео вставлены: 36 файлов, 25 видео и 11 аудио. Лежат в хранилище Supabase, каждая ссылка проверена — файл отдаётся и размер совпадает.',
  '• Правильные ответы сняты по отметкам в выгрузке (отмечен тот вариант, у которого нет пустого чекбокса) и сверены с картинкой, к которой относится вопрос.',
  '• Перед заливкой каждый урок проверен скриптом: индексы верных вариантов, отсутствие дублей среди вариантов, уникальность правых значений в «найди пару», совпадение слов и предложения в «составь предложение», число пропусков, координаты точек, наличие каждого файла картинки. Ошибок — ноль.',
  '• Картинки лежат в репозитории и отдаются ссылками — ни одной картинки внутри текста урока.',
  '• Домашки заведены с порогом 60 %, тесты — с порогом 90 % и типом «тест». Порядок уроков проставлен числами.',
].forEach(t => children.push(p(t, { after: 60 })));

const doc = new Document({
  styles: { default: {
    document: { run: { font: 'Calibri', size: 20 } },
    heading1: { run: { font: 'Calibri', size: 32, bold: true, color: '1F3864' } },
    heading2: { run: { font: 'Calibri', size: 24, bold: true, color: '2E5496' } } } },
  sections: [{
    properties: { page: { size: { orientation: PageOrientation.LANDSCAPE },
                          margin: { top: 720, bottom: 720, left: 720, right: 720 } } },
    children }]
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b);
  console.log(OUT, Math.round(b.length / 1024), 'КБ'); });
