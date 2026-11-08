"""How to Find Your Way in an Unknown Town  |  CEFR B1  |  Year 2 Economics (economist)  |  Hobbies design.

Text   = the teacher's HW15 text unchanged, every word kept; split into 4 paragraphs at natural boundaries
         (no em-dashes or colons in the source, nothing replaced). All 44 glossary units bolded.
Glossary = all 44 source units with the teacher's translations + B1 English definitions.
Retelling task from the source = Part 9 Option 3. The announcement about glossaries is not carried over.

Facts used (Option 5), Moscow public transport, central zone, fares from 2 January 2026
  Troika card, Wallet fare   75 roubles per trip
  bank card / NFC phone      83 roubles per trip
  biometric payment          71 roubles per trip
  Sources  Interfax https://www.interfax.ru/moscow/1060092
           Kommersant https://www.kommersant.ru/doc/8336906
           RIAMO https://riamo.ru/articles/shpargalki/skolko-budet-stoit-proezd-v-obschestvennom-transporte-moskvy-s-2-janvarja-2026-goda/
  The official transport.mos.ru page was not reached; the figures agree across the sources above.

Usage   python3 HW15_Find_Your_Way_B1_Economics_Y2.py <source HW15.docx> <output folder>
"""
import sys, pathlib, re, zipfile
SKILL = pathlib.Path(__file__).resolve().parents[2] / '.claude' / 'skills' / 'worksheet-builder'
sys.path.insert(0, str(SKILL / 'scripts'))
from hob_fill import build, original_texts, DELETE

TPL = str(SKILL / 'assets' / 'hobbies_template.docx')
SRC = sys.argv[1]
OUTDIR = pathlib.Path(sys.argv[2])
OUT = str(OUTDIR / 'Find_Your_Way_B1_Economics_Y2.docx')

orig = original_texts(TPL)
assert len(orig) == 227
T = {}

def dash_label(i):
    return orig[i].replace(' — ', '   ').replace(' -- ', '   ').rstrip()

def then_line(prefix, idx):
    return prefix + orig[idx][orig[idx].index('  then  '):]

# ── SOURCE TEXT (unchanged, split into 4 paragraphs) ────────────────────────
x = zipfile.ZipFile(SRC).read('word/document.xml').decode('utf-8')
paras = [''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p)) for p in re.findall(r'<w:p[ >].*?</w:p>', x, re.S)]
paras = [p.replace('\xa0', ' ').strip() for p in paras if p.strip()]   # non-breaking spaces -> spaces
i0 = paras.index('How to Find Your Way in an Unknown Town')
SRC1, SRC2 = paras[i0 + 1], paras[i0 + 2]
assert SRC1.startswith('Finding your way') and SRC2.startswith('While walking')
cut = SRC1.index('If you have no idea how to find')
cut2 = SRC2.index('Additionally, using a smartphone')
TEXT = [SRC1[:cut].strip(), SRC1[cut:].strip(), SRC2[:cut2].strip(), SRC2[cut2:].strip()]
assert ' '.join(TEXT) == SRC1 + ' ' + SRC2          # every word kept
assert not any('—' in t or ':' in t for t in TEXT)

