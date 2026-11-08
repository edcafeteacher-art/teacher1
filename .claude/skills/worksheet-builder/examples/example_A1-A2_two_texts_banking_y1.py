"""Financial Independence  |  CEFR A1-A2 (two text versions)  |  Year 1 Banking  |  Hobbies design."""
import sys, pathlib
SKILL = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))

from hob_fill import build, original_texts, DELETE

TPL = str(SKILL / 'assets' / 'hobbies_template.docx')
OUT = str(pathlib.Path.cwd() / 'Financial_Independence_A1-A2_Banking_Y1.docx')
orig = original_texts(TPL)
T = {}

def dash_label(i):
    return orig[i].replace(' — ', '   ').rstrip()

def then_line(prefix, idx):
    return prefix + orig[idx][orig[idx].index('  then  '):]

# ── HEADER ──────────────────────────────────────────────────────────────────
T[0] = 'Financial Independence'
T[1] = 'Modern Youth Problems and Ways to Solve Them'
T[2] = '90 min   •   Level A1–A2   •   Year 1   •   Banking'

# ── PART 1 PROBLEM CASE ─────────────────────────────────────────────────────
T[5] = ('You are a first-year student at a banking college. Today your group is talking about money. '
        'Your teacher asks a simple question, "Who is financially independent in this room?"')
T[6] = ('Your teacher says, "Financial independence is not about a lot of money. It is about knowing how to use '
        'money. A good banker helps clients with this every day, so you need to learn it first."')
T[7] = ('Your classmate Artem says, "I get money from my parents, and I spend it all in one week." '
        'Your classmate Lisa says, "I have a part-time job, and I save some money every month."')
T[9] = 'Talk with a partner. Answer the questions. Give 1 or 2 reasons.'
T[10] = 'Is Artem financially independent? Why or why not?'
T[11] = 'What does Lisa do with her money? Is it a good idea? Why?'
T[12] = 'Guess. What can a young person do to become financially independent? Give 1 idea.'
T[13] = 'Tell the group your ideas (1 to 2 minutes).'

# ── PART 2 TEXT (two versions in one box) ───────────────────────────────────
A1 = [
    ('Many teenagers want to be **independent**. They want to make their own decisions and spend money without '
     'asking their parents. But **financial independence** needs more than money. You also need '
     '**responsibility** and **knowledge**.'),
    ('There is a problem. Many schools do not teach students about **personal finances**. So many teenagers do '
     'not know how to **save** money, make a **budget**, or stay out of **debt**. **Social media** also shows '
     'expensive things and **brands**. Many young people feel **pressure** to buy them.'),
    ('What can young people do? First, they can learn simple **financial skills**. For example, they can open a '
     '**bank account**, write down their **expenses**, and set a **saving goal**. Second, they can find a '
     '**part-time job** and earn money. Third, they can learn the difference between **needs** and **wants**.'),
    ('Financial independence is not about a lot of money. It is about smart and careful use of money. Start good '
     '**habits** early, and your **future** will be safe.'),
]
A2 = [
    ('Today’s teenagers live in a world full of opportunities, but also full of financial challenges. Many young '
     'people want to be **independent**, make their own decisions, and spend money without asking their parents. '
     'However, real **financial independence** needs not only money, but also **responsibility** and '
     '**knowledge**.'),
    ('One of the main problems is that most schools do not teach students how to manage **personal finances**. '
     'As a result, many teenagers do not know how to **save** money, plan a **budget**, or avoid **debt**. '
     '**Social media** also plays a role. It often shows a rich lifestyle and expensive **brands**, and it tells '
     'young people that success means spending a lot. This creates **pressure** and unrealistic hopes.'),
    ('To become financially independent, young people can start with small but important steps. First, they '
     'should learn basic **financial skills**, for example how to open a **bank account**, track **expenses**, and '
     'set **saving goals**. Second, they can look for **part-time jobs** or online projects that help them '
     '**earn** money and get experience. Finally, teenagers should understand the difference between **needs** '
     'and **wants**. Saving for something important, such as education or travel, is better than buying things '
     'you do not need.'),
    ('Financial independence is not about having a lot of money. It is about being smart, **disciplined**, and '
     'confident in how you use it. The earlier young people start these good **habits**, the more successful and '
     'secure their **future** will be.'),
]
T[15] = (['**Text A1   Easier version**'] + [f'{i + 1}.  {p}' for i, p in enumerate(A1)]
         + ['**Text A2   Standard version**'] + [f'{i + 1}.  {p}' for i, p in enumerate(A2)])
