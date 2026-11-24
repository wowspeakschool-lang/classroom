function renderAdvent(){
  var bar;
  if(isTest())bar='<span class="date">🧪 Тест</span><span class="hint">Открыто: '+nOpened()+' из 31</span>';
  else if(over())bar='<span class="date">🎄 Календарь закончился</span><span class="pill p-green">Ёлка и мастерская остаются с тобой — наряжай и слушай слова</span>';
  else bar='<span class="date">📅 Сегодня '+S.day+' декабря</span>'+((S.day in S.opened)?'<span class="pill p-green">Сегодняшнее окошко открыто ✓</span>':'<span class="pill p-pink">Сегодняшнее окошко — бесплатно</span>')+(S.day>1&&!((S.day-1) in S.opened)?'<span class="pill p-pink">Вчерашнее — тоже бесплатно</span>':'')+
    '<span class="legend"><span><i class="lg" style="background:var(--pink)"></i>сегодня и вчера — бесплатно</span><span>🪙 5 — окошко раньше</span><span><i class="lg" style="background:#E6E9F5"></i>ещё рано 🔒</span></span>';
  $('page').innerHTML='<div class="adv-tabs">'+[['cal','🗓 Календарь'],['tree','🎄 Мастерская и ёлка'],['forest','🌲 Лес']].map(function(x){return '<button type="button" data-t="'+x[0]+'" class="'+(S.tab===x[0]?'on':'')+'">'+x[1]+'</button>';}).join('')+'</div>'+
    plaque()+(S.tab==='cal'?'<div class="advbar">'+bar+'</div>':'')+'<div id="adv"></div>';
  $$('.adv-tabs button').forEach(function(b){b.onclick=function(){S.tab=b.dataset.t;sel=null;save();render();};});
  if(S.tab==='tree')renderTree();else if(S.tab==='forest')renderForest();else renderCal();
}
/* лес ёлок — делается отдельно; здесь заглушка */
function renderForest(){$('adv').innerHTML='<div class="forest"><div><b>🌲 Лес ёлок</b>Здесь будут ёлки всех ребят школы: снег, зверьки и твоя ёлка с подписью.<br>Скоро!</div></div>';}
/* шкала «Гирлянда дней»: 31 лампочка, открытые мерцают; будущие подарки — одинаковые закрытые коробки */
function scaleHtml(){
  var n=nOpened(),nx=nextMilestone(),COL=['#FF5A5A','#FFD23F','#4CD97B','#4C9BFF','#C26BFF','#FF8AD8'];
  var W='<svg viewBox="0 0 100 56" preserveAspectRatio="none"><path d="M0 6 Q12.5 30 25 6 Q37.5 30 50 6 Q62.5 30 75 6 Q87.5 30 100 6" stroke="#0E1433" stroke-width=".6" fill="none"/></svg>';
  for(var k=1;k<=31;k++){var x=1.6+(k-1)*(96.8/30),y=4+Math.sin(((x)%25)/25*Math.PI)*16,m=MILE[k],g='';
    if(m){if(k<=n){g='<span class="gift got" title="Получено">'+(m.cert?'🎓':m.r?pic('img/n/'+(SPEC.r[[5,10,15,20,25].indexOf(k)]||'snow_globe')+'.webp'):'🪙'+m.a)+'</span>';}
      else g='<span class="gift'+(k===nx&&k-n<=2?' next':'')+'">'+pic('img/box_common.webp')+'</span>';}
    W+='<div class="gb'+(k<=n?' on':'')+(k===n+1?' today':'')+'" style="left:'+x+'%;--y:'+y+'px;--c:'+COL[k%6]+';--i:'+k+'"><span class="l"></span><span class="d">'+k+'</span>'+g+'</div>';}
  var sub=nx?'Открыто '+n+' из 31 · до следующего подарка — '+(nx-n)+' '+(nx-n===1?'окошко':nx-n<5?'окошка':'окошек'):'Все подарки шкалы получены 🎉';
  return '<div class="gscale"><h3>✨ Гирлянда подарков <small>'+sub+'</small></h3><div class="wire'+(over()?' all':'')+'"><div class="in">'+W+'</div></div></div>';
}
/* мои подарки: настоящие подарки из окошков */
function giftsHtml(){
  var got=S.gifts||[],h='';
  Object.keys(GIFTS).forEach(function(d){var g=GIFTS[d],has=got.indexOf(+d)>=0;
    h+='<div class="gcard'+(has?'':' lock')+'"><span class="gi">'+(has?g.ic:'🎁')+'</span><div><b>'+(has?g.t:'Секретный подарок')+'</b><small>'+(has?g.s:'спрятан в одном из окошек')+'</small>'+(has&&g.promo?'<span class="promo">'+g.promo+'</span>':'')+'</div>'+
      (has&&g.btn?'<button type="button" class="btn sm" data-g="'+d+'">'+g.btn+'</button>':'')+'</div>';});
  return '<div class="mygifts"><h3>🎁 Мои подарки</h3><p class="hint" style="margin:0">Иногда в окошке вместе с игрушкой лежит настоящий подарок от школы. Всего их 5.</p><div class="gl">'+h+'</div></div>';
}
function renderCal(){
  $('adv').innerHTML=scaleHtml()+calHtml(S,false)+giftsHtml();
  $$('#adv .door').forEach(function(b){b.onclick=function(){doorClick(+b.dataset.d,b);};});
  $$('#adv .gcard [data-g]').forEach(function(b){b.onclick=function(){var g=GIFTS[b.dataset.g];toast(g.btn==='Скачать'?'В макете файла нет — на платформе здесь скачается '+g.t.toLowerCase():'В макете записи нет — на платформе здесь откроется запись');};});
}
function shake(b){b.classList.add('shake');setTimeout(function(){b.classList.remove('shake');},500);}
function doorClick(d,b){
  var o=S.opened[d];if(o!==undefined){wordModal(DAYS[o],{});return;}
  if(isTest()||freeDay(d))return openDay(d,b);
  if(d>S.day){shake(b);toast('Это окошко откроется '+d+' декабря ⭐');return;}
  var m=modal('<div class="mcard"><div class="art" style="width:120px;height:120px">'+pic(gift(d))+'</div><h3>Окошко '+d+' декабря</h3>'+
    '<p class="hint" style="margin:0">Это окошко можно открыть за 5 монеток. Сегодняшнее и вчерашнее окошко — всегда бесплатные.</p>'+
    '<p style="margin:0"><b>У тебя: 🪙 '+coins()+'</b></p><div class="btns"><button type="button" class="btn pink" id="buyDay"'+(coins()<5?' disabled':'')+'>Открыть за 🪙 5</button><button type="button" class="btn ghost" data-close>Не сейчас</button></div>'+
    (coins()<5?'<p class="hint" style="margin:0">Не хватает монеток — их дают за уроки и домашку.</p>':'')+'</div>');
  var bb=m.querySelector('#buyDay');if(bb)bb.onclick=function(){m.remove();if(spend(5,'🎁','Окошко '+d+' декабря'))openDay(d,b);};
}
/* звуки и конфетти */
var SFX={};function sfx(n){try{var a=SFX[n]||(SFX[n]=new Audio('audio/s_'+n+'.mp3'));a.currentTime=0;a.volume=.8;a.play().catch(function(){});}catch(e){}}
function confetti(x,y,kind){var fx=document.createElement('div');fx.className='fx';
  var C={c:['#F7628C','#FFC83D','#6A4DF4','#22B573','#4CC3FF'],r:['#4C9BFF','#9CC8FF','#ffffff','#2E6FD6'],e:['#B26BFF','#E07BFF','#F0D6FF','#7A2FD0'],l:['#FFD45A','#FF9F1C','#FFF2B8','#E39A10'],g:['#F7628C','#FFD45A','#ffffff','#22B573']}[kind||'c'];
  var h='<span class="flash" style="left:'+x+'px;top:'+y+'px"></span>';
  for(var i=0;i<46;i++){var a=Math.random()*Math.PI*2,r=120+Math.random()*260;h+='<i style="left:'+x+'px;top:'+y+'px;background:'+C[i%C.length]+';--dx:'+Math.cos(a)*r+'px;--dy:'+(Math.sin(a)*r+160)+'px;--rot:'+(Math.random()*720-360)+'deg;--t:'+(1+Math.random()*.8)+'s"></i>';}
  fx.innerHTML=h;document.body.appendChild(fx);setTimeout(function(){fx.remove();},2000);}
