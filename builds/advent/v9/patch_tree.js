/* ---------- мастерская эльфов и ёлка (24.11.2026, решения Анны) ----------
   Игрушка выпадает в одном экземпляре. Ещё один такой же — 🪙 3, новый цвет — 🪙 1.
   Гирлянда, огоньки и мишура выпадают тремя кусками: маленький, средний, большой.
   Особые игрушки: редкие — за шкалу подарков, эпические — за друзей, легендарные — за пост в соцсетях. */
var openFam=null,sel=null;
var FREE_SZ=[.5,.7,1];
function placedOf(f){return S.placed.filter(function(p){return p.f===f;}).length;}
function cntOf(f){return (S.cnt&&S.cnt[f])||0;}
function freeOf(f){return cntOf(f)-placedOf(f);}
function sizesLeft(f){var all=(S.wsz&&S.wsz[f]||[]).slice();S.placed.forEach(function(p){if(p.f!==f)return;var i=all.indexOf(p.s);if(i<0){var best=0;all.forEach(function(v,k){if(Math.abs(v-p.s)<Math.abs(all[best]-p.s))best=k;});i=best;}if(all.length)all.splice(i,1);});return all;}
function rar(f){return F[f].rar||'c';}
var RARN={c:'Обычные',r:'Редкие',e:'Эпические',l:'Легендарные'};
var TIPS={c:['🎁 Обычная игрушка','Выпадет в одном из окошек календаря. Открывай окошко каждый день!','#9C5E36'],
 r:['🔵 Редкая игрушка','Открывай окошки: на 5, 10, 15, 20 и 25 открытых окошках шкала подарков дарит редкую игрушку.','#2E6FD6'],
 e:['🟣 Эпическая игрушка','Позови друга в адвент. Когда он откроет своё первое окошко, игрушка откроется у тебя.','#7A2FD0'],
 l:['🟡 Легендарная игрушка','Выложи свою ёлку в соцсети и отметь нашу школу. Можно 3 раза — 3 легендарные игрушки.','#E39A10']};
function spk(c){if(c!=='e'&&c!=='l')return '';var s='',P=[[6,16],[80,8],[86,62],[10,70]];for(var k=0;k<(c==='l'?4:2);k++)s+='<i class="spk" style="left:'+P[k][0]+'%;top:'+P[k][1]+'%;animation-delay:'+(k*.45)+'s">✦</i>';return s;}
function shelfToy(f){
  var c=rar(f),hf=hasFam(f);
  if(hf){var col=pickOf(f);return '<div class="wt slot'+(c!=='c'?' t-'+c:'')+(openFam===f?' s-open':'')+'" data-f="'+f+'" tabindex="0" role="button" title="'+esc(en(f,col))+'" aria-label="'+esc(en(f,col))+'">'+spk(c)+pic(src(f,col))+'<span class="ok">'+placedOf(f)+'/'+cntOf(f)+'</span></div>';}
  return '<div class="wt m'+(c!=='c'?' t-'+c:'')+'" tabindex="0" data-lock="'+c+'">'+spk(c)+'<div class="wtip"><b>'+TIPS[c][0]+'</b>'+TIPS[c][1]+'<br><button class="more" type="button" data-c="'+c+'" style="background:'+TIPS[c][2]+'">Подробнее об условиях</button></div>'+pic('img/box_'+{c:'common',r:'rare',e:'epic',l:'legend'}[c]+'.webp').replace('class="pic"','class="pic bx"')+'</div>';
}
function shelf(cls,title,list,inCase){var own=list.filter(hasFam).length;
  var row='<div class="wrow">'+list.map(shelfToy).join('')+'</div>';
  return '<div class="sh '+cls+'"><span class="wplate">'+title+' <small>'+own+' из '+list.length+'</small></span>'+(inCase?'<div class="case">'+row+'</div>':row)+'</div>';}