BOLD = [  # (paragraph, exact phrase as it stands in the text)
    (0, 'daunting task'), (0, 'exciting adventure'), (0, 'tips'), (0, 'navigate your way'),
    (0, 'unfamiliar surroundings'), (0, 'take a moment to gather your thoughts'), (0, 'places of interest'),
    (0, 'monuments'), (0, 'galleries'), (0, 'look for'), (0, 'maps'), (0, 'tourist information centres'),
    (0, 'highlight important sights'),
    (1, 'hesitate'), (1, 'ask a passer-by for directions'), (1, 'approach someone'), (1, 'greet them politely'),
    (1, 'could you help me find'), (1, 'specific landmarks'), (1, 'make your request clear'),
    (1, 'For instance'), (1, 'give you a full idea'), (1, 'Walk straight down this street'), (1, 'turn left'),
    (2, 'pay attention to your surroundings'), (2, 'Look for signs'), (2, 'indicate'), (2, 'attractions'),
    (2, 'feel lost'), (2, 'change your route'), (2, 'stranger'), (2, 'observe'), (2, 'environment'),
    (3, 'nearest underground (tube) station'), (3, 'efficient way to travel'), (3, 'noisy and crowded city'),
    (3, 'Keep in mind'), (3, 'rich in culture and history'), (3, 'guided tours'),
    (3, 'learn about important events and sights'), (3, 'confirm any appointments or reservations'),
    (3, 'in advance'), (3, 'explore an unknown town'), (3, 'confidently and enjoyably'),
]
assert len(BOLD) == 44
for k, phrase in BOLD:
    # bold the first occurrence that is not already inside a bold span
    parts = re.split(r'(\*\*[^*]+\*\*)', TEXT[k])
    for j, seg in enumerate(parts):
        if not seg.startswith('**') and phrase in seg:
            parts[j] = seg.replace(phrase, f'**{phrase}**', 1)
            break
    else:
        raise AssertionError(phrase)
    TEXT[k] = ''.join(parts)
# "approach someone": only the verb is a glossary unit, the noun "This approach" stays plain
TEXT[1] = TEXT[1].replace('**approach someone**', '**approach** someone')

# ── HEADER ──────────────────────────────────────────────────────────────────
T[0] = 'How to Find Your Way in an Unknown Town'
T[1] = 'Orientation Skills for a Future Economist on a Business Trip'
T[2] = '90 min   •   Level B1   •   Year 2   •   Economics'

# ── PART 1 PROBLEM CASE ─────────────────────────────────────────────────────
T[5] = ('You are a second-year economics student and an intern at a consulting company. Next week the company '
        'sends two interns to a city they have never visited. They must collect data at a client’s office and '
        'meet the client’s finance director at 10 a.m. on the first day.')
T[6] = ('Your supervisor says, "An economist works with numbers and with people. If you cannot find the '
        'client’s office on time, nobody will listen to your analysis."')
T[7] = ('Your classmate Gleb says, "I don’t need a plan. My phone will show me everything." '
        'Another intern, Vera, says, "I always study the map, confirm the meeting the day before, and I am '
        'not afraid to ask people for help."')
T[9] = 'Discuss with a partner. Give your opinion with 2 reasons. Then make a prediction.'
T[10] = 'Is Gleb right that a smartphone is enough to find your way in a new city? Give 2 reasons for your answer.'
T[11] = 'Compare Gleb’s and Vera’s strategies. Which one is safer for a business trip, and why?'
T[12] = 'Predict. What can happen to Gleb on his first morning in the new city? Give 1 idea.'
T[13] = 'Share your ideas with the group (2 minutes).'

# ── PART 2 TEXT ─────────────────────────────────────────────────────────────
for k in range(4):
    T[15 + k] = f'{k + 1}.  ' + TEXT[k]
T[19] = DELETE

# ── PART 3 TEXT STRUCTURE ───────────────────────────────────────────────────
T[21] = 'Task 1   Match each paragraph to its function (A to E). One function is extra.'
T[22] = 'A.   How to ask a stranger for directions politely and clearly'
T[23] = 'B.   Other ways to move around the city and to plan your visit'
T[24] = 'C.   How to choose a cheap hotel in a big city'
T[25] = 'D.   What to do first when you arrive in a new place'
T[26] = 'E.   How to stay on the right route while you are walking'
T[27] = ('Paragraph 1 is ____     Paragraph 2 is ____     Paragraph 3 is ____     '
         'Paragraph 4 is ____     The extra function is ____')
T[28] = 'Task 2   Build the logical chain. Fill in the three missing steps with ideas from the text.'
T[29] = ('[You arrive in an unknown town]  then  [________]  then  [________]  then  [________]  then  '
         '[You reach your destination confidently]')
T[30] = 'Task 3   Cause and Effect. Complete each sentence using information from the text.'
T[31] = then_line('You greet a passer-by politely before you ask your question', 31)
T[32] = then_line('You use specific landmarks or street names in your question', 32)
T[33] = then_line('A young economist confirms the meeting with a client in advance', 33)

