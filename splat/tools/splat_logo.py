"""Общий логотип SPLAT Kids × WowSpeak для PDF (вариант 1, Анна 11.11.2026):
красная плашка SPLAT KIDS и белая плашка WowSpeak в тёмной рамке — одной высоты h.
На сайте и в уроке — тот же вид в CSS (.logo в index.html и lesson.html)."""
import os
from PIL import ImageFont

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
RED, INK = (227, 38, 47), (45, 58, 92)


def _font(name, size, weight='Bold'):
    f = ImageFont.truetype(os.path.join(FONTS, name + '.ttf'), size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def draw_logo(d, x, y, h=92):
    """Рисует логотип с левого верхнего угла (x, y); возвращает правый край."""
    r = int(h * .15)
    w = int(h * 2.28)
    d.rounded_rectangle((x, y, x + w, y + h), r, fill=RED)
    d.text((x + w / 2, y + h * .41), 'SPLAT', font=_font('Fredoka', int(h * .59)), fill='white', anchor='mm')
    d.text((x + w / 2, y + h * .83), 'K I D S', font=_font('Fredoka', int(h * .24)), fill='white', anchor='mm')
    x += w
    d.text((x + h * .3, y + h / 2), '×', font=_font('Nunito', int(h * .5), 'Black'), fill=INK, anchor='mm')
    x += int(h * .6)
    f = _font('Fredoka', int(h * .44))
    w = int(d.textlength('WowSpeak', font=f) + h * .6)
    d.rounded_rectangle((x, y, x + w, y + h), r, outline=INK, width=max(3, h // 22), fill='white')
    d.text((x + w / 2, y + h / 2), 'WowSpeak', font=f, fill=INK, anchor='mm')
    return x + w
