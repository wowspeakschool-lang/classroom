/* особые игрушки: без цветов, свечение редкости — стилями (24.11.2026) */
var SPEC={r:['snow_globe','nutcracker','lantern','polar_bear','rocking_horse'],
  e:['teddy_bear','penguin','owl','fox','toy_train','drum','ice_skates','gingerbread_house','carousel','hot_chocolate'],
  l:['golden_unicorn','santa_sleigh','ice_palace']};
[['snow_globe','snow globe','снежный шар','m','r'],['nutcracker','nutcracker','Щелкунчик','m','r'],['lantern','lantern','фонарик','m','r'],['polar_bear','polar bear','белый медведь','m','r'],['rocking_horse','rocking horse','лошадка-качалка','f','r'],
 ['teddy_bear','teddy bear','плюшевый мишка','m','e'],['penguin','penguin','пингвин','m','e'],['owl','owl','сова','f','e'],['fox','fox','лиса','f','e'],['toy_train','toy train','игрушечный паровозик','m','e'],['drum','drum','барабан','m','e'],['ice_skates','ice skates','коньки','p','e'],['gingerbread_house','gingerbread house','пряничный домик','m','e'],['carousel','carousel','карусель','f','e'],['hot_chocolate','hot chocolate','горячий шоколад','m','e'],
 ['golden_unicorn','golden unicorn','золотой единорог','m','l'],['santa_sleigh',"Santa's sleigh",'сани Санты','p','l'],['ice_palace','ice palace','ледяной дворец','m','l']].forEach(function(x){
  F[x[0]]={w:x[1],t:x[2],g:x[3],sz:x[0]==='santa_sleigh'?16:12,rar:x[4],cols:{'':'n/'+x[0]}};AUDIO[x[1]]='audio/w_'+x[0]+'.mp3';});

/* 31 окошко: что выпадает по порядку открытия. Звезда-верхушка — третьей, гирлянда — шестой,
   чтобы главное было у всех (Анна, 24.11.2026). Последнее — ангел. */
var DAYS=[{tree:'pine'},{f:'ball',c:'red'},{f:'top_star',c:'gold'},{f:'star',c:'gold'},{f:'bell',c:'gold'},{f:'garland',c:''},{f:'candy_cane',c:'red'},{f:'snowflake',c:'white'},
 {f:'ball',c:'blue'},{f:'gingerbread',c:''},{f:'bow',c:'red'},{f:'fairy_lights',c:''},{f:'pine_cone',c:''},{f:'ball',c:'green'},{f:'stocking',c:'red'},
 {f:'present',c:'red'},{tree:'snowy'},{f:'ball',c:'gold'},{f:'tinsel',c:'gold'},{f:'heart',c:'pink'},{f:'snowman',c:''},{f:'ball',c:'silver'},{f:'icicle',c:''},
 {f:'reindeer',c:''},{f:'ball',c:'purple'},{f:'sweet',c:'pink'},{f:'mitten',c:'blue'},{tree:'gold'},{f:'cracker',c:''},{f:'clock',c:''},{f:'angel',c:''}];
var N=DAYS.length;
var ORDERF=[];DAYS.forEach(function(d){if(d.f&&ORDERF.indexOf(d.f)<0)ORDERF.push(d.f);});
function dayImg(it){return it.tree?'img/tree_'+it.tree+'.webp':src(it.f,it.c);}
function dayEn(it){return it.tree?TREES[it.tree][0]:en(it.f,it.c);}
function dayRu(it){return it.tree?TREES[it.tree][1]:ru(it.f,it.c);}
/* в кружке календаря у гирлянд — свой значок: кусок с крючком и 3–5 бусинами (23.11.2026) */
function doorImg(it){if(it.f&&F[it.f].wide)return 'img/ic_'+F[it.f].cols[it.c].split('/').pop()+'.webp';return dayImg(it);}
function gift(d){return 'img/gift'+(d%6+1)+'.webp';}

