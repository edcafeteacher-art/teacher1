"""How to Find Your Way in an Unknown Town  |  CEFR A2  |  Year 1 Banking (38.02.07)  |  Hobbies design.

Base script for the Year 1 A2 sheets. HW15_Find_Your_Way_A2_Logistics_Y1.py loads it and overrides only the
professional context, so the text, the glossary, and every answer-bearing task stay identical and one key
(Find_Your_Way_A2_Y1_KEY.docx, written by this script) works for both groups.

Text   = the teacher's HW15 text unchanged, every word kept, 4 numbered paragraphs (cuts before
         "If you have no idea how to find" and before "Additionally, using a smartphone"), as in the B1 sheet.
         All 44 glossary units bolded (teacher's choice, above the Year 1 norm of 6 to 7 per paragraph).
Glossary = all 44 source units, teacher's translations unchanged, A2 English definitions.
Part 9 Option 3 = the teacher's retelling task. The announcement "REMEMBER! Next Tuesday..." is not carried over.

Facts used (Option 5), Moscow public transport, central zone, fares from 2 January 2026, per trip
  Troika card, Wallet fare   75 roubles
  bank card                  83 roubles
  biometric payment          71 roubles
  Sources  Interfax    https://www.interfax.ru/moscow/1060092
           Kommersant  https://www.kommersant.ru/doc/8336906
  Calculation in the key   5 days x 4 trips = 20 trips; 1,500 / 1,660 / 1,420 roubles.

Usage   python3 HW15_Find_Your_Way_A2_Banking_Y1.py <source HW15.docx> <output folder>
"""
import sys, pathlib, re, zipfile
SKILL = pathlib.Path(__file__).resolve().parents[2] / '.claude' / 'skills' / 'worksheet-builder'
sys.path.insert(0, str(SKILL / 'scripts'))
from hob_fill import build, original_texts, DELETE

TPL = str(SKILL / 'assets' / 'hobbies_template.docx')
SRC = sys.argv[1]
OUTDIR = pathlib.Path(sys.argv[2])
OUT = str(OUTDIR / 'Find_Your_Way_A2_Banking_Y1.docx')
KEY = str(OUTDIR / 'Find_Your_Way_A2_Y1_KEY.docx')

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
T[1] = 'Getting Around a New Place for a Future Bank Consultant'
T[2] = '90 min   •   Level A2   •   Year 1   •   Banking'

# ── PART 1 PROBLEM CASE ─────────────────────────────────────────────────────
T[5] = ('You are a first-year student at a banking college. Next Monday you start your practice at a bank '
        'branch in a part of Moscow that you do not know. The branch opens at 9 a.m., and the first clients '
        'come at 9.')
T[6] = ('The branch manager says, "Clients do not like to wait. A good bank consultant is never late, so plan your '
        'way to work before your first day."')
T[7] = ('Your classmate Denis says, "I don’t need a plan. My phone will show me the way." '
        'Your classmate Polina says, "I will look at the map tonight, and I will ask people for help if I feel '
        'lost."')
T[9] = 'Talk with a partner. Answer the questions. Give 1 or 2 reasons.'
T[10] = 'Is Denis right? Is a phone enough to find your way? Why or why not?'
T[11] = 'Who has a better plan, Denis or Polina? Why?'
T[12] = 'Guess. What can happen to Denis on his first morning at the bank branch? Give 1 idea.'
T[13] = 'Tell the group your ideas (1 to 2 minutes).'

# ── PART 2 TEXT ─────────────────────────────────────────────────────────────
for k in range(4):
    T[15 + k] = f'{k + 1}.  ' + TEXT[k]
T[19] = DELETE

# ── PART 3 TEXT STRUCTURE ───────────────────────────────────────────────────
T[21] = 'Task 1   Match each paragraph to its topic (A to E). One topic is extra.'
T[22] = 'A.   How to ask a stranger for directions politely'
T[23] = 'B.   Other ways to travel and how to plan your visit'
T[24] = 'C.   How to choose a cheap hotel in a big city'
T[25] = 'D.   What to do first in a new place'
T[26] = 'E.   What to do while you are walking'
T[27] = ('Paragraph 1 is ____     Paragraph 2 is ____     Paragraph 3 is ____     '
         'Paragraph 4 is ____     The extra topic is ____')
T[28] = ('Task 2   Put the steps in the right order. Use these steps (walk and look for signs, '
         'take a moment and look at a map, ask a passer-by for directions).')