for i in (16, 17, 18, 19):
    T[i] = DELETE

# ── PART 3 TEXT STRUCTURE ───────────────────────────────────────────────────
T[21] = 'Task 1   Match each paragraph of your text (A1 or A2) to its topic. One topic is extra.'
T[22] = 'A.   How young people can become financially independent'
T[23] = 'B.   What financial independence really means'
T[24] = 'C.   How to open a bank account online'
T[25] = 'D.   Why teenagers have problems with money'
T[26] = 'E.   The main idea and why good habits are important'
T[27] = ('Paragraph 1 is ____     Paragraph 2 is ____     Paragraph 3 is ____     '
         'Paragraph 4 is ____     The extra topic is ____')
T[28] = ('Task 2   Put the steps in order. Use these steps (open a bank account, set a saving goal, '
         'save money every month).')
T[29] = ('[A student gets a part-time job]  then  [________]  then  [________]  then  [________]  then  '
         '[The student pays for something important, for example a course]')
T[30] = 'Task 3   Cause and effect. Finish each sentence. Use the text to help you.'
T[31] = then_line('Schools do not teach students about personal finances', 31)
T[32] = then_line('Social media shows expensive brands every day', 32)
T[33] = then_line('A student writes down all expenses every week', 33)

# ── PART 4 GLOSSARY (22 units) ──────────────────────────────────────────────
T[34] = 'PART 4   VOCABULARY GLOSSARY'
GLOSS = [
    ('independent', 'независимый', 'Able to live and make decisions without help from others.'),
    ('financial independence', 'финансовая независимость', 'Having enough money and skills to pay for your own life.'),
    ('responsibility', 'ответственность', 'Being careful and doing what you must do.'),
    ('knowledge', 'знания', 'What you know and understand.'),
    ('personal finances', 'личные финансы', 'Your own money, what you get and what you spend.'),
    ('save', 'копить, откладывать', 'To keep money for later and not spend it now.'),
    ('budget', 'бюджет', 'A plan for how you will spend your money.'),
    ('debt', 'долг', 'Money that you must pay back to someone.'),
    ('social media', 'социальные сети', 'Websites and apps where people share photos, videos, and ideas.'),
    ('brand', 'бренд, марка', 'The name of a company and its products.'),
    ('pressure', 'давление', 'A strong feeling that you must do something.'),
    ('financial skills', 'финансовые навыки', 'Abilities that help you use money well.'),
    ('bank account', 'банковский счёт', 'A place in a bank where you keep your money.'),
    ('expenses', 'расходы', 'Money that you spend on things.'),
    ('saving goal', 'цель накопления', 'The amount of money you want to save for something.'),
    ('part-time job', 'подработка, работа на неполный день', 'A job for only some hours a day or a week.'),
    ('earn', 'зарабатывать', 'To get money for your work.'),
    ('needs', 'потребности', 'Things that you must have, such as food and a home.'),
    ('wants', 'желания', 'Things that you would like to have but do not really need.'),
    ('disciplined', 'дисциплинированный', 'Able to follow your plan and your rules.'),
    ('habit', 'привычка', 'Something that you do often and regularly.'),
    ('future', 'будущее', 'The time that will come after now.'),
]

# ── PART 5 VOCABULARY ACTIVATION ────────────────────────────────────────────
T[87] = dash_label(87)
T[88] = 'Put these words into the correct column. Some words can go in two columns.'
T[89] = ('food   •   rent   •   medicine   •   bus ticket   •   expensive brand clothes   •   a new phone every year'
         '   •   concert tickets   •   a budget   •   a bank account   •   a saving goal   •   a list of expenses')