/* шкала подарков по числу открытых окошек */
var MILE={3:{a:3},5:{r:1},7:{a:5},10:{r:1},12:{a:5},15:{r:1},18:{a:7},20:{r:1},23:{a:7},25:{r:1},28:{a:10},31:{a:15,cert:1}};
function nextMilestone(n){n=n===undefined?nOpened():n;for(var k=n+1;k<=31;k++)if(MILE[k])return k;return 0;}
/* настоящие подарки — в окошках по датам */
var GIFTS={5:{id:'recipe',ic:'🍪',t:'Рецепт имбирного печенья',s:'на английском, с картинками',btn:'Скачать'},
 10:{id:'club',ic:'🗣',t:'Занятие разговорного клуба WowSpace',s:'одно занятие в подарок',btn:'Записаться'},
 15:{id:'mk',ic:'🎨',t:'Мастер-класс WowSpace',s:'один мастер-класс в подарок',btn:'Записаться'},
 22:{id:'bingo',ic:'🎲',t:'Christmas Bingo',s:'семейная игра из твоих слов',btn:'Скачать'},
 28:{id:'sale',ic:'🏷',t:'−50 % на подписку WowSpace',s:'промокод на первый месяц',promo:'XMAS50'}};

/* ---------- варианты показа ---------- */
function baseLog(){return [
  {d:'1 ноя',ic:'💼',t:'Было на начало месяца',a:31,start:1},
  {d:'4 ноя',ic:'📖',t:'Урок',s:'Super Minds 2',a:10},
  {d:'5 ноя',ic:'📚',t:'Домашка сдана',s:'Unit 2 · Homework 6',a:3},
  {d:'11 ноя',ic:'📖',t:'Урок',s:'Super Minds 2',a:10},
  {d:'12 ноя',ic:'🎡',t:'Колесо удачи',s:'выпало: наклейки',a:-30},
  {d:'18 ноя',ic:'📖',t:'Урок',s:'Super Minds 2',a:10},
  {d:'19 ноя',ic:'⭐',t:'Активность на уроке',a:2},
  {d:'25 ноя',ic:'📖',t:'Урок',s:'Super Minds 2',a:10},
  {d:'26 ноя',ic:'📚',t:'Домашка сдана',s:'Unit 3 · Homework 1',a:3}
];}
function blank(mode){return {mode:mode,day:1,opened:{},own:{},cnt:{},wsz:{},pick:{},placed:[],tree:'pine',page:'home',tab:'cal',log:baseLog(),gifts:[],rew:{},friends:0,posts:0};}
/* игрушка из окошка: один экземпляр; гирлянды — тремя кусками (маленький, средний, большой) */
function give(s,it){if(it.tree){s.tree=it.tree;return false;}var had=!!s.own[it.f];s.own[it.f]=s.own[it.f]||{};var nc=!s.own[it.f][it.c];s.own[it.f][it.c]=1;
  s.cnt[it.f]=(s.cnt[it.f]||0)+(F[it.f].wide?3:1);if(F[it.f].wide)s.wsz[it.f]=(s.wsz[it.f]||[]).concat([.5,.7,1]);return had&&nc;}
function giveSpec(s,f){s.own[f]={'':1};s.cnt[f]=1;}
/* открыть окошко d: игрушка по порядку, подарок по дате, награды шкалы. Возвращает, что выпало */
function applyOpen(s,d,quiet){var idx=Object.keys(s.opened).length,it=DAYS[idx];s.opened[d]=idx;var newCol=give(s,it);if(it.f)s.pick[it.f]=it.c;
  var ev={it:it,newCol:newCol,gift:null,rew:[]};
  if(GIFTS[d]&&s.gifts.indexOf(d)<0){s.gifts.push(d);ev.gift=GIFTS[d];}
  var n=idx+1,m=MILE[n];if(m&&!s.rew[n]){s.rew[n]=1;var r={n:n,a:m.a||0,cert:!!m.cert};
    if(m.a)s.log.push({d:s.mode==='test'?'сегодня':(s.day>31?'янв':s.day+' дек'),ic:'✨',t:'Шкала подарков: '+n+' окошек',a:m.a,s:'адвент-календарь'});
    if(m.r){var f=SPEC.r.filter(function(x){return !s.own[x];})[0];if(f){giveSpec(s,f);r.f=f;}}
    ev.rew.push(r);}
  return ev;}
