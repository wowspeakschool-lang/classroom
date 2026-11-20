// Программа курса Reading Club 10+ → pptx (по образцу программы SM0)
const pptxgen = require('pptxgenjs');
const { applyTheme } = require(process.env.SK + '/scripts/apply_theme.js');
const path = require('path');
const THEME = { name: 'Reading Club 10+', headFontFace: 'Trebuchet MS', bodyFontFace: 'Calibri',
  colors: { dk1: '20313B', lt1: 'FFFFFF', dk2: '0A5C86', lt2: 'F2FAFE', accent1: '1CA3DE', accent2: '6C3DE0',
            accent3: 'EE9A2B', accent4: 'E8553E', accent5: '5FB81F', accent6: '5C6B73', hlink: '1CA3DE', folHlink: '6C3DE0' } };
const pres = new pptxgen(); pres.layout = 'LAYOUT_WIDE'; pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = 'Reading Club 10+ — программа курса'; pres.author = 'WowSpeak';
const C = pres.SchemeColor;
const TYPE = { 'Новые звуки': C.accent1, 'Алфавит': C.accent3, 'Magic e': C.accent2, 'Сочетания': C.accent2, 'Повторение + тест': C.accent4 };
const TINT = { 'Новые звуки': 'DFF3FC', 'Алфавит': 'FDF0DD', 'Magic e': 'EDE6FF', 'Сочетания': 'EDE6FF', 'Повторение + тест': 'FCE3DE' };

pres.defineSlideMaster({ title: 'TITLE', background: { color: C.background2 },
  objects: [ { ellipse: { x: -1.2, y: -1.4, w: 4.2, h: 4.2, fill: { color: C.accent1, transparency: 80 }, line: { type: 'none' } } },
             { ellipse: { x: 10.6, y: 4.6, w: 4.2, h: 4.2, fill: { color: C.accent5, transparency: 82 }, line: { type: 'none' } } },
             { ellipse: { x: 9.6, y: -0.9, w: 2.4, h: 2.4, fill: { color: C.accent3, transparency: 82 }, line: { type: 'none' } } },
             { placeholder: { options: { name: 'title', type: 'title', x: 0.9, y: 1.5, w: 11, h: 1.0, fontSize: 48, bold: true, color: C.accent1, fontFace: 'Trebuchet MS', margin: 0, align: 'left' }, text: '' } },
             { placeholder: { options: { name: 'body', type: 'body', x: 0.9, y: 2.5, w: 11, h: 0.5, fontSize: 18, italic: true, color: C.text2, margin: 0, align: 'left' }, text: '' } } ] });
pres.defineSlideMaster({ title: 'CONTENT', background: { color: C.background1 },
  objects: [ { placeholder: { options: { name: 'title', type: 'title', x: 0.5, y: 0.3, w: 12.3, h: 0.6, fontSize: 28, bold: true, color: C.text2, fontFace: 'Trebuchet MS', margin: 0, align: 'left' }, text: '' } },
             { placeholder: { options: { name: 'body', type: 'body', x: 0.5, y: 0.92, w: 12.3, h: 0.4, fontSize: 13, color: C.accent6, margin: 0, align: 'left' }, text: '' } },
             { text: { text: 'Reading Club 10+ · программа курса', options: { x: 0.5, y: 7.05, w: 6, h: 0.3, fontSize: 10, color: C.accent6, margin: 0 } } } ],
  slideNumber: { x: 12.3, y: 7.05, w: 0.5, h: 0.3, fontSize: 10, color: C.accent6 } });

// ---------- 1. Титул ----------
pres.addSection({ title: 'Обзор' });
let s = pres.addSlide({ masterName: 'TITLE', sectionTitle: 'Обзор' });
s.addText('Reading Club 10+', { placeholder: 'title' });
s.addText('Курс чтения для 10–12 лет · программа курса · история «Код»', { placeholder: 'body' });
const cards = [ ['Phase A · Звуки букв (по 5)', 'L1 → L5 · все 26 букв', C.accent1],
                ['Алфавит + Magic e', 'L6 – L7 · имена букв, одно правило', C.accent3],
                ['Phase B · Сочетания', 'L8 – L9 · sh ch th · ee oo ar', C.accent2] ];
