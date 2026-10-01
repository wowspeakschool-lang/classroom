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

# --- третья порция: листы 11-15 ---
row(I+'11.webp', 2, 271, ['bakery','bookshop',"butcher's",'café'], O+'1.2', gap=12, min_area=150)
row(I+'11.webp', 312, 624, ["chemist's",'clothes shop','department store','market'], O+'1.2', gap=12, min_area=150)
row_x(I+'11.webp', 678, 963, ["newsagent's",'shoe shop','supermarket','sweet shop'], O+'1.2', [379, 731, 1165])
row(I+'12.webp', 23, 266, ['a pair of','a set of','a slice of','a variety of'], O+'1.3', gap=12, min_area=150)
row(I+'12.webp', 319, 604, ['centimetres','metres','kilometres','grams'], O+'1.3', gap=12, min_area=150)
row(I+'12.webp', 649, 943, ['kilograms','litres','millilitres'], O+'1.3', gap=12, min_area=150)
row(I+'13.webp', 40, 384, ['dollars and cents','euros and cents','pounds and pence','a brilliant day out','a fun day out'], O+'1.4', gap=12, min_area=150)
row_x(I+'13.webp', 484, 909, ['an exciting day out','a brilliant hobby','a fun hobby','an exciting hobby','a fantastic feeling'], O+'1.4', [324, 627, 840, 1202])
# рука singing нависает над крылом самолётика — граница ступенькой
row_x(I+'14.webp', 54, 433, ['playing computer games','playing sport','reading books','singing','spend time doing something'], O+'2.2', [295, 617, 962, (230, 1243, 1195)])
row(I+'14.webp', 546, 909, ['spending time online','watching TV','making things','spend time with someone'], O+'2.2', gap=12, min_area=150)
row(I+'15.webp', 17, 425, ['be glad','be happy','enjoy an activity','enjoy yourself'], O+'2.3', gap=12, min_area=150)
row(I+'15.webp', 500, 929, ['feel happy','have a great time','have a laugh','have fun'], O+'2.3', gap=12, min_area=150)
