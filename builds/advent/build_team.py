"""Сборка одного файла для команды платформы (Анна, 24.11.2026):
только адвент (календарь, мастерская и ёлка, сказочный лес) без остального кабинета,
три режима показа — Тест, 20 декабря, Январь. Все картинки и звуки внутри файла (data:),
файл открывается сам по себе, без сервера.

Как устроено: в начале страницы лежит словарь __A {путь: data-URI}. Маленький загрузчик
подменяет пути img/…, audio/…, recept/… на data-URI там, где страница их ставит:
innerHTML / insertAdjacentHTML, img.src, audio.src, new Audio(). Лес, рецепт и Bingo —
iframe со srcdoc, у них свой такой же загрузчик, словарь берут у родителя.
"""
import os, re, json, base64, glob
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, 'team', 'advent_wowspeak.html')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
rd = lambda p: open(os.path.join(D, p), encoding='utf-8').read()

# ---------- ресурсы ----------
SKIP = re.compile(r'(_orig\.webp$|/peek_|/drift|les_tile\.webp$|/les_[ABC]_|^audio/w_|\.wav$|map\.json$)')
assets = {}
def add(path):
    full = os.path.join(D, path)
    ext = path.rsplit('.', 1)[1]
    mime = {'webp': 'image/webp', 'png': 'image/png', 'mp3': 'audio/mpeg'}[ext]
    assets[path] = 'data:%s;base64,%s' % (mime, base64.b64encode(open(full, 'rb').read()).decode())
for p in sorted(glob.glob(os.path.join(D, 'img', '**', '*.webp'), recursive=True)) + \
         sorted(glob.glob(os.path.join(D, 'recept', '*.webp'))):
    rel = os.path.relpath(p, D)
    if not SKIP.search(rel): add(rel)
cab = rd('cabinet.html')
used_audio = set(re.findall(r'audio/[A-Za-z0-9_]+\.mp3', cab + rd('les_page.html')))
used_audio |= {os.path.relpath(p, D) for p in glob.glob(os.path.join(D, 'audio', 's_*.mp3'))}
for a in sorted(used_audio):
    if os.path.exists(os.path.join(D, a)) and not SKIP.search(a): add(a)

ASSET_RE = r'(?:img|audio|recept)/[A-Za-z0-9_/.\-]+?\.(?:webp|png|mp3)'
BOOT = r"""<script>
/* Загрузчик ресурсов: пути img/…, audio/…, recept/… заменяются на data-URI из словаря __A.
   На платформе этот блок и словарь можно убрать и положить файлы рядом — пути в коде обычные. */
(function(){
  var A=window.__A;if(!A){try{A=window.__A=parent.__A;}catch(e){}}if(!A)return;
  var RE=/(?:img|audio|recept)\/[A-Za-z0-9_\/.\-]+?\.(?:webp|png|mp3)/g;
  function m(u){return (typeof u==='string'&&A[u])?A[u]:u;}
  function ms(s){return typeof s==='string'?s.replace(RE,function(k){return A[k]||k;}):s;}
  function hook(proto,prop,f){var d=Object.getOwnPropertyDescriptor(proto,prop);if(!d||!d.set)return;
    Object.defineProperty(proto,prop,{configurable:true,enumerable:d.enumerable,get:d.get,set:function(v){d.set.call(this,f(v));}});}
  hook(Element.prototype,'innerHTML',ms);hook(Element.prototype,'outerHTML',ms);
  hook(HTMLImageElement.prototype,'src',m);hook(HTMLMediaElement.prototype,'src',m);hook(HTMLSourceElement.prototype,'src',m);
  hook(HTMLIFrameElement.prototype,'srcdoc',function(v){return v;});
  var ia=Element.prototype.insertAdjacentHTML;Element.prototype.insertAdjacentHTML=function(p,h){return ia.call(this,p,ms(h));};
  var sa=Element.prototype.setAttribute;Element.prototype.setAttribute=function(n,v){return sa.call(this,n,(n==='src'||n==='style')?ms(String(v)):v);};
  var OA=window.Audio;window.Audio=function(u){var a=new OA();if(u!==undefined)a.src=u;return a;};window.Audio.prototype=OA.prototype;
  var cs=CSSStyleDeclaration.prototype.setProperty;CSSStyleDeclaration.prototype.setProperty=function(p,v,pr){return cs.call(this,p,ms(v),pr);};
})();
</script>"""