# ── PART 4 GLOSSARY (all 44 source units, teacher's translations) ───────────
T[34] = 'PART 4   VOCABULARY GLOSSARY'
GLOSS = [
    ('daunting task', 'пугающая/сложная задача', 'A job that looks very difficult and makes you a little afraid.'),
    ('exciting adventure', 'захватывающее приключение', 'An unusual and interesting experience that you enjoy.'),
    ('tips', 'советы', 'Short pieces of useful advice.'),
    ('navigate your way', 'ориентироваться', 'To find the right direction and reach the place you need.'),
    ('unfamiliar surroundings', 'незнакомая обстановка', 'A place that you do not know and have not seen before.'),
    ('take a moment to gather your thoughts', 'остановиться, чтобы собраться с мыслями',
     'To stop for a short time and think calmly about what to do next.'),
    ('places of interest', 'достопримечательности', 'Famous or beautiful places that visitors like to see.'),
    ('monuments', 'памятники', 'Statues or buildings that help people remember a person or an event.'),
    ('galleries', 'галереи', 'Buildings where people can look at paintings and other art.'),
    ('look for', 'искать', 'To try to find something or someone.'),
    ('maps', 'карты', 'Drawings of an area that show streets, buildings, and routes.'),
    ('tourist information centres', 'туристические информационные центры',
     'Offices where visitors get free maps and advice about a town.'),
    ('highlight important sights', 'выделять важные достопримечательности',
     'To mark the most interesting places so that people notice them.'),
    ('hesitate', 'колебаться, стесняться', 'To wait before you do something because you feel shy or unsure.'),
    ('ask a passer-by for directions', 'спросить у прохожего дорогу',
     'To ask a person in the street how to get to a place.'),
    ('approach', 'подходить', 'To come closer to someone, for example to speak to them.'),
    ('greet politely', 'вежливо приветствовать', 'To say hello to someone in a kind and respectful way.'),
    ('could you help me find', 'не могли бы вы помочь мне найти', 'A polite way to ask a stranger for help.'),
    ('specific landmarks', 'конкретные ориентиры',
     'Well-known buildings or objects that help you understand where a place is.'),
    ('make your request clear', 'чётко сформулировать просьбу',
     'To ask in a way that the other person understands exactly.'),
    ('for instance', 'например', 'Words that you use before you give an example.'),
    ('give you a full idea', 'дать полное представление', 'To explain something completely and clearly.'),
    ('walk straight down this street', 'идти прямо по этой улице',
     'To go along the same street without turning.'),
    ('turn left', 'повернуть налево', 'To change direction and go to the left.'),
    ('pay attention to your surroundings', 'обращать внимание на окружение',
     'To look carefully at the place around you.'),
    ('look for signs', 'искать указатели', 'To try to find boards that show names and directions.'),
    ('indicate', 'указывать', 'To show or point to something.'),
    ('attractions', 'достопримечательности', 'Interesting places that many visitors come to see.'),
    ('feel lost', 'чувствовать себя потерянным', 'To not know where you are or which way to go.'),
    ('change your route', 'изменить маршрут', 'To choose a different way to get to a place.'),
    ('stranger', 'незнакомец', 'A person you do not know.'),
    ('observe', 'наблюдать', 'To watch people or things carefully.'),
    ('environment', 'окружающая обстановка', 'The place and the conditions around you.'),
    ('nearest underground (tube) station', 'ближайшая станция метро',
     'The metro station that is closest to you. In London people call the metro the tube.'),
    ('efficient way to travel', 'эффективный способ передвижения',
     'A way to travel that saves time and money.'),
    ('noisy and crowded city', 'шумный и многолюдный город', 'A city with a lot of noise and a lot of people.'),
    ('keep in mind', 'иметь в виду', 'To remember something important when you plan or decide.'),
    ('rich in culture and history', 'богатый культурой и историей',
     'Having many old buildings, traditions, museums, and important events.'),
    ('guided tours', 'экскурсии с гидом', 'Visits to places with a person who tells you about them.'),
    ('learn about important events and sights', 'узнавать о важных событиях и достопримечательностях',
     'To get new information about the history and famous places of a town.'),
    ('confirm appointments or reservations', 'подтвердить встречи или бронирования',
     'To check that a meeting, a hotel room, or a ticket is still planned for you.'),
    ('in advance', 'заранее', 'Before the time when something happens.'),
    ('explore an unknown town', 'исследовать незнакомый город', 'To travel around a new town to learn about it.'),
    ('confidently and enjoyably', 'уверенно и с удовольствием', 'Without fear and with pleasure.'),
]
assert len(GLOSS) == 44
assert [g[0] for g in GLOSS] == [
    'daunting task', 'exciting adventure', 'tips', 'navigate your way', 'unfamiliar surroundings',
    'take a moment to gather your thoughts', 'places of interest', 'monuments', 'galleries', 'look for', 'maps',
    'tourist information centres', 'highlight important sights', 'hesitate', 'ask a passer-by for directions',
    'approach', 'greet politely', 'could you help me find', 'specific landmarks', 'make your request clear',
    'for instance', 'give you a full idea', 'walk straight down this street', 'turn left',
    'pay attention to your surroundings', 'look for signs', 'indicate', 'attractions', 'feel lost',
    'change your route', 'stranger', 'observe', 'environment', 'nearest underground (tube) station',
    'efficient way to travel', 'noisy and crowded city', 'keep in mind', 'rich in culture and history',
    'guided tours', 'learn about important events and sights', 'confirm appointments or reservations',
    'in advance', 'explore an unknown town', 'confidently and enjoyably']

