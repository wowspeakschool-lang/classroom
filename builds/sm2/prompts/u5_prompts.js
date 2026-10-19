const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
        WidthType, ShadingType, PageOrientation } = require('docx');
const fs = require('fs');

const W = 14400;
const HEAD = 'E8EEF7', ALT = 'F7F9FC', GRN = 'E9F6EC';

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
    children: r.map((v, i) => cell(v, widths[i],
      { shade: ri % 2 ? ALT : undefined, mono: i === 0 }))
  }));
  return new Table({ columnWidths: widths, rows: [head, ...body],
    width: { size: W, type: WidthType.DXA } });
}

const h1 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_1, spacing: { after: 160 } });
const h2 = t => new Paragraph({ text: t, heading: HeadingLevel.HEADING_2, spacing: { before: 360, after: 140 } });
const p  = (t, o = {}) => new Paragraph({
  children: [new TextRun({ text: t, size: 20, italics: !!o.i, bold: !!o.b,
                           font: o.mono ? 'Consolas' : undefined })],
  spacing: { after: o.after == null ? 120 : o.after } });
const gap = () => new Paragraph({ text: '', spacing: { after: 160 } });

// ─────────────────────────────────────────────── две строки стиля ──
const FRAME = 'IMPORTANT FRAMING: the whole subject is small in the frame and fully visible, '
            + 'with a generous empty white margin on all four sides; nothing touches or crosses '
            + 'the edge of the image.';

const OBJ = 'Children’s coursebook illustration, friendly 3D-rendered cartoon style with soft '
          + 'rounded shapes, smooth matte surfaces and gentle studio lighting, bright saturated '
          + 'colours, thick clean silhouette, centred, plain flat pure white background, no shadow '
          + 'on the background under the object, no text, no letters, no signs, no border, no frame. '
          + FRAME;

const SCENE = 'Children’s coursebook illustration, friendly 3D-rendered cartoon style with soft '
            + 'rounded shapes, smooth matte surfaces and gentle lighting, bright saturated colours, '
            + 'wide landscape scene, no text, no letters, no signs, no border, no frame. ' + FRAME;

