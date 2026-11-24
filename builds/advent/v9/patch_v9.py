import re
D='/tmp/claude-0/-home-user/4f1aec8c-7236-5d0b-8cab-c22529efe1d2/scratchpad/advent/'
t=open(D+'cabinet_v8_backup.html',encoding='utf-8').read()
def R(a,b,n=1):
    global t
    assert t.count(a)==n,(a[:80],t.count(a)); t=t.replace(a,b)
def between(start,end,new,keep_end=True):
    global t
    i=t.index(start); j=t.index(end,i)
    t=t[:i]+new+(t[j:] if keep_end else t[j+len(end):])
rd=lambda n:open(D+n,encoding='utf-8').read()
# шрифт для вывески мастерской
R('family=Montserrat:wght@600;700;800;900&family=Nunito:wght@500;600;700;800&display=swap','family=Montserrat:wght@600;700;800;900&family=Nunito:wght@500;600;700;800&family=Pacifico&display=swap')
# CSS
css=rd('patch_css.txt').replace('  .treearea{order:-1}','  .treearea{order:-1;height:calc(100svh - 300px);min-height:380px}')
i=t.index('</style>'); t=t[:i]+css+t[i:]
# состояние: от «/* 31 окошко» до «load();»
between('/* 31 окошко:','load();\n',rd('patch_state.js'),keep_end=False)
# календарь, окошки, слово
between('function renderAdvent(){','/* ---------- ёлка и сундук',rd('patch_cal.js'))
# ёлка и мастерская
between('/* ---------- ёлка и сундук','/* перетаскивание пальцем',rd('patch_tree.js'))
# старый renderCal/doorClick… уже внутри patch_cal; убедиться, что дублей нет
for fn in ['function renderCal(','function doorClick(','function openDay(','function wordModal(','function renderTree(','function placeAt(']:
    assert t.count(fn)==1,(fn,t.count(fn))
# шапка: музыка рядом с монетками
R('<button type="button" class="coins" id="coins"','<span class="music" id="music"><button type="button" id="mBtn" aria-label="Музыка">🎵</button><input type="range" id="mVol" min="0" max="100" value="18" aria-label="Громкость музыки"></span><button type="button" class="coins" id="coins"')
# плашки вариантов
between('function plaque(){','function coinsModal(){','''function plaque(){
  if(isTest())return '<div class="plaque"><span class="vn">Вариант 1 · Тест</span><span class="vt">Все 31 окошко открываются подряд, без дат — чтобы посмотреть, что внутри каждого: игрушки, подарки школы (5, 10, 15, 22, 28) и награды шкалы.</span></div>';
  if(S.mode==='late')return '<div class="plaque"><span class="vn">Вариант 3 · Новичок</span><span class="vt">Ученица впервые зашла 15 декабря. При первом входе ей выпадают монетки — ровно на все ранние окошки: 13 × 5 = 🪙 65. Вчерашнее (14) и сегодняшнее (15) — бесплатно.</span></div>';
  if(S.mode==='guest')return '<div class="plaque"><span class="vn">Вариант 4 · Гость по ссылке</span><span class="vt">Ещё не ученик школы: пришёл по ссылке друга 2 декабря. После регистрации заявка уходит в школу, а ему сразу 🪙 20. Другу, который позвал, — эпическая игрушка, когда гость откроет первое окошко.</span></div>';
  if(S.mode==='after')return '<div class="plaque"><span class="vn">Вариант 5 · Январь</span><span class="vt">Календарь закончился: все 31 окошко открыты, гирлянда дней горит целиком, ёлка в огнях и звезда на верхушке светится. Мастерская и ёлка остаются.</span></div>';
  return '<div class="plaque"><span class="vn">Вариант 2 · 20 декабря</span><span class="vt">Сегодня 20 декабря. Сегодняшнее и вчерашнее (19) окошко — бесплатные, окошки 7, 8, 14 и 18 — за 🪙 5. Открыто 14 окошек: на гирлянде следующий подарок через 1. Друг уже пришёл — у Маши эпический мишка.</span></div>';
}
function earnHtml(){return '<div class="earn">'+[['📖','Урок','≈ 🪙 10'],['🎓','Вводный урок <small>(для новых учеников)</small>','🪙 30'],['🎫','Покупка абонемента','🪙 100'],['🎙','«Повтори за мной» в адвенте','🪙 1 в день'],['✨','Шкала подарков: открывай окошки','🪙 3–15'],['👫','Друг пришёл по твоей ссылке','эпическая игрушка'],['📸','Пост с ёлкой и отметкой школы','легендарная игрушка']].map(function(x){return '<div><span>'+x[0]+'</span><span>'+x[1]+'</span><b>'+x[2]+'</b></div>';}).join('')+'</div>';}
''')
R("'<p class=\"hint\" style=\"margin:0\">Монетки дают за уроки, сданную домашку и активность на уроке. Тратить можно на колесо удачи, сундучок-сюрприз, окошки ранних дней (🪙 5; вчерашнее и сегодняшнее — бесплатно) и новые цвета украшений (🪙 1).</p>'+",
  "'<h4 style=\"margin:4px 0 0;font-family:var(--ff-head)\">Как заработать монетки</h4>'+earnHtml()+'<p class=\"hint\" style=\"margin:0\">Тратить: окошко раньше вчерашнего — 🪙 5, новый цвет игрушки — 🪙 1, ещё одна такая же игрушка — 🪙 3, колесо удачи и сундучок-сюрприз.</p>'+")
