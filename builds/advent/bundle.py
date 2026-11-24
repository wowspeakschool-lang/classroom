"""Собрать один самодостаточный HTML: все картинки и записи внутри файла (data:)."""
import base64, json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
src, out = sys.argv[1], sys.argv[2]
html = open(os.path.join(D, src), encoding='utf-8').read()
emb = {}
for sub, mime in (('img', 'image/webp'), ('audio', 'audio/mpeg')):
    for root, _, files in os.walk(os.path.join(D, sub)):
        for f in files:
            if not f.endswith(('.webp', '.mp3')):
                continue
            p = os.path.join(root, f)
            key = os.path.relpath(p, D).replace(os.sep, '/')
            if key in html or '/v/' in key or sub == 'audio' or f.startswith(('tree_', 'gift', 'ic_')) or True:
                emb[key] = 'data:%s;base64,%s' % (mime, base64.b64encode(open(p, 'rb').read()).decode())
# фон в CSS — заменить прямо в тексте
for k, v in emb.items():
    html = html.replace('url(%s)' % k, 'url(%s)' % v)
shim = '''<script>
/* Файл самодостаточный: картинки и звук лежат внутри него. Пути img/… и audio/… подменяются на встроенные. */
(function(){var EMB=%s;
function m(u){if(typeof u!=='string')return u;var k=u.replace(/^\\.\\//,'');return EMB[k]||u;}
function patch(proto,prop){var d=Object.getOwnPropertyDescriptor(proto,prop);if(!d||!d.set)return;
 Object.defineProperty(proto,prop,{configurable:true,enumerable:d.enumerable,get:d.get,set:function(v){d.set.call(this,m(v));}});}
patch(HTMLImageElement.prototype,'src');patch(HTMLMediaElement.prototype,'src');patch(HTMLSourceElement.prototype,'src');
var sa=Element.prototype.setAttribute;Element.prototype.setAttribute=function(n,v){if(n==='src')v=m(v);return sa.call(this,n,v);};
function fix(el){if(el.nodeType!==1)return;if(el.hasAttribute&&el.hasAttribute('src')){var s=el.getAttribute('src'),t=m(s);if(t!==s)sa.call(el,'src',t);}
 var st=el.getAttribute&&el.getAttribute('style');if(st&&st.indexOf('url(')>=0){var n=st.replace(/url\\((['"]?)([^'")]+)\\1\\)/g,function(a,q,p){return 'url('+m(p)+')';});if(n!==st)sa.call(el,'style',n);}
 if(el.querySelectorAll)el.querySelectorAll('[src],[style*="url("]').forEach(fix0);}
function fix0(e){if(e.hasAttribute('src')){var s=e.getAttribute('src'),t=m(s);if(t!==s)sa.call(e,'src',t);}
 var st=e.getAttribute('style');if(st&&st.indexOf('url(')>=0){var n=st.replace(/url\\((['"]?)([^'")]+)\\1\\)/g,function(a,q,p){return 'url('+m(p)+')';});if(n!==st)sa.call(e,'style',n);}}
new MutationObserver(function(ms){ms.forEach(function(r){if(r.type==='attributes')fix0(r.target);else r.addedNodes.forEach(fix);});})
 .observe(document.documentElement,{subtree:true,childList:true,attributes:true,attributeFilter:['src','style']});
document.addEventListener('DOMContentLoaded',function(){fix(document.body);});
window.__EMB=m;})();
</script>
''' % json.dumps(emb)
i = html.find('<style>')
html = html[:i] + shim + html[i:]
open(out, 'w', encoding='utf-8').write(html)
print(len(emb), 'files,', len(html) // 1024, 'KB')