function renderTree(){
  var has={pine:true};for(var d in S.opened){var it=DAYS[S.opened[d]];if(it.tree)has[it.tree]=true;}
  var common=ORDERF,all=common.concat(SPEC.r,SPEC.e,SPEC.l),got=all.filter(hasFam).length;
  var COLL=['#FF5A5A','#FFD23F','#4CD97B','#4C9BFF','#C26BFF','#FF8AD8'],L='';
  for(var i=0;i<14;i++)L+='<span class="wbulb" style="left:'+(4+i*7)+'%;top:'+(10+Math.sin(i/13*Math.PI)*12)+'px;background:'+COLL[i%6]+';color:'+COLL[i%6]+';animation-delay:'+(i%5*.4)+'s"></span>';
  var h='<div class="wsduo"><div class="room" id="room"><div class="wlights"><svg viewBox="0 0 100 40" preserveAspectRatio="none"><path d="M0 6 Q50 34 100 6" stroke="#2b3a2a" stroke-width=".5" fill="none"/></svg>'+L+'</div>'+
   '<div class="wwin" style="left:20px"><i></i><i></i></div><div class="wwin" style="right:20px"><i></i><i></i></div>'+
   '<div class="wsign"><div class="board"><b>Мастерская эльфов</b><small>Elf\'s Workshop</small></div></div>'+
   '<div class="wtop"><span class="wcoll">🎄 Собрано '+got+' из '+all.length+'</span><span class="wcoins">🪙 '+coins()+'</span></div>'+
   '<div id="panelBox"></div><div class="shelves" id="shelves">'+
   shelf('','Обычные',common)+shelf('rare','🔵 Редкие — за шкалу подарков',SPEC.r)+shelf('epic','🟣 Эпические — за друзей',SPEC.e)+shelf('leg','🟡 Легендарные — за соцсети',SPEC.l,true)+'</div>'+
   '<div class="wtrees"><span>Моя ёлка:</span>'+['pine','snowy','gold'].map(function(t){return '<button type="button" data-tree="'+t+'" class="'+(S.tree===t?'on':'')+'" '+(has[t]?'':'disabled title="Выпадет в календаре"')+' aria-label="'+TREES[t][1]+'">'+pic('img/tree_'+t+'.webp')+(has[t]?'':'<span class="lk">🔒</span>')+'</button>';}).join('')+
   '<span class="tb"><button type="button" class="btn sm" id="snapB">📸 Сохранить ёлку</button><button type="button" class="btn ghost sm" id="allBack">Снять всё</button></span></div></div>'+
   '<div class="treearea'+(nyeOn()?' nye':'')+'" id="area"><div class="snowfall"></div><div class="nyesw"><button type="button" data-n="0" class="'+(nyeOn()?'':'on')+'">Сейчас</button><button type="button" data-n="1" class="'+(nyeOn()?'on':'')+'">31 декабря ✨</button></div><div class="tree">'+pic('img/tree_'+S.tree+'.webp')+'</div></div></div>';
  $('adv').innerHTML=h;
  var area=$('area');
  S.placed.forEach(function(pl){addPlaced(area,pl);});
  area.querySelector('.tree img').addEventListener('load',placeToppers);placeToppers();
  area.addEventListener('pointerdown',function(e){if(e.target===area||e.target.closest('.tree')){sel=null;drawSel();}});
  $$('.nyesw button').forEach(function(b){b.onclick=function(e){e.stopPropagation();S.nye=b.dataset.n==='1';save();renderTree();};b.onpointerdown=function(e){e.stopPropagation();};});
  $$('.wtrees button[data-tree]').forEach(function(b){b.onclick=function(){S.tree=b.dataset.tree;save();renderTree();};});
  $('snapB').onclick=snapTree;
  $('allBack').onclick=function(){if(!S.placed.length){toast('На ёлке пока ничего нет');return;}
    var m=modal('<div class="mcard"><h3>Снять все украшения с ёлки?</h3><p class="hint" style="margin:0">Они вернутся на полки мастерской — повесишь заново, когда захочешь.</p><div class="btns"><button type="button" class="btn" id="y">Снять</button><button type="button" class="btn ghost" data-close>Нет</button></div></div>');
    m.querySelector('#y').onclick=function(){m.remove();S.placed=[];sel=null;save();renderTree();};};
  $$('.wt.slot').forEach(function(sl){var f=sl.dataset.f;
    drag(sl,{ok:function(){if(freeOf(f)>0)return true;openPanel(f);toast('Все '+F[f].w+' уже на ёлке. Ещё одна — 🪙 3');return false;},ghost:function(){return pic(src(f,pickOf(f)));},
      tap:function(){openPanel(f);say(en(f,pickOf(f)));},drop:function(x,y){placeAt(f,pickOf(f),x,y);}});
    sl.onkeydown=function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();openPanel(f);}};});
  $$('.wt.m').forEach(function(t){var r=t.getBoundingClientRect(),R=$('room').getBoundingClientRect();if(r.left-R.left<110)t.classList.add('edge-l');else if(R.right-r.right<110)t.classList.add('edge-r');
    t.onclick=function(e){if(e.target.closest('.more'))return;$$('.wt.m.open').forEach(function(x){if(x!==t)x.classList.remove('open');});t.classList.toggle('open');};});
  $$('.wt .more').forEach(function(b){b.onclick=function(e){e.stopPropagation();moreModal(b.dataset.c);};});
  if(openFam)openPanel(openFam,true);
  drawSel();
}
function nyeOn(){return over()||!!S.nye;}
/* «Подробнее об условиях» — что сделать, чтобы открыть игрушку */
function moreModal(c){
  var nx=nextMilestone(),own=SPEC[c]?SPEC[c].filter(hasFam).length:0;
  var body={c:'<p style="margin:0">Каждый день в календаре открывается одно окошко, а в нём — игрушка и новое английское слово. Сегодняшнее и вчерашнее окошко — бесплатно, более ранние — за 🪙 5.</p><p style="margin:0">Какая игрушка в каком окошке — секрет, пока не откроешь.</p>',
    r:'<p style="margin:0">Каждое открытое окошко зажигает лампочку на гирлянде дней. На 5, 10, 15, 20 и 25 открытых окошках — редкая игрушка-сюрприз, между ними — монетки.</p><p style="margin:0"><b>Сейчас:</b> открыто '+nOpened()+' окошек'+(nx?', до следующего подарка — '+(nx-nOpened()):'')+'. Собрано редких: '+own+' из 5.</p>',
    e:'<ol style="margin:0;padding-left:20px;text-align:left"><li>Нажми «Позвать друга» и отправь ссылку.</li><li>Друг заходит по ссылке, регистрируется и открывает своё первое окошко.</li><li>У тебя открывается эпическая игрушка-сюрприз.</li></ol><p style="margin:0">По одной за каждого друга, всего 10. Друзей пришло: '+(S.friends||0)+' из 10.</p><div class="promo" style="font-size:12px;letter-spacing:0">app.wowteach.ru/advent?friend='+esc((S.name||'masha').toLowerCase())+'</div>',
    l:'<ol style="margin:0;padding-left:20px;text-align:left"><li>Нажми «📸 Сохранить ёлку» под мастерской.</li><li>Выложи картинку в пост или сторис и отметь нашу школу.</li><li>Сделай скриншот и прикрепи его здесь.</li><li>Мы проверим — и откроется легендарная игрушка.</li></ol><p style="margin:0">Можно 3 раза. Прикреплено: '+(S.posts||0)+' из 3.</p>'}[c];
  var btn={c:'<button type="button" class="btn" data-close id="mGo">К календарю</button>',r:'<button type="button" class="btn" data-close id="mGo">К календарю</button>',
    e:'<button type="button" class="btn" id="mFr">📨 Позвать друга</button><button type="button" class="btn ghost sm" id="mDemoE">👀 В макете: друг открыл окошко</button>',
    l:'<button type="button" class="btn" id="mSh" style="background:#E39A10">📎 Прикрепить скриншот</button><button type="button" class="btn ghost sm" id="mDemoL" hidden>👀 В макете: проверка пройдена</button>'}[c];
  var m=modal('<div class="mcard wide"><h3>'+TIPS[c][0].replace('игрушка','игрушки')+'</h3>'+body+'<div class="btns">'+btn+'<button type="button" class="btn ghost" data-close>Закрыть</button></div></div>');
  var go=m.querySelector('#mGo');if(go)go.onclick=function(){m.remove();S.tab='cal';save();render();};
  var fr=m.querySelector('#mFr');if(fr)fr.onclick=function(){var t='Привет! Давай вместе вести новогодний адвент-календарь в WowSpeak: app.wowteach.ru/advent?friend='+(S.name||'masha').toLowerCase();try{navigator.clipboard.writeText(t).then(function(){toast('Ссылка скопирована — отправь её другу');},function(){toast('Ссылка: app.wowteach.ru/advent');});}catch(e){toast('Ссылка: app.wowteach.ru/advent');}};
  var de=m.querySelector('#mDemoE');if(de)de.onclick=function(){if((S.friends||0)>=10){toast('Все 10 эпических уже собраны');return;}m.remove();S.friends=(S.friends||0)+1;var f=grant('e');save();if(f)revealSpec(f);};
  var sh=m.querySelector('#mSh');if(sh)sh.onclick=function(){if((S.posts||0)>=3){toast('Все 3 легендарные уже собраны');return;}sh.textContent='⏳ Скриншот на проверке';sh.disabled=true;m.querySelector('#mDemoL').hidden=false;};
  var dl=m.querySelector('#mDemoL');if(dl)dl.onclick=function(){m.remove();S.posts=(S.posts||0)+1;var f=grant('l');save();if(f)revealSpec(f);};
}
function grant(k){var f=SPEC[k].filter(function(x){return !hasFam(x);})[0];if(!f)return null;giveSpec(S,f);return f;}
/* открытие особой игрушки: лучи цвета редкости, искры, звук */
function revealSpec(f){var c=rar(f);sfx('rare');
  var m=modal('<div class="mcard rev '+c+'"><span class="rib">'+{r:'Редкая',e:'Эпическая',l:'Легендарная'}[c]+'</span><div class="art">'+pic(src(f,''))+'</div><div class="word">'+esc(F[f].w)+'<button type="button" class="say" aria-label="Послушать">🔊</button></div><div class="trn">'+esc(F[f].t)+'</div><div class="hint">Она уже на полке мастерской — тяни её на ёлку!</div><div class="btns"><button type="button" class="btn pink" id="toTree">К ёлке 🎄</button><button type="button" class="btn ghost" data-close>Ура!</button></div></div>');
  confetti(window.innerWidth/2,window.innerHeight/2,c);setTimeout(function(){say(F[f].w);},700);m.querySelector('.say').onclick=function(){say(F[f].w);};
  m.querySelector('#toTree').onclick=function(){m.remove();S.page='advent';S.tab='tree';save();render();};
  if(S.page==='advent'&&S.tab==='tree')renderTree();return m;}