function freshTest(){var s=blank('test');s.log.push({d:'30 ноя',ic:'🎁',t:'Подарок к адвенту',a:31});return s;}
function freshMiss(){
  var s=blank('miss');s.day=20;var missed=[7,8,14,18,19];
  for(var d=1;d<20;d++){if(missed.indexOf(d)>=0)continue;applyOpen(s,d,true);}
  s.tree='pine';s.own.bell.silver=1;s.own.star.red=1;s.friends=1;giveSpec(s,'teddy_bear');
  s.log=s.log.concat([
    {d:'2 дек',ic:'📖',t:'Урок',s:'Super Minds 2',a:10},
    {d:'3 дек',ic:'🎨',t:'Новый цвет: серебряный колокольчик',s:'адвент-календарь',a:-1},
    {d:'5 дек',ic:'🎨',t:'Новый цвет: красная звезда',s:'адвент-календарь',a:-1},
    {d:'9 дек',ic:'📖',t:'Урок',s:'Super Minds 2',a:10},
    {d:'10 дек',ic:'📚',t:'Домашка сдана',s:'Unit 3 · Homework 4',a:3},
    {d:'16 дек',ic:'📖',t:'Урок',s:'Super Minds 2',a:10},
    {d:'17 дек',ic:'🎡',t:'Колесо удачи',s:'выпало: 10 монеток',a:-30},
    {d:'17 дек',ic:'🎡',t:'Выигрыш на колесе',a:10}]);
  [['garland','',50,44,1],['fairy_lights','',50,62,.7],['ball','red',38,52],['ball','blue',63,63],['star','red',55,34],['bell','silver',43,73],['candy_cane','red',30,68],
   ['ball','green',70,51],['snowflake','white',48,60],['gingerbread','',58,79],['bow','red',47,27,.9,10],['snow_globe','',30,86],['teddy_bear','',70,86]].forEach(function(p,i){
    s.placed.push({id:i+1,f:p[0],c:p[1],x:p[2],y:p[3],s:p[4]||1,r:p[5]||0,sx:1,sy:1});});
  s.placed.push({id:50,f:'top_star',c:'gold',x:50,y:12,s:1,r:0,sx:1,sy:1,auto:1});
  return s;
}
/* «Новичок»: ученица впервые зашла 15 декабря — монетки на все прошлые платные окошки */
function freshLate(){var s=blank('late');s.day=15;s.welcomed=false;return s;}
/* «Гость по ссылке»: ещё не ученик — регистрация, 🪙 20 сразу. Зашла 2 декабря */
function freshGuest(){var s=blank('guest');s.day=2;s.log=[];s.reg=false;return s;}
/* «Январь»: календарь закончился, ёлка и мастерская остаются, ёлка в огнях */
function freshAfter(){
  var s=blank('after');s.day=N+1;for(var d=1;d<=N;d++)applyOpen(s,d,true);
  s.friends=3;['teddy_bear','penguin','owl'].forEach(function(f){giveSpec(s,f);});s.posts=1;giveSpec(s,'golden_unicorn');
  s.tree='gold';s.page='advent';s.tab='tree';
  [['fairy_lights','',50,40,.7],['garland','',50,58,1],['tinsel','gold',50,75,1],['ball','red',38,47],['ball','blue',62,50],['ball','gold',44,66],['ball','purple',58,68],
   ['star','gold',52,30],['bell','gold',34,62],['candy_cane','red',67,62],['snowflake','white',41,35],['heart','pink',60,36],['bow','red',48,49],
   ['present','red',30,90],['snowman','',84,86],['reindeer','',16,86],['golden_unicorn','',70,88],['penguin','',57,88],['snow_globe','',42,86]].forEach(function(p,i){
    s.placed.push({id:i+1,f:p[0],c:p[1],x:p[2],y:p[3],s:p[4]||1,r:0,sx:1,sy:1});});
  s.placed.push({id:99,f:'top_star',c:'gold',x:50,y:12,s:1,r:0,sx:1,sy:1,auto:1});
  return s;}
var FRESH={test:freshTest,miss:freshMiss,late:freshLate,guest:freshGuest,after:freshAfter};
var MODES=[['test','1 · Тест','Тест: все окошки подряд'],['miss','2 · 20 декабря','20 декабря: есть неоткрытые окошки'],['late','3 · Новичок','Ученица пришла 15 декабря'],['guest','4 · Гость','Гость по ссылке друга'],['after','5 · Январь','Январь: календарь закончился'],
  ['teacher','6 · Карточка','Карточка для учителя'],['tview','7 · Учитель','Глазами учителя'],['q','8 · Вопросы','Вопросы к решению']];
function viewMode(c){return c==='teacher'||c==='tview'||c==='q';}
var KEY='wow-cabinet-advent-v9',ALL,S;
function load(){try{var r=localStorage.getItem(KEY);if(r)ALL=JSON.parse(r);}catch(e){}
  if(!ALL)ALL={cur:'miss'};Object.keys(FRESH).forEach(function(k){if(!ALL[k])ALL[k]=FRESH[k]();});
  S=ALL[viewMode(ALL.cur)?'miss':ALL.cur];}
function save(){try{localStorage.setItem(KEY,JSON.stringify(ALL));}catch(e){}}
load();
