"""Financial Independence  |  Version 2 (harder)  |  CEFR A2  |  Year 1 Banking  |  Hobbies design.
Reuses the unchanged parts of version 1, overrides text, glossary, and tasks."""
import sys, pathlib
SKILL = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))

import re
from hob_fill import build, original_texts, DELETE

src = open(str(SKILL / 'examples' / 'example_A1-A2_two_texts_banking_y1.py'), encoding='utf-8').read()
src = src[:src.rindex('build(TPL')]          # take T, GLOSS, helpers from version 1 without building
ns = {'__file__': str(SKILL / 'examples' / 'example_A1-A2_two_texts_banking_y1.py')}
exec(compile(src, 'v1', 'exec'), ns)
T, TPL, orig, dash_label, then_line = ns['T'], ns['TPL'], ns['orig'], ns['dash_label'], ns['then_line']
OUT = str(pathlib.Path.cwd() / 'Financial_Independence_A2_Version2_Banking_Y1.docx')

# ── HEADER ──────────────────────────────────────────────────────────────────
T[1] = 'Modern Youth Problems and Ways to Achieve It'
T[2] = 'Version 2   •   90 min   •   Level A2   •   Year 1   •   Banking'

# ── PART 1 (less support) ───────────────────────────────────────────────────
T[9] = 'Discuss with a partner. Give your opinion with 2 reasons. Then make a prediction.'
T[10] = 'Is Artem financially independent? Give 2 reasons for your answer.'
T[11] = 'Lisa has a part-time job and saves money. What are the advantages and disadvantages of her choice?'
T[12] = 'Predict. Why do many young people find it difficult to save money today? Give 2 ideas.'
T[13] = 'Share your ideas with the group (2 minutes).'

# ── PART 2 ORIGINAL TEXT (em-dashes replaced) ───────────────────────────────
P = [
    ('Today’s teenagers live in a world full of opportunities, but also full of financial challenges. '
     'Many young people want to be **independent**, make their own decisions, and spend money without asking '
     'their parents. However, real **financial independence** requires not only money, but also '
     '**responsibility** and knowledge.'),
    ('One of the main problems is that most schools do not teach students how to **manage** **personal finances**. '
     'As a result, many teenagers do not know how to **save** money, plan a **budget**, or **avoid debt**. '
     '**Social media** also plays a role. It often **promotes** a **luxurious lifestyle**, expensive **brands**, '
     'and the idea that success means spending a lot. This creates **pressure** and **unrealistic expectations**.'),
    ('To achieve financial independence, young people can start with small but important steps. First, they '
     'should learn basic **financial skills**, for example how to open a **bank account**, **track expenses**, and '
     'set **saving goals**. Second, they can look for **part-time jobs** or online projects that help them '
     '**earn** money and **gain experience**. Finally, teenagers should understand the difference between '
     '**needs** and **wants**. Saving for something **meaningful**, such as education or travel, is more valuable '
     'than buying **unnecessary** things.'),
    ('Financial independence is not about having a lot of money. It’s about being smart, **disciplined**, and '
     '**confident** in how you use it. The earlier young people start developing these **habits**, the more '
     'successful and **secure** their future will be.'),
]
T[15] = [f'{i + 1}.  {p}' for i, p in enumerate(P)]

# ── PART 3 (no step hints) ──────────────────────────────────────────────────
T[21] = 'Task 1   Match each paragraph to its function (A to E). One function is extra.'
T[28] = 'Task 2   Build the logical chain. Fill in the three missing steps with ideas from the text.'
T[29] = ('[A teenager learns basic financial skills]  then  [________]  then  [________]  then  [________]  '
         'then  [The young person feels secure and confident about the future]')
T[30] = 'Task 3   Cause and Effect. Complete each sentence using information from the text.'
T[31] = then_line('Most schools do not teach students how to manage personal finances', 31)
T[32] = then_line('Social media promotes a luxurious lifestyle and expensive brands', 32)
T[33] = then_line('A teenager saves for something meaningful instead of unnecessary things', 33)