/* показать окна по очереди: следующее — когда закрыли предыдущее */
function chain(fns){var i=0;function next(){var f=fns[i++];if(!f)return;var m=f();if(!m){next();return;}var orig=m.remove.bind(m);m.remove=function(){orig();setTimeout(next,180);};}next();}
function openDay(d,b){
  var it=DAYS[nOpened()];shake(b);preload(dayEn(it));sfx('open');
  var r=b.getBoundingClientRect();confetti(r.left+r.width/2,r.top+r.height/2,'c');
  setTimeout(function(){
    var ev=applyOpen(S,d);var bonus=ev.rew.some(function(x){return x.a;})||false;
    save();renderNav();renderAdvent();showCoins(bonus);
    var eb=it.tree?'Новая ёлка!':d===N||nOpened()===N?'Последнее окошко! С Новым годом!':ev.newCol?'Новый цвет — в подарок!':'Новое украшение!';
    var hint=it.tree?'Ёлка поменялась — посмотри!':F[it.f].top?'Это украшение для макушки ёлки — поставь его наверх.':F[it.f].wide?'Сразу три куска: маленький, средний и большой — все на полке мастерской.':'Оно уже на полке мастерской 🧝 — тяни его на ёлку.';
    var q=[function(){return wordModal(it,{eb:eb,hint:hint,fin:nOpened()===N});}];
    if(ev.gift)q.push(function(){return giftModal(ev.gift);});
    ev.rew.forEach(function(rw){q.push(function(){return rewardModal(rw);});});
    chain(q);
  },350);
}
function giftModal(g){sfx('gift');
  var m=modal('<div class="mcard rev g"><span class="rib">Подарок от школы</span><div class="art">'+pic('img/gift3.webp').replace('class="pic"','class="pic giftbox"')+'</div><h3 style="color:#fff">'+g.ic+' '+esc(g.t)+'</h3><div class="trn">'+esc(g.s)+'</div>'+
    (g.promo?'<div class="promo">'+g.promo+'</div><div class="hint">Покажи промокод маме или папе — он действует на первый месяц подписки WowSpace.</div>':'<div class="hint">Подарок лежит в блоке «Мои подарки» под календарём.</div>')+
    '<div class="btns"><button type="button" class="btn pink" data-close>Ура!</button></div></div>');
  setTimeout(function(){confetti(window.innerWidth/2,window.innerHeight/2,'g');},900);return m;}