T[29] = ('[You arrive in an unknown town]  then  [________]  then  [________]  then  [________]  then  '
         '[You find the place you need]')
T[30] = 'Task 3   Cause and effect. Finish each sentence. Use the text to help you.'
T[31] = then_line('You greet a passer-by politely before your question', 31)
T[32] = then_line('You use specific landmarks or street names', 32)
T[33] = then_line('You confirm your appointments in advance', 33)

# ── PART 4 GLOSSARY (all 44 source units, teacher's translations, A2 definitions) ──
T[34] = 'PART 4   VOCABULARY GLOSSARY'
GLOSS = [
    ('daunting task', 'пугающая/сложная задача', 'A very difficult job that makes you a little afraid.'),
    ('exciting adventure', 'захватывающее приключение', 'A new and interesting experience that you enjoy.'),
    ('tips', 'советы', 'Short pieces of useful advice.'),
    ('navigate your way', 'ориентироваться', 'To find the right way to a place.'),
    ('unfamiliar surroundings', 'незнакомая обстановка', 'A place that you do not know.'),
    ('take a moment to gather your thoughts', 'остановиться, чтобы собраться с мыслями',
     'To stop for a short time and think calmly.'),
    ('places of interest', 'достопримечательности', 'Famous or beautiful places that visitors like to see.'),
    ('monuments', 'памятники', 'Statues or old buildings that remind people of a person or an event.'),
    ('galleries', 'галереи', 'Buildings where you can look at paintings and other art.'),
    ('look for', 'искать', 'To try to find something or someone.'),
    ('maps', 'карты', 'Pictures of a place that show streets and buildings.'),
    ('tourist information centres', 'туристические информационные центры',
     'Offices where visitors get maps and advice about a town.'),
    ('highlight important sights', 'выделять важные достопримечательности',
     'To mark the most interesting places so that people see them.'),
    ('hesitate', 'колебаться, стесняться', 'To wait before you do something because you feel shy or unsure.'),
    ('ask a passer-by for directions', 'спросить у прохожего дорогу',
     'To ask a person in the street how to get to a place.'),
    ('approach', 'подходить', 'To come closer to someone.'),
    ('greet politely', 'вежливо приветствовать', 'To say hello to someone in a kind way.'),
    ('could you help me find', 'не могли бы вы помочь мне найти', 'A polite way to ask for help.'),
    ('specific landmarks', 'конкретные ориентиры',
     'Well-known buildings or places that help you find your way.'),
    ('make your request clear', 'чётко сформулировать просьбу',
     'To ask in a way that is easy to understand.'),
    ('for instance', 'например', 'Words you say before an example.'),
    ('give you a full idea', 'дать полное представление', 'To explain something fully and clearly.'),
    ('walk straight down this street', 'идти прямо по этой улице',
     'To go along the same street and not turn.'),
    ('turn left', 'повернуть налево', 'To change direction and go to the left.'),
    ('pay attention to your surroundings', 'обращать внимание на окружение',
     'To look carefully at the place around you.'),
    ('look for signs', 'искать указатели', 'To try to find boards with names and directions.'),
    ('indicate', 'указывать', 'To show something.'),
    ('attractions', 'достопримечательности', 'Interesting places that many visitors come to see.'),
    ('feel lost', 'чувствовать себя потерянным', 'To not know where you are or where to go.'),
    ('change your route', 'изменить маршрут', 'To choose a different way to a place.'),
    ('stranger', 'незнакомец', 'A person you do not know.'),
    ('observe', 'наблюдать', 'To watch people or things carefully.'),
    ('environment', 'окружающая обстановка', 'The place and the things around you.'),
    ('nearest underground (tube) station', 'ближайшая станция метро',
     'The metro station that is closest to you. In London people say the tube.'),
    ('efficient way to travel', 'эффективный способ передвижения',
     'A way to travel that saves time and money.'),
    ('noisy and crowded city', 'шумный и многолюдный город', 'A city with a lot of noise and a lot of people.'),
    ('keep in mind', 'иметь в виду', 'To remember something important.'),
    ('rich in culture and history', 'богатый культурой и историей',
     'With many old buildings, museums, and traditions.'),
    ('guided tours', 'экскурсии с гидом', 'Visits to places with a guide who tells you about them.'),
    ('learn about important events and sights', 'узнавать о важных событиях и достопримечательностях',
     'To get new facts about the history and famous places of a town.'),
    ('confirm appointments or reservations', 'подтвердить встречи или бронирования',
     'To check that your meeting, room, or table is still planned.'),
    ('in advance', 'заранее', 'Before something happens.'),
    ('explore an unknown town', 'исследовать незнакомый город', 'To walk around a new town and learn about it.'),
    ('confidently and enjoyably', 'уверенно и с удовольствием', 'Without fear and with pleasure.'),
]
assert len(GLOSS) == 44

