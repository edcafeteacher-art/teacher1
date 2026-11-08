"""The Role of English in the Modern World  |  CEFR B1  |  Year 2 Finance (F2)  |  Hobbies design.
Text = source text unchanged (4 paragraphs), only the em-dash replaced and glossary terms bolded.
Glossary = all 35 source units with source translations (ё restored) + B1 English definitions."""
import sys, pathlib
SKILL = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))

import subprocess, re
from hob_fill import build, original_texts, DELETE

TPL = str(SKILL / 'assets' / 'hobbies_template.docx')
SRC = sys.argv[1]   # path to the teacher's source .docx with the original text
OUT = str(pathlib.Path.cwd() / 'The_Role_of_English_F2_B1_Finance.docx')

orig = original_texts(TPL)
T = {}

def dash_label(i):
    return orig[i].replace(' — ', '   ').rstrip()

def then_line(prefix, idx):
    return prefix + orig[idx][orig[idx].index('  then  '):]

# ── SOURCE TEXT ─────────────────────────────────────────────────────────────
src = subprocess.run(['pandoc', '-t', 'plain', '--wrap=none', SRC], capture_output=True, text=True).stdout
src_paras = [l.strip() for l in src.splitlines() if l.strip()]
start = next(i for i, l in enumerate(src_paras) if l.startswith('In the twenty-first century'))
TEXT = src_paras[start:start + 4]
assert TEXT[3].startswith('Today, English in finance'), TEXT[3][:40]
assert TEXT[2].count(' — ') == 1
TEXT[2] = TEXT[2].replace(' — ', ', ')

BOLD = [  # (paragraph, exact phrase in the source text)
    (0, 'global language'), (0, 'professional and intellectual growth'), (0, 'academic exchange'),
    (0, 'strategic skill'), (0, 'competitiveness'), (0, 'international job market'),
    (1, 'data-driven'), (1, 'common code for communication'), (1, 'investment companies'),
    (1, 'digital finance platforms'), (1, 'International Monetary Fund (IMF)'),
    (1, 'London Stock Exchange (LSE)'), (1, 'fintech corporations'), (1, 'financial statements (IFRS)'),
    (1, 'credit rating reports'), (1, 'cryptocurrency analytics'), (1, 'online training programs'),
    (1, 'Chartered Financial Analyst (CFA)'), (1, 'ACCA'), (1, 'professional mindset'), (1, 'global standards'),
    (2, 'transparency'), (2, 'unification'), (2, 'digital innovation'), (2, 'linguistic inequality'),
    (2, 'native speakers'), (2, 'global discourse'), (2, 'intercultural nuances'), (2, 'financial communication'),
    (3, 'medium of exchange'), (3, 'medium of thought'), (3, 'interpret global trends'),
    (3, 'analyze financial risks'), (3, 'shaping the economic future'), (3, 'international financial dialogue'),
]
for k, phrase in BOLD:
    assert TEXT[k].count(phrase) >= 1, phrase
    TEXT[k] = TEXT[k].replace(phrase, f'**{phrase}**', 1)

# ── HEADER ──────────────────────────────────────────────────────────────────
T[0] = 'The Role of English in the Modern World'
T[1] = 'Its Connection with My Future Profession as a Financier'
T[2] = '90 min   •   Level B1   •   Year 2   •   Finance'

# ── PART 1 PROBLEM CASE ─────────────────────────────────────────────────────
T[3] = 'PART 1   PROBLEM CASE'
T[5] = ('You are a second-year finance student. Your college has a partnership with an international fintech '
        'company, and two students from your group can join a short online internship. The internship is in '
        'English, and all documents, reports, and meetings are in English too.')
T[6] = ('The internship coordinator says, "Our analysts read financial statements under IFRS, follow global '
        'credit rating reports, and discuss risks with colleagues from different countries. We need people who '
        'can think in English, not only translate."')
T[7] = ('Your classmate Denis says, "My English is enough for tests. All the reports I need are in Russian." '
        'Another classmate, Polina, says, "I study English online every day, because I want to take the CFA '
        'exam one day."')