// имя · где используется · стиль · промпт
const MUST = [
  ['f_bed', 'ДЗ 1 бл. 3, 4, 13 · Тест бл. 2', 'ПРЕДМЕТ',
   'A single child’s bed seen from the side, light wooden frame, white mattress, one blue pillow and a folded blue blanket'],
  ['f_sofa', 'ДЗ 1 бл. 3, 4, 13 · Тест бл. 2', 'ПРЕДМЕТ',
   'A two-seat sofa seen from the front, soft red upholstery, two cushions, rounded armrests, short wooden legs'],
  ['f_armchair', 'ДЗ 1 бл. 3, 4, 13 · Тест бл. 2', 'ПРЕДМЕТ',
   'A single comfy armchair seen at a slight angle, green upholstery, wide soft armrests, short wooden legs'],
  ['f_table', 'ДЗ 1 бл. 3, 4, 13', 'ПРЕДМЕТ',
   'A small wooden table with four straight legs seen at a slight angle, light warm wood, empty table top'],
  ['f_wardrobe', 'ДЗ 1 бл. 3, 4, 13 · Тест бл. 2', 'ПРЕДМЕТ',
   'A tall two-door wooden wardrobe, doors closed, two round handles, one drawer at the bottom'],
  ['f_mirror', 'ДЗ 1 бл. 3, 4, 13 · Тест бл. 2', 'ПРЕДМЕТ',
   'An oval standing mirror in a golden frame on a small stand, the glass pale blue and empty with a soft highlight'],
  ['f_rug', 'ДЗ 1 бл. 3, 4, 13 · Тест бл. 2', 'ПРЕДМЕТ',
   'A rectangular rug lying flat, seen from above at a slight angle, purple with a simple pattern of circles and short fringes on two edges'],
  ['f_lamp', 'ДЗ 1 бл. 3, 4, 13', 'ПРЕДМЕТ',
   'A table lamp with a round yellow lampshade on a slim metal stand and a small round base, switched on'],
  ['f_poster', 'ДЗ 1 бл. 3, 4, 13', 'ПРЕДМЕТ',
   'A poster in a thin frame hanging on a plain wall, the picture on it is a rocket flying among stars, no writing anywhere'],

  ['mat_wood', 'ДЗ 6 бл. 3', 'ПРЕДМЕТ',
   'A short log of wood with two planks lying beside it, warm brown wood with visible grain and rings'],
  ['mat_metal', 'ДЗ 6 бл. 3', 'ПРЕДМЕТ',
   'A shiny silver metal spoon and a small metal key lying side by side, cool grey surfaces with bright highlights'],
  ['mat_plastic', 'ДЗ 6 бл. 3', 'ПРЕДМЕТ',
   'A bright blue plastic bottle standing next to a small red plastic cup, smooth glossy plastic surfaces'],
  ['mat_glass', 'ДЗ 6 бл. 3', 'ПРЕДМЕТ',
   'A clear empty drinking glass next to a small transparent glass jar, pale blue-green transparent glass with bright highlights'],
  ['mat_fabric', 'ДЗ 6 бл. 3', 'ПРЕДМЕТ',
   'A folded piece of soft cloth with a small ball of wool beside it, warm red and orange fabric with visible soft texture'],

  ['ap_this', 'ДЗ 2 бл. 7', 'СЦЕНА',
   'A plain room with a wooden table. A child’s hand comes in from the left and points at ONE big red apple lying on the table right beside the hand, very close to the viewer. Keep exactly the same room, table and camera angle in all four apple pictures'],
  ['ap_that', 'ДЗ 2 бл. 7', 'СЦЕНА',
   'The same plain room, table and camera angle. A child’s hand comes in from the left in the foreground and points far away at ONE small red apple lying on the table at the back of the room'],
  ['ap_these', 'ДЗ 2 бл. 7', 'СЦЕНА',
   'The same plain room, table and camera angle. A child’s hand comes in from the left and points at THREE big red apples lying together on the table right beside the hand, very close to the viewer'],
  ['ap_those', 'ДЗ 2 бл. 7', 'СЦЕНА',
   'The same plain room, table and camera angle. A child’s hand comes in from the left in the foreground and points far away at THREE small red apples lying on the table at the back of the room'],

  ['t_reading', 'Тест бл. 10', 'СЦЕНА',
   'A boy’s bedroom seen from the doorway: in the middle a bed with a light wooden frame, on the left a shelf full of colourful books, further away on the right a big soft armchair, and in the foreground on the floor a pair of trainers with two small toy cars beside them'],
  ['t_speaking', 'Тест бл. 12', 'СЦЕНА',
   'Two pictures of the same bedroom side by side, separated by a thin vertical line, with five differences between them: the bed is orange on the left and blue on the right; there is a rug on the left and no rug on the right; the lamp stands on the table on the left and on the floor on the right; there are three books on the shelf on the left and two on the right; the poster shows a rocket on the left and a car on the right'],
];

