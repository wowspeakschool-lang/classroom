# Общие помощники для вебинаров WOW Speak: фирменный вид + анимации <p:timing>.
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from lxml import etree
import copy

W, H = 12192000, 6858000
IN = 914400
DARK, DARK2, HEAD = '1E1535', '2A2140', '3D2B5A'
PINK, TEAL, TEAL2, GREEN, GREENBG = 'E91E8C', '00BCD4', '0097A7', '43A047', 'F0FFF4'
ORANGE, GOLD, WHITE = 'FB8C00', 'FFD700', 'FFFFFF'
PASTELS = ['F7F3FF', 'F0FFF7', 'FFFDF0', 'FFF5EE']
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}


def rgb(h):
    return RGBColor.from_string(h)


def i(x):
    return Emu(int(x * IN))


class Deck:
    def __init__(self):
        self.prs = Presentation()
        self.prs.slide_width, self.prs.slide_height = W, H
        self.n = 0

    def slide(self, bg=None):
        s = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        if bg is None:
            bg = PASTELS[self.n % len(PASTELS)]
        self.n += 1
        f = s.background.fill
        f.solid()
        f.fore_color.rgb = rgb(bg)
        s._clicks = []
        return s

    def save(self, path):
        for s in self.prs.slides:
            write_timing(s)
        self.prs.save(path)


def text(s, x, y, w, h, runs, size=20, color=HEAD, bold=True, align='c',
         italic=False, fill=None, line=None, lw=2.0, shape='round', anchor='m'):
    """runs: str | [(text, color)] | [[(text,color)], ...] — абзацы."""
    if fill or line:
        sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if shape == 'round'
                                else MSO_SHAPE.RECTANGLE, i(x), i(y), i(w), i(h))
        if shape == 'round':
            sh.adjustments[0] = min(0.5, 0.12 * 1.0 / max(h, 0.3))
        if fill:
            sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
        else:
            sh.fill.background()
        if line:
            sh.line.color.rgb = rgb(line); sh.line.width = Pt(lw)
        else:
            sh.line.fill.background()
        sh.shadow.inherit = False
    else:
        sh = s.shapes.add_textbox(i(x), i(y), i(w), i(h))
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = i(0.12)
    tf.margin_top = tf.margin_bottom = i(0.04)
    tf.vertical_anchor = {'m': MSO_ANCHOR.MIDDLE, 't': MSO_ANCHOR.TOP}[anchor]
    if isinstance(runs, str):
        paras = [[(runs, color)]]
    elif runs and isinstance(runs[0], tuple):
        paras = [runs]
    else:
        paras = runs
    for k, pr in enumerate(paras):
        p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
        p.alignment = {'c': PP_ALIGN.CENTER, 'l': PP_ALIGN.LEFT, 'r': PP_ALIGN.RIGHT}[align]
        for item in pr:
            t, c = item[0], item[1]
            r = p.add_run(); r.text = t
            f = r.font; f.name = 'Arial'; f.bold = bold; f.italic = italic
            f.size = Pt(item[2] if len(item) > 2 else size)
            f.color.rgb = rgb(c)
    return sh


def transparent(path):
    """Белый фон, связанный с краем, делаем прозрачным (кэш рядом с файлом)."""
    import os, numpy as np
    from PIL import Image
    from scipy import ndimage
    out = os.path.join(os.path.dirname(path), '.alpha', os.path.basename(path))
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(path):
        return out
    os.makedirs(os.path.dirname(out), exist_ok=True)
    a = np.asarray(Image.open(path).convert('RGB'))
    white = a.min(axis=2) >= 236
    lab, _ = ndimage.label(white)
    edge = set(lab[0]) | set(lab[-1]) | set(lab[:, 0]) | set(lab[:, -1])
    edge.discard(0)
    bg = np.isin(lab, list(edge))
    alpha = np.where(bg, 0, 255).astype('uint8')
    alpha = ndimage.uniform_filter(alpha.astype(float), 3).astype('uint8')
    Image.fromarray(np.dstack([a, alpha])).save(out)
    return out


def pic(s, path, x, y, w=None, h=None):
    from PIL import Image
    path = transparent(path)
    im = Image.open(path); ar = im.width / im.height
    if w and h:  # вписать в рамку по центру
        if w / h > ar:
            nw = h * ar; x += (w - nw) / 2; w = nw
        else:
            nh = w / ar; y += (h - nh) / 2; h = nh
    elif h:
        w = h * ar
    else:
        h = w / ar
    return s.shapes.add_picture(path, i(x), i(y), i(w), i(h))


def header(s, title, pill=None, sub=None):
    text(s, 10.3, 0.22, 2.8, 0.5, [('WOW', PINK), (' Speak', HEAD)], size=18, align='r')
    if pill:
        text(s, 0.45, 0.28, 2.7, 0.5, pill, size=15, color=WHITE, fill=PINK)
    text(s, 1.0, 0.55, 11.3, 0.9, title, size=33)
    if sub:
        text(s, 1.0, 1.35, 11.3, 0.45, sub, size=16, color='555555', bold=False, italic=True)


def chat(s, hint):
    text(s, 0.45, 6.65, 12.43, 0.62, '', fill=DARK2)
    text(s, 0.6, 6.65, 0.6, 0.62, '💬', size=20, color=WHITE, bold=False)
    text(s, 1.2, 6.65, 9.6, 0.62, hint, size=15, color=WHITE, bold=False, italic=True, align='l')
    text(s, 11.1, 6.74, 1.5, 0.44, '➤', size=16, color=WHITE, fill=PINK)