T[9] = 'Discuss with a partner. Give your opinion with 2 reasons. Then make a prediction.'
T[10] = 'Is Denis right that English for tests is enough for a financier in Russia? Give 2 reasons for your answer.'
T[11] = 'Polina wants to take the CFA exam. Which resources in English will she need? Name 2 and explain why.'
T[12] = ('Predict. How can English help a Russian financier in five years, when finance becomes even more '
         'digital? Give 1 idea.')
T[13] = 'Share your ideas with the group (2 minutes).'

# ── PART 2 TEXT (4 source paragraphs, 5th slot removed) ─────────────────────
for k in range(4):
    T[15 + k] = TEXT[k]
T[19] = DELETE

# ── PART 3 TEXT STRUCTURE ───────────────────────────────────────────────────
T[21] = 'Task 1   Match each paragraph to its function (A to E). One function is extra.'
T[22] = 'A.   The problems that the spread of English can create and how students can respond'
T[23] = 'B.   Why English is a strategic skill for students who want a career in finance'
T[24] = 'C.   How English changes the way future financiers think and act'
T[25] = 'D.   How to choose the best English course for a finance student'
T[26] = 'E.   Which global institutions and professional resources depend on English'
T[27] = ('Paragraph 1 is ____     Paragraph 2 is ____     Paragraph 3 is ____     '
         'Paragraph 4 is ____     The extra function is ____')
T[28] = 'Task 2   Build the logical chain. Fill in the three missing steps with ideas from the text.'
T[29] = ('[A finance student masters professional English]  then  [________]  then  [________]  then  '
         '[________]  then  [The specialist takes part in the international financial dialogue]')
T[30] = 'Task 3   Cause and Effect. Complete each sentence using information from the text.'
T[31] = then_line('English functions as the common code for communication in finance', 31)
T[32] = then_line('A Russian financier reads credit rating reports and IFRS statements in English', 32)
T[33] = then_line('English gives an advantage to native speakers', 33)