cards.forEach(([a, b, col], i) => {
  const x = 0.9 + i * 3.75;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 3.4, w: 3.5, h: 1.25, rectRadius: 0.12, fill: { color: C.background1 }, line: { color: col, width: 1.5 }, objectName: 'card' + i });
  s.addText([{ text: a, options: { bold: true, color: col, fontSize: 16, breakLine: true } }, { text: b, options: { color: C.accent6, fontSize: 13 } }],
    { x: x + 0.2, y: 3.5, w: 3.1, h: 1.05, valign: 'middle', isTextBox: true, margin: 0 });
});
s.addText('10 уроков · 30 / 40 минут · онлайн · ЧТЕНИЕ — большая часть каждого урока', { x: 0.9, y: 5.0, w: 11, h: 0.4, fontSize: 15, bold: true, color: C.text1, isTextBox: true, margin: 0 });
s.addText('Для учеников 10–12 лет, которые не читают. Герои Sam и Dan расшифровывают записки: каждый урок открывает новые символы шифра. После курса — Go Getter.',
  { x: 0.9, y: 5.45, w: 10.5, h: 0.7, fontSize: 14, color: C.accent6, isTextBox: true, margin: 0 });

// ---------- 2–3. Карта курса ----------
const L = [
 ['L1', 'Новые звуки', 's a t p i', 'sat, tap, pit, tip', 'I', 'I sat. Tap it.', 'Записка из значков на шкафчике; Агент X: «прочитать могут только те, кто знает код»'],
 ['L2', 'Новые звуки', 'n m d o g', 'man, dog, dig, pond', 'the', 'Sam and Dan: dig in the pit!', 'Надпись на стене двора — ребята читают свои имена'],
 ['L3', 'Новые звуки', 'c k e u r', 'cat, kid, pen, sun, red', 'said, are, you', 'Run! Get the red cup.', 'Записка под красной кружкой в столовой'],
 ['L4', 'Новые звуки', 'h b f l j', 'hat, bus, fun, leg, jam', 'is, he, she, to', 'Get on the big red bus. Sit at the top.', 'Подсказка на автобусной остановке'],
 ['L5', 'Новые звуки', 'v w x y z qu', 'van, wet, box, yes, zip, quiz', 'was, my, go, no', 'Zip up the box. It is in the van.', 'Коробка в фургоне · все 26 букв открыты'],
 ['L6', 'Алфавит', 'имена букв, A → Z', 'гласные a e i o u · S-A-M · TV, PE, DJ', '—', 'From A to Z.', 'Мастер-ключ: открыты все 26 символов'],
 ['L7', 'Magic e', 'a_e · i_e · o_e · u_e', 'tape, pine, hope, cube, bike', 'have, one', 'Hide the code at nine. Take the bike.', 'Немая буква: e гаснет, гласная говорит своё имя'],
 ['L8', 'Сочетания', 'sh · ch · th', 'ship, fish, chip, thin, this', 'do, some, come', 'Shh! Chat at the chip shop. Then run!', 'Двойные коды: два символа склеены — новый звук'],
 ['L9', 'Сочетания', 'ee · oo · ar', 'tree, moon, book, car, park', 'your, who', 'Meet at the park at noon. Look at the green car.', 'Встреча в парке — разгадка близко'],
 ['L10', 'Повторение + тест', 'всё пройденное', 'итоговый текст · тест', 'все', 'You did it! Come to the club!', 'Агент X — старшеклассница, ведёт клуб дешифровщиков · сертификат'],
];
const hdr = ['Урок', 'Тип урока', 'Звуки → слова', 'Слова-исключения', 'Сообщение урока · сюжет'].map((t, i) => ({ text: t, options: { bold: true, color: C.text2, fontSize: 12, fill: { color: i === 4 ? 'EDE6FF' : C.background1 }, border: [{ type: 'none' }, { type: 'none' }, { pt: 1.5, color: C.text2 }, { type: 'none' }] } }));
function mapSlide(part, rows) {
  const sl = pres.addSlide({ masterName: 'CONTENT', sectionTitle: 'Карта курса' });
  sl.addText('Карта курса · 10 уроков', { placeholder: 'title' });
  sl.addText(`Часть ${part} / 2 · ${part === 1 ? 'L1 – L5 · звуки всех 26 букв' : 'L6 – L10 · алфавит, Magic e, сочетания, итог'}`, { placeholder: 'body' });
  const data = [hdr];
  rows.forEach(r => {
    const [n, type, snd, words, tw, msg, plot] = r; const col = TYPE[type];
    const bd = [{ type: 'none' }, { type: 'none' }, { pt: 0.75, color: 'CFE6F4' }, { type: 'none' }];
    data.push([
      { text: n, options: { bold: true, color: C.background1, fill: { color: col }, align: 'center', fontSize: 16, border: bd } },
      { text: type, options: { bold: true, color: col, fill: { color: TINT[type] }, fontSize: 12, border: bd } },
      { text: [{ text: snd, options: { bold: true, fontSize: 14, color: C.text1, breakLine: true } }, { text: words, options: { fontSize: 11.5, color: C.accent6 } }], options: { border: bd } },
      { text: tw, options: { fontSize: 12, color: C.text1, border: bd } },
      { text: [{ text: msg, options: { bold: true, fontSize: 12, color: C.accent2, breakLine: true } }, { text: plot, options: { fontSize: 11, color: C.accent6 } }], options: { fill: { color: 'EDE6FF' }, border: bd } },
    ]);
  });
  sl.addTable(data, { x: 0.5, y: 1.45, w: 12.3, colW: [0.75, 1.75, 3.1, 1.9, 4.8], rowH: [0.4, 1.0, 1.0, 1.0, 1.0, 1.0], valign: 'middle', margin: [0.04, 0.1, 0.04, 0.1], fontFace: 'Calibri', objectName: 'map' + part });
}
pres.addSection({ title: 'Карта курса' });
mapSlide(1, L.slice(0, 5)); mapSlide(2, L.slice(5));

