# Картинки шифра для презентации: ключ урока 3 и сообщение символами
import importlib.util, os, subprocess, sys
here=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location("b", os.path.join(here,"build.py"))
src=open(os.path.join(here,"build.py")).read().split("# ---------- программа ----------")[0]
ns={"__file__":os.path.join(here,"build.py")}; exec(src, ns)
css="body{margin:0;font-family:Calibri,Inter,sans-serif;background:#fff;color:#20313B}.key{display:flex;flex-wrap:wrap;gap:8px;padding:6px}.k{border:2px solid #CFE6F4;border-radius:10px;padding:6px 6px 2px;text-align:center;width:52px;background:#fff}.k b{font-size:20px}.k.off{background:#F2FAFE;border-style:dashed}.q{height:34px;line-height:34px;font-size:22px;color:#6B8794}.coded{display:flex;flex-wrap:wrap;gap:18px;padding:12px 14px;background:#F2FAFE;border-radius:12px}.coded .w{display:inline-flex;gap:3px;align-items:center}.coded .p{font-size:26px;font-weight:700}"
open(os.path.join(here,"key.html"),"w").write(f"<html><head><meta charset=utf-8><style>{css}</style></head><body><div id=a style='width:620px'>{ns['key']('satpinmdogckeur','bfhjlqvwxyz')}</div><div id=b style='width:620px;margin-top:20px'>{ns['coded']('Run! Get the red cup.')}</div></body></html>")
