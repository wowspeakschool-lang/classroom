const pptxgen = require("pptxgenjs");
const React = require("react");
const RDS = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");
const { applyTheme } = require("/root/.claude/skills/synced/2db1ff95-891a-4c1f-a667-46b28ba5f10e_087417d9-ead4-4ae0-a8a5-b0fa77517268/pptx/scripts/apply_theme.js");

const OUT = process.argv[2];
const THEME = {
  name: "Olympiad Spotlight",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B2340", lt1: "FFFFFF", dk2: "1F2A55", lt2: "EEF1F8",
    accent1: "C8102E", accent2: "1F2A55", accent3: "F2B705", accent4: "5B6B95",
    accent5: "2E8B57", accent6: "8A94B3", hlink: "1F2A55", folHlink: "5B6B95",
  },
};
const NAVY = "1F2A55", RED = "C8102E", GOLD = "F2B705", TINT = "EEF1F8", MUTED = "5B6B95", GREEN = "2E8B57";

async function icon(Comp, color, px = 256) {
  const svg = RDS.renderToStaticMarkup(React.createElement(Comp, { color: "#" + color, size: px }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10 x 5.625
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = "Олимпиада Spotlight — паспорт проекта";
  const C = pres.SchemeColor;

  pres.defineSlideMaster({
    title: "TITLE_DARK",
    background: { color: NAVY },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 1.5, w: 8.8, h: 1.3, fontSize: 40, bold: true, color: "FFFFFF", fontFace: "Cambria", valign: "bottom", align: "left", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "body", type: "body", x: 0.6, y: 3.0, w: 8.8, h: 1.2, fontSize: 18, color: "DDE3F2", fontFace: "Calibri", valign: "top", align: "left", margin: 0 }, text: "" } },
    ],
  });
  pres.defineSlideMaster({
    title: "CONTENT",
    background: { color: "FFFFFF" },
    margin: [0.5, 0.5, 0.5, 0.5],
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.35, w: 9, h: 0.75, fontSize: 30, bold: true, color: NAVY, fontFace: "Cambria", valign: "middle", margin: 0 }, text: "" } },
    ],
    slideNumber: { x: 9.2, y: 5.2, w: 0.5, h: 0.3, fontSize: 10, color: MUTED },
  });

  const I = {
    book: await icon(fa.FaBookOpen, "FFFFFF"),
    users: await icon(fa.FaUserGraduate, "FFFFFF"),
    cal: await icon(fa.FaCalendarAlt, "FFFFFF"),
    laptop: await icon(fa.FaLaptopHouse, "FFFFFF"),
    head: await icon(fa.FaHeadphones, "FFFFFF"),
    read: await icon(fa.FaBook, "FFFFFF"),
    puzzle: await icon(fa.FaPuzzlePiece, "FFFFFF"),
    globe: await icon(fa.FaGlobeEurope, "FFFFFF"),
    pen: await icon(fa.FaPenNib, "FFFFFF"),
    mic: await icon(fa.FaMicrophone, "FFFFFF"),
    trophy: await icon(fa.FaTrophy, GOLD),
    clock: await icon(fa.FaClock, NAVY),
    check: await icon(fa.FaCheck, "FFFFFF"),
    q: await icon(fa.FaQuestion, "FFFFFF"),
  };
  const circle = (s, x, y, d, fill, img, name) => {
    s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill }, objectName: name + " circle" });
    const p = d * 0.26;
    s.addImage({ data: img, x: x + p, y: y + p, w: d - 2 * p, h: d - 2 * p, objectName: name + " icon" });
  };
  const T = (s, text, o) => s.addText(text, Object.assign({ isTextBox: true, fontFace: "Calibri", color: "1B2340", margin: 0, valign: "top" }, o));

  // 1. Title
  pres.addSection({ title: "Проект" });
  let s = pres.addSlide({ masterName: "TITLE_DARK", sectionTitle: "Проект" });
  s.addText("Олимпиада по английскому Spotlight", { placeholder: "title" });
  s.addText("Паспорт проекта · пилот 5–9 классы · январь 2027", { placeholder: "body" });
  s.addImage({ data: I.trophy, x: 8.3, y: 0.5, w: 1.1, h: 1.1, objectName: "trophy" });
  s.addNotes("Короткое обсуждение: что делаем, что уже решено и три вопроса, которые нужно решить.");

  // 2. What & why — 4 cards
  s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Проект" });
  s.addText("Что делаем", { placeholder: "title" });
  const cards = [
    [I.book, "Что", "Онлайн-олимпиада по учебникам Spotlight"],
    [I.users, "Для кого", "Ученики 5–9 классов, пройти могут и друзья"],
    [I.cal, "Когда", "Вторая половина января 2027, итоги до 31 января"],
    [I.laptop, "Где", "Платформа app.wowteach.ru, из дома"],
  ];
  cards.forEach((c, i) => {
    const x = 0.5 + i * 2.3, y = 1.35, w = 2.05, h = 2.6;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: TINT }, line: { color: TINT }, objectName: "card " + c[1] });
    circle(s, x + 0.25, y + 0.25, 0.7, i % 2 ? RED : NAVY, c[0], c[1]);
    T(s, c[1], { x: x + 0.25, y: y + 1.1, w: w - 0.5, h: 0.4, fontSize: 18, bold: true, color: NAVY, fontFace: "Cambria" });
    T(s, c[2], { x: x + 0.25, y: y + 1.55, w: w - 0.45, h: 1.0, fontSize: 14 });
  });
  T(s, "Зачем: признание для учеников, интерес к языку и культуре, проверка формата, знакомство новых детей со школой", { x: 0.5, y: 4.3, w: 9, h: 0.6, fontSize: 14, italic: true, color: MUTED });

  // 3. Decided — checklist two columns
  s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Проект" });
  s.addText("Что уже решено", { placeholder: "title" });
  const done = [
    "Свой комплект заданий на каждый класс",
    "Онлайн из дома: окно 1–2 дня, таймер, одна попытка",
    "Без созвонов, апелляций и показа работ",
    "После закрытия ученик видит свои ответы и правильные",
    "Только пройденное по Spotlight",
    "Ориентир — ВсОШ, в облегчённом виде",
  ];
  done.forEach((t, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 0.5 + col * 4.6, y = 1.35 + row * 1.15;
    circle(s, x, y, 0.5, GREEN, I.check, "done " + i);
    T(s, t, { x: x + 0.7, y: y - 0.02, w: 3.7, h: 0.9, fontSize: 16, valign: "middle" });
  });

  // 4. Sections
  pres.addSection({ title: "Олимпиада" });
  s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Олимпиада" });
  s.addText("Разделы", { placeholder: "title" });
  const secs = [
    [I.head, "Аудирование", "5–9", true], [I.read, "Чтение", "5–9", true], [I.puzzle, "Use of English", "5–9", true],
    [I.globe, "Страноведение", "5–9", true], [I.pen, "Письмо", "5–9", false], [I.mic, "Устная часть", "7–9", false],
  ];
  secs.forEach((c, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.5 + col * 3.05, y = 1.3 + row * 1.6, w = 2.85, h = 1.4;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: c[3] ? TINT : "FCE8EB" }, line: { color: c[3] ? TINT : "FCE8EB" }, objectName: "section " + c[1] });
    circle(s, x + 0.2, y + 0.35, 0.7, c[3] ? NAVY : RED, c[0], c[1]);
    T(s, c[1], { x: x + 1.05, y: y + 0.3, w: 1.75, h: 0.4, fontSize: 14, bold: true, color: NAVY, fontFace: "Cambria" });
    T(s, c[2] + " кл. · " + (c[3] ? "автопроверка" : "проверяет человек"), { x: x + 1.05, y: y + 0.75, w: 1.75, h: 0.5, fontSize: 12, color: MUTED });
  });
  T(s, "Страноведение: культура, история, символы — «что это за здание?» (Big Ben), «чей это флаг?»", { x: 0.5, y: 4.6, w: 9, h: 0.45, fontSize: 13, italic: true, color: MUTED });

  // 5. Time & awards — big stats
  s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Олимпиада" });
  s.addText("Время и награды", { placeholder: "title" });
  const stats = [["40 мин", "5–6 классы"], ["60 мин", "7–9 классы"], ["+15–20", "минут запаса в таймере"]];
  stats.forEach((st, i) => {
    const x = 0.5 + i * 1.95;
    T(s, st[0], { x, y: 1.4, w: 1.85, h: 0.8, fontSize: 34, bold: true, color: i === 2 ? RED : NAVY, fontFace: "Cambria" });
    T(s, st[1], { x, y: 2.25, w: 1.75, h: 0.6, fontSize: 13, color: MUTED });
  });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 6.5, y: 1.3, w: 3.0, h: 3.4, rectRadius: 0.12, fill: { color: NAVY }, line: { color: NAVY }, objectName: "awards card" });
  s.addImage({ data: I.trophy, x: 6.75, y: 1.5, w: 0.7, h: 0.7, objectName: "awards icon" });
  T(s, [
    { text: "1, 2, 3 места", options: { bold: true, fontSize: 18, breakLine: true } },
    { text: "в каждом классе", options: { fontSize: 14, breakLine: true } },
    { text: " ", options: { fontSize: 8, breakLine: true } },
    { text: "Сертификат", options: { bold: true, fontSize: 18, breakLine: true } },
    { text: "каждому участнику", options: { fontSize: 14, breakLine: true } },
    { text: " ", options: { fontSize: 8, breakLine: true } },
    { text: "В списке: «Маша К., 6 класс»", options: { fontSize: 13, italic: true } },
  ], { x: 6.75, y: 2.35, w: 2.6, h: 2.2, color: "FFFFFF" });
  s.addImage({ data: I.clock, x: 0.5, y: 3.35, w: 0.45, h: 0.45, objectName: "clock" });
  T(s, "Задания рассчитаны на 40 и 60 минут, а таймер стоит с запасом, чтобы ребёнок не торопился", { x: 1.1, y: 3.3, w: 4.9, h: 0.9, fontSize: 14 });

  // 6. Decide — 3 questions
  pres.addSection({ title: "Решения" });
  s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Решения" });
  s.addText("Что нужно решить", { placeholder: "title" });
  const qs = [
    ["1. Туры", [["Предлагаю: один тур", true], ["пилотный поток, укладываемся в январь", false], ["Вариант: два тура, во второй — лучшие", false]]],
    ["2. Ручная проверка", [["а) письмо и устная часть", false], ["б) только письмо, проверяет Claude", false], ["в) только автопроверка", false]]],
    ["3. Гости олимпиады", [["Не наши ученики проходят по ссылке друга", false], ["Идея: регистрация и приглашение в школу", true], ["нужно согласие родителей", false]]],
  ];
  qs.forEach((q, i) => {
    const x = 0.5 + i * 3.05, y = 1.3, w = 2.85, h = 3.5;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: TINT }, line: { color: TINT }, objectName: "question " + (i + 1) });
    circle(s, x + 0.2, y + 0.2, 0.55, RED, I.q, "q" + i);
    T(s, q[0], { x: x + 0.2, y: y + 0.9, w: w - 0.3, h: 0.45, fontSize: 16, bold: true, color: NAVY, fontFace: "Cambria" });
    T(s, q[1].map((r, k) => ({ text: r[0], options: { bold: r[1], bullet: true, breakLine: k < q[1].length - 1, paraSpaceAfter: 6 } })),
      { x: x + 0.2, y: y + 1.45, w: w - 0.35, h: 1.9, fontSize: 14 });
  });

  // 7. Plan — timeline
  s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Решения" });
  s.addText("План до 31 января", { placeholder: "title" });
  const steps = [["Концепция", "конец ноября"], ["Задания", "середина декабря"], ["Вычитка", "до 25 декабря"], ["Сборка", "до 31 декабря"], ["Прогон", "11–15 января"], ["Олимпиада", "вторая половина января"], ["Итоги", "до 31 января"]];
  s.addShape(pres.shapes.LINE, { x: 0.8, y: 2.0, w: 8.4, h: 0, line: { color: "C9CFE0", width: 2 }, objectName: "timeline" });
  steps.forEach((st, i) => {
    const cx = 0.8 + i * 1.4;
    const hl = i === 5;
    s.addShape(pres.shapes.OVAL, { x: cx - 0.2, y: 1.8, w: 0.4, h: 0.4, fill: { color: hl ? RED : NAVY }, line: { color: "FFFFFF", width: 2 }, objectName: "step " + st[0] });
    T(s, st[0], { x: cx - 0.65, y: 2.4, w: 1.3, h: 0.4, fontSize: 14, bold: true, align: "center", color: hl ? RED : NAVY });
    T(s, st[1], { x: cx - 0.65, y: 2.8, w: 1.3, h: 0.7, fontSize: 11, align: "center", color: MUTED });
  });
  T(s, "Главный риск: умеет ли платформа ставить таймер, открывать олимпиаду на заданное окно и показывать ответы после закрытия. Проверяем заранее", { x: 0.5, y: 3.9, w: 9, h: 0.7, fontSize: 14, italic: true, color: MUTED });

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("written", OUT);
})();