# ── PART 4 GLOSSARY (all 35 source units) ───────────────────────────────────
T[34] = 'PART 4   VOCABULARY GLOSSARY'
GLOSS = [
    ('global language', 'мировой язык',
     'A language that people in many countries use for business, science, and education.'),
    ('professional and intellectual growth', 'профессиональное и интеллектуальное развитие',
     'The development of your work skills and of your ability to think.'),
    ('academic exchange', 'академический обмен',
     'Sharing knowledge and ideas between students, scientists, and universities of different countries.'),
    ('international job market', 'международный рынок труда',
     'All the jobs that are open to specialists from different countries.'),
    ('strategic skill', 'стратегический навык',
     'An important ability that helps you reach long-term career goals.'),
    ('competitiveness', 'конкурентоспособность',
     'The ability of a person or a company to be more successful than others.'),
    ('data-driven world', 'мир, основанный на данных',
     'A world where people make decisions after they analyse data.'),
    ('common code for communication', 'общий код коммуникации',
     'A shared language that all participants understand in the same way.'),
    ('digital finance platforms', 'цифровые финансовые платформы',
     'Online services and apps for payments, loans, and investments.'),
    ('investment companies', 'инвестиционные компании',
     'Companies that invest money for their clients to make a profit.'),
    ('financial institutions', 'финансовые институты',
     'Organisations that work with money, such as banks and insurance companies.'),
    ('International Monetary Fund (IMF)', 'Международный валютный фонд (МВФ)',
     'An international organisation that supports the stability of the world financial system.'),
    ('London Stock Exchange (LSE)', 'Лондонская фондовая биржа',
     'One of the oldest and largest stock exchanges in the world, located in the UK.'),
    ('fintech corporations', 'финтех-компании',
     'Large companies that use technology to provide financial services.'),
    ('financial statements (IFRS)', 'финансовая отчётность (МСФО)',
     'Official reports on a company’s finances prepared under international standards.'),
    ('credit rating reports', 'отчёты кредитных рейтингов',
     'Reports that show how likely a borrower is to pay back its debts.'),
    ('cryptocurrency analytics', 'аналитика криптовалют',
     'The study of data about digital currencies and their markets.'),
    ('online training programs', 'онлайн-программы обучения',
     'Courses that you take on the internet.'),
    ('Chartered Financial Analyst (CFA)', 'Дипломированный финансовый аналитик (CFA)',
     'An international qualification for investment and financial analysts.'),
    ('Association of Chartered Certified Accountants (ACCA)',
     'Ассоциация дипломированных сертифицированных бухгалтеров (ACCA)',
     'A global professional body that gives an international qualification to accountants.'),
    ('professional mindset', 'профессиональное мышление',
     'The way a specialist thinks, makes decisions, and behaves at work.'),
    ('global standards', 'международные стандарты',
     'Rules and norms that many countries accept and use.'),
    ('transparency and unification', 'прозрачность и унификация',
     'Open access to information and the use of the same rules and terms.'),
    ('digital innovation', 'цифровые инновации',
     'New technologies and ideas that change how services work.'),
    ('linguistic inequality', 'языковое неравенство',
     'A situation where some people have fewer chances because of the language they speak.'),
    ('native speakers', 'носители языка',
     'People who learned a language as their first language in childhood.'),
    ('global discourse', 'глобальный дискурс',
     'The international discussion of important topics.'),
    ('intercultural nuances', 'межкультурные нюансы',
     'Small differences in how people from different cultures communicate.'),
    ('financial communication', 'финансовая коммуникация',
     'The exchange of financial information between specialists, companies, and clients.'),
    ('medium of exchange', 'средство обмена',
     'Something that people use to exchange goods, services, or information.'),
    ('medium of thought', 'средство мышления',
     'A tool that people use to think and to form ideas.'),
    ('interpret global trends', 'интерпретировать мировые тенденции',
     'To explain what changes in the world economy mean.'),
    ('analyze financial risks', 'анализировать финансовые риски',
     'To study possible losses before you make a financial decision.'),
    ('shaping the economic future', 'формирование экономического будущего',
     'Influencing how the economy will develop.'),
    ('international financial dialogue', 'международный финансовый диалог',
     'Communication and cooperation between financial specialists of different countries.'),
]
assert len(GLOSS) == 35
for i in range(38, 86):          # template glossary cells are rebuilt from GLOSS
    T[i] = None

# ── PART 5 VOCABULARY ACTIVATION ────────────────────────────────────────────
T[87] = 'Task 1   Categorisation'
T[88] = 'Put these words and phrases into the correct column. Be ready to explain your choice.'
T[89] = ('International Monetary Fund   •   London Stock Exchange   •   fintech corporations   •   investment companies'
         '   •   financial statements (IFRS)   •   credit rating reports   •   CFA   •   ACCA   •   professional mindset'
         '   •   strategic skill   •   intercultural nuances   •   analyze financial risks')
T[90] = 'Institutions and companies'
T[91] = 'Resources and qualifications'
T[92] = 'Skills and ways of thinking'
T[93] = dash_label(93)
T[94] = '1.   Medium of exchange   and   Medium of thought'
T[95] = '2.   Transparency   and   Unification'
T[96] = '3.   Linguistic inequality   and   Competitiveness'
T[97] = '4.   Global discourse   and   Financial communication'
T[98] = 'Task 3   Complete the sentences with the correct word or phrase from the glossary.'
T[99] = 'a)  Revolut and PayPal are examples of __________________ that provide financial services online.'
T[100] = 'b)  Analysts study __________________ to see how reliable a borrower or a company is.'
T[101] = ('c)  Companies that publish __________________ follow the same global standards, so investors '
          'can compare them.')
T[102] = ('d)  Good professional English increases a young financier’s __________________ on the '
          'international job market.')
T[103] = ('e)  When you talk to foreign partners, you must notice __________________ , not only the meaning '
          'of words.')