const NICE = [
  ['m_bed', 'ДЗ 7 бл. 9, вопрос 1', 'ПРЕДМЕТ',
   'A single bed with a white painted metal frame with thin round bars at the head and foot, made up with a grey fabric duvet and a grey pillow'],
  ['m_mirror', 'ДЗ 7 бл. 9, вопрос 2', 'ПРЕДМЕТ',
   'A tall standing mirror in a carved golden wooden frame, the glass empty with a soft highlight'],
  ['m_armchair', 'ДЗ 7 бл. 9, вопрос 3', 'ПРЕДМЕТ',
   'An armchair with a wooden frame and wooden armrests and a dark red fabric seat and back'],
  ['m_lamp', 'ДЗ 7 бл. 9, вопрос 4', 'ПРЕДМЕТ',
   'A desk lamp with a black plastic head and a bent silver metal neck on a black plastic base'],
  ['my_things', 'ДЗ 6 бл. 11', 'СЦЕНА',
   'Five objects standing in a row on a plain floor: a table with a clear glass top and wooden legs, a red plastic chair, a silver metal desk lamp, a round mirror in a white frame, and an armchair with a wooden frame and patterned fabric'],
  ['w_wardrobe', 'ДЗ 2 бл. 11', 'ПРЕДМЕТ',
   'A tall two-door wardrobe standing wide open, clothes on hangers inside and a row of shoes at the bottom'],
  ['w_chair', 'ДЗ 2 бл. 12', 'ПРЕДМЕТ',
   'A single wooden chair with a tall slatted back, seen at a slight angle'],
  ['w_posters', 'ДЗ 2 бл. 13', 'ПРЕДМЕТ',
   'Three colourful posters hanging side by side on a plain wall, the pictures on them are a rocket, a dinosaur and a football, no writing anywhere'],
  ['w_lamps', 'ДЗ 2 бл. 14', 'СЦЕНА',
   'Four different table lamps standing in a row, each with a differently shaped lampshade, all switched off'],
  ['room_boy', 'ДЗ 1 бл. 10', 'СЦЕНА',
   'A cheerful boy’s bedroom: a bed with a blue blanket, a desk with a lamp, a bookshelf, a rug on the floor and a poster on the wall'],
  ['room_photo', 'ДЗ 5 бл. 10', 'СЦЕНА',
   'A bright child’s bedroom seen from the doorway: a bed under the window, a wardrobe, a small table with a lamp and a green rug on the floor'],
  ['room_real', 'ДЗ 6 бл. 12', 'СЦЕНА',
   'A tidy child’s bedroom: a wooden bed, a table with a glass top, a metal lamp, a mirror on the wall and a striped rug on the floor'],
  ['dream_room', 'ДЗ 7 бл. 10', 'СЦЕНА',
   'A pink and white dream bedroom: a white wooden bed, a pink chair beside it, a small table with a white lamp standing on it, soft pink walls'],
  ['dream_room2', 'ДЗ 7 бл. 11', 'СЦЕНА',
   'An unusual dream bedroom for a child: a bed built like a little wooden house with a ladder up to it, round windows and warm glowing lamps'],
];

const KEEP = [
  ['card_room · card_this · card_whose · card_tidy · card_materials',
   'Ваши обучающие карточки уроков — их вы делали сами'],
  ['rule_apples',
   'Таблица-правило This / That / These / Those из выгрузки — на неё ссылается задание'],
  ['story_1 · story_2',
   'Комикс истории «Tidy Up!», восемь кадров с репликами — это текст для чтения в ДЗ 4'],
  ['squirrels · materials_five · lines_whose · two_rooms · family',
   'Картинки, на которых стоят точки или по которым сверяются ответы; перерисовать — значит сдвинуть все точки'],
  ['video_room · video_room3 · mess_room · flash_room',
   'Кадры из видео и иллюстрации к ним'],
  ['point_six · point_near_far',
   'Картинки «рука у предмета / рука вдали» — от них зависят ответы в ДЗ 2'],
  ['room_my · t_bedroom · t_skateboard · t_football · t_pictures · t_socks',
   'Картинки заданий из учебника: по ним ученик заполняет пропуски и выбирает вариант'],
];

const CM = ['Имя файла', 'Где используется', 'Стиль', 'Промпт'];
const WM = [1900, 2600, 1100, 8800];

const CK = ['Файлы', 'Почему не трогаем'];
const WK = [6000, 8400];