# ── PART 5 VOCABULARY ACTIVATION ────────────────────────────────────────────
T[87] = 'Task 1   Categorisation'
T[88] = 'Put these words and phrases into the correct column. Some can go in more than one column. Be ready to explain your choice.'
T[89] = ('monuments   •   galleries   •   tourist information centres   •   attractions   •   greet politely'
         '   •   ask a passer-by for directions   •   make your request clear   •   could you help me find'
         '   •   guided tours   •   confirm appointments or reservations   •   in advance'
         '   •   take a moment to gather your thoughts')
T[90] = 'Places and services in a town'
T[91] = 'Asking for help'
T[92] = 'Planning ahead'
T[93] = 'Task 2   What is the difference? Write 1 to 2 sentences for each pair.'
T[94] = '1.   Monuments   and   Galleries'
T[95] = '2.   Places of interest   and   Specific landmarks'
T[96] = '3.   Passer-by   and   Stranger'
T[97] = '4.   Look for   and   Observe'
T[98] = 'Task 3   Complete the sentences with the correct word or phrase from the glossary.'
T[99] = 'a)  Olga called the client the day before to confirm the meeting __________________ .'
T[100] = 'b)  The city centre is very __________________ , so the underground is faster than a taxi.'
T[101] = 'c)  If you cannot find the client’s office, don’t __________________ to ask a passer-by for directions.'
T[102] = 'd)  The old clock tower on the main square is a good __________________ , so you can use it in your directions.'
T[103] = 'e)  Pavel looked at the map, but he still felt __________________ , so he decided to __________________ .'
T[104] = 'Task 4   Talk about yourself'
T[105] = 'Answer these questions in full sentences. Write your answers below, then share with a partner.'
T[106] = '1)  Have you ever been in an unknown town? How did you navigate your way?'
T[107] = '2)  Do you prefer to use a smartphone or to ask a passer-by for directions? Why?'
T[108] = '3)  Which places of interest in your town would you show to a business partner from another country? Why?'