# ── PART 4 GLOSSARY (28 units) ──────────────────────────────────────────────
GLOSS = [
    ('independent', 'независимый', 'Able to live and make decisions without help from others.'),
    ('financial independence', 'финансовая независимость', 'Having enough money and skills to pay for your own life.'),
    ('responsibility', 'ответственность', 'Being careful and doing what you must do.'),
    ('manage', 'управлять, распоряжаться', 'To control and organise something, for example money.'),
    ('personal finances', 'личные финансы', 'Your own money, what you get and what you spend.'),
    ('save', 'копить, откладывать', 'To keep money for later and not spend it now.'),
    ('budget', 'бюджет', 'A plan for how you will spend your money.'),
    ('avoid debt', 'избегать долгов', 'To live without borrowing money that you must pay back.'),
    ('social media', 'социальные сети', 'Websites and apps where people share photos, videos, and ideas.'),
    ('promote', 'продвигать, рекламировать', 'To show something as good so that people want it.'),
    ('luxurious lifestyle', 'роскошный образ жизни', 'A way of life with very expensive things.'),
    ('brand', 'бренд, марка', 'The name of a company and its products.'),
    ('pressure', 'давление', 'A strong feeling that you must do something.'),
    ('unrealistic expectations', 'нереалистичные ожидания', 'Hopes that are too high and cannot come true.'),
    ('financial skills', 'финансовые навыки', 'Abilities that help you use money well.'),
    ('bank account', 'банковский счёт', 'A place in a bank where you keep your money.'),
    ('track expenses', 'отслеживать расходы', 'To write down and check all the money you spend.'),
    ('saving goal', 'цель накопления', 'The amount of money you want to save for something.'),
    ('part-time job', 'подработка, работа на неполный день', 'A job for only some hours a day or a week.'),
    ('earn', 'зарабатывать', 'To get money for your work.'),
    ('gain experience', 'получать опыт', 'To learn by doing something in real life.'),
    ('needs and wants', 'потребности и желания', 'Things you must have and things you only would like to have.'),
    ('meaningful', 'значимый, важный', 'Important and useful for your life.'),
    ('unnecessary', 'ненужный', 'Not needed.'),
    ('disciplined', 'дисциплинированный', 'Able to follow your plan and your rules.'),
    ('confident', 'уверенный', 'Sure about yourself and your decisions.'),
    ('habit', 'привычка', 'Something that you do often and regularly.'),
    ('secure', 'надёжный, защищённый', 'Safe and without serious problems.'),
]
assert len(GLOSS) == 28, len(GLOSS)

# ── PART 5 (no word box, longer answers) ────────────────────────────────────
T[88] = 'Put these words into the correct column. Some words can go in two columns. Be ready to explain your choice.'
T[93] = 'Task 2   What is the difference? Write 2 sentences for each pair with an example.'
T[94] = '1.   Needs   and   Wants'
T[95] = '2.   Save   and   Earn'
T[96] = '3.   Budget   and   Track expenses'
T[97] = '4.   Meaningful   and   Unnecessary'
T[98] = 'Task 3   Complete the sentences with the correct word or phrase from the glossary. There is no word box.'
T[99] = 'a)  Bloggers often __________________ expensive brands and a luxurious lifestyle.'
T[100] = 'b)  Pavel works in a café on Saturdays. He earns money and __________________ .'
T[101] = 'c)  If you spend more than you earn, it is difficult to __________________ .'
T[102] = 'd)  Nina writes down every purchase in an app. She wants to __________________ .'
T[103] = 'e)  Many young people feel __________________ because they see rich people online every day.'
T[104] = 'Task 4   Talk about yourself'
T[106] = '1)  How do you manage your money? Do you plan a budget or track expenses? Why?'
T[107] = '2)  What is your saving goal? Why is it meaningful for you?'
T[108] = '3)  Does social media influence what you buy? Give an example.'

# ── PART 6 (more analysis) ──────────────────────────────────────────────────
T[132] = ('Analyse the case. Fill in the table. Write one good habit, one problem, and the glossary words that '
          'describe them.')