T[90] = 'Needs'
T[91] = 'Wants'
T[92] = 'Money tools'
T[93] = 'Task 2   What is the difference? Write 1 sentence for each pair.'
T[94] = '1.   Needs   and   Wants'
T[95] = '2.   Save   and   Earn'
T[96] = '3.   Budget   and   Expenses'
T[97] = '4.   Debt   and   Saving goal'
T[98] = dash_label(98)
T[99] = 'a)  Nina writes down how much money she spends every day. She tracks her __________________ .'
T[100] = 'b)  Pavel works in a café on Saturdays. He has a __________________ .'
T[101] = 'c)  Food and a home are __________________ , but a new phone every year is a want.'
T[102] = 'd)  Maks borrowed 2,000 roubles from a friend. Now he has a __________________ .'
T[103] = 'e)  I want to buy a laptop. My __________________ is 40,000 roubles.'
T[104] = dash_label(104)
T[105] = 'Answer the questions in full sentences. Write your answers below. Then tell your partner.'
T[106] = '1)  Do you have a bank account or a bank card? What do you use it for?'
T[107] = '2)  Do you save money? What is your saving goal?'
T[108] = '3)  What is one need and one want in your life?'

# ── PART 6 ANALYTICAL TASK ──────────────────────────────────────────────────
T[110] = 'Case   Three Classmates, Three Ways to Use Money'
T[111] = 'Read about three students. Then do the tasks below.'
T[112], T[113], T[114] = 'Lisa, 17', 'Artem, 18', 'Kira, 17'
T[115] = 'Works in a café on Saturdays'
T[116] = 'Saves 3,000 roubles every month'
T[117] = 'Has a bank account and a saving goal'
T[118] = 'Does not buy expensive brands'
T[119] = 'Says "I want to pay for an English course."'
T[120] = 'Gets money from his parents'
T[121] = 'Spends all his money in one week'
T[122] = 'Buys expensive sneakers he saw on social media'
T[123] = 'Says "I want to look like the people online."'
T[124] = 'Owes a friend 5,000 roubles'
T[125] = 'Makes videos for an online project'
T[126] = 'Earns money, but not every month'
T[127] = 'Has no budget'
T[128] = 'Says "Sometimes I have money, sometimes I do not."'
T[129] = 'Wants to travel next summer'
T[132] = 'Analyse the case. Fill in the table. Write one good habit and one problem for each student.'
T[133], T[134], T[135] = 'Student', 'Good habit', 'Problem'
T[136], T[137], T[138] = 'Lisa', 'Artem', 'Kira'
T[139] = ('Give your opinion. Which student is the most financially independent? Give 2 reasons. '
          'Use the words because and responsibility.')
T[140] = ('Help Artem. Write 3 to 4 sentences. Give him 2 ideas from the text and say why they will help. '
          'Use 3 words from the glossary.')

# ── PART 7 CRITICAL THINKING ────────────────────────────────────────────────
T[142] = '"Young people do not need to save money. They can start saving when they are older."'
T[143] = dash_label(143)
T[144] = 'Do you agree or disagree? Write one sentence. Start with I agree or I disagree.'
T[145] = 'Give 2 reasons. Start each reason with because.'
T[146] = 'Think of 1 reason for the other opinion. Then say why your opinion is still right.'
T[147] = 'Use 3 words from the glossary. Use because in every reason.'

# ── PART 8 SYNTHESIS ────────────────────────────────────────────────────────
T[149] = dash_label(149)
T[150] = 'Write 4 to 5 short sentences to answer this question.'
T[151] = 'How can a young person become financially independent?'
T[152] = 'Write about all three points. Use your own words. Do not copy sentences from the text.'
T[153] = 'What financial independence means'
T[154] = 'Why it is difficult for many teenagers today'
T[155] = 'Two steps that you want to take this year'

# ── PART 9 PROFESSIONAL OUTPUT ──────────────────────────────────────────────
T[156] = 'PART 9   PROFESSIONAL OUTPUT   CHOOSE ONE'
T[157] = 'Option 1   Short Presentation||   [2 min]'
T[158] = ('Imagine you work at a bank. A school asks you to give a short talk, "How to start managing your '
          'money."')
