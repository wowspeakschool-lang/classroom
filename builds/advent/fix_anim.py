p='/tmp/claude-0/-home-user/4f1aec8c-7236-5d0b-8cab-c22529efe1d2/scratchpad/advent/les.html'
t=open(p,encoding='utf-8').read()
def R(a,b):
    global t
    assert t.count(a)==1,(a[:60],t.count(a)); t=t.replace(a,b)
R("canvas.snow{",""".anim{position:absolute;pointer-events:none;width:0;height:0}
.anim img{position:absolute;bottom:0;left:0;transform:translateX(-50%);display:block;filter:drop-shadow(0 6px 4px rgba(0,0,0,.25))}
canvas.snow{""")
R("function init(){size();build();}","""/* Зверьки: две позы (сидит / в прыжке) — прыжок по дуге собираем сами.
   Иногда кто-то пробегает по лесу (то за ёлками, то перед ними), иногда выглядывает из-за ёлки. */
var AN={bunny:{s:[252,308],j:[420,308],h:.12,hop:1.6,hh:.12,sp:.55},fox:{s:[287,236],j:[420,236],h:.12,hop:1.5,hh:.035,sp:.75},
 deer:{s:[253,338],j:[420,337],h:.17,hop:1.8,hh:.09,sp:.8},squirrel:{s:[227,419],j:[405,420],h:.12,hop:1.3,hh:.10,sp:.6}};
var KEYS=Object.keys(AN),world=document.getElementById('world');
function mk(n,z){var a=AN[n],el=document.createElement('div');el.className='anim';el.style.zIndex=z;
 var k=H*a.h/a.s[1];el.innerHTML='<img src="img/an/'+n+'_sit.webp" alt="" style="width:'+(a.s[0]*k)+'px">';world.appendChild(el);return {el:el,img:el.firstChild,k:k,a:a,n:n};}
function frame(o,j){var f=j?o.a.j:o.a.s;o.img.src='img/an/'+o.n+(j?'_jump':'_sit')+'.webp';o.img.style.width=(f[0]*o.k)+'px';}
function run(){var n=KEYS[Math.floor(Math.random()*KEYS.length)],front=Math.random()<.45,o=mk(n,front?6:1),dir=Math.random()<.5?1:-1;
 var vw=sc.clientWidth,x0=sc.scrollLeft+(dir>0?-120:vw+120),x1=sc.scrollLeft+(dir>0?vw+120:-120),gy=H*(front?.905:.86);
 var size=H*o.a.h,L=size*o.a.hop,speed=vw*o.a.sp/6,dist=Math.abs(x1-x0),t0=null;
 o.img.style.transform='translateX(-50%) scaleX('+dir+')';var last=-1;
 function step(ts){if(t0===null)t0=ts;var d=(ts-t0)/1000*speed;if(d>=dist){o.el.remove();return;}
  var p=(d%L)/L,air=p<.72,y=air?-Math.sin(Math.PI*p/.72)*H*o.a.hh:0;
  if(air!==last){frame(o,air);last=air;}
  o.el.style.left=(x0+dir*d)+'px';o.el.style.top=(gy+y)+'px';requestAnimationFrame(step);}
 requestAnimationFrame(step);}
function peek(){var vw=sc.clientWidth,s=sc.scrollLeft,ts=[].slice.call(document.querySelectorAll('.t')).filter(function(t){var x=parseFloat(t.style.left);return x>s+80&&x<s+vw-80;});
 if(!ts.length)return;var tr=ts[Math.floor(Math.random()*ts.length)],tw=tr.offsetWidth,n=['bunny','squirrel','fox'][Math.floor(Math.random()*3)],o=mk(n,2),side=Math.random()<.5?-1:1;
 var x=parseFloat(tr.style.left),gy=H*.875;o.el.style.left=x+'px';o.el.style.top=gy+'px';o.img.style.transform='translateX(-50%) scaleX('+side+')';
 o.el.animate([{transform:'translateX(0)'},{transform:'translateX('+(side*tw*.42)+'px)',offset:.2},{transform:'translateX('+(side*tw*.42)+'px)',offset:.8},{transform:'translateX(0)'}],{duration:4200,easing:'ease-in-out'}).onfinish=function(){o.el.remove();};}
function life(){if(!document.hidden){Math.random()<.6?run():peek();}setTimeout(life,4000+Math.random()*4000);}
if(!matchMedia('(prefers-reduced-motion: reduce)').matches)setTimeout(life,1500);
function init(){size();build();}""")
open(p,'w',encoding='utf-8').write(t);print('ok')
