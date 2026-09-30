# Пример вызова нарезки — заход 1 Prepare 3 (колоды 160-176).
# Полосы (y0,y1) взяты из профиля каждого листа, см. HANDOVER.md раздел 5.
# Для новых листов пересчитывать профиль, а не копировать эти числа.
from lib import row
U='/mnt/user-data/uploads/'
J=[
 ('1789239433674',[(22,267),(332,591),(655,927)],[['biology','chemistry','design and technology','drama'],['foreign languages','geography','history','ICT'],['maths','PE','physics','science']],'out1',18,600),
 ('1789239438682',[(12,274),(339,604),(667,941)],[['take (carry)','take (catch)','take (do)','take (go along)'],['take (make)','take (study)','take (use)','get back'],['get lost','get on','get to','get up']],'out2',18,600),
 ('1789239442227',[(8,288),(359,611),(665,945)],[['cotton','glass','gold','leather'],['metal','paper','plastic','silver'],['wood','wool','wooden']],'out3',18,600),
 ('1789239444812',[(6,287),(343,613),(668,928)],[['colourful','hard','heavy','large'],['little','lovely','old','pretty'],['round','small','smooth','soft']],'out4',18,600),
 ('1789241253312',[(42,402),(495,899)],[['camping','diving','hiking','horse riding','kite surfing'],['mountain biking','paddle boarding','sailing','waterskiing','zip wiring']],'out5',12,600),
 ('1789241261177',[(22,278),(350,594),(652,917)],[['backpack','first aid kit','map and compass','sleeping bag'],['snacks','sun cream','tent','torch'],['trainers','walking boots','wash bag','waterproof trousers and jacket']],'out6',18,600),
 ('1789241265425',[(9,279),(340,604),(664,932)],[['air conditioning','barbecue','bin','bookcase'],['drawer','fridge','heating','lights'],['roof','seat','stairs','washing machine']],'out7',18,120),
 ('1789241269492',[(26,280),(351,600),(664,924)],[['book (for reading)','book (reserve)','kind (nice)','kind (variety)'],['letter (in the mail)','letter (part of writing)','picture (drawing)','picture (photo)'],['ring (jewellery)','ring (phone)','watch (for the time)','watch (look at)']],'out8',18,120),
 ('1789246616442',[(21,406),(532,892)],[['badminton','board game','card game','climbing'],['cricket','dance class','fishing']],'out9',12,150),
 ('1789246621051',[(67,419),(537,889)],[['golf','fitness class','karate','puzzle'],['skateboarding','skiing','video game']],'out10',12,150),
 ('1789246624795',[(20,413),(490,897)],[['champion','fan','prize'],['professional','take part','tournament']],'out11',12,150),
 ('1789246627891',[(9,304),(374,631),(681,953)],[['cleaner','climber','dancer','diver'],['golfer','photographer','runner','singer'],['skier','swimmer','teacher','worker']],'out12',12,150),
 ('1789246643196',[(48,414),(537,898)],[['best friend','classmate','close friend','contact','guest'],['member','neighbour','old friend','penfriend','relative']],'out13',12,150),
 ('1789246647297',[(27,268),(356,604),(696,937)],[['blog','download','link','menu'],['message board','post','record','save'],['search','site','the web','upload']],'out14',12,150),
 ('1789246650372',[(38,288),(346,624),(679,944)],[['art gallery','cathedral','embassy','fountain','mosque'],['old town','palace','shopping area','skyscraper'],['sports centre','stadium','statue','temple']],'out15',12,150),
 ('1789250718647',[(32,291),(364,623),(692,944)],[['animals','electricity','food','furniture','homework'],['information','jewellery','luggage','money'],['news','staff','traffic','wildlife']],'out16',12,150),
 ('1789294426286',[(13,278),(341,612),(667,954)],[['a comedy','a drama','a horror film'],['a musical','a science fiction film','a thriller'],['an action film','an adventure film','an animated film']],'out17',12,150),
]
bad=0
for f,bands,wss,out,g,ma in J:
    for (a,b),ws in zip(bands,wss):
        if not row(U+f+'_image.png',a,b,ws,out,gap=g,min_area=ma): bad+=1
# замена animated film
row(U+'1789294452534_image.png',658,943,['z1','z2','z3','z4','z5','an animated film'],'out17',gap=12,min_area=150)
import os
for z in ['z1','z2','z3','z4','z5']:
    p='out17/'+z+'.png'
    if os.path.exists(p): os.remove(p)
print('errors:',bad)
