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

# --- вторая порция: листы 6-10 ---
row(I+'6.webp', 10, 295, ['ankle','back','blood','brain','ear'], O+'3.2', gap=12, min_area=150)
row(I+'6.webp', 343, 629, ['finger','heart','mouth','neck'], O+'3.2', gap=12, min_area=150)  # подпись вплотную — режем по 629
row(I+'6.webp', 675, 960, ['stomach','thumb','toe','tongue'], O+'3.2', gap=12, min_area=150)
row_x(I+'7.webp', 20, 436, ['angry','confident','embarrassed','friendly','lazy'], O+'3.3', [304, 609, 863, 1140])
# скамейка lonely заходит под чёрточки surprised — граница ступенькой
row_x(I+'7.webp', 507, 945, ['lonely','surprised','unhappy','upset','worried'], O+'3.3', [(754, 382, 398), 594, 918, 1261])
row(I+'8.webp', 9, 420, ['bring back','find out','give back','pick up'], O+'3.4', gap=12, min_area=150)
row(I+'8.webp', 510, 923, ['put back','put down','take back','take out'], O+'3.4', gap=12, min_area=150)
row(I+'9.webp', 7, 286, ['add','bake','boil','cover'], O+'4.2', gap=12, min_area=150)
row(I+'9.webp', 341, 611, ['dry','fill','fried','grilled'], O+'4.2', gap=12, min_area=150)
row(I+'9.webp', 658, 949, ['mix','prepare','roast'], O+'4.2', gap=12, min_area=150)
row(I+'10.webp', 8, 412, ['do the cleaning','do the dishes','do the shopping','do the washing','do your homework'], O+'4.3', gap=12, min_area=150)
row_x(I+'10.webp', 486, 921, ['make a cake','make a cup of tea','make a mess','make a mistake','make the bed'], O+'4.3', [298, 592, 917, 1225])
