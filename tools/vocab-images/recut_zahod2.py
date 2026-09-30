# Нарезка захода 2 Prepare 3. Листы — картинки, вставленные в чат (images/N.webp в scratchpad
# сессии). Полосы взяты из профиля строк; слипшиеся ряды режутся row_x по заданным x.
import sys
from lib import row, row_x
I = sys.argv[1] if len(sys.argv) > 1 else './'
O = 'out/'
row(I+'1.webp', 31, 412, ['chatting','collecting things','cooking','dancing','going out with friends'], O+'2.1', gap=12, min_area=150)
row(I+'1.webp', 506, 898, ['going shopping','listening to music','photography','playing an instrument'], O+'2.1', gap=12, min_area=150)
row(I+'2.webp', 51, 424, ['camp under the stars','climb a tree','explore a cave','kayak down a river','look for fossils'], O+'1.1', gap=12, min_area=150)
row(I+'2.webp', 512, 868, ['pick wild fruit','play in the snow','record birdsong','track wild animals','try rock climbing'], O+'1.1', gap=3, min_area=150)
row(I+'3.webp', 52, 411, ['article','exercise','guess','list','look up'], O+'3.1', gap=12, min_area=150)
# кошка из spell и мальчик из topic заходят друг за друга — граница ступенькой
row_x(I+'3.webp', 539, 846, ['meaning','mistake','spell','topic','translate'], O+'3.1', [307, 603, (705, 878, 900), 1200], fill=('topic',))
row(I+'4.webp', 71, 376, ['author','chapter','cover','drawings','end'], O+'4.1', gap=12, min_area=150)
row_x(I+'4.webp', 487, 801, ['fan','opinion','pages','shelf','title'], O+'4.1', [278, 610, 916, 1270])
row(I+'5.webp', 12, 321, ['beans','carrots','garlic','melon'], O+'5.1', gap=12, min_area=150)
row(I+'5.webp', 402, 657, ['pears','potatoes','salt and pepper','steak'], O+'5.1', gap=12, min_area=150)