T[134] = 'Good habit (glossary words)'
T[135] = 'Problem (glossary words)'
T[139] = ('Give your opinion. Which student is the most financially independent, and which student is the least? '
          'Give 2 reasons for each answer with evidence from the case.')
T[140] = ('Advise Artem and Kira. Write 5 to 6 sentences. Give each of them 2 ideas from the text and explain why '
          'they will help. Use at least 5 words from the glossary.')

# ── PART 7 (counterargument with refutation) ────────────────────────────────
T[142] = '"Social media is the main reason why young people cannot save money."'
T[144] = 'Do you agree or disagree? Write your position in one sentence.'
T[145] = 'Give 2 reasons for your position. Use examples from the text or from your own life.'
T[146] = 'Think of 1 argument against your position. Then explain why your opinion is still correct.'
T[147] = 'Use at least 4 words from the glossary. Try to use because and as a result.'

# ── PART 8 (longer synthesis) ───────────────────────────────────────────────
T[150] = 'Write 6 to 8 sentences answering this question.'
T[151] = 'What does financial independence mean for a young person, and how can he or she achieve it?'
T[152] = 'Cover all three points. Use your own words. Do not copy sentences from the text.'
T[153] = 'Why financial independence is more than having money'
T[154] = 'Which problems make it difficult for teenagers today'
T[155] = 'Which steps you would recommend and why, with an example from your life'

# ── PART 9 (less support) ───────────────────────────────────────────────────
T[159] = ('Speak for 2 minutes. Explain what financial independence is, name 2 problems, and give 3 steps '
          'from the text with reasons.')
T[160] = 'Use linking words (First..., As a result..., However..., Finally...).'
T[161] = ('Requirements   Use 6 or more words from the glossary   •   Full sentences only   •   '
          'Speak without reading your notes')
T[164] = ('"Financial independence means having a lot of money. Most schools teaches students how to manage '
          'personal finances. Social media promotes a simple lifestyle. Buying unnecessary things is more '
          'valuable than saving for education."')
T[167] = 'Use all 6 words below to talk about youth and money without notes. Connect them in a logical order.'
T[168] = 'Words   pressure   unrealistic expectations   track expenses   saving goal   disciplined   as a result'
T[172] = ('Student A asks at least 4 questions about the client’s income, expenses, debts, and saving goal. '
          'Student B answers. Student A gives 3 tips and explains them.')
T[174] = 'Requirements   Use 6 glossary words each   •   Be polite   •   Ask and answer follow-up questions'
T[175] = 'Option 5   Product   My Saving Plan||   [20 min, then 2 min presentation]'
T[176] = ('Make a presentation (5 to 6 slides) or a dashboard (Excel or Google Sheets) called "My Saving Plan" '
          'for the next three months.')
T[177] = ('Show your monthly income and expenses, a chart that compares needs and wants, a saving goal with the '
          'amount, and how many months you need to reach it. Add 3 steps from the text that you will follow. '
          'Present your product to the group in 2 minutes.')
T[178] = ('Requirements   Correct calculation of the saving period   •   One chart   •   '
          '6 glossary words on the slides or in the dashboard')

# ── LANGUAGE TIPS (more complex) ────────────────────────────────────────────
T[198] = 'To give an opinion'
T[199] = 'In my opinion, ...'
T[200] = 'I partly agree, but ...'
T[201] = 'On the one hand ..., on the other hand ...'
T[202] = 'The main reason is that ...'
T[203] = 'To show cause and result'
T[204] = '... because ...'
T[205] = 'As a result, ...'
T[206] = 'That is why ...'
T[207] = 'If ..., young people will ...'

# ── PEER ASSESSMENT ─────────────────────────────────────────────────────────
T[213] = '1. Vocabulary. Used 5 or more words from the glossary correctly'
T[217] = '3. Reasons. Gave reasons and examples, used because and as a result'

for k, v in T.items():
    vals = v if isinstance(v, list) else [v]
    for x in vals:
        if isinstance(x, str):
            assert '—' not in x, k
build(TPL, T, OUT, glossary=GLOSS, glossary_widths=[2700, 2900, 3760])