def inline_static(html):
    """Пути в разметке и CSS (вне <script>) заменяем сразу — их разбирает браузер, а не код."""
    parts = re.split(r'(<script\b[^>]*>.*?</script>)', html, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(ASSET_RE, lambda mm: assets.get(mm.group(0), mm.group(0)), parts[i])
    return ''.join(parts)

def R(s, a, b, cnt=1):
    assert s.count(a) == cnt, (a[:80], s.count(a))
    return s.replace(a, b)

# ---------- лес ----------
les = rd('les_page.html')
les = R(les, "var IN_CAB=/[?&]in=cab/.test(location.search);", "var IN_CAB=true; /* внутри страницы адвента */")
les = R(les, "if(/[?&]nye=1/.test(location.search))document.body.classList.add('nye');",
        "try{if(parent.__advNye&&parent.__advNye())document.body.classList.add('nye');}catch(e){}")
les = les.replace('Лес ёлок WowSpeak', 'Сказочный лес WowSpeak').replace('<title>Лес ёлок', '<title>Сказочный лес')
les = les.replace('<head>', '<head>' + BOOT, 1) if '<head>' in les else BOOT + les
les = inline_static(les)

# ---------- рецепт и Bingo ----------
rec = rd('recept.html')
rec = rec.replace('<head>', '<head>' + BOOT, 1)
rec = inline_static(rec)
bng = rd('bingo.html')
bng = R(bng, "var D=null;try{var m=location.hash.match(/d=([^&]+)/);",
        "var D=null;try{if(parent.__bingoData)D=parent.__bingoData;}catch(e){}try{var m=!D&&location.hash.match(/d=([^&]+)/);")
bng = bng.replace('<head>', '<head>' + BOOT, 1)
bng = inline_static(bng)

def js_str(s):
    return json.dumps(s, ensure_ascii=False).replace('</', '<\\/')

# ---------- адвент ----------
t = cab
t = R(t, "var MODES=[['test','1 · Тест','Тест: все окошки подряд'],['miss','2 · 20 декабря','20 декабря: есть неоткрытые окошки'],['late','3 · Новичок','Ученица пришла 15 декабря'],['guest','4 · Гость','Гость по ссылке друга'],['after','5 · Январь','Январь: календарь закончился'],",
      "var MODES=[['test','1 · Тест','Тест: все окошки подряд'],['miss','2 · 20 декабря','20 декабря: есть неоткрытые окошки'],['after','3 · Январь','Январь: календарь закончился']];var _MODES_OFF=[")
t = R(t, "if(!ALL)ALL={cur:'miss'};", "if(!ALL)ALL={cur:'miss'};if(['test','miss','after'].indexOf(ALL.cur)<0)ALL.cur='miss';")
t = re.sub(r"var KEY='wow-cabinet-advent-v\d+'", "var KEY='wowspeak-advent-team-v1'", t)
t = t.replace('Вариант 5 · Январь','Вариант 3 · Январь')
t = R(t, "function render(){", "function render(){S.page='advent';")
t = t.replace("'🌲 Лес'", "'🌲 Сказочный лес'")
t = R(t, """function renderForest(){$('adv').innerHTML='<iframe class="lesf" src="les_page.html?in=cab'+(nyeOn()?'&nye=1':'')+'" title="Лес ёлок"></iframe>';}""",
      """window.__advNye=function(){return nyeOn();};
function renderForest(){$('adv').innerHTML='<iframe class="lesf" title="Сказочный лес"></iframe>';$('adv').querySelector('iframe').srcdoc=FOREST_HTML;}""")
t = re.sub(r"function openRecipe\(\)\{modal\((.*?)\);\}", lambda mm: "function openRecipe(){modal("+mm.group(1).replace(' src="recept.html"','').replace('В макете — страница рецепта.','Страница рецепта.')+").querySelector('iframe').srcdoc=RECEPT_HTML;}", t, count=1, flags=re.S)
assert 'RECEPT_HTML;}' in t
t = R(t, """var d=btoa(unescape(encodeURIComponent(JSON.stringify({name:'Маша',words:ws}))));""",
      """window.__bingoData={name:'Маша',words:ws};""")
t = R(t, """<iframe class="bingof" src="bingo.html#d='+encodeURIComponent(d)+'" title="Christmas Bingo"></iframe>""",
      """<iframe class="bingof" title="Christmas Bingo"></iframe>""")
t = R(t, """На платформе здесь скачается PDF: две страницы карточек и лист ведущего.</p><div class="btns"><button type="button" class="btn ghost" data-close>Закрыть</button></div></div>');}""",
      """На платформе здесь скачается PDF: две страницы карточек и лист ведущего.</p><div class="btns"><button type="button" class="btn ghost" data-close>Закрыть</button></div></div>').querySelector('iframe').srcdoc=BINGO_HTML;}""")
# мастерская на телефоне — до нижнего края экрана (нижнего меню кабинета тут нет)
t = R(t, "  if(!bn||getComputedStyle(bn).display==='none'){room.style.height='';return;}",
      "  if(!bn||getComputedStyle(bn).display==='none'){if(window.innerWidth>860){room.style.height='';return;}var dm=document.getElementById('demo');bn={getBoundingClientRect:function(){return {top:dm&&getComputedStyle(dm).display!=='none'?dm.getBoundingClientRect().top:window.innerHeight};}};}")
# страница без кабинета: нет бокового и нижнего меню, «дней подряд» и чужих разделов
t = t.replace('<title>Адвент в кабинете ученика</title>', '<title>Адвент-календарь WowSpeak</title>')
t = R(t, "<style>", """<style>
/* только адвент, без остального кабинета ученика (24.11.2026) */
.side,.bnav,.streak{display:none!important}
.app{grid-template-columns:minmax(0,1fr)!important}
@media (max-width:860px){.demo{bottom:max(8px,env(safe-area-inset-bottom,0px))!important}.page{padding-bottom:90px!important}}
""")
consts = '<script>window.__A=' + json.dumps(assets) + ';</script>' + BOOT + \
    '<script>var FOREST_HTML=' + js_str(les) + ';var RECEPT_HTML=' + js_str(rec) + ';var BINGO_HTML=' + js_str(bng) + ';</script>'
t = t.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + consts, 1)
t = inline_static(t)
head = '<!doctype html>\n<html lang="ru">\n<head>\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
if not t.lstrip().lower().startswith('<!doctype'):
    t = head + t
open(OUT, 'w', encoding='utf-8').write(t)
left = set(re.findall(r'["\'(](' + ASSET_RE + r')', t))
print('файл', OUT, round(os.path.getsize(OUT) / 1e6, 2), 'МБ; ресурсов', len(assets))
print('путей без файла:', sorted(p for p in left if p not in assets)[:20])