# ── PART 5 VOCABULARY ACTIVATION ────────────────────────────────────────────
T[87] = 'Task 1   Categorisation'
T[88] = 'Put these words into the correct column. Some words can go in two columns.'
T[89] = ('monuments   •   galleries   •   tourist information centres   •   attractions   •   greet politely'
         '   •   ask a passer-by for directions   •   make your request clear   •   could you help me find'
         '   •   guided tours   •   confirm appointments or reservations   •   in advance')
T[90] = 'Places in a town'
T[91] = 'Asking for help'
T[92] = 'Planning ahead'
T[93] = 'Task 2   What is the difference? Write 1 sentence for each pair.'
T[94] = '1.   Monuments   and   Galleries'
T[95] = '2.   Turn left   and   Walk straight down the street'
T[96] = '3.   Maps   and   Signs'
T[97] = '4.   Look for   and   Observe'
T[98] = ('Task 3   Complete the sentences. Use these words (feel lost, guided tours, hesitate, in advance, '
         'turn left).')
T[99] = 'a)  I always book a table in a café __________________ , for example two days before.'
T[100] = 'b)  If you cannot find the station, don’t __________________ to ask a passer-by for directions.'
T[101] = 'c)  Go straight on, then __________________ at the traffic lights. The museum is on your left.'
T[102] = 'd)  Nina joined two __________________ , and the guides told her about the history of the town.'
T[103] = 'e)  Pavel has no map, and he does not know where he is. He starts to __________________ .'
T[104] = 'Task 4   Talk about yourself'
T[105] = 'Answer the questions in full sentences. Use the sentence starters. Then tell your partner.'
T[106] = '1)  Did you visit a new town last year? What did you see there? (Last year I visited ... I saw ...)'
T[107] = '2)  Do you use a phone or ask people for directions? Why? (I usually ... because ...)'
T[108] = '3)  What places of interest are there in your town? (In my town there is ... There are ...)'

# ── PART 6 ANALYTICAL TASK ──────────────────────────────────────────────────
T[110] = 'Case   Three Students, Three Ways to Get to the Bank Branch'
T[111] = 'Read about three students on their first day of practice. Then do the tasks below.'
T[112], T[113], T[114] = 'Denis, 17', 'Polina, 17', 'Timur, 18'
T[115] = 'Uses only his phone map'
T[116] = 'Did not check the route'
T[117] = 'His phone battery died'
T[118] = 'Came 30 minutes late'
T[119] = 'Says "I don’t ask strangers."'
T[120] = 'Studied the map at home'
T[121] = 'Left home early'
T[122] = 'Asked people politely'
T[123] = 'Came 10 minutes early'
T[124] = 'Says "Landmarks help me."'
T[125] = 'Takes the underground'
T[126] = 'Never looks at a map'
T[127] = 'Asks 4 or 5 people a day'
T[128] = 'Is often 5 minutes late'
T[129] = 'Wants to work at a bank.'
T[132] = 'Analyse the case. Fill in the table. Write one good idea and one problem for each student.'
T[133], T[134], T[135] = 'Student', 'Good idea', 'Problem'
T[136], T[137], T[138] = 'Denis', 'Polina', 'Timur'
T[139] = ('Give your opinion. Who is the best prepared for the first day at the bank branch? Give 2 reasons. '
          'Use the word because.')
T[140] = ('Help Denis. Write 3 to 4 sentences. Give him 2 tips from the text and say why they will help. '
          'Use 3 words from the glossary.')

# ── PART 7 CRITICAL THINKING ────────────────────────────────────────────────
T[142] = '"A smartphone is enough. You never need to ask a stranger for directions."'
T[143] = 'Task   Your Opinion'
T[144] = 'Do you agree or disagree? Write one sentence. Start with I agree or I disagree.'
T[145] = 'Give 2 reasons. Start each reason with because.'
T[146] = ('Give 1 reason for the other opinion (for example, a phone battery can die, or a phone is fast). '
          'Then say why you are still right.')