T[104] = dash_label(104)
T[106] = '1)  Which English resources (courses, reports, news) do you use for your studies? Why?'
T[107] = ('2)  What is the most difficult part of professional English for you, vocabulary, logic, or '
          'intercultural nuances? Explain.')
T[108] = '3)  Would you like to get an international qualification such as CFA or ACCA? Why or why not?'

# ── PART 6 ANALYTICAL TASK ──────────────────────────────────────────────────
T[110] = 'Case   Three Classmates, Three Ways to Use English'
T[111] = 'Read the information about three finance students. Then complete the tasks below.'
T[112] = 'Denis, 19'
T[113] = 'Polina, 19'
T[114] = 'Arina, 20'
T[115] = 'Uses English only for college tests'
T[116] = 'Reads financial news only in Russian'
T[117] = 'Plans to work in a local bank branch'
T[118] = 'Has never taken an online course in English'
T[119] = 'Says "Russian reports are enough for my job."'
T[120] = 'Takes online training programs in English'
T[121] = 'Reads credit rating reports to practise'
T[122] = 'Plans to take the CFA exam'
T[123] = 'Says "English helps me analyze financial risks."'
T[124] = 'Finds intercultural nuances difficult'
T[125] = 'Works part-time at a fintech start-up'
T[126] = 'Uses English on digital finance platforms every day'
T[127] = 'Writes short reports for foreign partners'
T[128] = 'Says "English is my medium of thought at work."'
T[129] = 'Wants to work in an investment company.'
T[132] = ('Analyse the case. Fill in the table below. Write how each student uses English and which skill or '
          'resource from the glossary it develops.')
T[133] = 'Student'
T[134] = 'How they use English'
T[135] = 'Skill or resource from the glossary'
T[136], T[137], T[138] = 'Denis', 'Polina', 'Arina'
T[139] = ('Give your opinion. Which student is the most competitive on the international job market? '
          'Give 2 reasons with evidence from the case. Use the words because and competitiveness in your answer.')
T[140] = ('Advise Denis. Write 4 to 5 sentences. Suggest 2 English resources from the text and explain how each '
          'one will help his career. Use at least 4 words from the glossary.')

# ── PART 7 CRITICAL THINKING ────────────────────────────────────────────────
T[142] = '"The dominance of English in finance gives an unfair advantage to native speakers."'
T[143] = dash_label(143)
T[145] = 'Give 2 reasons for your position. Use examples from the text or from your own experience.'
T[147] = ('Use at least 4 words from the glossary, for example linguistic inequality, global discourse, '
          'transparency. Try to use because in every reason.')

# ── PART 8 SYNTHESIS ────────────────────────────────────────────────────────
T[149] = dash_label(149)
T[150] = 'Write 6 to 8 sentences answering this question.'
T[151] = 'How is English connected with my future profession as a financier?'
T[153] = 'What resources and opportunities English opens for a financier in Russia'
T[154] = 'What problems the dominance of English can create and how a student can deal with them'
T[155] = 'How you plan to develop your professional English in the next two years'

# ── PART 9 PROFESSIONAL OUTPUT ──────────────────────────────────────────────
T[156] = 'PART 9   PROFESSIONAL OUTPUT   CHOOSE ONE'
T[157] = 'Option 1   Short Presentation||   [2 min]'
T[158] = ('Imagine you are at an interview for an internship at an international fintech company. '
          'The interviewer asks, "Why is English important for your career in finance?"')
T[159] = ('Answer in 2 minutes. Give 3 reasons and support each one with an example from the text '
          '(an institution, a resource, or a qualification).')
T[160] = 'Use the language from the Language tips (I am convinced that..., On the one hand..., That is why...).'
T[161] = ('Requirements   Use 5 or more words from the glossary   •   3 reasons with examples   •   '
          'Speak without reading your notes')
T[162] = 'Option 2   Error Finding||   [3 min]'
T[163] = ('A student wrote this paragraph. Find 4 mistakes (grammar, word choice, or ideas that are wrong based on '
          'the text). Write the correct version for each mistake.')