// ---------- 4. Прогрессия чтения ----------
pres.addSection({ title: 'Методика' });
s = pres.addSlide({ masterName: 'CONTENT', sectionTitle: 'Методика' });
s.addText('Прогрессия чтения', { placeholder: 'title' });
s.addText('Чтение — большая часть каждого урока. Каждый урок кончается текстом только из пройденного: ученик читает сам, а не угадывает.', { placeholder: 'body' });
const bands = [
 ['PHASE A', 'Звуки букв · по 5', 'L1 → L5', C.accent1, 'Все 26 букв как ЗВУКИ: «This is c. Sound /k/.» Имя буквы не прячем, но и не разбираем. Слияние с первого урока: sat → dig → red → bus → zip. У каждой буквы одно слово-якорь с картинкой.'],
 ['ABC', 'Алфавит', 'L6', C.accent3, 'Имена букв, порядок A → Z, пять гласных — ПОСЛЕ звуков. Разница «звук и имя» — мост к Magic e.'],
 ['MAGIC E', 'Одно правило', 'L7', C.accent2, 'a_e · i_e · o_e · u_e одним правилом: e в конце молчит, гласная говорит своё имя. tap → tape, pin → pine, hop → hope, cub → cube.'],
 ['PHASE B', 'Сочетания · по 3', 'L8 – L9', C.accent2, 'sh · ch · th (thin и this) → ee · oo (moon и book) · ar. В шифре новое сочетание — склейка двух уже открытых символов.'],
];
bands.forEach(([a, b, c, col, txt], i) => {
  const y = 1.5 + i * 1.12;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y, w: 12.3, h: 0.98, rectRadius: 0.08, fill: { color: C.background1 }, line: { color: col, width: 1.25 }, objectName: 'bandbox' + i });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y, w: 2.3, h: 0.98, rectRadius: 0.08, fill: { color: col }, line: { type: 'none' }, objectName: 'band' + i });
  s.addText([{ text: a, options: { bold: true, fontSize: 15, color: C.background1, breakLine: true } }, { text: b, options: { fontSize: 11.5, color: C.background1 } }], { x: 0.65, y, w: 2.05, h: 0.98, valign: 'middle', isTextBox: true, margin: 0 });
  s.addText([{ text: c, options: { bold: true, fontSize: 13, color: col, breakLine: true } }, { text: txt, options: { fontSize: 12.5, color: C.text1 } }], { x: 3.0, y, w: 9.6, h: 0.98, valign: 'middle', isTextBox: true, margin: 0 });
});
s.addText([{ text: 'Итог: ', options: { bold: true } }, { text: '26 букв + алфавит + Magic e + 6 сочетаний · к L10 ученик читает короткий текст (≈ 140 слов). ' },
  { text: 'Не берём ', options: { bold: true } }, { text: '(пойдут в Go Getter 1, по одному в урок): ck ff ll ss · ai/ay · ea · oa/ow · igh/y · or · ur/er/ir · ow/ou · oi/oy · ear air ure · ph wh wr.' }],
  { x: 0.5, y: 6.0, w: 12.3, h: 0.8, fontSize: 12.5, color: C.text1, isTextBox: true, margin: 0 });

