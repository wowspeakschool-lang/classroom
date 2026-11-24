p='/tmp/claude-0/-home-user/4f1aec8c-7236-5d0b-8cab-c22529efe1d2/scratchpad/advent/cabinet.html'
t=open(p,encoding='utf-8').read()
def R(a,b):
    global t
    assert t.count(a)==1,(a[:70],t.count(a)); t=t.replace(a,b)
# 24.11 Анна: награда шкалы не выскакивает сама. Сначала окно окошка; после закрытия на гирлянде
# загорается лампочка, коробка с подарком светится — ребёнок нажимает на неё сам.
R("""  var n=idx+1,m=MILE[n];if(m&&!s.rew[n]){s.rew[n]=1;var r={n:n,a:m.a||0,cert:!!m.cert};
    if(m.a)s.log.push""","""  var n=idx+1,m=MILE[n];if(m&&!s.rew[n]){
    if(!quiet){s.pend=s.pend||[];if(s.pend.indexOf(n)<0)s.pend.push(n);ev.pend=n;return ev;}
    s.rew[n]=1;var r={n:n,a:m.a||0,cert:!!m.cert};
    if(m.a)s.log.push""")
R("function freshTest(){","""/* забрать награду шкалы, ждущую на гирлянде */
function claimRew(n){var s=S,m=MILE[n];if(!m||s.rew[n])return null;s.pend=(s.pend||[]).filter(function(x){return x!==n;});
  s.rew[n]=1;var r={n:n,a:m.a||0,cert:!!m.cert};
  if(m.a)s.log.push({d:s.mode==='test'?'сегодня':(s.day>31?'янв':s.day+' дек'),ic:'✨',t:'Шкала подарков: '+n+' окошек',a:m.a,s:'адвент-календарь'});
  if(m.r){var f=SPEC.r.filter(function(x){return !s.own[x];})[0];if(f){giveSpec(s,f);r.f=f;}}
  save();return r;}
function freshTest(){""")
# гирлянда: ждущий подарок светится и нажимается
R("if(m){if(k<=n){g='<span class=\"gift got\"","if(m&&(S.pend||[]).indexOf(k)>=0){g='<button type=\"button\" class=\"gift ready\" data-k=\"'+k+'\" aria-label=\"Забрать подарок\">'+pic('img/box_common.webp')+'<span class=\"tap\">Нажми!</span></button>';}\n    else if(m){if(k<=n){g='<span class=\"gift got\"")
R(".gb .gift.next{",""".gb .gift.ready{border:0;padding:0;background:radial-gradient(circle,rgba(255,224,120,.9),rgba(255,200,80,0) 70%);border-radius:50%;cursor:pointer;animation:gready 1s ease-in-out infinite;z-index:3}
.gb .gift.ready .tap{position:absolute;top:100%;left:50%;transform:translateX(-50%);margin-top:2px;font-family:var(--ff-head);font-weight:900;font-size:10px;background:#FFD45A;color:#4A2E00;border-radius:999px;padding:1px 7px;white-space:nowrap}
@keyframes gready{0%,100%{transform:scale(1) rotate(0);box-shadow:0 0 10px 4px rgba(255,212,90,.55)}25%{transform:scale(1.15) rotate(-8deg)}50%{transform:scale(1.2) rotate(8deg);box-shadow:0 0 24px 10px rgba(255,212,90,.8)}75%{transform:scale(1.15) rotate(-4deg)}}
.gb.lit .l{animation:litup 1.2s ease-out 2!important}
@keyframes litup{0%{transform:scale(1)}40%{transform:scale(2.2);filter:brightness(2)}100%{transform:scale(1)}}
.gb .gift.next{""")
# окошко: окно -> после закрытия подсветить лампочку и ждущий подарок
R("    if(ev.gift||ev.rew.length){comboModal(it,ev,{eb:eb,hint:hint,fin:nOpened()===N});return;}\n    wordModal(it,{eb:eb,hint:hint,fin:nOpened()===N});",
  """    var m=ev.gift?comboModal(it,ev,{eb:eb,hint:hint,fin:nOpened()===N}):wordModal(it,{eb:eb,hint:hint,fin:nOpened()===N});
    if(ev.pend&&m){var orig=m.remove.bind(m);m.remove=function(){orig();setTimeout(function(){showPend(ev.pend);},250);};}""")
R("function comboModal(it,ev,o){","""function showPend(k){if(S.page!=='advent'||S.tab!=='cal')return;var gb=document.querySelectorAll('.gb')[k-1];if(!gb)return;
  gb.scrollIntoView({behavior:'smooth',block:'center'});gb.classList.add('lit');sfx('rare');
  var r=gb.getBoundingClientRect();setTimeout(function(){var r2=gb.getBoundingClientRect();confetti(r2.left+r2.width/2,r2.top+20,'l');},500);
  toast('✨ '+k+' окошек открыто — на гирлянде тебя ждёт подарок! Нажми на него');}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.gb .gift.ready');if(!b)return;var k=+b.dataset.k,r=claimRew(k);if(!r)return;
  renderAdvent();showCoins(!!r.a);rewardModal(r);});
function comboModal(it,ev,o){""")
# общее окно: только окошко + подарок школы; подсвечиваются по очереди: эффект -> слово звучит -> следующая карточка
R("  ev.rew.forEach(function(rw){if(rw.f){","  (ev.rew||[]).forEach(function(rw){if(rw.f){")
R(".combo .cc{position:relative;",".combo .cc{transition:opacity .4s,transform .4s,box-shadow .4s;opacity:.35;transform:scale(.94)}\n.combo .cc.lit{opacity:1;transform:scale(1);box-shadow:0 0 0 3px rgba(255,255,255,.7),0 0 28px rgba(255,230,150,.6)}\n.combo .cc{position:relative;")
R("  draw();sfx(ev.gift?'gift':'rare');if(o.fin)say(dayEn(it),'Merry Christmas!');else say(dayEn(it));\n  setTimeout(function(){confetti(window.innerWidth/2,window.innerHeight/2,'g');},300);",
  """  draw();
  /* по очереди: карточка загорается -> через миг звучит её слово -> следующая */
  var cards=box.querySelectorAll('.cc'),step=0;
  function lightNext(){var c=cards[step];if(!c||!document.body.contains(m))return;c.classList.add('lit');var x=items[step];step++;
    if(x.k==='g'){sfx('gift');var r=c.getBoundingClientRect();confetti(r.left+r.width/2,r.top+r.height/2,'g');setTimeout(lightNext,1600);}
    else{setTimeout(function(){if(!document.body.contains(m))return;if(step===1&&o.fin)say(x.say,'Merry Christmas!');else if(x.say)say(x.say);setTimeout(lightNext,1600);},900);}}
  setTimeout(lightNext,250);""")
# одиночное окно слова тоже: сначала эффект, слово — через миг
R("  if(o.eb)sayIt();m.querySelector('.say').onclick=sayIt;","  if(o.eb)setTimeout(function(){if(document.body.contains(m))sayIt();},900);m.querySelector('.say').onclick=sayIt;")
open(p,'w',encoding='utf-8').write(t);print('ok')