T[164] = ('"English is a temporary skill for financiers. The IMF and the London Stock Exchange relies on many '
          'languages in their documentation. CFA programs are available mostly in English. English makes global '
          'discourse more inclusive for everyone."')
T[165] = ('Requirements   Find 4 mistakes   •   Write the correct sentence for each one   •   '
          'Explain why it is wrong in 1 short sentence')
T[166] = 'Option 3   Keyword Speaking||   [2 min]'
T[167] = ('Use all 6 words below to talk about English in finance without notes. Connect them in a logical order. '
          'Talk for 2 minutes.')
T[168] = ('Words   strategic skill   global standards   transparency   linguistic inequality   '
          'professional mindset   because')
T[169] = 'Requirements   Use all 6 words correctly   •   Speak in full sentences   •   No reading from notes'
T[170] = 'Option 4   Mini Debate||   [4 min (2 plus 2)]'
T[171] = 'Statement   "One global language makes finance more transparent and more fair."'
T[172] = ('Student A argues FOR the statement. Student B argues AGAINST it. Each person speaks for 2 minutes. '
          'Use examples from the text.')
T[173] = 'The class votes for the most convincing argument and gives 1 reason.'
T[174] = ('Requirements   Use at least 4 glossary words each   •   2 arguments each   •   '
          'Listen and respond to your partner')
T[175] = 'Option 5   Partner Dialogue||   [3 min, pairs]'
T[176] = ('You are a financial analyst at a Russian bank. Your new partner from Singapore says, "We expect '
          'transparency in all transactions, so we follow global standards."')
T[177] = ('Continue the dialogue in pairs (6 to 8 lines). Explain how your bank works with international documents '
          'and why English matters for this partnership.')
T[178] = ('Requirements   Use 5 or more glossary words   •   6 to 8 lines   •   Polite and professional tone')

# ── SPEAKING PRACTICE ───────────────────────────────────────────────────────
T[179] = 'SPEAKING PRACTICE   DISCUSSION QUESTIONS'
QS = [
    'Why has English become the global language of business?',
    'Is English a strategic skill or just a college subject for you?',
    'Which international institutions use English in their work?',
    'Do you read any financial news or reports in English?',
    'Would you like to work for a fintech corporation? Why?',
    'Which online training programs in English do you know?',
    'Is it fair that native speakers have an advantage in finance?',
    'How can a student overcome linguistic inequality?',
    'What does a professional mindset mean for a financier?',
    'Why are global standards important for investors?',
    'Which intercultural nuances can be important in business?',
    'Is cryptocurrency analytics a useful skill? Why?',
    'How can English help you analyze financial risks?',
    'Would you prefer to work in Russia or abroad? Why?',
    'What does "English is a medium of thought" mean for you?',
    'How will you develop your professional English after college?',
]
for i, s in enumerate(QS):
    T[181 + i] = s

# ── LANGUAGE TIPS ───────────────────────────────────────────────────────────
T[198] = 'To express your position'
T[199] = 'I am convinced that ...'
T[200] = 'In my opinion, ... because ...'
T[201] = 'On the one hand ..., on the other hand ...'
T[202] = 'I partly agree, but ...'
T[203] = 'To show cause and result'
T[204] = '... that is why ...'
T[205] = 'As a result, ...'
T[206] = 'This allows financiers to ...'
T[207] = 'This leads to ...'

# ── PEER ASSESSMENT ─────────────────────────────────────────────────────────
T[213] = '1. Vocabulary. Used 5 or more words from the glossary correctly'
T[215] = '2. Structure. Had a clear beginning, middle, and end'
T[217] = '3. Evidence. Supported ideas with examples from the text'
T[219] = '4. Task completion. Answered all parts of the task'
T[221] = '5. Clarity. Spoke or wrote in full sentences, easy to understand'

assert len(orig) == 227
build(TPL, T, OUT, glossary=GLOSS)