T[159] = 'Say 4 to 5 sentences. Explain what financial independence is and give 2 simple steps from the text.'
T[160] = 'Use the phrases from the Language tips (I think..., First..., because...).'
T[161] = ('Requirements   Use 4 or more words from the glossary   •   Full sentences only   •   '
          'Speak without reading your notes')
T[162] = 'Option 2   Error Finding||   [3 min]'
T[163] = ('A student wrote this text. Find 4 mistakes (grammar or ideas that are wrong based on the text). '
          'Write the correct sentence for each mistake.')
T[164] = ('"Financial independence means having a lot of money. Most schools teach students how to plan a '
          'budget. Lisa save money every month. Expensive brand sneakers are a need."')
T[165] = ('Requirements   Find 4 mistakes   •   Write the correct sentence for each one   •   '
          'Say why it is wrong in a few words')
T[166] = 'Option 3   Keyword Speaking||   [2 min]'
T[167] = 'Use all 6 words below. Talk about your money habits for 2 minutes without notes.'
T[168] = 'Words   budget   save   expenses   needs   wants   because'
T[169] = 'Requirements   Use all 6 words correctly   •   Speak in full sentences   •   No reading from notes'
T[170] = 'Option 4   Role Play   At the Bank||   [3 min, pairs]'
T[171] = ('Student A is a bank consultant. Student B is a student who says, "I want to open my first bank '
          'account and start saving."')
T[172] = ('Student A asks 3 questions about the client’s income, expenses, and saving goal. Student B answers. '
          'Student A gives 2 simple tips.')
T[173] = 'Then change roles.'
T[174] = 'Requirements   Use 4 glossary words each   •   Be polite   •   Speak in full sentences'
T[175] = 'Option 5   Product   My Saving Plan||   [15 min, then 2 min presentation]'
T[176] = ('Make a short presentation (4 slides) or a simple dashboard (a table in Excel or Google Sheets) called '
          '"My Saving Plan" for one month.')
T[177] = ('Show your income, 5 expenses marked as needs or wants, one saving goal with the amount and the date, and '
          '2 steps from the text. Then show your product to the group and explain it in 2 minutes.')
T[178] = ('Requirements   Real numbers in roubles   •   Needs and wants clearly marked   •   '
          '4 glossary words on the slides or in the table')

# ── SPEAKING PRACTICE ───────────────────────────────────────────────────────
T[179] = 'SPEAKING PRACTICE   DISCUSSION QUESTIONS'
T[180] = 'Work with a partner. Ask and answer the questions. Give full answers. Ask one more question each time.'
QS = [
    'Do you get pocket money? From whom?',
    'Do you have a bank card?',
    'What do you usually spend money on?',
    'Do you save money? Why or why not?',
    'What is your saving goal?',
    'Do you have a part-time job?',
    'What job can a student do after college?',
    'Is it easy to save money? Why?',
    'What is the difference between needs and wants?',
    'Do you plan a budget?',
    'Do you buy things that you see on social media?',
    'Do you like expensive brands? Why?',
    'Is it a good idea to borrow money from friends?',
    'Who taught you about money?',
    'What is more important, education or travel? Why?',
    'What is one good money habit?',
]
for i, s in enumerate(QS):
    T[181 + i] = s

# ── LANGUAGE TIPS ───────────────────────────────────────────────────────────
T[198] = 'To talk about money'
T[199] = 'I spend money on ...'
T[200] = 'I save money for ...'
T[201] = 'My saving goal is ...'
T[202] = 'I earn money by ...'
T[203] = 'To give a reason'
T[204] = '... because it is important.'
T[205] = '... because I want to ...'
T[206] = 'I think ... is better because ...'
T[207] = 'First, ... Second, ...'

# ── PEER ASSESSMENT ─────────────────────────────────────────────────────────
T[213] = '1. Vocabulary. Used 3 or more words from the glossary correctly'
T[215] = '2. Structure. Had a beginning, a middle and an end'
T[217] = '3. Reasons. Used because to give reasons'
T[219] = '4. Task. Answered all parts of the task'
T[221] = '5. Clarity. Spoke or wrote in full, clear sentences'

assert len(orig) == 227
build(TPL, T, OUT, glossary=GLOSS, glossary_widths=[2700, 2900, 3760])
