# Общий список картинок на декабрь: листы по группам, промпты и таблицы «предмет → урок».
C = 'an animated film character, a child '
T = 'an animated film character, a teenage '
TEEN = [
 ('01.12 Plurals', ['a closed cardboard box','one round dinner dish (plate)','a kitchen knife lying flat','one empty wooden wall shelf','one potato','a smiling baby sitting']),
 ('04.12 Prepositions of place', ['a school building front with a blank sign','a bank building front with columns and a blank sign','a cinema building front with a blank sign','a train station building front with a blank sign','a hospital building front with a red cross','a post office building front with a postbox and a blank sign']),
 ('08.12 Prepositions of time', ['a small house at sunrise (morning)','a small house under a bright midday sun (afternoon)','a small house at sunset (evening)','a small house under a moon and stars (night)','a decorated Christmas tree with presents','a snowy winter street with falling snowflakes']),
 ('11.12 Present Simple', ['a passenger train','a city bus','a round alarm clock with a blank face','%sgirl having breakfast at a table'%T,'%sboy lifting light weights at the gym'%T,'%sgirl walking a dog'%T]),
 ('15.12 Present Continuous', ['%sboy decorating a Christmas tree'%T,'%sgirl hanging fairy lights'%T,'an animated film character, a woman carrying shopping bags with presents','%sgirl wrapping a present'%T,'an animated film character, a man selling hot drinks at a small street stall','two animated film characters, teenagers singing carols holding blank songbooks']),
 ('18.12 Present Simple vs Continuous', ['%sboy sleeping in bed late in the morning'%T,'%sgirl switching off an alarm clock early in the morning'%T,'%sboy playing a video game with a controller'%T,'%sgirl skiing down a snowy slope'%T,'%sboy hugging his grandparents at their door'%T,'%sgirl watching a film on a sofa with popcorn'%T]),
 ('22.12 Comparatives', ['a running cheetah','a blue whale','a tall giraffe','a tortoise','a big elephant','a tiny mouse']),
 ('25.12 Can: requests', ['a mug of hot chocolate with whipped cream','a glass of water','a slice of pizza on a plate','a closed restaurant menu with a blank cover','a wooden chair','a smartphone with a dark blank screen and a charging cable']),
 ('29.12 Countable / Uncountable', ['two suitcases and a travel bag (luggage)','a pile of coins and plain banknotes without numbers','a closed passport with a blank cover','a blank travel ticket','a folded paper map','a backpack']),
]
KIDS = [
 ('07.12 There is / There are', ['a snowman with a carrot nose and a scarf','%sice skating'%C,'%ssitting on a sledge'%C,'a fir tree covered with snow','a park bench covered with snow','a small bird on a snowy branch']),
 ('10.12 Present Simple -s/-es', ['an animated film character, a girl sleeping in bed','an animated film character, a boy eating a bowl of soup','an animated film character, a girl playing with a ball','an animated film character, a boy swimming','an animated film character, a girl watching TV with a blank screen','an animated film character, a boy washing his face at a sink']),
 ('14.12 opposite, between', ['a small bank building front with a blank sign','a small cafe front with tables outside and a blank sign','a bakery front with bread in the window and a blank sign','a supermarket front with trolleys and a blank sign','a bookshop front with books in the window and a blank sign','a toy shop front with toys in the window and a blank sign']),
 ('17.12 Have to', ['%sgetting up and stretching next to a bed'%C,'%sbrushing teeth'%C,'%sin a school uniform'%C,'%smaking the bed'%C,'%sgetting on a yellow school bus'%C,'%sdoing homework at a desk'%C]),
 ('21.12 Ordinal numbers + dates', ['a birthday cake with candles','a wrapped present with a bow','a bunch of colourful balloons','a blank wall calendar page with an empty grid','a decorated Christmas tree','colourful fireworks in a small round patch of dark night sky']),
 ('24.12 Comparatives -y / the most', ['a funny monkey making a silly face','a lazy sloth sleeping on a branch','a heavy elephant','a noisy parrot with its beak open','a happy smiling dog','a beautiful peacock with its tail open']),
 ("28.12 Imperative + Let's", ['%smaking a snowman'%C,'%sputting on a warm hat'%C,'%sthrowing a snowball'%C,'%sbuilding a snow fort'%C,'%sputting on gloves'%C,'%szipping up a warm winter coat'%C]),
 ('31.12 Would like', ['a slice of cake on a plate','a glass of orange juice','a slice of pizza','a bowl of ice cream','a plate of cookies','a cup of tea']),
]
WORDS = {  # короткое название предмета для таблицы
}
HEAD = ('plain flat pure white background, wide empty white gaps between the items, '
        'every item complete and not touching any other item or the edge.')