def option(s, x, y, w, h, label, body, correct, size=22):
    """Вариант ответа. У верного — зелёная копия снизу и обычная сверху (крышка)."""
    runs = [(label + ')  ', PINK), (body, '2A2140')] if label else [(body, '2A2140')]
    if correct:
        g = [(label + ')  ', GREEN), (body, GREEN)] if label else [(body, GREEN)]
        text(s, x + 0.03, y + 0.03, w - 0.06, h - 0.06, g, size=size, fill=GREENBG, line=GREEN, lw=2)
        return text(s, x, y, w, h, runs, size=size, fill=WHITE, line=TEAL)
    text(s, x, y, w, h, runs, size=size, fill=WHITE, line=TEAL)
    return None


def timer(s, y=6.32, secs=10):
    """Полоса «подумай»: исчезает стиранием за secs секунд."""
    text(s, 3.5, y, 5.2, 0.16, '', fill='E3DCF2', shape='rect')
    bar = text(s, 3.5, y, 5.2, 0.16, '', fill=PINK, shape='rect')
    return ('wipe', bar, secs)


# ---------- анимации ----------
# s._clicks: список кликов; клик — список эффектов (kind, shape[, secs]).
# kind: appear | fade (вход) · hide (мгновенное исчезновение) · wipe (таймер, выход)

def click(s, *effects):
    s._clicks.append([e if isinstance(e, tuple) else ('appear', e) for e in effects])


def _id(sh):
    return sh.shape_id


def _set(cid, spid, val, delay='0'):
    return (f'<p:set><p:cBhvr><p:cTn id="{cid}" dur="1" fill="hold"><p:stCondLst>'
            f'<p:cond delay="{delay}"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{spid}"/>'
            f'</p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>'
            f'</p:cBhvr><p:to><p:strVal val="{val}"/></p:to></p:set>')


def write_timing(s):
    if not s._clicks:
        return
    n = [2]

    def nid():
        n[0] += 1
        return n[0]
    pars = []
    builds = []
    for cl in s._clicks:
        effs = []
        for k, e in enumerate(cl):
            kind, sh = e[0], e[1]
            spid = _id(sh)
            node = 'clickEffect' if k == 0 else 'withEffect'
            c = nid()
            if kind == 'appear':
                body = _set(nid(), spid, 'visible')
                head = f'presetID="1" presetClass="entr" presetSubtype="0"'
            elif kind == 'fade':
                body = (_set(nid(), spid, 'visible') +
                        f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{nid()}" dur="600"/>'
                        f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>')
                head = f'presetID="10" presetClass="entr" presetSubtype="0"'
            elif kind == 'hide':
                body = _set(nid(), spid, 'hidden')
                head = f'presetID="1" presetClass="exit" presetSubtype="0"'
            elif kind == 'wipe':
                ms = e[2] * 1000
                body = (f'<p:animEffect transition="out" filter="wipe(right)"><p:cBhvr><p:cTn id="{nid()}" dur="{ms}"/>'
                        f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>' +
                        _set(nid(), spid, 'hidden', str(ms - 1)))
                head = f'presetID="22" presetClass="exit" presetSubtype="2"'
            effs.append(f'<p:par><p:cTn id="{c}" {head} fill="hold" grpId="0" nodeType="{node}">'
                        f'<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>{body}'
                        f'</p:childTnLst></p:cTn></p:par>')
            if sh.has_text_frame if hasattr(sh, 'has_text_frame') else False:
                builds.append(spid)
        a, b = nid(), nid()
        pars.append(f'<p:par><p:cTn id="{a}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/>'
                    f'</p:stCondLst><p:childTnLst><p:par><p:cTn id="{b}" fill="hold"><p:stCondLst>'
                    f'<p:cond delay="0"/></p:stCondLst><p:childTnLst>{"".join(effs)}</p:childTnLst>'
                    f'</p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    bld = ''.join(f'<p:bldP spid="{x}" grpId="0" animBg="1"/>' for x in dict.fromkeys(builds))
    xml = (f'<p:timing xmlns:p="{NS["p"]}"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" '
           f'nodeType="tmRoot"><p:childTnLst><p:seq concurrent="1" nextAc="seek"><p:cTn id="2" '
           f'dur="indefinite" nodeType="mainSeq"><p:childTnLst>{"".join(pars)}</p:childTnLst></p:cTn>'
           f'<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond>'
           f'</p:prevCondLst><p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl>'
           f'</p:cond></p:nextCondLst></p:seq></p:childTnLst></p:cTn></p:par></p:tnLst>'
           + (f'<p:bldLst>{bld}</p:bldLst>' if bld else '') + '</p:timing>')
    el = etree.fromstring(xml)
    sld = s._element
    old = sld.find('p:timing', NS)
    if old is not None:
        sld.remove(old)
    ext = sld.find('p:extLst', NS)
    if ext is not None:
        ext.addprevious(el)
    else:
        sld.append(el)


def count_anims(path):
    import zipfile, re
    z = zipfile.ZipFile(path); tot = 0; per = {}
    for nm in z.namelist():
        if re.match(r'ppt/slides/slide\d+\.xml$', nm):
            x = z.read(nm).decode()
            c = len(re.findall(r'presetClass="', x))
            if c:
                per[int(re.findall(r'\d+', nm)[0])] = c
            tot += c
    return tot, per
