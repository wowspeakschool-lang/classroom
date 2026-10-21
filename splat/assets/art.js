/* Splat Kids × WowSpeak — общий набор иллюстраций (SVG-строки).
   ART.tooth({mood:'happy'}) → '<svg …>'. Опция line:true даёт контур для раскраски:
   все заливки белые, обводка чёрная — так одни и те же рисунки идут и в урок, и в печать. */
(function () {
  const COLOR = {
    ink: '#3b2d5c', tooth: '#ffffff', toothShade: '#e3ecff', cheek: '#ffb3cf', gum: '#ff8fb1',
    mint: '#33c7b0', mintD: '#1f9e8b', sky: '#5bb8ff', skyD: '#2f8ee0', pink: '#ff7eb6', pinkD: '#e2559a',
    sun: '#ffd23f', sunD: '#f2a81d', lilac: '#a98bff', lilacD: '#7c5ce0', germ: '#8bd34a', germD: '#5fa82a',
    water: '#7fd3ff', waterD: '#3aa8e8', white: '#ffffff', cloud: '#ffffff', candy: '#ff5a5a',
  };
  const LINE = Object.fromEntries(Object.keys(COLOR).map(k => [k, '#ffffff']));
  LINE.ink = '#222';
  let P = COLOR, SW = 1;

  const svg = (body, vb = '0 0 200 200', cls = '') =>
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}" class="art art-${cls}">${body}</svg>`;
  const st = (w = 5) => `stroke="${P.ink}" stroke-width="${w * SW}" stroke-linejoin="round" stroke-linecap="round"`;
  const isLine = () => P === LINE;

  function face(cx, cy, s = 1, mood = 'happy') {
    const eyeY = cy - 6 * s, dx = 15 * s;
    let eyes;
    if (mood === 'sad') eyes = `<path d="M${cx - dx - 6 * s} ${eyeY - 4 * s} l12 ${4 * s} M${cx + dx + 6 * s} ${eyeY - 4 * s} l-12 ${4 * s}" fill="none" ${st(4)}/>` +
      `<circle cx="${cx - dx}" cy="${eyeY + 4 * s}" r="${4.5 * s}" fill="${P.ink}"/><circle cx="${cx + dx}" cy="${eyeY + 4 * s}" r="${4.5 * s}" fill="${P.ink}"/>`;
    else eyes = [cx - dx, cx + dx].map(x =>
      `<ellipse cx="${x}" cy="${eyeY}" rx="${6 * s}" ry="${7.5 * s}" fill="${P.ink}"/>` +
      (isLine() ? '' : `<circle cx="${x + 2 * s}" cy="${eyeY - 3 * s}" r="${2.4 * s}" fill="#fff"/>`)).join('');
    const mouth = mood === 'sad'
      ? `<path d="M${cx - 10 * s} ${cy + 16 * s} q${10 * s} ${-9 * s} ${20 * s} 0" fill="none" ${st(4)}/>`
      : `<path d="M${cx - 13 * s} ${cy + 8 * s} q${13 * s} ${16 * s} ${26 * s} 0 z" fill="${isLine() ? '#fff' : P.pinkD}" ${st(4)}/>`;
    const cheeks = isLine() ? '' :
      `<ellipse cx="${cx - 27 * s}" cy="${cy + 6 * s}" rx="${7 * s}" ry="${4.5 * s}" fill="${P.cheek}" opacity=".85"/>` +
      `<ellipse cx="${cx + 27 * s}" cy="${cy + 6 * s}" rx="${7 * s}" ry="${4.5 * s}" fill="${P.cheek}" opacity=".85"/>`;
    return eyes + cheeks + mouth;
  }
  const sparkle = (x, y, r = 10, c) =>
    `<path d="M${x} ${y - r} Q${x + r * .18} ${y - r * .18} ${x + r} ${y} Q${x + r * .18} ${y + r * .18} ${x} ${y + r} Q${x - r * .18} ${y + r * .18} ${x - r} ${y} Q${x - r * .18} ${y - r * .18} ${x} ${y - r}z" fill="${c || P.sun}" ${isLine() ? st(3) : ''}/>`;

  const TOOTH_PATH = 'M100 28c-14 0-22-8-40-8-24 0-38 20-38 46 0 22 8 36 14 58 6 22 6 50 22 50 15 0 14-34 26-34h32c12 0 11 34 26 34 16 0 16-28 22-50 6-22 14-36 14-58 0-26-14-46-38-46-18 0-26 8-40 8z';

  const A = {};
  A.tooth = (o = {}) => {
    const mood = o.mood || 'happy';
    let b = `<path d="${TOOTH_PATH}" fill="${P.tooth}" ${st(6)}/>`;
    if (!isLine()) b += `<path d="M44 44c-8 10-10 26-6 40" fill="none" stroke="${P.toothShade}" stroke-width="9" stroke-linecap="round"/>`;
    if (o.dirty) b += [[70, 70], [130, 60], [115, 115], [62, 118]].map(([x, y]) =>
      `<circle cx="${x}" cy="${y}" r="9" fill="#d9c27a" opacity=".75"/>`).join('');
    b += face(100, 84, 1, mood);
    if (o.shine) b += sparkle(166, 34, 14) + sparkle(30, 150, 9) + sparkle(178, 112, 8, P.sky);
    if (o.crown) b += `<path d="M70 26l8-22 14 14 8-18 8 18 14-14 8 22z" fill="${P.sun}" ${st(5)}/>`;
    return svg(b, '0 -6 200 214', 'tooth');
  };
  A.toothbrush = (o = {}) => {
    const c = o.color || P.mint, cd = o.colorD || P.mintD;
    let b = `<g transform="rotate(-35 100 100)">
      <rect x="92" y="62" width="18" height="130" rx="9" fill="${c}" ${st(6)}/>
      ${isLine() ? '' : `<rect x="97" y="80" width="5" height="90" rx="2.5" fill="#fff" opacity=".45"/>`}
      <rect x="92" y="20" width="18" height="50" rx="6" fill="${c}" ${st(6)}/>
      <rect x="62" y="16" width="30" height="46" rx="5" fill="${P.white}" ${st(5)}/>
      ${[24, 34, 44, 54].map(y => `<path d="M64 ${y}h26" ${st(3)} opacity=".5"/>`).join('')}
      <circle cx="101" cy="172" r="5" fill="${cd}" ${isLine() ? st(3) : ''}/>
    </g>`;
    if (o.paste) b += `<path d="M44 46c6-14 22-16 30-8 6-10 22-8 24 4" fill="${isLine() ? '#fff' : P.sky}" ${st(5)}/>`;
    return svg(b, '0 0 200 200', 'toothbrush');
  };
  A.toothpaste = (o = {}) => {
    const label = o.label === false ? '' :
      `<text x="100" y="112" text-anchor="middle" font-family="Fredoka,Nunito,sans-serif" font-weight="700" font-size="22" fill="${isLine() ? '#222' : '#fff'}" ${isLine() ? '' : `stroke="${P.pinkD}" stroke-width="1"`}>SPLAT</text>
       <text x="100" y="136" text-anchor="middle" font-family="Fredoka,Nunito,sans-serif" font-weight="700" font-size="17" fill="${isLine() ? '#222' : P.sun}">KIDS</text>`;
    const b = `<path d="M54 60h92l-10 120c0 6-4 10-10 10H74c-6 0-10-4-10-10z" fill="${isLine() ? '#fff' : P.sky}" ${st(6)}/>
      <path d="M58 182h84" ${st(6)}/>
      ${[66, 82, 98, 114, 130].map(x => `<path d="M${x} 182v10" ${st(3)}/>`).join('')}
      <rect x="80" y="30" width="40" height="32" rx="6" fill="${P.pink}" ${st(6)}/>
      ${isLine() ? '' : `<rect x="86" y="34" width="8" height="24" rx="4" fill="#fff" opacity=".45"/>`}
      ${label}
      ${isLine() ? '' : `<path d="M66 72c-2 30 0 70 4 100" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".35" fill="none"/>`}`;
    return svg(b, '0 0 200 210', 'toothpaste');
  };
  A.cup = () => svg(`<path d="M52 56h96l-12 124c-1 8-6 12-14 12H78c-8 0-13-4-14-12z" fill="${P.lilac}" ${st(6)}/>
      ${isLine() ? '' : `<path d="M60 70h80l-3 30H63z" fill="#fff" opacity=".25"/>`}
      <path d="M144 86c26-4 34 32 4 40" fill="none" ${st(8)}/>
      <circle cx="100" cy="128" r="16" fill="${isLine() ? '#fff' : P.sun}" ${st(4)}/>
      <path d="M92 128a8 8 0 0 0 16 0" fill="none" ${st(3)}/>
      <ellipse cx="100" cy="56" rx="48" ry="8" fill="${isLine() ? '#fff' : P.lilacD}" ${st(5)}/>`, '0 0 200 210', 'cup');
  A.water = () => svg(`<path d="M100 18C80 58 50 88 50 126a50 50 0 0 0 100 0c0-38-30-68-50-108z" fill="${P.water}" ${st(6)}/>
      ${isLine() ? '' : `<path d="M74 118c0 18 8 30 22 36" stroke="#fff" stroke-width="9" stroke-linecap="round" fill="none" opacity=".6"/>`}
      ${face(100, 128, .8)}`, '0 0 200 200', 'water');
  A.smile = () => svg(`<path d="M24 82c30 18 122 18 152 0 0 50-36 84-76 84S24 132 24 82z" fill="${isLine() ? '#fff' : P.pinkD}" ${st(6)}/>
      <path d="M38 90c24 12 100 12 124 0v20c-24 10-100 10-124 0z" fill="#fff" ${st(4)}/>
      ${[62, 86, 110, 134].map(x => `<path d="M${x} 96v18" ${st(3)}/>`).join('')}
      ${isLine() ? '' : `<path d="M60 140c20 10 60 10 80 0" stroke="${P.pink}" stroke-width="10" stroke-linecap="round" fill="none"/>`}
      ${sparkle(168, 44, 14)}${sparkle(36, 40, 9, P.sky)}`, '0 0 200 200', 'smile');
  A.germ = (o = {}) => {
    const c = o.color || P.germ;
    const spikes = Array.from({ length: 9 }, (_, i) => {
      const a = i / 9 * Math.PI * 2, x1 = 100 + Math.cos(a) * 48, y1 = 104 + Math.sin(a) * 44,
        x2 = 100 + Math.cos(a) * 70, y2 = 104 + Math.sin(a) * 64;
      return `<path d="M${x1} ${y1}L${x2} ${y2}" ${st(6)}/><circle cx="${x2}" cy="${y2}" r="7" fill="${c}" ${st(4)}/>`;
    }).join('');
    return svg(`${spikes}<ellipse cx="100" cy="104" rx="54" ry="50" fill="${c}" ${st(6)}/>
      ${isLine() ? '' : `<circle cx="78" cy="132" r="6" fill="${P.germD}"/><circle cx="128" cy="78" r="5" fill="${P.germD}"/>`}
      <path d="M70 80l18 8M130 80l-18 8" ${st(5)}/>
      <circle cx="82" cy="98" r="7" fill="${P.ink}"/><circle cx="118" cy="98" r="7" fill="${P.ink}"/>
      <path d="M80 122q20 14 40 0" fill="none" ${st(5)}/><path d="M90 126l4 8 4-6 4 6 4-8" fill="#fff" ${st(3)}/>`, '0 0 200 210', 'germ');
  };
  A.cloud = (o = {}) => svg(`<path d="M50 140c-24 0-38-16-34-34 4-18 22-26 38-20 4-26 30-40 54-30 14-22 52-20 62 8 22-2 36 16 30 36 18 6 18 40-10 40z" fill="${o.color || P.cloud}" ${o.flat ? '' : st(5)}/>`, '0 30 220 130', 'cloud');
  A.star = (o = {}) => svg(`<path d="M100 14l25 54 58 6-44 40 13 58-52-30-52 30 13-58-44-40 58-6z" fill="${o.color || P.sun}" ${st(6)}/>
      ${o.face === false ? '' : face(100, 108, .7)}`, '0 0 200 200', 'star');
  A.candy = () => svg(`<path d="M30 70l30 30-30 30M170 70l-30 30 30 30" fill="${P.pink}" ${st(5)}/>
      <circle cx="100" cy="100" r="42" fill="${P.candy}" ${st(6)}/>
      ${isLine() ? '' : `<path d="M70 86c12-14 40-18 56 0M68 110c16 14 44 14 62-2" stroke="#fff" stroke-width="8" stroke-linecap="round" fill="none" opacity=".7"/>`}`, '0 0 200 200', 'candy');
  A.ball = () => svg(`<circle cx="100" cy="100" r="70" fill="${P.sun}" ${st(6)}/>
      <path d="M32 90c40 20 96 20 136 0M100 30c-24 40-24 100 0 140" fill="none" ${st(6)}/>
      <path d="M100 30c-14 30 50 60 40 132" fill="none" stroke="${isLine() ? '#222' : P.pinkD}" stroke-width="${8 * SW}"/>`, '0 0 200 200', 'ball');
  A.fairy = () => svg(`
      <path d="M62 92C20 50 8 110 40 124c-28 20 6 54 34 22z" fill="${isLine() ? '#fff' : '#d8f1ff'}" ${st(5)} opacity="${isLine() ? 1 : .95}"/>
      <path d="M138 92c42-42 54 18 22 32 28 20-6 54-34 22z" fill="${isLine() ? '#fff' : '#d8f1ff'}" ${st(5)} opacity="${isLine() ? 1 : .95}"/>
      <path d="M100 52c-10 0-16-6-30-6-18 0-28 14-28 34 0 16 6 26 10 42s5 36 16 36c11 0 10-24 19-24h26c9 0 8 24 19 24 11 0 12-20 16-36s10-26 10-42c0-20-10-34-28-34-14 0-20 6-30 6z" fill="${P.tooth}" ${st(6)}/>
      ${face(100, 98, .82)}
      <path d="M76 52l6-20 10 12 8-16 8 16 10-12 6 20z" fill="${P.sun}" ${st(4)}/>
      <path d="M160 150l26-60" ${st(6)}/>${sparkle(186, 84, 15, P.pink)}
      ${isLine() ? '' : sparkle(40, 40, 8, P.sky) + sparkle(170, 30, 6)}`, '0 0 210 200', 'fairy');
  A.castle = (o = {}) => {
    const lit = o.lit ?? 5;
    const tower = (x, y, w, h, i) => {
      const on = i < lit, glow = on ? P.sun : (isLine() ? '#fff' : '#c9d6ef');
      return `<g>
        <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="8" fill="${isLine() ? '#fff' : (on ? '#fff' : '#e4ebf7')}" ${st(5)}/>
        <path d="M${x - 8} ${y + 2}c0-30 ${w / 2 + 8}-48 ${w / 2 + 8}-48s${w / 2 + 8} 18 ${w / 2 + 8} 48z" fill="${isLine() ? '#fff' : (on ? [P.pink, P.sky, P.mint, P.lilac, P.pink][i] : '#b8c4dd')}" ${st(5)}/>
        <path d="M${x + w / 2} ${y - 46}v-22l18 7-18 7" fill="${isLine() ? '#fff' : P.sun}" ${st(3)}/>
        <path d="M${x + w / 2 - 9} ${y + 40}a9 9 0 0 1 18 0v16h-18z" fill="${glow}" ${st(4)}/>
        ${on && !isLine() ? sparkle(x + w + 4, y + 14, 8) : ''}
      </g>`;
    };
    return svg(`
      ${isLine() ? '' : `<ellipse cx="200" cy="262" rx="190" ry="34" fill="#fff"/><ellipse cx="90" cy="250" rx="70" ry="26" fill="#fff"/><ellipse cx="320" cy="252" rx="70" ry="24" fill="#fff"/>`}
      ${tower(40, 130, 54, 110, 0)}${tower(306, 130, 54, 110, 1)}
      ${tower(96, 96, 60, 150, 2)}${tower(244, 96, 60, 150, 3)}
      <path d="M200 70c-14 0-22-8-40-8-24 0-36 20-36 44 0 20 6 32 10 52 5 22 4 90 22 90 14 0 12-46 26-46h36c14 0 12 46 26 46 18 0 17-68 22-90 4-20 10-32 10-52 0-24-12-44-36-44-18 0-26 8-40 8z" fill="#fff" ${st(6)}/>
      ${lit >= 5 ? face(200, 140, 1.3) : face(200, 140, 1.3, 'sad')}
      ${isLine() ? '' : `<ellipse cx="200" cy="268" rx="150" ry="18" fill="#fff"/>`}
      <path d="M176 62l8-24 12 14 4-20 4 20 12-14 8 24z" fill="${lit >= 5 && !isLine() ? P.sun : (isLine() ? '#fff' : '#c9d6ef')}" ${st(4)}/>
    `, '0 0 400 290', 'castle');
  };
  A.bag = () => svg(`<path d="M40 70h120l10 110H30z" fill="${P.mint}" ${st(6)}/>
      <path d="M70 70c0-40 60-40 60 0" fill="none" ${st(8)}/>
      <text x="100" y="130" text-anchor="middle" font-family="Fredoka,sans-serif" font-weight="700" font-size="26" fill="#fff">SPLAT</text>
      <text x="100" y="156" text-anchor="middle" font-family="Fredoka,sans-serif" font-weight="700" font-size="18" fill="${P.sun}">KIDS</text>`, '0 0 200 200', 'bag');

  // Слова курса: ключ → картинка и звук (audio/w_*.mp3)
  const WORDS = [
    { w: 'tooth', ru: 'зуб', art: () => A.tooth() },
    { w: 'toothbrush', ru: 'зубная щётка', art: () => A.toothbrush() },
    { w: 'toothpaste', ru: 'зубная паста', art: () => A.toothpaste() },
    { w: 'water', ru: 'вода', art: () => A.water() },
    { w: 'cup', ru: 'стаканчик', art: () => A.cup() },
    { w: 'smile', ru: 'улыбка', art: () => A.smile() },
    { w: 'germ', ru: 'микроб', art: () => A.germ() },
    { w: 'fairy', label: 'Tooth Fairy', ru: 'зубная фея', art: () => A.fairy() },
    { w: 'castle', ru: 'замок', art: () => A.castle() },
    { w: 'brush', ru: 'чистить', art: () => A.toothbrush({ paste: true }) },
    { w: 'clean', ru: 'чистый', art: () => A.tooth({ shine: true }) },
  ];

  const ART = {};
  for (const k of Object.keys(A)) ART[k] = (o = {}) => {
    const prev = [P, SW];
    if (o.line) { P = LINE; SW = 1.15; }
    try { return A[k](o); } finally { [P, SW] = prev; }
  };
  ART.WORDS = WORDS.map(x => ({ ...x, label: x.label || x.w, art: (o) => {
    const prev = [P, SW]; if (o && o.line) { P = LINE; SW = 1.15; }
    try { return x.art(); } finally { [P, SW] = prev; } } }));
  ART.COLOR = COLOR;
  window.ART = ART;
})();