T[147] = 'Use 3 glossary words (stranger, feel lost, hesitate). Use because in every reason.'

# ── PART 8 SYNTHESIS ────────────────────────────────────────────────────────
T[149] = 'Task   Write Your Answer'
T[150] = 'Write 4 to 5 short sentences to answer this question.'
T[151] = 'How can a new bank consultant find the way to a bank branch and come on time?'
T[152] = 'Write about all three points. Use your own words. Do not copy sentences from the text.'
T[153] = 'What you can do before your first day (a map, the route)'
T[154] = 'What you can do if you feel lost (ask a passer-by politely)'
T[155] = 'Why a bank consultant must be on time for clients'

# ── PART 9 PROFESSIONAL OUTPUT ──────────────────────────────────────────────
T[156] = 'PART 9   PROFESSIONAL OUTPUT   CHOOSE ONE'
T[157] = 'Option 1   Short Presentation||   [2 min]'
T[158] = ('Imagine you work at a bank branch in Moscow. A new client from another city calls and asks, '
          '"How do I get from the underground station to your branch?"')
T[159] = 'Say 4 to 5 sentences. Explain the route with 2 landmarks and give 1 tip from the text.'
T[160] = 'Use the phrases from the Language tips (Walk straight down..., Turn left at..., You will see...).'
T[161] = ('Requirements   Use 4 or more words from the glossary   •   Full sentences only   •   '
          'Speak without reading your notes')
T[162] = 'Option 2   Error Finding||   [3 min]'
T[163] = ('A student wrote this text. Find 4 mistakes (grammar or ideas that are wrong based on the text). '
          'Write the correct sentence for each mistake.')
T[164] = ('"When you arrive in a new place, you should never ask a passer-by for directions. Tourist information '
          'centres usually has maps. These maps hide important sights. The underground is a slow way to travel '
          'around a crowded city. It is a good idea to confirm your reservations in advance."')
T[165] = ('Requirements   Find 4 mistakes   •   Write the correct sentence for each one   •   '
          'Say why it is wrong in a few words')
T[166] = 'Option 3   Retelling||   [3 min]'
T[167] = ('Retell the text. Try to use as many words from the glossary as possible. '
          'Follow the four steps of the plan below.')
T[168] = ('Plan   1 Arrival and maps   •   2 Asking for directions   •   3 While walking   •   '
          '4 Transport, tours, and planning ahead')
T[169] = ('Requirements   Use 8 or more glossary words   •   Keep the order of the text   •   '
          'Do not read the text')
T[170] = 'Option 4   Role Play   At the Bank Branch||   [3 min, pairs]'
T[171] = ('Student A is a client from another city. He or she is lost near the bank branch and calls the bank. '
          'Student B is a bank consultant at the branch.')
T[172] = ('Student A greets politely, says where he or she is, and asks for directions. Student B asks about '
          'landmarks and explains the route in 3 or 4 steps.')
T[173] = 'Then change roles.'
T[174] = 'Requirements   Use 4 glossary words each   •   Be polite   •   Speak in full sentences'
T[175] = 'Option 5   Product   The Best Way to Pay for Trips||   [15 min, then 2 min presentation]'
T[176] = ('You work at a bank branch. A client works in the centre of Moscow 5 days a week. Every day she makes '
          '4 trips by public transport in the central zone. She asks you, "How can I pay less for my trips?"')
T[177] = ('Make a simple dashboard (a table in Excel or Google Sheets) or 3 slides. Step 1. Count the trips for '
          'one week. Step 2. Count the cost for each way to pay. Moscow fares from 2 January 2026 per trip   '
          'Troika card (Wallet) 75 roubles   •   bank card 83 roubles   •   biometric payment 71 roubles. '
          'Step 3. Add a chart and choose the best way to pay. Present your product to the group in 2 minutes.')
T[178] = ('Requirements   Real numbers in roubles   •   A total for each way to pay   •   '
          'One choice with 2 reasons   •   3 glossary words in the presentation')