STY = {'kids': 'Style: semi-cartoon illustration, soft shading, clean outlines, bright friendly colours, the same style for every item.',
       'teen': 'Style: semi-cartoon illustration, soft shading, clean outlines, natural proportions, people are teenagers and adults (not little children), bright friendly colours, the same style for every item.'}
NUM = {8: 'eight', 9: 'nine'}

def sheets(topics, per, cols, key, label):
    flat = [(t, it) for t, items in topics for it in items]
    out = []
    for n in range(0, len(flat), per):
        chunk = flat[n:n+per]
        rows = [chunk[r:r+cols] for r in range(0, len(chunk), cols)]
        rtxt = ' '.join(f'Row {k+1}, left to right: ' + '; '.join(it for _, it in row) + '.' for k, row in enumerate(rows))
        g = f'{cols}×{len(rows)}'
        prompt = (f'A {g} grid of {NUM[len(chunk)]} separate illustrations on a {HEAD} {rtxt} {STY[key]} '
                  'No text, no letters, no labels, no numbers.')
        out.append((f'{label} · лист {n//per+1}', prompt, chunk))
    return out

SCENES = [
 ('7–9 · сцена · 07.12 There is / There are',
  'A wide winter park scene, landscape format. In the scene there is exactly: one snowman with a carrot nose on the left; two children ice skating on a small frozen pond in the middle; one empty bench covered with snow on the right; three small birds on a snowy tree branch; a few fir trees in the background. There is no dog, no sledge, no people on the bench and no shops. Plain light winter sky. Style: semi-cartoon illustration, soft shading, clean outlines, bright friendly colours. No text, no letters, no labels, no numbers.',
  'зимний парк для вопросов Is there…? / Are there any…? (есть: snowman, 2 skaters, bench, 3 birds, trees; нет: dog, sledge, people on the bench)'),
 ('10+ · сцена · 15.12 Present Continuous',
  'A wide city street scene just before Christmas, landscape format, seen from the side. In the scene: a teenage boy is hanging fairy lights over a shop window; a woman is carrying shopping bags; two teenagers are singing carols; a man is selling hot drinks at a small stall; a teenage girl is taking a photo of a big Christmas tree; light snow is falling. All shop signs are blank. Style: semi-cartoon illustration, soft shading, clean outlines, natural proportions, bright friendly colours. No text, no letters, no labels, no numbers.',
  'улица перед праздником: What is he doing? — He is hanging lights… (5 действий)'),
]

if __name__ == '__main__':
    md = ['# Картинки к вебинарам декабря — общий список\n',
          '03.12 A / an (еда) уже нарезан. Листы ниже — всё остальное.\n']
    for name, prompt, chunk in sheets(TEEN, 9, 3, 'teen', '10+') + sheets(KIDS, 8, 4, 'kids', '7–9'):
        md.append(f'\n## {name}\n\n```\n{prompt}\n```\n\n| № | предмет | урок |\n|---|---|---|')
        for k, (t, it) in enumerate(chunk, 1):
            short = it.replace('an animated film character, ', '').replace('two animated film characters, ', '')
            md.append(f'| {k} | {short} | {t} |')
    for name, prompt, use in SCENES:
        md.append(f'\n## {name}\n\n```\n{prompt}\n```\n\nЗачем: {use}')
    open('kartinki_dekabr.md', 'w').write('\n'.join(md) + '\n')
    print('\n'.join(md))