# ── PART 6 ANALYTICAL TASK ──────────────────────────────────────────────────
T[110] = 'Case   Three Interns, Three Ways to Find the Client’s Office'
T[111] = 'Read the information about three economics interns on their first business trip. Then complete the tasks below.'
T[112] = 'Gleb, 19'
T[113] = 'Vera, 19'
T[114] = 'Timur, 20'
T[115] = 'Arrived in the city without any plan'
T[116] = 'Uses only the navigator on his phone'
T[117] = 'His phone battery died at 9 a.m.'
T[118] = 'Did not confirm the meeting with the client'
T[119] = 'Says "Asking strangers is a waste of time."'
T[120] = 'Studied the map at the hotel the evening before'
T[121] = 'Confirmed the meeting in advance'
T[122] = 'Asked a passer-by politely when a street was closed'
T[123] = 'Took the underground to save time'
T[124] = 'Says "Landmarks help me more than any app."'
T[125] = 'Joined a guided tour on the first evening'
T[126] = 'Knows the places of interest in the centre well'
T[127] = 'Took a taxi through the crowded centre in the morning'
T[128] = 'Arrived at the meeting 20 minutes late'
T[129] = 'Wants to work as a consultant for international clients.'
T[132] = ('Analyse the case. Fill in the table below. Write one good strategy and one mistake or risk for '
          'each intern. Use words from the glossary.')
T[133] = 'Intern'
T[134] = 'Good strategy'
T[135] = 'Mistake or risk'
T[136], T[137], T[138] = 'Gleb', 'Vera', 'Timur'
T[139] = ('Give your opinion. Which intern is the best prepared for work with clients in another city? '
          'Give 2 reasons with evidence from the case. Use the word because in your answer.')
T[140] = ('Advise Gleb. Write 4 to 5 sentences. Suggest 2 tips from the text and explain how each one will help '
          'him on his next business trip. Use at least 4 words from the glossary.')

# ── PART 7 CRITICAL THINKING ────────────────────────────────────────────────
T[142] = '"With a smartphone, you never need to ask a stranger for directions."'
T[143] = 'Task   Your Opinion'
T[145] = 'Give 2 reasons for your position. Use examples from the text or from your own experience.'
T[147] = ('Use at least 4 words from the glossary, for example ask a passer-by for directions, specific landmarks, '
          'feel lost. Try to use because in every reason.')

# ── PART 8 SYNTHESIS ────────────────────────────────────────────────────────
T[149] = 'Task   Write Your Answer'
T[150] = 'Write 6 to 8 sentences answering this question.'
T[151] = 'How can the skill of finding your way in an unknown town help an economist in professional life?'
T[153] = 'How an economist can prepare for a business trip or a meeting with a client in another city'
T[154] = 'Why it is important to ask strangers for help politely and to make your request clear'
T[155] = 'How observing a new environment can help an economist understand the city and its economy'

# ── PART 9 PROFESSIONAL OUTPUT ──────────────────────────────────────────────
T[156] = 'PART 9   PROFESSIONAL OUTPUT   CHOOSE ONE'
T[157] = 'Option 1   Short Presentation||   [2 min]'
T[158] = ('You work at a consulting company in Moscow. A colleague from a partner company arrives tomorrow and asks, '
          '"How do I get from my hotel to your office, and what should I see in the evening?"')
T[159] = ('Give a 2-minute briefing. Explain the route with specific landmarks, recommend 2 places of interest, '
          'and give 2 tips from the text.')
T[160] = 'Use the language from the Language tips (Walk straight down..., Take the underground to..., Keep in mind that...).'
T[161] = ('Requirements   Use 5 or more words from the glossary   •   A clear route with landmarks   •   '
          'Speak without reading your notes')
T[162] = 'Option 2   Error Finding||   [3 min]'
T[163] = ('A student wrote this paragraph. Find 4 mistakes (grammar, word choice, or ideas that are wrong based on '
          'the text). Write the correct version for each mistake.')
T[164] = ('"When you arrive in a new town, you should never ask a passer-by for directions. Tourist information '
          'centres usually has maps that hide important sights. The underground is a slow way to travel around '
          'a crowded city. It is wise to confirm your reservations in advance."')
T[165] = ('Requirements   Find 4 mistakes   •   Write the correct sentence for each one   •   '
          'Explain why it is wrong in 1 short sentence')
T[166] = 'Option 3   Retelling||   [3 min]'
T[167] = ('Retell the text. Try to use as many words from the glossary as possible. Follow the order of the four '
          'paragraphs and speak without reading the text.')