/* панель игрушки: цвета, сколько штук, купить ещё одну */
function openPanel(f,silent){
  openFam=f;$$('.wt.slot').forEach(function(s){s.classList.toggle('s-open',s.dataset.f===f);});
  var box=$('panelBox');if(!box)return;
  var cur=S.pick[f]!==undefined?S.pick[f]:pickOf(f),cs=colsOf(f),spec=rar(f)!=='c';
  var sw=cs.length>1?cs.map(function(c){var o=owns(f,c);return '<div class="swi '+(o?'own':'not')+(c===cur?' cur':'')+'" data-c="'+c+'" tabindex="0" role="button" title="'+esc(en(f,c))+'">'+pic(src(f,c))+
      (c?'<i class="cd" style="background:'+CW[c][3]+'"></i>':'')+'<span class="c">'+(o?'✓':'🪙1')+'</span></div>';}).join(''):'';
  var wide=F[f].wide?'<span class="hint" style="font-size:12px">Куски: '+(S.wsz[f]||[]).map(function(v){return v<.6?'маленький':v<.9?'средний':'большой';}).join(', ')+'</span>':'';
  box.innerHTML='<div class="panel"><div class="panel-h"><b>'+esc(F[f].w)+' — '+esc(F[f].t)+'</b><button type="button" class="x" aria-label="Закрыть">×</button></div>'+(sw?'<div class="sw">'+sw+'</div>':'')+wide+'<div class="act" id="act"></div></div>';
  box.querySelector('.x').onclick=closePanel;
  function act(){var c=S.pick[f]!==undefined?S.pick[f]:cur,a=$('act'),o=owns(f,c);
    a.innerHTML='<button type="button" class="mini-say" aria-label="Послушать">🔊</button><div class="t"><b>'+esc(en(f,c))+'</b> — '+esc(ru(f,c))+'<br>У тебя '+cntOf(f)+' шт., на ёлке '+placedOf(f)+(o?'':' · этого цвета пока нет')+'</div>'+
      (o?'':'<button type="button" class="btn sm" id="buy">Цвет · 🪙 1</button>')+(spec?'':'<button type="button" class="btn sm pink" id="more1">Ещё одна · 🪙 3</button>');
    a.querySelector('.mini-say').onclick=function(){say(en(f,c));};
    var b=a.querySelector('#buy');if(b)b.onclick=function(){buyColour(f,c,function(){renderTree();});};
    var m1=a.querySelector('#more1');if(m1)m1.onclick=function(){buyCopy(f);};}
  act();
  $$('.swi',box).forEach(function(s){var c=s.dataset.c;
    drag(s,{ok:function(){if(!owns(f,c))return false;if(freeOf(f)>0)return true;toast('Все '+F[f].w+' уже на ёлке. Ещё одна — 🪙 3');return false;},ghost:function(){return pic(src(f,c));},
      tap:function(){S.pick[f]=c;save();$$('.swi',box).forEach(function(e){e.classList.toggle('cur',e===s);});act();say(en(f,c));
        var sl=document.querySelector('.wt.slot[data-f="'+f+'"] .pic');if(sl&&owns(f,c))sl.src=src(f,c);},
      drop:function(x,y){S.pick[f]=c;placeAt(f,c,x,y);}});});
  if(!silent)box.scrollIntoView({block:'nearest'});
}
function closePanel(){openFam=null;var b=$('panelBox');if(b)b.innerHTML='';$$('.wt.slot').forEach(function(s){s.classList.remove('s-open');});}
function buyColour(f,c,then){
  var m=modal('<div class="mcard"><div class="art" style="width:130px;height:130px">'+pic(src(f,c))+'</div><h3>'+esc(en(f,c))+'</h3><div class="trn">'+esc(ru(f,c))+'</div>'+
    '<p class="hint" style="margin:0">Новый цвет останется у тебя насовсем: любую такую игрушку можно перекрасить в него.</p><p style="margin:0"><b>У тебя: 🪙 '+coins()+'</b></p>'+
    '<div class="btns"><button type="button" class="btn pink" id="yb"'+(coins()<1?' disabled':'')+'>Купить за 🪙 1</button><button type="button" class="btn ghost" data-close>Не сейчас</button></div></div>');
  m.querySelector('#yb').onclick=function(){m.remove();if(!spend(1,'🎨','Новый цвет: '+ru(f,c)))return;S.own[f][c]=1;S.pick[f]=c;save();sfx('coin');say(en(f,c));toast(en(f,c)+' — твой! (−1 🪙)');then();};
}
function buyCopy(f){var c=pickOf(f);
  var m=modal('<div class="mcard"><div class="art" style="width:130px;height:130px">'+pic(src(f,c))+'</div><h3>Ещё один '+esc(F[f].w)+'</h3>'+
    '<p class="hint" style="margin:0">У тебя '+cntOf(f)+' шт. Ещё одна такая игрушка — 🪙 3. Цвет выберешь из тех, что уже есть.</p><p style="margin:0"><b>У тебя: 🪙 '+coins()+'</b></p>'+
    '<div class="btns"><button type="button" class="btn pink" id="yb"'+(coins()<3?' disabled':'')+'>Купить за 🪙 3</button><button type="button" class="btn ghost" data-close>Не сейчас</button></div></div>');
  m.querySelector('#yb').onclick=function(){m.remove();if(!spend(3,'🎄','Ещё одна игрушка: '+F[f].t))return;S.cnt[f]=cntOf(f)+1;if(F[f].wide)S.wsz[f]=(S.wsz[f]||[]).concat([1]);save();sfx('coin');toast(F[f].w+' — ещё одна! (−3 🪙)');renderTree();};
}
function cl(v,a,b){return Math.max(a,Math.min(b,v));}
function placeAt(f,c,x,y){
  if(!f||c===null)return;var area=$('area');if(!area)return;var r=area.getBoundingClientRect();
  if(x<r.left||x>r.right||y<r.top||y>r.bottom)return;
  if(freeOf(f)<=0){toast('Все '+F[f].w+' уже на ёлке. Ещё одна — 🪙 3');openPanel(f);return;}
  var gs=1;if(F[f].wide){var left=sizesLeft(f);gs=left.length?Math.max.apply(null,left):1;}
  var pl={id:Date.now(),f:f,c:c,x:cl((x-r.left)/r.width*100,3,97),y:cl((y-r.top)/r.height*100,3,97),s:gs,r:0,sx:1,sy:1,auto:F[f].top?1:0};
  if(F[f].top)S.placed=S.placed.filter(function(p){return !F[p.f].top;});
  S.placed.push(pl);sel=pl.id;save();renderTree();say(en(f,c));
}
/* верхушка встаёт на кончик ёлки — считаем по тому, где на самом деле нарисована ёлка */
function placeToppers(keepSel){
  var area=$('area');if(!area)return;var img=area.querySelector('.tree img');if(!img||!img.naturalWidth)return;
  var A=area.getBoundingClientRect(),B=img.getBoundingClientRect(),sc=Math.min(B.width/img.naturalWidth,B.height/img.naturalHeight),h=img.naturalHeight*sc;
  var tipY=(B.top-A.top)+(B.height-h)/2+0.019*h,cx=(B.left-A.left)+B.width/2;
  $$('.placed.ptop',area).forEach(function(el){var pl=S.placed.filter(function(p){return p.id==el.dataset.id;})[0];if(!pl||!pl.auto)return;
    var w=A.width*F[pl.f].sz*pl.s/100,k=pl.f==='angel'?0.36:0.3;pl.x=cx/A.width*100;pl.y=Math.max(tipY-w*k,w/2+6)/A.height*100;
    el.style.left=pl.x+'%';el.style.top=pl.y+'%';});
  if(!keepSel)drawSel();
}
window.addEventListener('resize',function(){if($('area'))placeToppers();if(S.tab==='cal'&&S.page==='advent'&&!ALLteacher())renderCal();});
function ALLteacher(){return viewMode(ALL.cur);}
function styleEl(el,pl){var fm=F[pl.f],w=fm.sz*pl.s*(fm.wide?pl.sx:1);
  el.style.left=pl.x+'%';el.style.top=pl.y+'%';el.style.width=w+'%';el.style.aspectRatio=fm.wide?String(fm.wide*pl.sx/pl.sy):'1';el.style.setProperty('--r',pl.r+'deg');}