// ---------- 5. Как устроен урок ----------
s = pres.addSlide({ masterName: 'CONTENT', sectionTitle: 'Методика' });
s.addText('Как устроен урок', { placeholder: 'title' });
s.addText('Один скелет на уроки 2–10; задания и игры внутри меняются. В режиме 40 минут добавляются экраны из правого столбца.', { placeholder: 'body' });
const ST = [
 ['Mission briefing', 'Сообщение символами, часть ключа — «?»', '1', ''],
 ['Code review', 'Символы; слова-исключения; скороговорка прошлого урока (строки 3–4)', '2', '+3 слова на время, личный рекорд'],
 ['HW check', '1–2 слова, где были ошибки в ДЗ', '1', ''],
 ['New code', '«This is c. Sound /k/.» + слово-якорь с картинкой', '4', ''],
 ['Hear it', 'Устно: первый звук, деление слова на звуки', '2', ''],
 ['Write it', 'Буква со стрелками → в тетради → списать 2 слова', '3', '+2 списать ещё 3 слова'],
 ['Blending', 'Звуки → слово; картинка — после прочтения', '4', '+3 «Настоящее или фейк?»'],
 ['Word building', 'Собрать слово из букв-магнитов', '2', ''],
 ['Tricky words', 'Слова-исключения урока целиком', '2', ''],
 ['Dictation', '4 слова на слух — в тетради', '3', '+2 фраза на слух'],
 ['Decode the message', 'Фразы → сообщение символами → чтение → 2 вопроса', '4', ''],
 ['Code chant', 'Скороговорка урока, строки 1–2 — медленно, потом быстрее', '1', ''],
 ['Mission complete', 'Счётчик слов, что умею, ДЗ, монетки', '1', ''],
];
const bd2 = [{ type: 'none' }, { type: 'none' }, { pt: 0.75, color: 'CFE6F4' }, { type: 'none' }];
const t2 = [['Этап', 'Что происходит', '30', '40 мин +'].map(t => ({ text: t, options: { bold: true, color: C.text2, fontSize: 11.5, border: [{ type: 'none' }, { type: 'none' }, { pt: 1.5, color: C.text2 }, { type: 'none' }] } }))];
ST.forEach(([a, b, c, d], i) => t2.push([
  { text: `${i + 1} · ${a}`, options: { bold: true, fontSize: 11.5, color: C.text1, border: bd2 } },
  { text: b, options: { fontSize: 11.5, color: C.text1, border: bd2 } },
  { text: c, options: { bold: true, fontSize: 12, align: 'center', color: C.accent1, border: bd2 } },
  { text: d, options: { fontSize: 10.5, color: C.accent2, fill: { color: d ? 'EDE6FF' : C.background1 }, border: bd2 } }]));
