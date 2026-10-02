const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
        WidthType, ShadingType, PageOrientation } = require('docx');
const fs = require('fs');

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
  return new Table({ columnWidths: widths, rows: [head, ...body], width: { size: W, type: WidthType.DXA } });
}

const h1 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_1, spacing: { after: 160 } });
const h2 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_2, spacing: { before: 360, after: 140 } });
const p  = (t, o = {}) => new Paragraph({
  children: [new TextRun({ text: t, size: 20, italics: !!o.i, bold: !!o.b })],
  spacing: { after: o.after == null ? 120 : o.after } });
const gap = () => new Paragraph({ text: '', spacing: { after: 160 } });

const OBJ = 'Children’s coursebook illustration, friendly 3D-rendered cartoon style with soft rounded shapes, smooth matte surfaces and gentle studio lighting, bright saturated colours, thick clean silhouette, centred, plain flat pure white background, no shadow on the background under the object, no text, no letters, no signs, no border, no frame. IMPORTANT FRAMING: the whole subject is small in the frame and fully visible, with a generous empty white margin on all four sides; nothing touches or crosses the edge of the image.';
const SCENE = 'Children’s coursebook illustration, friendly 3D-rendered cartoon style with soft rounded shapes, smooth matte surfaces and gentle lighting, bright saturated colours, wide landscape scene, no text, no letters, no signs, no border, no frame. IMPORTANT FRAMING: the whole scene is fully visible with a generous empty margin on all four sides; nothing touches or crosses the edge of the image.';

// файл · стиль · где нужна · промпт
const ROWS = [
  ['f_tomato', 'объект', 'ДЗ 1 (карточки, найди пару, скрэмбл), тест блок 1',
   'One ripe red tomato with a small green stalk and leaves on top, glossy and plump'],
  ['f_beans', 'объект', 'ДЗ 1',
   'A small heap of green string beans lying together, fresh and crisp, a few pods slightly curved'],
  ['f_greens', 'объект', 'ДЗ 1',
   'A fresh bunch of leafy green herbs — parsley and dill — tied together with a thin string'],
  ['f_potato', 'объект', 'ДЗ 1, ДЗ 2 блок 13, тест блок 2',
   'Three brown potatoes lying together, slightly earthy skin with small dimples'],
  ['f_kiwi', 'объект', 'ДЗ 1',
   'One whole brown fuzzy kiwi fruit next to one half kiwi cut open, showing the bright green inside with black seeds'],
  ['f_lemon', 'объект', 'ДЗ 1, ДЗ 2 блок 12, тест блок 2',
   'Two bright yellow lemons, one whole and one cut in half showing the juicy inside, a small green leaf beside them'],
  ['f_bread', 'объект', 'ДЗ 1, ДЗ 2, тест блоки 2 и 3',
   'A golden brown loaf of crusty bread next to two cut slices, bakery style'],
  ['f_mango', 'объект', 'ДЗ 1, ДЗ 2, тест блок 3',
   'One ripe mango with red and orange skin, next to a half mango showing the bright yellow flesh'],
  ['f_grapes', 'объект', 'ДЗ 1, ДЗ 3, тест блок 2',
   'A bunch of green grapes on a small stem with two green leaves'],
  ['f_egg', 'объект', 'ДЗ 1, ДЗ 3, ДЗ 5',
   'Three white chicken eggs lying together, one slightly in front'],
  ['f_watermelon', 'объект', 'ДЗ 1, ДЗ 2, тест блок 2',
   'A whole round watermelon with dark green stripes next to one triangular slice showing red flesh and black seeds'],
  ['f_apple', 'объект', 'ДЗ 2, ДЗ 3, ДЗ 4 блок 5',
   'Three shiny red apples lying together, each with a short brown stalk and one green leaf'],
  ['f_cake', 'объект', 'Тест блок 3, первое предложение',
   'A round birthday cake with white frosting, pastel pink and blue swirls around the edge and a few sprinkles on top, no writing on the cake'],
  ['f_strawberries', 'объект', 'Тест блок 3, третье предложение',
   'A small heap of fresh red strawberries with green leafy tops, one cut in half'],
  ['f_cheese', 'объект', 'ДЗ 3, ДЗ 5, тест блок 3',
   'A big wedge of yellow cheese with round holes, next to two smaller cubes of the same cheese'],
  ['f_fish', 'объект', 'Тест блок 2 — «соедини слова с картинками»',
   'One whole fresh fish lying on its side, silver and blue scales, friendly not scary, like a fish from a market counter'],
  ['f_basket', 'объект', 'ДЗ 1 (2) блок 4 — задание «расскажи, что вы покупаете»',
   'A wicker shopping basket filled with food: bread, a bottle of milk, tomatoes, a green pepper, a wedge of cheese and some greens sticking out of the top'],
  ['fridge_speaking', 'сцена', '🟥 Тест блок 9 и 10 — SPEAKING, картинки в выгрузке нет совсем',
   'An open fridge seen from the front, shelves filled with food: a jug of juice, a plate of cupcakes, a whole fish, a bunch of carrots, a wedge of cheese, a bunch of bananas, some tomatoes and a carton of milk; door shelves with bottles and a tray of eggs'],
  // ── ДЗ 7: фрукты-гибриды. В выгрузке это фотоколлажи, перерисовываем в стиле программы.
  ['hy_apple_mandarin', 'объект', 'ДЗ 7 — «выбери два фрукта», вопрос 1. Ответ: apple + mandarin',
   'A funny hybrid fruit: a red apple cut in half, but inside it is the bright orange segmented flesh of a mandarin instead of apple flesh; the whole apple stands behind the cut half'],
  ['hy_pineapple_banana', 'объект', 'ДЗ 7, вопрос 2. Ответ: pineapple + banana',
   'A funny hybrid fruit: a bunch of bananas whose skin is rough scaly pineapple skin, with a spiky green pineapple crown growing out of the top of the bunch'],
  ['hy_tomato_lemon', 'объект', 'ДЗ 7, вопрос 3. Ответ: tomato + lemon',
   'A funny hybrid fruit: a yellow lemon cut in half, but inside it is the red seedy flesh of a tomato instead of lemon flesh; a whole lemon stands behind the cut halves'],
  ['hy_strawberry_apple', 'объект', 'ДЗ 7, вопрос 4. Ответ: strawberry + apple',
   'A funny hybrid fruit: a big strawberry with a green leafy top, cut in half, and inside it is the pale white flesh and dark pips of an apple instead of strawberry flesh'],
  ['hy_banana_orange', 'объект', 'ДЗ 7, вопрос 5. Ответ: banana + orange',
   'A funny hybrid fruit: two curved banana shapes with orange peel instead of banana skin, each cut across to show the round segmented orange flesh inside'],
  ['hy_orange_kiwi', 'объект', 'ДЗ 7, вопрос 6. Ответ: orange + kiwi',
   'A funny hybrid fruit: an orange cut in half, but inside it is the bright green flesh with black seeds and a white centre of a kiwi instead of orange flesh'],
  ['hy_grape_potato', 'объект', 'ДЗ 7 блок 11 — пример «grapetatoes» к заданию «придумай свой гибрид»',
   'A funny hybrid fruit: a bunch of grapes on a green vine with leaves, but every grape is a small brown potato with potato skin'],
];

