import os, io, base64
from PIL import Image
from lib import fname

DECKS = {
 160: ('out1', ['biology','chemistry','design and technology','drama','foreign languages','geography','history','ICT','maths','PE','physics','science']),
 161: ('out2', ['take (carry)','take (catch)','take (do)','take (go along)','take (make)','take (study)','take (use)']),
 162: ('out3', ['cotton','glass','gold','leather','metal','paper','plastic','silver','wood','wool']),
 163: (None,   [('colourful','out4'),('hard','out4'),('heavy','out4'),('large','out4'),('little','out4'),('lovely','out4'),('old','out4'),('pretty','out4'),('round','out4'),('small','out4'),('smooth','out4'),('soft','out4'),('wooden','out3')]),
 164: ('out2', ['get back','get lost','get on','get to','get up']),
 165: ('out5', ['camping','diving','hiking','horse riding','kite surfing','mountain biking','paddle boarding','sailing','waterskiing','zip wiring']),
 166: ('out6', ['backpack','first aid kit','map and compass','sleeping bag','snacks','sun cream','tent','torch','trainers','walking boots','wash bag','waterproof trousers and jacket']),
 167: ('out7', ['air conditioning','barbecue','bin','bookcase','drawer','fridge','heating','lights','roof','seat','stairs','washing machine']),
 168: ('out8', ['book (for reading)','book (reserve)','kind (nice)','kind (variety)','letter (in the mail)','letter (part of writing)','picture (drawing)','picture (photo)','ring (jewellery)','ring (phone)','watch (for the time)','watch (look at)']),
 169: (None,   [('badminton','out9'),('board game','out9'),('card game','out9'),('climbing','out9'),('cricket','out9'),('dance class','out9'),('diving','out5'),('fishing','out9'),('fitness class','out10'),('golf','out10'),('karate','out10'),('puzzle','out10'),('skateboarding','out10'),('skiing','out10'),('video game','out10')]),
 170: ('out11',['champion','fan','prize','professional','take part','tournament']),
 171: ('out12',['cleaner','climber','dancer','diver','golfer','photographer','runner','singer','skier','swimmer','teacher','worker']),
 172: ('out13',['best friend','classmate','close friend','contact','guest','member','neighbour','old friend','penfriend','relative']),
 173: ('out14',['blog','download','link','menu','message board','post','record','save','search','site','the web','upload']),
 174: ('out15',['art gallery','cathedral','embassy','fountain','mosque','old town','palace','shopping area','skyscraper','sports centre','stadium','statue','temple']),
 175: ('out16',['animals','electricity','food','furniture','homework','information','jewellery','luggage','money','news','staff','traffic','wildlife']),
 176: ('out17',['a comedy','a drama','a horror film','a musical','a science fiction film','a thriller','an action film','an adventure film','an animated film']),
}

def webp_uri(path, q=80):
    im = Image.open(path).convert('RGBA')
    buf = io.BytesIO(); im.save(buf,'WEBP',quality=q,method=6)
    return 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()

os.makedirs('/mnt/user-data/outputs/sql', exist_ok=True)
missing=[]; total=0
for deck in sorted(DECKS):
    d, items = DECKS[deck]
    rows=[]
    for it in items:
        term, src = (it, d) if isinstance(it,str) else it
        p=os.path.join(src, fname(term))
        if not os.path.exists(p): missing.append((deck,term,p)); continue
        t=term.replace("'","''")
        rows.append(f"UPDATE words SET image_url = '{webp_uri(p)}' WHERE deck_id = {deck} AND term = '{t}';")
    body=f"-- deck {deck}: {len(rows)} слов\nBEGIN;\n\n"+"\n\n".join(rows)+"\n\nCOMMIT;\n"
    out=f'/mnt/user-data/outputs/sql/deck_{deck}.sql'
    open(out,'w').write(body)
    kb=os.path.getsize(out)/1024; total+=len(rows)
    print(f'deck {deck}: {len(rows):2d} слов, {kb:6.0f} KB' + ('  !!! >500KB' if kb>500 else ''))
print('итого', total, 'MISSING:', missing)
