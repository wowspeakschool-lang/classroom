import re,json,base64
SRC='/root/.claude/uploads/804eac6d-911f-5112-b4f5-c1e3887b7b56/6c5036b9-halloween_lesson_4-6.html'
IMG='/tmp/claude-0/-home-user-classroom/804eac6d-911f-5112-b4f5-c1e3887b7b56/images/'
orig=open(SRC).read(); t=open('template.html').read()
A=json.loads(re.search(r'const ASSETS=(\{.*?\});\n',orig).group(1))
music=re.search(r'const MUSIC="([^"]*)";',orig).group(1)
keep=['dragon','dragon_vampire','dragon_ghost','dragon_pumpkin','pumpkin_big','emo_happy','emo_sad','emo_angry',
      'word_ghost','word_bat','word_spider','word_monster','warmup']
N={k:A[k] for k in keep}
files=['1.jpg']+[f'{i}.webp' for i in range(2,12)]
for i,f in enumerate(files):
    mime='image/jpeg' if f.endswith('jpg') else 'image/webp'
    N[f'room_{i:02d}']=f'data:{mime};base64,'+base64.b64encode(open(IMG+f,'rb').read()).decode()
import os
for f in ['door_1','door_2','door_3','door_4','door_5','cauldron','cauldron_potion','candy','candy_1','candy_2','candy_3','candy_4','candy_5','candy_6']:
    N[f]='data:image/webp;base64,'+base64.b64encode(open('cut/'+f+'.webp','rb').read()).decode()
for f in ['dragon','dragon_vampire','dragon_ghost','dragon_pumpkin']:
    N[f]='data:image/png;base64,'+base64.b64encode(open('cut/'+f+'.png','rb').read()).decode()