t2.push([{ text: 'Итого', options: { bold: true, fontSize: 12 } }, { text: '' }, { text: '30', options: { bold: true, align: 'center', fontSize: 12, color: C.accent1 } }, { text: '+10', options: { bold: true, fontSize: 12, color: C.accent2 } }]);
s.addTable(t2, { x: 0.5, y: 1.4, w: 8.6, colW: [2.2, 3.85, 0.55, 2.0], rowH: 0.365, valign: 'middle', margin: [0.02, 0.08, 0.02, 0.08], fontFace: 'Calibri', objectName: 'skeleton' });
const side = [
 ['⭐ If time · 2–3 игры', 'Скоростной дешифратор · Взломщик (слово символами на время) · Поймай звук · Сортировка на слух · Буквы-магниты · Найди слово в сетке. В каждом уроке минимум две интересные игры.', C.accent3, 'FDF0DD'],
 ['Урок 1 — другой', 'Повторять ещё нечего: брифинг длиннее (кто такой Агент X, что такое шифр и ключ), сообщение совсем короткое.', C.accent1, 'DFF3FC'],
 ['Тетрадь и ручка', 'К каждому уроку — сообщаем ученику заранее: письмо идёт лесенкой (буква → списать → собрать → диктант).', C.accent4, 'FCE3DE'],
];
side.forEach(([a, b, col, tint], i) => {
  const y = 1.4 + i * 1.85;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 9.4, y, w: 3.4, h: 1.7, rectRadius: 0.1, fill: { color: tint }, line: { type: 'none' }, objectName: 'side' + i });
  s.addText([{ text: a, options: { bold: true, fontSize: 14, color: col, breakLine: true } }, { text: b, options: { fontSize: 11.5, color: C.text1 } }], { x: 9.6, y: y + 0.1, w: 3.0, h: 1.5, valign: 'top', isTextBox: true, margin: 0 });
});

// ---------- 6. История и шифр ----------
pres.addSection({ title: 'История' });
s = pres.addSlide({ masterName: 'CONTENT', sectionTitle: 'История' });
s.addText('История «Код» и шифр', { placeholder: 'title' });
s.addText('Чтение по-английски — это и есть расшифровка (decoding): ученик не «учит буквы, как малыш», а взламывает код.', { placeholder: 'body' });
s.addText([
  { text: 'Герои', options: { bold: true, color: C.accent1, breakLine: true } },
  { text: 'Sam (Саманта) и Dan, 11–12 лет. В городе кто-то оставляет записки значками. Каждый урок открывает новые символы и приносит сообщение, которое теперь можно прочитать. В финале — кто такой Агент X.', options: { breakLine: true } },
  { text: ' ', options: { fontSize: 6, breakLine: true } },
  { text: 'Ключ', options: { bold: true, color: C.accent1, breakLine: true } },
  { text: 'У каждой буквы свой символ. Внизу экрана — ключ: открытые символы подписаны, закрытые — «?».', options: { breakLine: true } },
  { text: ' ', options: { fontSize: 6, breakLine: true } },
  { text: 'Сочетания и Magic e', options: { bold: true, color: C.accent2, breakLine: true } },
  { text: 'sh — склейка двух уже открытых символов: s + h = один звук. В Magic e символ e «гаснет», от него стрелка к гласной: «скажи своё имя».', options: { breakLine: true } },
  { text: ' ', options: { fontSize: 6, breakLine: true } },
  { text: 'Шифра в уроке — одно короткое сообщение: читает ученик обычными буквами.', options: { italic: true, color: C.accent6 } } ],
  { x: 0.5, y: 1.45, w: 5.6, h: 5.3, fontSize: 13.5, color: C.text1, valign: 'top', isTextBox: true, margin: 0 });
