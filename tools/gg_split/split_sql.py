"""Go Getter: разбиение колод-юнитов по голубым блокам Vocabulary учебника (Анна, 11.11.2026).
DECKS[deck_id] = [(название блока как в учебнике, первое слово блока в колоде), ...].
Первая колода сохраняет id, остальные создаются; слова переносятся (deck_id), не пересоздаются.
Безымянные блоки учебника названы по смыслу. Снимок до переноса: words_deckid_backup_20261111_gg."""
import json
DECKS = {
 42: [('Clothes', 'boots'), ('Adjectives', 'big'), ('My things', 'backpack')],
 43: [('Parts of the house', 'bathroom'), ('Furniture', 'armchair'), ('Household objects', 'carpet')],
 44: [('Face and hair', 'ears'), ('Parts of the body', 'arm'), ('Personality adjectives', 'clever')],
 46: [('Daily activities', 'do my homework'), ('Days of the week', 'Monday'), ('Months', 'January')],
 47: [('Wild animals', 'bird'), ('Pets', 'cat'), ('Adjectives', 'cute')],
 48: [('Sports', 'badminton'), ('Healthy lifestyle', 'brush your teeth')],
 41: [('School subjects', 'Art'), ('School things', 'calculator'), ('After-school activities', 'ballet'), ('Places in a school', 'canteen')],
 40: [('Food and drink (1)', 'apples'), ('Food and drink (2)', 'butter'), ('Containers', 'a bar of chocolate')],
 49: [('Technology', 'camera'), ('Using technology', 'chat online'), ('Feelings', 'angry')],
 50: [('Geographical features', 'beach'), ('Adjectives (1)', 'boring'), ('Adjectives (2)', 'beautiful')],
 55: [('Household chores', 'clear the table'), ('Personality adjectives', 'bossy')],
 56: [('Shopping', 'cashier'), ('Shops', "baker's")],
 57: [('Going on holiday', 'explore an area'), ('Phrases with get', 'get bored')],
 58: [('Useful things', 'blender'), ('Smartphones', 'app')],
 59: [('Health problems', 'a blocked nose'), ('Injuries', 'broken leg'), ('The body', 'blood')],
 60: [('Cooking verbs', 'add'), ('Cooking nouns', 'bowl'), ('Describing food', 'delicious')],
 61: [('Places to live', 'block of flats'), ('Parts of the house', 'attic'), ('In the house', 'bookcase'), ('Phrasal verbs', 'check out')],
 62: [('Life ambitions', 'be a doctor'), ('Being with people', 'call'), ('Good manners', 'arrive on time')],
}
rows = [{'d': d, 'k': k, 't': t, 'w': w} for d, bl in DECKS.items() for k, (t, w) in enumerate(bl)]
print(json.dumps(rows, ensure_ascii=False))
# Применено 11.11.2026: 18 колод → 51 (GG1 Unit 2,3,4,6,7,8; GG2 Unit 1–4; GG3 Unit 1–8), GG2 Unit 5 — отдельно (3 колоды).
# Ждут PDF меньше 10 МБ: GG2 Unit 6–8 (часть 3), весь GG4.
# 11.11.2026, Анна: «надо под колоды, как в Prepare» — юнит стал папкой (Go Getter N / Unit K: …, "order" = 100 − K),
# колоды внутри — по названию блока («Clothes», «Adjectives»). Снимок до этого: word_decks_backup_20261111_gg2.