# главная: блок «Как заработать монетки» у гостя
R("'<div class=\"card\"><h3>🪙 Мои монетки</h3><div class=\"bigcoin\">'+coins()+'</div><div class=\"sub\">За уроки, домашку и активность</div><button type=\"button\" class=\"btn ghost\" id=\"coinCard\">Откуда пришли и куда ушли</button></div>'+",
  "'<div class=\"card\"><h3>🪙 Мои монетки</h3><div class=\"bigcoin\">'+coins()+'</div><div class=\"sub\">За уроки, домашку и активность</div><button type=\"button\" class=\"btn ghost\" id=\"coinCard\">Откуда пришли и куда ушли</button></div>'+(S.mode==='guest'?'<div class=\"card\" style=\"grid-column:1/-1\"><h3>Как заработать монетки</h3>'+earnHtml()+'</div>':'')+")
# имя в меню
R("<div class=\"me\"><div class=\"ava\">М</div><div><b>Маша</b><small>Super Minds 2 · 8 лет</small></div></div>","<div class=\"me\"><div class=\"ava\">'+esc(meName()[0])+'</div><div><b>'+esc(meName())+'</b><small>'+(S.mode==='guest'?'гость · по ссылке друга':'Super Minds 2 · 8 лет')+'</small></div></div>")
R("function renderNav(){","function meName(){return S.mode==='guest'?(S.name||'Гость'):'Маша';}\nfunction renderNav(){")
# render(): регистрация гостя
R("  var wc=S.mode==='late'&&!S.welcomed?credit():0;\n  if(S.page==='home')renderHome();else if(S.page==='advent')renderAdvent();else renderStub(S.page);",
  "  var wc=S.mode==='late'&&!S.welcomed?credit():0;\n  if(S.mode==='guest'&&!S.reg){renderReg();return;}\n  $('ttl').textContent=S.page==='advent'?'🎄 Мой адвент-календарь':S.page==='home'?'Привет, '+meName()+'! 👋':$('ttl').textContent;\n  if(S.page==='home')renderHome();else if(S.page==='advent')renderAdvent();else renderStub(S.page);")