s.addText('Ключ урока 3: открыты s a t p i n m d o g c k e u r', { x: 6.5, y: 1.45, w: 6.3, h: 0.35, fontSize: 12, bold: true, color: C.text2, isTextBox: true, margin: 0 });
s.addImage({ path: path.join(__dirname, 'key_l3.png'), x: 6.5, y: 1.85, w: 6.0, h: 6.0 * 948 / 1860, altText: 'Ключ шифра: открытые символы с буквами и закрытые клетки со знаком вопроса' });
s.addText('Сообщение урока 3 символами → «Run! Get the red cup.»', { x: 6.5, y: 5.15, w: 6.3, h: 0.35, fontSize: 12, bold: true, color: C.text2, isTextBox: true, margin: 0 });
s.addImage({ path: path.join(__dirname, 'msg_l3.png'), x: 6.5, y: 5.55, w: 6.0, h: 6.0 * 168 / 1860, altText: 'Фраза Run! Get the red cup, записанная символами шифра' });
s.addText('Символы — эскиз по мотивам старинного шифра pigpen; финальные нарисуем одним стилем.', { x: 6.5, y: 6.3, w: 6.3, h: 0.4, fontSize: 10.5, italic: true, color: C.accent6, isTextBox: true, margin: 0 });

// ---------- 7. Вокруг курса ----------
pres.addSection({ title: 'Вокруг курса' });
s = pres.addSlide({ masterName: 'CONTENT', sectionTitle: 'Вокруг курса' });
s.addText('До и после курса', { placeholder: 'title' });
s.addText('Кто идёт на курс · итоговый тест · мотивация · что дальше', { placeholder: 'body' });
const box = [
 ['Кто идёт на курс', 'Уровень определяют на вводном уроке. На курс идут все, кто не знает букв или не умеет читать, и начинают с L1 — отдельной входной проверки нет.', C.accent1, 'DFF3FC'],
 ['Итоговый тест · L10', 'Чтение слов и выдуманных слов, сочетания и Magic e, диктант 5 слов, чтение короткого текста с вопросами. Сертификат дешифровщика.', C.accent4, 'FCE3DE'],
 ['Мотивация', 'Счётчик слов в конце урока («теперь ты читаешь 140 слов») · личный рекорд скорости · ранг агента · монетки платформы.', C.accent3, 'FDF0DD'],
 ['Дальше — Go Getter 1', 'Фоника продолжается в GG1 по Genki Phonics: всё, кроме букв алфавита, — по одному сочетанию в урок (ai, oa, igh, or…), прочитать и повторить. Так закрываются и отдельные пробелы.', C.accent5, 'E6F5DA'],
];
box.forEach(([a, b, col, tint], i) => {
  const x = 0.5 + (i % 2) * 6.25, y = 1.55 + Math.floor(i / 2) * 2.35;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 6.05, h: 2.15, rectRadius: 0.1, fill: { color: tint }, line: { type: 'none' }, objectName: 'box' + i });
  s.addText([{ text: a, options: { bold: true, fontSize: 17, color: col, breakLine: true } }, { text: b, options: { fontSize: 15, color: C.text1 } }], { x: x + 0.25, y: y + 0.2, w: 5.55, h: 1.8, valign: 'top', isTextBox: true, margin: 0 });
});

(async () => { const f = path.join(__dirname, 'Программа курса Reading Club 10+.pptx'); await pres.writeFile({ fileName: f }); await applyTheme(f, THEME); console.log('ok'); })();
