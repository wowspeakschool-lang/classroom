"""Дракон со стрелкой на хвост — карточка слова tail (WD2 ДЗ 67)."""
import sys
from PIL import Image
sys.path.insert(0, 'builds/kartinki/gg1_12112026')
from listy import strelka

src = 'media/wow-dragon-2/legacy/e85681b44de3.webp'
dst = 'media/wow-dragon-2/new/dragon_tail.webp'

im = Image.open(src).convert('RGBA')
# стрелка из пустого правого нижнего угла в середину хвоста
strelka(im, (0.97, 0.93), (0.79, 0.715))
im.save(dst, 'WEBP', quality=90)
print(dst, im.size)

prev = Image.new('RGB', im.size, 'white')
prev.paste(im, (0, 0), im)
prev = prev.resize((im.width * 2, im.height * 2), Image.LANCZOS)
prev.save('/tmp/claude-0/-home-user-classroom/28688f32-2607-5bdf-bf1c-8d151d5e328a/scratchpad/tail_arrow.png')