/* лампочки поверх картинки огоньков: мерцают по очереди (положения взяты по самой картинке) */
var FL=[[10,46,'#FFE14A'],[20.5,60,'#FF5CB8'],[33,68,'#4CC3FF'],[44.8,73,'#7DFF5A'],[55.3,73,'#FFE14A'],[67.2,69,'#FF5CB8'],[79.2,60,'#4CC3FF'],[89.6,47,'#7DFF5A']];
function addPlaced(area,pl){
  var fm=F[pl.f],el=document.createElement('div');if(!fm)return;
  el.className='placed'+(fm.wide?' pwide':'')+(fm.top?' ptop':'');el.dataset.id=pl.id;el.innerHTML=pic(src(pl.f,pl.c))+(pl.f==='fairy_lights'?'<span class="fl">'+FL.map(function(b,k){return '<i style="left:'+b[0]+'%;top:'+b[1]+'%;--c:'+b[2]+';animation-delay:'+(k*.21)+'s"></i>';}).join('')+'</span>':'');el.setAttribute('aria-label',en(pl.f,pl.c));
  styleEl(el,pl);area.appendChild(el);
  drag(el,{ok:function(){return true;},move:true,
    tap:function(){sel=pl.id;drawSel();say(en(pl.f,pl.c));},
    drop:function(x,y){var r=area.getBoundingClientRect();
      if(x<r.left||x>r.right||y<r.top||y>r.bottom){removePl(pl);return;}
      pl.x=cl((x-r.left)/r.width*100,2,98);pl.y=cl((y-r.top)/r.height*100,2,98);pl.auto=0;sel=pl.id;save();styleEl(el,pl);drawSel();}});
}
function removePl(pl){S.placed=S.placed.filter(function(p){return p.id!==pl.id;});if(sel===pl.id)sel=null;save();renderTree();toast(en(pl.f,pl.c)+' — вернулась на полку');}
/* рамка выбранного украшения: уголок — размер, кружок сверху — поворот, у гирлянд розовые — немного длину и толщину */
function drawSel(){
  var area=$('area');if(!area)return;$$('.frame,.hd,.tool',area).forEach(function(e){e.remove();});$$('.placed.sel',area).forEach(function(e){e.classList.remove('sel');});
  if(sel===null)return;var pl=S.placed.filter(function(p){return p.id===sel;})[0];if(!pl){sel=null;return;}
  var el=area.querySelector('.placed[data-id="'+pl.id+'"]');if(!el)return;var fm=F[pl.f];el.classList.add('sel');
  el.insertAdjacentHTML('beforeend','<span class="frame"></span><span class="hd sc" data-h="sc" title="Потяни — больше или меньше">⤡</span><span class="hd ro" data-h="ro" title="Потяни — повернуть">↻</span>'+
    (fm.wide?'<span class="hd lx" data-h="sx" title="Длиннее или короче">↔</span><span class="hd rx" data-h="sx" title="Длиннее или короче">↔</span><span class="hd by" data-h="sy" title="Толще или тоньше">↕</span>':''));
  $$('.hd',el).forEach(function(hd){handle(hd,el,pl);});
  var t=document.createElement('div');t.className='tool';
  var cs=colsOf(pl.f),dots=cs.length>1?cs.map(function(c){return '<button type="button" class="dt'+(c===pl.c?' cur':'')+(owns(pl.f,c)?'':' no')+'" data-c="'+c+'" style="background:'+CW[c][3]+'" title="'+esc(en(pl.f,c))+(owns(pl.f,c)?'':' · 🪙 1')+'" aria-label="'+esc(ru(pl.f,c))+'"></button>';}).join(''):'';
  t.innerHTML='<button type="button" data-a="say">🔊 '+esc(en(pl.f,pl.c))+'</button>'+dots+'<button type="button" data-a="rm">↩ На полку</button><span class="hint2">'+(fm.top?'Верхушку можно двигать. ':'')+'⤡ размер · ↻ поворот'+(fm.wide?' · ↔ длина · ↕ толщина':'')+'</span>';
  area.appendChild(t);
  var A=area.getBoundingClientRect(),E=el.getBoundingClientRect(),top=E.bottom-A.top+22;if(top>A.height-90)top=E.top-A.top-100;
  t.style.left=cl((E.left+E.width/2-A.left)/A.width*100,22,78)+'%';t.style.top=Math.max(6,top)+'px';
  t.querySelector('[data-a="say"]').onclick=function(){say(en(pl.f,pl.c));};
  t.querySelector('[data-a="rm"]').onclick=function(){removePl(pl);};
  $$('.dt',t).forEach(function(b){b.onclick=function(){var c=b.dataset.c;
    function apply(){pl.c=c;S.pick[pl.f]=c;save();renderTree();say(en(pl.f,c));}
    if(owns(pl.f,c))apply();else buyColour(pl.f,c,apply);};});
}
function handle(hd,el,pl){
  hd.addEventListener('pointerdown',function(e){e.stopPropagation();e.preventDefault();
    var E=el.getBoundingClientRect(),cx=E.left+E.width/2,cy=E.top+E.height/2,k=hd.dataset.h,s0=pl.s,sx0=pl.sx,sy0=pl.sy;
    function loc(x,y){var a=-pl.r*Math.PI/180,dx=x-cx,dy=y-cy;return [dx*Math.cos(a)-dy*Math.sin(a),dx*Math.sin(a)+dy*Math.cos(a)];}
    var st=loc(e.clientX,e.clientY),d0=Math.hypot(st[0],st[1])||1;
    try{hd.setPointerCapture(e.pointerId);}catch(_){}
    function mv(ev){
      if(k==='ro'){pl.r=Math.round(Math.atan2(ev.clientX-cx,-(ev.clientY-cy))*180/Math.PI);}
      else{var p=loc(ev.clientX,ev.clientY);
        if(k==='sc')pl.s=cl(s0*Math.hypot(p[0],p[1])/d0,.3,3);if(k==='sc'&&F[pl.f].wide)pl.s=cl(pl.s,.4,1.3);
        if(k==='sx')pl.sx=cl(sx0*Math.abs(p[0])/(Math.abs(st[0])||1),.85,1.2);
        if(k==='sy')pl.sy=cl(sy0*Math.abs(p[1])/(Math.abs(st[1])||1),.85,1.25);}
      styleEl(el,pl);if(F[pl.f].top)placeToppers(true);
    }
    function up(){hd.removeEventListener('pointermove',mv);hd.removeEventListener('pointerup',up);hd.removeEventListener('pointercancel',up);save();drawSel();}
    hd.addEventListener('pointermove',mv);hd.addEventListener('pointerup',up);hd.addEventListener('pointercancel',up);
  });
}