T[168] = ('Plan   Arrival and maps   •   Asking for directions   •   While walking   •   '
          'Transport, tours, and planning ahead')
T[169] = 'Requirements   Use 10 or more glossary words   •   Keep the order of the text   •   No reading from the text'
T[170] = 'Option 4   Role Play||   [4 min, pairs]'
T[171] = ('Situation   An analyst from a partner company (Student A) is lost near your office and calls you. '
          'You are an economist at a consulting company (Student B).')
T[172] = ('Student A greets politely, explains where he or she is, and asks for directions. Student B asks about '
          'specific landmarks and explains the route step by step. Then change roles.')
T[173] = 'At the end, Student A repeats the route to check that the request is clear.'
T[174] = ('Requirements   Use at least 4 glossary words each   •   Polite questions   •   '
          'Listen and respond to your partner')
T[175] = 'Option 5   Product   Business Trip Transport Budget||   [15 min, then 2 min presentation]'
T[176] = ('A colleague from a partner company will work in Moscow for 5 working days. Every day he makes 4 trips '
          'by public transport in the central zone (hotel, office, client, office, hotel).')
T[177] = ('Make a simple dashboard (a table in Excel or Google Sheets) that compares the cost of his trips for the '
          'whole week with three ways to pay. Moscow fares from 2 January 2026 per trip   Troika card (Wallet) '
          '75 roubles   •   bank card 83 roubles   •   biometric payment 71 roubles. Add a chart, choose the best '
          'option for a short business trip, and present it to the group in 2 minutes.')
T[178] = ('Requirements   Real numbers in roubles   •   A total for each way to pay   •   '
          'One recommendation with 2 reasons   •   4 glossary words in the presentation')

# ── SPEAKING PRACTICE ───────────────────────────────────────────────────────
T[179] = 'SPEAKING PRACTICE   DISCUSSION QUESTIONS'
QS = [
    'Is finding your way in a new town a daunting task for you?',
    'What do you do first when you arrive in a new place?',
    'Do you use paper maps or only your phone?',
    'Have you ever asked a passer-by for directions?',
    'How do you greet a stranger politely in English?',
    'Have you ever felt lost in a city? What did you do?',
    'Which landmarks would you use to explain a route to your college?',
    'Is the underground an efficient way to travel? Why?',
    'Do you like noisy and crowded cities or quiet towns?',
    'Have you ever joined a guided tour? Was it useful?',
    'Which places of interest in Russia would you recommend to a foreigner?',
    'Why is it wise to confirm appointments in advance?',
    'What can you learn about a town when you observe people?',
    'Would you like to go on business trips as an economist? Why?',
    'Which town rich in culture and history would you like to explore?',
    'Which tip from the text is the most useful for an economist on a business trip?',
]
for i, s in enumerate(QS):
    T[181 + i] = s

# ── LANGUAGE TIPS ───────────────────────────────────────────────────────────
T[198] = 'To give directions'
T[199] = 'Walk straight down ... and turn left at ...'
T[200] = 'It is next to / opposite the ...'
T[201] = 'Take the underground to ... station.'
T[202] = 'You will see ... on your right.'
T[203] = 'To ask for help politely'
T[204] = 'Excuse me, could you help me find ...?'
T[205] = 'Can you tell me how to get to ...?'
T[206] = 'Is it far from here?'
T[207] = 'Thank you, that is very helpful.'

# ── PEER ASSESSMENT ─────────────────────────────────────────────────────────
T[209] = 'Listen to your partner’s output. Complete the checklist below.'
T[213] = '1. Vocabulary. Used 5 or more words from the glossary correctly'
T[215] = '2. Structure. Had a clear beginning, middle, and end'
T[217] = '3. Evidence. Supported ideas with examples from the text'
T[219] = '4. Task completion. Answered all parts of the task'
T[221] = '5. Clarity. Spoke or wrote in full sentences, easy to understand'

build(TPL, T, OUT, glossary=GLOSS, glossary_widths=[3000, 2900, 3460])