function rewardModal(rw){
  if(rw.f){S.page==='advent'&&S.tab==='tree'&&renderTree();var m=revealSpec(rw.f);m.querySelector('.hint').textContent='Шкала подарков: '+rw.n+' открытых окошек! Игрушка уже на полке мастерской.';return m;}
  sfx('coin');var m2=modal('<div class="mcard rev '+(rw.cert?'l':'g')+'"><span class="rib">Шкала подарков</span><div class="art" style="display:grid;place-items:center;font-size:90px">'+(rw.cert?'🎓':'🪙')+'</div><h3 style="color:#fff">'+rw.n+' открытых окошек!</h3>'+
    (rw.cert?'<div class="trn">Грамота «Знаток новогодних слов» — все 31 слово твои!</div>':'')+'<div class="word" style="color:#FFE9A0">+🪙 '+rw.a+'</div><div class="btns"><button type="button" class="btn pink" data-close>Забрать</button></div></div>');
  confetti(window.innerWidth/2,window.innerHeight/2,rw.cert?'l':'g');return m2;}
/* карточка слова: послушать, повторить за голосом и послушать себя рядом с образцом */
function wordModal(it,o){
  var m=modal('<div class="mcard" role="dialog">'+(o.eb?'<div class="eb">'+o.eb+'</div>':'')+'<div class="art">'+pic(dayImg(it))+'</div>'+
    '<div class="word">'+esc(dayEn(it))+'<button type="button" class="say" aria-label="Послушать">🔊</button></div><div class="trn">'+esc(dayRu(it))+'</div>'+
    '<div class="rep"><button type="button" class="btn sm rec" id="recB">🎙 Повтори за мной</button><span class="rt" id="recT"></span>'+
    '<button type="button" class="btn ghost sm" id="cmpB" hidden>▶ Образец и я</button></div><div class="hint" id="recN">'+(S.repDay===S.day?'':'Повтори слово — получишь 🪙 1 (раз в день)')+'</div>'+
    (o.hint?'<div class="hint">'+o.hint+'</div>':'')+
    '<div class="btns"><button type="button" class="btn pink" id="toTree">К ёлке 🎄</button><button type="button" class="btn ghost" data-close>'+(o.eb?'Дальше':'Закрыть')+'</button></div></div>');
  function sayIt(){if(o.fin)say(dayEn(it),'Merry Christmas!');else say(dayEn(it));}
  if(o.eb)sayIt();m.querySelector('.say').onclick=sayIt;
  m.querySelector('#toTree').onclick=function(){S.page='advent';S.tab='tree';save();render();m.remove();};
  repeatAfterMe(m,dayEn(it));return m;
}
/* «Повтори за мной»: запись голоса там, где браузер даёт микрофон; 🪙 1 раз в день (Анна, 24.11.2026) */
function repCoin(m){if(S.repDay===S.day)return;S.repDay=S.day;addLog('🎙','Повтори за мной',1);save();showCoins(true);sfx('coin');toast('+🪙 1 за «Повтори за мной»!');var n=m.querySelector('#recN');if(n&&n.textContent.indexOf('🪙 1')>=0)n.textContent='';}
function repeatAfterMe(m,word){
  var recB=m.querySelector('#recB'),recT=m.querySelector('#recT'),cmpB=m.querySelector('#cmpB'),recN=m.querySelector('#recN'),mine=null,busy=false;
  function count(sec,done){var n=sec;recT.textContent='● '+n;recT.className='rt on';var iv=setInterval(function(){n--;if(n<=0){clearInterval(iv);recT.className='rt';recT.textContent='';done();}else recT.textContent='● '+n;},1000);}
  function demo(){busy=true;recB.textContent='🎙 Говори…';count(3,function(){busy=false;recB.textContent='🎙 Ещё раз';cmpB.hidden=false;repCoin(m);
    recN.hidden=false;recN.textContent='В этом макете микрофон не подключён — на платформе здесь будет твоя запись: «Образец и я» включит голос, а потом тебя.';});}
  recB.onclick=function(){if(busy)return;say(word);
    if(!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia||typeof MediaRecorder==='undefined'){demo();return;}
    navigator.mediaDevices.getUserMedia({audio:true}).then(function(st){busy=true;var ch=[],r=new MediaRecorder(st);
      r.ondataavailable=function(e){ch.push(e.data);};
      r.onstop=function(){st.getTracks().forEach(function(x){x.stop();});mine=URL.createObjectURL(new Blob(ch,{type:r.mimeType||'audio/webm'}));busy=false;recB.textContent='🎙 Ещё раз';cmpB.hidden=false;recN.hidden=true;repCoin(m);};
      setTimeout(function(){recB.textContent='🎙 Говори…';r.start();count(3,function(){try{r.stop();}catch(e){}});},900);
    }).catch(function(){demo();});};
  cmpB.onclick=function(){say(word);if(!mine){toast('В макете своей записи нет — на платформе здесь прозвучит твой голос');return;}
    setTimeout(function(){var a=new Audio(mine);a.play().catch(function(){});},1400);};
}

