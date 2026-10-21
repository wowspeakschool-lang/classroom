/* Общее для урока и тренажёра: звук, облака, фирменная плашка, конфетти. */
const SND = (() => {
  const cache = {}; let cur = null, muted = false;
  return {
    play(name, { stopPrev = true } = {}) {
      if (muted) return Promise.resolve();
      if (stopPrev && cur) { cur.pause(); cur.currentTime = 0; }
      const a = cache[name] || (cache[name] = new Audio(`audio/${name}.mp3`));
      a.currentTime = 0; cur = a;
      return new Promise(res => { a.onended = res; a.play().catch(res); });
    },
    stop() { if (cur) { cur.pause(); cur.currentTime = 0; } },
    toggle() { muted = !muted; if (muted) this.stop(); return muted; },
  };
})();

function mountClouds(n = 6) {
  const box = document.createElement('div'); box.className = 'clouds';
  for (let i = 0; i < n; i++) {
    const c = document.createElement('i');
    const w = 120 + Math.random() * 200;
    c.style.cssText = `width:${w}px;top:${Math.random() * 85}%;animation-duration:${40 + Math.random() * 50}s;animation-delay:${-Math.random() * 80}s;opacity:${.55 + Math.random() * .4}`;
    c.innerHTML = ART.cloud({ flat: true });
    box.appendChild(c);
  }
  document.body.prepend(box);
}

/* Логотип Splat Kids: если в brand/ лежит logo.png — показываем его, иначе текстовую плашку. */
function brandHTML() {
  return `<div class="brandmark">
    <img src="brand/logo.png" alt="Splat Kids" onerror="this.replaceWith(Object.assign(document.createElement('span'),{className:'wm',innerHTML:'<b>SPLAT</b><s>KIDS</s>'}))">
    <span class="x">×</span><span class="ws">WowSpeak</span></div>`;
}

function confetti(ms = 3000) {
  const cv = document.createElement('canvas');
  cv.style.cssText = 'position:fixed;inset:0;pointer-events:none;z-index:999';
  document.body.appendChild(cv);
  const W = cv.width = innerWidth, H = cv.height = innerHeight, g = cv.getContext('2d');
  const cols = ['#33c7b0', '#ff7eb6', '#ffd23f', '#5bb8ff', '#a98bff', '#fff'];
  const ps = Array.from({ length: 160 }, () => ({
    x: Math.random() * W, y: -20 - Math.random() * H * .5, vx: (Math.random() - .5) * 4, vy: 2 + Math.random() * 4,
    r: 4 + Math.random() * 6, c: cols[Math.random() * cols.length | 0], a: Math.random() * 6, va: (Math.random() - .5) * .3, star: Math.random() < .3,
  }));
  const t0 = performance.now();
  (function f(t) {
    g.clearRect(0, 0, W, H);
    for (const p of ps) {
      p.x += p.vx; p.y += p.vy; p.a += p.va; p.vy += .03;
      g.save(); g.translate(p.x, p.y); g.rotate(p.a); g.fillStyle = p.c;
      if (p.star) { g.beginPath(); for (let i = 0; i < 10; i++) { const r = i % 2 ? p.r * .45 : p.r * 1.3, a = i * Math.PI / 5; g.lineTo(Math.cos(a) * r, Math.sin(a) * r); } g.fill(); }
      else g.fillRect(-p.r / 2, -p.r / 3, p.r, p.r * .66);
      g.restore();
    }
    if (t - t0 < ms) requestAnimationFrame(f); else cv.remove();
  })(t0);
}