R("/* новичок: монетки ровно на все платные прошлые окошки, без грустного */",'''/* гость по ссылке друга: регистрация → заявка в школу, 🪙 20 сразу (Анна, 24.11.2026) */
function renderReg(){$('ttl').textContent='🎄 Адвент-календарь WowSpeak';
  $('page').innerHTML=plaque()+'<form class="reg" id="regF"><span class="pill p-pink">🎁 Маша П. зовёт тебя!</span><h2>Новогодний адвент-календарь</h2><p class="sub" style="margin:0">31 окошко до Нового года: в каждом — украшение для твоей ёлки и новое английское слово. Зарегистрируйся — и сразу получишь 🪙 20.</p>'+
   '<label>Имя ребёнка<input id="rName" required autocomplete="given-name" placeholder="Например, Алёна"></label><label>Телефон родителя<input id="rPhone" type="tel" required autocomplete="tel" placeholder="+7 900 000-00-00"></label>'+
   '<button class="btn pink" type="submit">Начать и получить 🪙 20</button><p class="hint" style="margin:0">В макете ничего не отправляется. На платформе заявка уйдёт в школу, и с вами свяжутся.</p>'+
   '<h3 style="margin-top:6px">Как заработать монетки</h3>'+earnHtml()+'</form>';
  $('regF').onsubmit=function(e){e.preventDefault();S.reg=true;S.name=($('rName').value||'Гость').trim();S.log.push({d:'2 дек',ic:'🎁',t:'Подарок за регистрацию',a:20,s:'адвент-календарь'});S.page='advent';S.tab='cal';save();sfx('coin');render();toast('🪙 20 — твои! Открывай первое окошко');};}
/* новичок: монетки ровно на все платные прошлые окошки, без грустного */''')
# вопросы
between('var QS=[','function renderQ(){','''var QS=[
 ['По какому времени наступает новый день и открывается окошко?',['По Москве — для всех одинаково','По времени ученика — окошко открывается в его полночь']],
 ['Короткую гирлянду сделать ещё короче?',['Да — маленький кусок короче, чем сейчас','Нет — трёх кусков хватает']],
 ['Версии для других возрастов (4–6, 10–12, 13+)',['Позже, после запуска для 7–9','В этом году только 7–9']]];
''')
R("<span class=\"vt\">Что нужно решить до запуска. По каждому — вопрос и варианты.</span>","<span class=\"vt\">Что осталось решить до запуска. Решено и уйдёт в ТЗ: родителям сообщений не нужно, кнопку 🎄 команда кабинета добавит по желанию, окошко раньше вчерашнего — 🪙 5.</span>")
# текст для детей и карточка учителя — новые правила
between("var SCRIPT=","function renderTeacher(){","""var SCRIPT='Ребята, у меня для вас новогодняя новость! С 1 декабря в вашем личном кабинете появится адвент-календарь — 31 окошко, по одному на каждый день до Нового года.\\n\\n'+
 'Каждый день открывайте одно окошко. Внутри — украшение для ёлки и новое английское слово. Слово можно послушать и повторить за голосом — за это ещё и монетка.\\n\\n'+
 'Украшения попадают в Мастерскую эльфов, а оттуда вы сами вешаете их на свою ёлку. Их можно увеличить, повернуть и перекрасить. Иногда в окошке лежит настоящий подарок от школы!\\n\\n'+
 'Чем больше окошек откроете, тем ярче горит гирлянда подарков: на ней спрятаны монетки и редкие игрушки. Позовёте друга — получите эпическую игрушку, выложите ёлку в соцсети — легендарную.\\n\\n'+
 'Вчерашнее окошко тоже бесплатное, а более ранние можно открыть за 5 монеток. К 31 декабря у каждого будет своя нарядная ёлка — покажете мне её на уроке!';
""")
R("'<li><i>🎄</i><span>Украшения вешаешь на свою ёлку сам: больше, меньше, другой цвет</span></li>'+","'<li><i>🎄</i><span>Украшения вешаешь на свою ёлку сам: больше, меньше, другой цвет</span></li>'+\n   '<li><i>✨</i><span>Гирлянда подарков: монетки, редкие игрушки и подарки от школы</span></li>'+")
R("<li><i>🪙</i><span>Вчерашнее и сегодняшнее окошко — бесплатно, более ранние — за 5 монеток. Новый цвет — 1 монетка</span></li>","<li><i>👫</i><span>Позови друга — эпическая игрушка, пост с ёлкой — легендарная</span></li>")
# предзагрузка картинок: особые игрушки и коробки
R("Object.keys(F).forEach(function(f){colsOf(f).forEach(function(c){var i=new Image();i.src=src(f,c);});});",
  "Object.keys(F).forEach(function(f){colsOf(f).forEach(function(c){var i=new Image();i.src=src(f,c);});});\n['common','rare','epic','legend'].forEach(function(b){var i=new Image();i.src='img/box_'+b+'.webp';});")
# музыка: тихо, сама с первого касания; выключается только она
R("$('coins').onclick=coinsModal;","""$('coins').onclick=coinsModal;
/* фоновая музыка (своя аранжировка Jingle Bells): играет тихо и сама — браузер даёт звук после первого касания,
   поэтому пробуем сразу и при первом нажатии в любом месте. Выключается только музыка, слова звучат всегда (Анна, 24.11) */
var mus=new Audio('audio/music_jingle.mp3');mus.loop=true;mus.volume=.18;var musOff=false;
function mUI(){$('mBtn').textContent=mus.paused?'🎵':'⏸';$('mBtn').title=mus.paused?'Включить музыку':'Выключить музыку';}
function mStart(){if(!mus.paused||musOff)return;mus.play().then(mUI).catch(function(){});}
$('mVol').oninput=function(){mus.volume=this.value/100;};
$('mBtn').onclick=function(){if(mus.paused){musOff=false;mus.play().then(mUI).catch(function(){});}else{musOff=true;mus.pause();mUI();}};
mStart();['pointerdown','keydown','touchstart'].forEach(function(ev){document.addEventListener(ev,function(e){if(e.target.closest&&e.target.closest('#music'))return;mStart();},{once:true,capture:true});});""")
R("window.__adv={F:F,DAYS:DAYS,get S(){return S;},placeAt:placeAt,renderTree:renderTree,go:go,colsOf:colsOf,src:src};",
  "window.__adv={F:F,DAYS:DAYS,get S(){return S;},placeAt:placeAt,renderTree:renderTree,go:go,colsOf:colsOf,src:src,SPEC:SPEC};")
# варианты с собственной страницей не сбрасывают страницу
R("if(!viewMode(v)){S=ALL[v];if(v!=='late'&&v!=='after'){S.page=page;S.tab=tab;}}","if(!viewMode(v)){S=ALL[v];if(v!=='late'&&v!=='after'&&v!=='guest'){S.page=page;S.tab=tab;}}")
R("if(c!=='late'&&c!=='after'){S.page=page;S.tab=tab;}","if(c!=='late'&&c!=='after'&&c!=='guest'){S.page=page;S.tab=tab;}")
# доп. «эффект» на окошке: вспышка уже в openDay
open(D+'cabinet.html','w',encoding='utf-8').write(t); print('ok',len(t))