const children = [
  h1('Super Minds 2 · Unit 5 · My room — промпты на картинки'),
  p('Полный лист: всё, что нужно нарисовать для юнита, в одном стиле. Формат webp, класть в папку media/sm2/u5/ — имена файлов важны, под ними урок ищет картинку.', { after: 100 }),
  p('Как только файлы будут у вас — пришлите их, и я впишу картинки в блоки: в ДЗ 1 бл. 13 и Тесте бл. 2 «найди пару» переключу с перевода на картинки, в ДЗ 2 бл. 7 заменю мои вырезки, в Тесте бл. 12 поставлю свою картинку вместо взятой из ДЗ 3.', { after: 100 }),
  p('Составлено 17.09.2026.', { i: true, after: 240 }),

  h2('Две строки стиля — добавляйте к каждому промпту'),
  p('Для отдельных предметов (в таблицах помечено ПРЕДМЕТ):', { b: true, after: 60 }),
  p(OBJ, { i: true, after: 140 }),
  p('Для сцен и комнат (помечено СЦЕНА):', { b: true, after: 60 }),
  p(SCENE, { i: true, after: 140 }),
  p('Размеры: предмет 300–420 px по ширине, сцена 760–900 px. Качество webp 88 там, где на картинке есть мелкие детали, 80 для остального — если удобнее, присылайте png, я сама пережму.', { after: 60 }),
  gap(),

  h2('1. Обязательные — 20 картинок'),
  p('Этих картинок в выгрузке нет совсем. Сейчас уроки работают без них: карточки идут на тексте и озвучке, два «найди пару» я собрала на переводе, к яблокам поставила вырезки из таблицы-правила, к SPEAKING в тесте — картинку с двумя комнатами из ДЗ 3. Всё это временно.', { after: 140 }),
  table(CM, WM, MUST),
  gap(),

  h2('2. По желанию — 14 картинок, чтобы юнит был в одном стиле'),
  p('Здесь в выгрузке стояли стоковые фотографии, и они выбиваются из стиля остальных картинок. Ответы от замены не пострадают: это либо иллюстрации, либо предметы, про которые вопрос «из чего сделано» — материалы в промптах прописаны те же, что в правильных ответах.', { after: 140 }),
  table(CM, WM, NICE),
  gap(),

  h2('3. Не перерисовывать'),
  p('Это материал самих заданий. Если их заменить, разойдутся ответы и сдвинутся точки на картинках.', { after: 140 }),
  table(CK, WK, KEEP),
  gap(),

  h2('На что смотреть после генерации'),
  p('• Четыре картинки с яблоками должны быть в одной комнате и с одного ракурса — иначе ученик будет выбирать по фону, а не по расстоянию.', { after: 60 }),
  p('• В t_speaking отличия должны быть ровно те, что перечислены: задание проверяет учитель на слух, но пример в тексте — «This bed is orange» — опирается на первое отличие.', { after: 60 }),
  p('• В t_reading должны быть видны кровать, книги на полке, кресло подальше и туфли с машинками поближе — по ним ученик выбирает this / that / these / those.', { after: 60 }),
  p('• У предметов проверьте поля по краям: генератор любит упирать фигуру в край и срезать её.'),
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

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('SM2_Unit_5_промпты_на_картинки.docx', b);
  console.log('docx готов,', Math.round(b.length / 1024), 'КБ');
});

// готовые к копированию промпты — стиль уже подставлен
const lines = [];
for (const [title, rows] of [['ОБЯЗАТЕЛЬНЫЕ', MUST], ['ПО ЖЕЛАНИЮ', NICE]]) {
  lines.push('='.repeat(70), title, '='.repeat(70), '');
  for (const [name, where, style, prompt] of rows) {
    lines.push(`--- ${name}.webp   (${where})`);
    lines.push(prompt + '. ' + (style === 'ПРЕДМЕТ' ? OBJ : SCENE));
    lines.push('');
  }
}
fs.writeFileSync('SM2_Unit_5_промпты.txt', lines.join('\n'));
console.log('txt готов,', MUST.length + NICE.length, 'промптов');