const children = [
  h1('Super Minds 2 · Unit 4 · Food — картинки, которые нужно нарисовать'),
  p('25 картинок. Имя файла важно — под ним урок ищет картинку, поэтому сохраняйте ровно так, как в первой колонке, в формате png или webp.', { after: 100 }),
  p('Модель gpt-image-1-mini, качество medium, размер 1024×1024. К каждому промпту дописывается строка стиля из-под таблицы — «объект» или «сцена», смотря что стоит во второй колонке.', { after: 100 }),
  p('После генерации посмотрите на края: генератор любит упирать фигуру в край и обрезать её. Если обрезано — перегенерируйте, ничего страшного.', { i: true, after: 240 }),

  table(['Файл', 'Стиль', 'Где нужна', 'Промпт'], [2100, 900, 4200, 7200], ROWS),
  gap(),

  p('Строка стиля для «объект»:', { b: true, after: 60 }),
  p(OBJ, { i: true, after: 140 }),
  p('Строка стиля для «сцена»:', { b: true, after: 60 }),
  p(SCENE, { i: true, after: 140 }),
  gap(),

  h2('Что беру из выгрузки без перерисовки'),
  p('Шесть обучающих карточек уроков, карточка-правило A/AN/SOME, четыре кадра истории «Bad apples» и сцена рынка, два рисованных холодильника (ДЗ 3), фото холодильника из ДЗ 5, картинка с весами и «сколько весит 1 продукт» из ДЗ 6, ключ «1 carrot = 50g», картинка с примерами, прилавок с фруктами и таблица весов из ДЗ 7 — всё это и есть сам материал задания, перерисовывать нельзя, иначе разойдутся ответы.'),
  p('Фото открытого холодильника в ДЗ 5 оставляю как есть: на нём держатся пять утверждений True/False. Если захотите заменить — ответы придётся пересобирать под новую картинку, скажите, и я это сделаю.', { i: true }),
];

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

Packer.toBuffer(doc).then(b => { fs.writeFileSync('SM2_Unit_4_картинки_промпты.docx', b);
  console.log('готово,', Math.round(b.length / 1024), 'КБ,', ROWS.length, 'промптов'); });