N['bg_night']='data:image/jpeg;base64,'+base64.b64encode(open('cut/bg_night.jpg','rb').read()).decode()
slots={"dragon":{"cx":0.885,"cy":0.99,"w":0.18}}
t=re.sub(r'const ASSETS=\{.*?\};\n',lambda m:'const ASSETS='+json.dumps(N)+';\n',t,count=1)
t=re.sub(r'const SLOTS=\{.*?\};\n',lambda m:'const SLOTS='+json.dumps(slots)+';\n',t,count=1)
t=t.replace('const MUSIC="DATA";','const MUSIC="'+music+'";',1)
# lesson plan
m=re.search(r'const PLAN_HTML=("(?:[^"\\]|\\.)*");',t); plan=json.loads(m.group(1))
rows=re.findall(r'<tr><td class="pg">.*?</tr>\n',plan)
def row(pg,task,tl): return f'<tr><td class="pg">{pg}</td><td>{task}</td><td class="tl">{tl}</td></tr>\n'
R=" После игры загорается кнопка Next — нажмите её: откроется комната дракона, новый предмет подсветится. Спросите «What\'s new?» — ученик называет. Ещё раз Next — дальше. В комнате появляется: "
D=" Кружочки вверху показывают раунды."
new=[
 row(1,'<b>Warm-up: угадай праздник.</b> Картинка с символами Хэллоуина, на экране ничего не написано — вопросы задаёт учитель. Ученик называет, что видит, и угадывает праздник.','"Look! What can you see?" "What colour is it?" "What holiday is it?" "Yes! It\'s Halloween!"'),
 row(2,'<b>How do you feel?</b> Три тыквы-эмоции. Ученик выбирает свою и говорит. Учитель нажимает на выбранную тыкву.','"How do you feel today?" "Are you happy?" "I\'m happy too!"'),
 row(3,'<b>Выбери костюм.</b> Дракон-вампир / привидение / тыква. Ученик выбирает — дракон в этом костюме будет жить в комнате и танцевать в бонусной игре.','"Choose a costume!" "A vampire? A ghost? A pumpkin?" "Wow, cool!"'),
 row(4,'<b>Новые слова.</b> Одна страница, четыре слова подряд: ghost, bat, spider, monster. Появляется картинка — учитель сразу говорит «It\'s a ghost!», ученик повторяет. Следующее слово — кнопка Next (или нажать на картинку).'+D,'"Look! It\'s a ghost!" "Say: ghost!" "Great!" "And this? It\'s a bat!"'),
 row(5,'<b>Комната дракона.</b> Пустая комната: «Давай украсим её к Хэллоуину!». За каждую игру в комнате будет появляться новое украшение.','"Look! This is the dragon\'s room." "It\'s empty!" "Let\'s decorate it!"'),
 row(6,'<b>Волшебный туман (4 раунда).</b> Картинку закрывает густой туман, он очень медленно рассеивается. Ученик старается угадать как можно раньше. Угадал — учитель нажимает на картинку (или 👀): туман исчезает, звучит «правильно».'+D+R+'<b>кровать</b>.','"What\'s this?" "Is it a bat?" "Look… It\'s a spider!" "What\'s new? A bed!"'),
 row(7,'<b>Пантомима.</b> Учитель показывает слово телом, ученик угадывает и нажимает на картинку. <i>Подсказки:</i> ghost — парит, «Boo!»; bat — машет крыльями; spider — пальцы-лапки ползут; monster — рычит, когти.'+R+'<b>коврик</b>.','"What am I?" "Guess!" "Yes, a bat! Well done!"'),
 row(8,'<b>Knock, knock! (5 дверей).</b> Ученик выбирает дверь по номеру: «Number three!». Учитель жмёт на дверь — стук, дверь открывается, выпрыгивает персонаж. <b>Ученик сам называет:</b> «It\'s a ghost!» (подпись появляется через пару секунд). За одной дверью конфеты: «Trick or treat!».'+R+'<b>шторы</b>.','"Knock, knock! Who\'s there?" "Which door? Number two?" "What is it?" "Yes! It\'s a bat!"'),
 row(9,'<b>Фонарик (4 раунда).</b> Экран тёмный, картинки спрятаны в разных местах — без фонарика их не видно. Учитель водит фонарик мышкой (фонарик стоит там, где его оставили). Ученик говорит, куда светить, и ищет нужного персонажа. Нашли — учитель нажимает на картинку под фонариком. Кроме четырёх слов спрятаны тыква и конфеты — их называем тоже.'+D+R+'<b>гирлянда</b>.','"Find the monster!" "Is it here?" "No, it\'s a pumpkin!" "Yes! There it is!"'),
 row(10,'<b>Peekaboo — кто прячется? (4 раунда).</b> Персонаж прячется в комнате дракона: заглядывает в окно, за изголовьем кровати, за дверью, за кроватью — видно только кусочек. Ученик угадывает, учитель нажимает на него (или 👀) — персонаж выпрыгивает.'+D+R+'<b>летучие мыши</b>.','"Who\'s hiding?" "Look! What\'s this?" "Is it a ghost?" "Boo! It\'s a monster!"'),
 row(11,'<b>Волшебный котёл — считаем конфеты (3 раунда).</b> Вверху число: «Put 3 🍬 in!». Ученик кладёт в котёл конфеты (любые) — учитель перетаскивает или просто нажимает на конфету — и <b>считает вслух вместе с учителем</b>. Рядом с котлом растёт цифра. Набрали — «пуф!», зелье меняет цвет, из котла выглядывает сюрприз.'+D+R+'<b>тыква на полке</b>.','"Put three candies in!" "One candy, two candies, three candies!" "Poof! Magic!"'),
 row(12,'<b>I like / I don\'t like (4 карточки).</b> Ученик говорит «I like ghosts» или «I don\'t like spiders». Учитель нажимает 👍 или 👎.'+D+R+'<b>конфеты</b>.','"Do you like ghosts?" "I like ghosts!" "I don\'t like spiders!"'),
 row(13,'<b>What\'s missing? (2 раунда).</b> Четыре картинки. Через пару секунд прилетает тучка, накрывает одну картинку и улетает вместе с ней. Ученик угадывает, что пропало. Учитель нажимает 👀 — картинка возвращается.'+D+R+'<b>монстрик</b>.','"Look carefully!" "Close your eyes!" "What\'s missing?" "Yes! The bat is missing!"'),
 row(14,'<b>Bonus games (если есть время).</b> Можно сыграть во все, в любом порядке, или сразу нажать <b>Finish 🏁</b>. После каждой игры — кнопка 🎁: в комнате появляется новое украшение (паучок, потом привидение), затем кнопка «🎮 ←» возвращает к списку игр.<br>• <b>Dance 💃</b>: сначала разберите с учеником четыре карточки — учитель показывает движение, ученик повторяет (bat — машем крыльями, ghost — летаем и говорим «Boo!», spider — ползаем пальцами, monster — рычим и показываем когти). Потом ▶: музыка, дракон танцует, ученик танцует тоже. Музыка останавливается — появляется картинка, ученик показывает это движение. ▶ — танцуем дальше.<br>• <b>Memory 🧩</b>: найти пары, называя слова.<br>• <b>Shadows 👤</b>: найти тень картинки.','"Let\'s dance!" "Stop! What is it? Show me!" "Fly like a bat!" "Find the pairs!"'),
 row(15,'<b>Финал: фото комнаты.</b> Комната полностью украшена. «Save photo» — скачать картинку и отправить ученику/родителям. Стрелка ← возвращает к бонусным играм, если нажали случайно.','"Look at your room! Amazing!" "Happy Halloween!" "Well done!"'),
]
i0=plan.index(rows[0]); j0=plan.index(rows[-1])+len(rows[-1])
plan=plan[:i0]+''.join(new)+plan[j0:]
plan=re.sub(r'(<b>\U0001f5c2️ [^<]*</b>)[^<]*</div>',r'\1 ghost, bat, spider, monster • happy, sad, angry • bed, rug, curtains, lights, pumpkin, candy • I like / I don\'t like • numbers 1–5: one candy, two candies… • "Trick or treat!", "Happy Halloween!", "Boo!", "What\'s new?"</div>',plan,count=1)
plan=re.sub(r'(<div class="voc" style="font-size:13px;color:#777"><b>[^<]*</b>)[^<]*</div>',r'\1 стрелки ← → внизу экрана — вернуться или пропустить страницу; центральная кнопка Next загорается, когда задание выполнено. Номера страниц внизу справа соответствуют этой таблице. 📋 — этот план, 🎵 — фоновая музыка (вкл/выкл и громкость).</div>',plan,count=1)
plan=plan.replace("\\'","'")
from hwplan import add as hwadd
plan=hwadd(plan,'4-6')
t=t[:m.start(1)]+json.dumps(plan)+t[m.end(1):]
open('halloween_lesson_4-6.html','w').write(t)
print(len(t), 'DATA' in t)