# ── SPEAKING PRACTICE ───────────────────────────────────────────────────────
T[179] = 'SPEAKING PRACTICE   DISCUSSION QUESTIONS'
T[180] = 'Work with a partner. Ask and answer the questions. Give full answers. Ask one more question each time.'
QS = [
    'Is it easy for you to find your way?',
    'What do you do first in a new town?',
    'Do you use paper maps or your phone?',
    'Do you ask passers-by for directions?',
    'How do you greet a stranger politely?',
    'Did you ever feel lost in a city?',
    'What landmarks are near your college?',
    'Is the underground fast? Why?',
    'Do you like noisy and crowded cities?',
    'Did you ever join a guided tour?',
    'What places of interest do you like?',
    'Do you book tickets in advance? Why?',
    'What signs do you see on your way?',
    'Which town do you want to explore?',
    'Which tip from the text do you like?',
    'How can you help a lost bank client?',
]
assert len(QS) == 16
for i, s in enumerate(QS):
    T[181 + i] = s

# ── LANGUAGE TIPS ───────────────────────────────────────────────────────────
T[198] = 'To give directions'
T[199] = 'Walk straight down ...'
T[200] = 'Turn left at ...'
T[201] = 'It is next to ...'
T[202] = 'You will see ... on your right.'
T[203] = 'To ask for help politely'
T[204] = 'Excuse me, could you help me find ...?'
T[205] = 'How do I get to ...?'
T[206] = 'Is it far from here?'
T[207] = 'Thank you very much!'

# ── PEER ASSESSMENT ─────────────────────────────────────────────────────────
T[209] = 'Listen to your partner. Fill in the checklist below.'
T[213] = '1. Vocabulary. Used 3 or more words from the glossary correctly'
T[215] = '2. Structure. Had a beginning, a middle, and an end'
T[217] = '3. Reasons. Used because to give reasons'
T[219] = '4. Task. Answered all parts of the task'
T[221] = '5. Clarity. Spoke or wrote in full, clear sentences'

build(TPL, T, OUT, glossary=GLOSS, glossary_widths=[3000, 2900, 3460])

# ── ANSWER KEY (one file for the Banking and the Logistics sheets) ──────────
from docx import Document

KEY_SECTIONS = [
    ('Part 3   Task 1', ['Paragraph 1 is D, Paragraph 2 is A, Paragraph 3 is E, Paragraph 4 is B, '
                         'the extra topic is C']),
    ('Part 3   Task 2', ['Take a moment and look at a map',
                         'Ask a passer-by for directions',
                         'Walk and look for signs']),
    ('Part 3   Task 3 (sample answers)', [
        'Greet politely, then the answer is more likely to be positive (a positive response)',
        'Specific landmarks or street names, then the person can give you a full idea of how to reach the place',
        'Confirm in advance, then you will have everything ready when you get there']),
    ('Part 5   Task 1 (suggested)', [
        'Places in a town   monuments, galleries, tourist information centres, attractions, guided tours',
        'Asking for help   greet politely, ask a passer-by for directions, make your request clear, '
        'could you help me find',
        'Planning ahead   confirm appointments or reservations, in advance, guided tours (accept in two '
        'columns)']),
    ('Part 5   Task 3', ['a) in advance', 'b) hesitate', 'c) turn left', 'd) guided tours', 'e) feel lost']),
    ('Part 9   Option 2 (4 mistakes)', [
        '"should never ask a passer-by" is wrong, the text says do not hesitate to ask a passer-by for directions',
        '"centres usually has" is a grammar mistake, correct is "centres usually have"',
        '"These maps hide important sights" is wrong, the maps highlight important sights',
        '"a slow way to travel" is wrong, the underground is an efficient way to travel',
        'The last sentence is correct.']),
    ('Part 9   Option 5 (expected numbers)', [
        '5 days x 4 trips = 20 trips',
        'Troika card (Wallet)   20 x 75 = 1,500 roubles',
        'Bank card   20 x 83 = 1,660 roubles',
        'Biometric payment   20 x 71 = 1,420 roubles',
        'Fares for the central zone from 2 January 2026. The choice is open, accept any choice with 2 reasons.']),
    ('Open tasks', ['Part 1, Part 5 Tasks 2 and 4, Part 6, Part 7, Part 8, and Part 9 Options 1, 3, 4 have no '
                    'single answer. Check the use of glossary words and because.']),
]
kd = Document()
kd.add_heading('Answer Key   How to Find Your Way in an Unknown Town', level=1)
kd.add_paragraph('A2   •   Year 1   •   Banking and Logistics (one key for both sheets)   •   For the teacher')
for head, items in KEY_SECTIONS:
    kd.add_heading(head, level=2)
    for it in items:
        kd.add_paragraph(it, style='List Bullet')
kd.save(KEY)
