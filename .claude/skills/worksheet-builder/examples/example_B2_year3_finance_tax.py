"""PZ 42  Russian Tax System, Tax Accounting and Reporting, Filing a Return, Auditor Role Play
CEFR B2  |  Year 3 Finance (38.02.06)  |  Hobbies design (template engine hob_fill).
Facts checked Oct 2026: VAT 22% from 1 Jan 2026 (Federal Law 425-FZ of 28.11.2025), 10% reduced rate kept;
USN VAT exemption up to 20 mln RUB income of previous year, 5% / 7% reduced VAT rates for USN;
NDFL progressive scale 13-22% since 2025; ENS since 2023; USN return 25 March (companies) / 25 April (IE);
VAT return quarterly by the 25th, electronic only, tax paid in 3 equal parts; 3-NDFL by 30 April;
late filing penalty 5% per month of unpaid tax (art. 119 Tax Code)."""
import sys, pathlib
SKILL = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))

from hob_fill import build, original_texts

TPL = str(SKILL / 'assets' / 'hobbies_template.docx')
OUT = str(pathlib.Path.cwd() / 'PZ42_Tax_System_B2_Year3_Finance.docx')
orig = original_texts(TPL)
T = {}

def dash_label(i):
    return orig[i].replace(' — ', '   ').rstrip()

def then_line(prefix, idx):
    return prefix + orig[idx][orig[idx].index('  then  '):]

# ── HEADER ──────────────────────────────────────────────────────────────────
T[0] = 'The Russian Tax System'
T[1] = 'Tax Accounting, Reporting, and Filing a Tax Return'
T[2] = 'Practical Session 42   •   90 min   •   Level B2   •   Year 3   •   Finance'

# ── PART 1 PROBLEM CASE ─────────────────────────────────────────────────────
T[5] = ('You are a junior tax specialist at Volga Print LLC, a fictional printing company in Kazan that applies '
        'the simplified tax system. In 2025 the company’s income grew to 24 million roubles, so from 1 January '
        '2026 it is no longer exempt from VAT. The finance director has invited an external auditor to review the '
        'company’s tax position before the next reporting deadline.')
T[6] = ('The auditor says, "Your bookkeeping is accurate, but your tax accounting has not caught up with the new '
        'rules. If you choose the wrong VAT option or miss a filing deadline, the company may face penalties and '
        'even a blocked bank account."')
T[7] = ('The chief accountant, Maxim, says, "Let us choose the reduced 5 percent rate and keep things simple." '
        'The finance director, Irina, replies, "Perhaps the standard rate is better, because we buy a lot of '
        'expensive paper and equipment and could deduct input VAT."')
T[9] = 'Discuss with a partner. Give your opinion with 2 reasons. Then make a prediction.'
T[10] = 'Whose position, Maxim’s or Irina’s, seems more reasonable at first sight? Give 2 reasons.'
T[11] = 'Which tax risks can a company face when its tax obligations change? Name 2 and explain why.'
T[12] = 'Predict. What will the auditor recommend to reduce the company’s tax risks? Give 1 idea.'
T[13] = 'Share your ideas with the group (2 minutes).'

# ── PART 2 TEXT ─────────────────────────────────────────────────────────────
T[15] = ('The Russian tax system is based on the **Tax Code** of the Russian Federation, which sets out the rules '
         'for every tax, the rights and obligations of taxpayers, and the powers of the tax authorities. Taxes are '
         'divided into three levels. **Federal taxes**, such as **value added tax (VAT)**, corporate income tax, and '
         'personal income tax, apply across the whole country. **Regional taxes**, such as the corporate property '
         'tax, and **local taxes**, such as the land tax, are introduced by regional and municipal authorities '
         'within the limits of the Tax Code. Every tax has the same basic elements, namely a **taxpayer**, a '
         '**tax base**, a **tax rate**, and a tax period. The **Federal Tax Service (FNS)** collects taxes, checks '
         'returns, and runs online services for companies and individuals.')
T[16] = ('Every business works under a particular **tax regime**. Under the **general tax regime**, a company '
         'pays corporate income tax and VAT. Since 1 January 2026 the standard VAT rate has been 22 percent, while a '
         'reduced rate of 10 percent still applies to certain goods, for example some food products and children’s '
         'goods. Small and medium-sized businesses often prefer the **simplified tax system (USN)**, which replaces '
         'corporate income tax with a single tax on income or on income minus expenses. In 2026 a company on USN '
         'is exempt from VAT if its income for the previous year did not exceed 20 million roubles. Above this '
         'threshold it pays VAT at a reduced rate of 5 or 7 percent without deductions, or at the standard rate '
         'with the right to deduct **input VAT**. Individuals pay **personal income tax** under a progressive '
         'scale from 13 to 22 percent.')
T[17] = ('**Tax accounting** is not the same as bookkeeping. Financial accounting shows the company’s financial '
         'position to owners and investors, while tax accounting collects the data needed to calculate the tax '
         'base correctly. Accountants record every transaction on the basis of **primary documents**, such as '
         'invoices, contracts, and acts of acceptance, and summarise the data in **tax registers**. At the end of '
         'each tax period, the company prepares a **tax return**, which is an official statement of the tax base '
         'and the amount of tax due. Since 2023 most taxes have been paid through a **single tax account (ENS)**. '
         'The company transfers one **single tax payment**, and the FNS distributes the money between taxes. When '
         'a tax must be paid before the return is filed, the company sends a **notification of calculated tax**.')
T[18] = ('The filing process depends on the tax. A company on USN files its annual return by 25 March, and an '
         'individual entrepreneur by 25 April of the following year, while **advance payments** are made every '
         'quarter. A VAT return is filed every quarter by the 25th day of the following month, and only in '
         'electronic form through an operator of **electronic document flow**. The tax itself is paid in three '
         'equal instalments over the next three months. An individual who sold property or received income from '
         'abroad files form 3-NDFL by 30 April, usually through the **taxpayer’s personal account** on the FNS '
         'website, while a person who only claims a **tax deduction** can file it later in the year. After filing, '
         'the tax authority carries out a **desk tax audit** of the return. If a return is late, the taxpayer may '
         'pay a **penalty** of 5 percent of the unpaid tax for each month of delay.')
T[19] = ('Mistakes in tax accounting create **tax risks**, that is, the possibility of additional tax, **late '
         'payment interest**, and penalties after a tax audit. Typical sources of risk are a wrong VAT rate, missing '
         'primary documents, unreliable suppliers, and missed deadlines. That is why companies invite an independent '
         '**auditor**, who examines the accounts and gives an opinion on whether they are reliable. In a discussion '
         'with the client, the auditor identifies weak points and suggests a **risk mitigation strategy**, which may '
         'include internal controls, a **tax calendar**, regular checks of counterparties, and staff training. '
         'Reducing tax risk does not mean paying less tax at any price. **Tax optimisation** is legal only when it '
         'uses the options that the law provides, while **tax evasion** can be a criminal offence.')

# ── PART 3 TEXT STRUCTURE ───────────────────────────────────────────────────
T[21] = dash_label(21)
T[22] = 'A.   Sources of tax risk and the role of an independent auditor'
T[23] = 'B.   The structure of the tax system and the basic elements of every tax'
T[24] = 'C.   Deadlines and procedures for filing different tax returns'
T[25] = 'D.   The choice of a tax regime and the main tax rates in 2026'
T[26] = 'E.   The difference between bookkeeping and tax accounting, and how taxes are paid'
T[28] = 'Task 2   Build the logical chain. Fill in the three missing steps with ideas from the text.'
T[29] = ('[A business transaction takes place]  then  [________]  then  [________]  then  [________]  then  '
         '[The tax authority carries out a desk tax audit]')
T[30] = dash_label(30)
T[31] = then_line('A company on USN earned more than 20 million roubles last year', 31)
T[32] = then_line('A company sends its VAT return to the tax office on paper', 32)
T[33] = then_line('A company files its tax return two months late', 33)

# ── PART 4 GLOSSARY (32 units) ──────────────────────────────────────────────
GLOSS = [
    ('Tax Code', 'Налоговый кодекс',
     'The main law that sets out the rules for all taxes in Russia.'),
    ('federal, regional, and local taxes', 'федеральные, региональные и местные налоги',
     'The three levels of taxes, set for the whole country, a region, or a municipality.'),
    ('taxpayer', 'налогоплательщик',
     'A company or a person who is legally obliged to pay a tax.'),
    ('tax base', 'налоговая база',
     'The amount, such as income or the value of property, on which a tax is calculated.'),
    ('tax rate', 'налоговая ставка',
     'The percentage of the tax base that must be paid as tax.'),
    ('Federal Tax Service (FNS)', 'Федеральная налоговая служба (ФНС)',
     'The government body that collects taxes and controls how taxpayers meet their obligations.'),
    ('tax regime', 'режим налогообложения',
     'A set of rules that defines which taxes a business pays and how.'),
    ('general tax regime', 'общая система налогообложения (ОСНО)',
     'The standard regime under which a company pays corporate income tax and VAT.'),
    ('simplified tax system (USN)', 'упрощённая система налогообложения (УСН)',
     'A special regime for small and medium-sized businesses with one tax instead of several.'),
    ('value added tax (VAT)', 'налог на добавленную стоимость (НДС)',
     'An indirect tax on goods and services that is included in the price.'),
    ('input VAT', 'входящий НДС',
     'VAT that a company pays to its suppliers and may deduct from its own VAT.'),
    ('personal income tax', 'налог на доходы физических лиц (НДФЛ)',
     'A tax on the income of individuals, such as salaries or income from selling property.'),
    ('tax accounting', 'налоговый учёт',
     'The collection of data that a company needs to calculate its taxes correctly.'),
    ('primary documents', 'первичные учётные документы',
     'Documents that confirm a business transaction, such as invoices and contracts.'),
    ('tax register', 'налоговый регистр',
     'A table or form where tax accounting data is grouped and summarised.'),
    ('tax return', 'налоговая декларация',
     'An official statement of the tax base and the amount of tax due for a period.'),
    ('single tax account (ENS)', 'единый налоговый счёт (ЕНС)',
     'One account through which a taxpayer pays most taxes and contributions.'),
    ('single tax payment', 'единый налоговый платёж (ЕНП)',
     'One transfer of money to the single tax account to cover several taxes.'),
    ('notification of calculated tax', 'уведомление об исчисленных суммах налогов',
     'A message that tells the FNS how much tax is due before the return is filed.'),
    ('advance payment', 'авансовый платёж',
     'A part of the annual tax that is paid during the year, usually every quarter.'),
    ('electronic document flow', 'электронный документооборот (ЭДО)',
     'The exchange of official documents in electronic form with an electronic signature.'),
    ('tax deduction', 'налоговый вычет',
     'An amount that reduces the tax base or the tax, for example after buying a flat.'),
    ('taxpayer’s personal account', 'личный кабинет налогоплательщика',
     'An online service on the FNS website where taxpayers file returns and see their taxes.'),
    ('desk tax audit', 'камеральная налоговая проверка',
     'A check of a tax return that the tax office carries out without visiting the company.'),
    ('penalty', 'штраф',
     'A fixed sum of money that a taxpayer pays for breaking tax rules.'),
    ('late payment interest', 'пени',
     'An extra amount charged for each day that a tax is paid late.'),
    ('tax risk', 'налоговый риск',
     'The possibility of additional tax, interest, or penalties after a tax audit.'),
    ('auditor', 'аудитор',
     'An independent specialist who checks a company’s accounts and gives an opinion on them.'),
    ('risk mitigation strategy', 'стратегия снижения рисков',
     'A plan of measures that reduce the probability or the impact of risks.'),
    ('tax optimisation', 'налоговая оптимизация',
     'Legal ways to reduce the tax burden by using options that the law provides.'),
    ('tax evasion', 'уклонение от уплаты налогов',
     'Illegal actions to avoid paying taxes, such as hiding income.'),
    ('tax calendar', 'налоговый календарь',
     'A schedule of all tax deadlines for filing returns and making payments.'),
]
assert len(GLOSS) == 32

# ── PART 5 VOCABULARY ACTIVATION ────────────────────────────────────────────
T[87] = 'Task 1   Categorisation'
T[88] = 'Put these terms into the correct column. Some terms can go in more than one column. Be ready to explain.'
T[89] = ('VAT   •   personal income tax   •   simplified tax system   •   general tax regime   •   primary documents'
         '   •   tax register   •   tax return   •   single tax payment   •   desk tax audit   •   penalty'
         '   •   late payment interest   •   risk mitigation strategy')
T[90] = 'Taxes and regimes'
T[91] = 'Accounting and reporting'
T[92] = 'Control and risk'
T[93] = 'Task 2   What is the difference? Write 1 to 2 sentences for each pair.'
T[94] = '1.   Tax optimisation   and   Tax evasion'
T[95] = '2.   Bookkeeping   and   Tax accounting'
T[96] = '3.   Penalty   and   Late payment interest'
T[97] = '4.   Tax return   and   Notification of calculated tax'
T[98] = 'Task 3   Complete the sentences with the correct term from the glossary.'
T[99] = 'a)  Since 2026 the standard __________________ rate in Russia has been 22 percent.'
T[100] = ('b)  The company transfers money to its __________________ , and the FNS distributes it between '
          'taxes.')
T[101] = ('c)  Before the return is filed, the company sends a __________________ so that the FNS knows how '
          'much tax is due.')
T[102] = 'd)  After a return is filed, an inspector checks it during a __________________ .'
T[103] = 'e)  A taxpayer who has bought a flat can claim a property __________________ .'
T[104] = 'Task 4   Your experience and views'
T[105] = 'Answer these questions in full sentences. Write your answers below, then discuss them with a partner.'
T[106] = '1)  Have you or your family ever filed a tax return or claimed a tax deduction? What was the process like?'
T[107] = '2)  Which tax regime would you choose if you started a small business? Why?'
T[108] = '3)  Which qualities does a good tax accountant need? Explain with examples.'

# ── PART 6 ANALYTICAL TASK ──────────────────────────────────────────────────
T[110] = 'Case   Three Taxpayers, Three Tax Risks'
T[111] = 'Read the information about three taxpayers. Then complete the tasks below.'
T[112] = 'Volga Print LLC'
T[113] = 'Anna Lebedeva, IE'
T[114] = 'Nord Trade LLC'
T[115] = 'Applies USN, income in 2025 was 24 million roubles'
T[116] = 'Buys expensive paper and equipment with VAT'
T[117] = 'Main clients are large companies that pay VAT'
T[118] = 'Has no tax calendar'
T[119] = 'Chief accountant says "Let us just choose 5 percent."'
T[120] = 'Designer, applies USN on income'
T[121] = 'Pays advance payments on time through ENS'
T[122] = 'Forgot to send two notifications of calculated tax'
T[123] = 'Says "I paid on time, so there is no problem."'
T[124] = 'Sold a flat that she had owned for two years'
T[125] = 'Wholesale company on the general tax regime'
T[126] = 'Files VAT returns through electronic document flow'
T[127] = 'Deducted input VAT from a new supplier with no staff and no warehouse'
T[128] = 'Says "The invoice is correct, so the deduction is safe."'
T[129] = 'Received a request from the FNS during a desk tax audit'
T[132] = ('Analyse the case. Fill in the table below. Identify the main tax risk of each taxpayer and suggest one '
          'action that reduces it.')
T[133] = 'Taxpayer'
T[134] = 'Main tax risk'
T[135] = 'Recommended action'
T[136], T[137], T[138] = 'Volga Print', 'Anna Lebedeva', 'Nord Trade'
T[139] = ('Give your opinion. Which taxpayer faces the most serious tax risk? Give 2 reasons with evidence from the '
          'case and the text.')
T[140] = ('Advise Volga Print. Write 5 to 6 sentences comparing the 5 percent rate and the standard VAT rate for '
          'this company. Recommend one option and explain its risks. Use at least 5 words from the glossary.')

# ── PART 7 CRITICAL THINKING ────────────────────────────────────────────────
T[142] = '"If a company pays all its taxes on time, tax risk management is a waste of money."'
T[143] = dash_label(143)
T[145] = 'Give 2 reasons for your position. Use evidence from the text and the case.'
T[147] = ('Use at least 5 words from the glossary, for example tax risk, penalty, auditor, risk mitigation '
          'strategy.')

# ── PART 8 SYNTHESIS ────────────────────────────────────────────────────────
T[149] = dash_label(149)
T[150] = 'Write 8 to 10 sentences answering this question.'
T[151] = 'How can a finance specialist help a company to report its taxes correctly and reduce tax risks?'
T[153] = 'How the tax system and the choice of a tax regime shape a company’s tax obligations'
T[154] = 'How tax accounting and filing a return work for USN, VAT, or personal income tax (choose one)'
T[155] = 'Which measures of a risk mitigation strategy you consider most effective and why'

# ── PART 9 PROFESSIONAL OUTPUT ──────────────────────────────────────────────
T[156] = 'PART 9   PROFESSIONAL OUTPUT   CHOOSE ONE'
T[157] = 'Option 1   Role Play   Meeting with the Auditor||   [6 min, pairs]'
T[158] = ('Student A is the finance director of Volga Print LLC. Student B is an external auditor. Together you '
          'discuss a strategy to reduce the company’s tax risks in 2026.')
T[159] = ('Student A explains the situation and defends one VAT option. Student B asks questions, names at least '
          '3 risks, and proposes measures. Together you agree on 3 actions with deadlines and owners.')
T[160] = ('Use the language from the Language tips (The main risk is that..., I would recommend..., '
          'Could we agree to...?).')
T[161] = ('Requirements   Use 6 or more words from the glossary   •   3 risks and 3 agreed actions   •   '
          'Both roles speak equally')
T[162] = 'Option 2   Error Finding||   [3 min]'
T[163] = ('A trainee wrote this note for the finance director. Find 4 mistakes (facts that contradict the text, '
          'wrong terms, or grammar). Write the correct version of each sentence.')
T[164] = ('"Since 2026 the standard VAT rate has been 20 percent. A VAT return can be sent on paper or '
          'electronically. Companies on USN files their annual return by 25 March. Late payment interest is the '
          'same as a penalty."')
T[165] = ('Requirements   Find 4 mistakes   •   Write the correct sentence for each one   •   '
          'Explain why it is wrong in 1 short sentence')
T[166] = 'Option 3   Process Explanation||   [3 min]'
T[167] = ('Explain to a new colleague, step by step, how to file one return (USN, VAT, or 3-NDFL). Start with the '
          'primary documents and finish with the desk tax audit.')
T[168] = ('Words   primary documents   tax register   electronic document flow   single tax account   '
          'notification of calculated tax   desk tax audit')
T[169] = ('Requirements   Use at least 5 of the 6 words   •   Correct order and deadlines   •   '
          'No reading from notes')
T[170] = 'Option 4   Mini Debate||   [4 min (2 plus 2)]'
T[171] = 'Statement   "The simplified tax system is still the best choice for small businesses in 2026."'
T[172] = ('Student A argues FOR the statement. Student B argues AGAINST it. Each person speaks for 2 minutes. '
          'Use facts from the text.')
T[173] = 'The class votes for the most convincing argument and gives 1 reason.'
T[174] = ('Requirements   Use at least 4 glossary words each   •   2 arguments with facts each   •   '
          'Listen and respond to your partner')
T[175] = 'Option 5   Email to a Client||   [10 min]'
T[176] = ('Anna Lebedeva writes to you, "I paid all my advance payments on time, so why did the tax office send '
          'me a message about notifications?"')
T[177] = ('Write a reply of 120 to 150 words as her tax consultant. Explain the problem, the possible '
          'consequences, and the next steps, including the flat she sold.')
T[178] = 'Requirements   Use 5 or more glossary words   •   Clear structure   •   Polite and professional tone'

# ── SPEAKING PRACTICE ───────────────────────────────────────────────────────
T[179] = 'SPEAKING PRACTICE   DISCUSSION QUESTIONS'
QS = [
    'Why does a state need a tax system?',
    'Which taxes do ordinary people in Russia pay?',
    'Why are taxes divided into federal, regional, and local?',
    'What are the advantages of the simplified tax system?',
    'Why do you think the VAT rate was raised in 2026?',
    'How does the single tax account make life easier?',
    'Why is tax accounting different from bookkeeping?',
    'Have you used the taxpayer’s personal account? How?',
    'Which tax deadline do you think is the easiest to miss?',
    'Why must a VAT return be filed only electronically?',
    'What is the difference between a penalty and interest?',
    'How can a company check if a supplier is reliable?',
    'Where does tax optimisation end and evasion begin?',
    'What makes an auditor’s advice valuable?',
    'Would you like to work as a tax consultant? Why?',
    'How can digital services change tax control in future?',
]
for i, s in enumerate(QS):
    T[181 + i] = s

# ── LANGUAGE TIPS ───────────────────────────────────────────────────────────
T[198] = 'To discuss risks and recommend'
T[199] = 'The main risk is that ...'
T[200] = 'If ..., the company may face ...'
T[201] = 'I would recommend ... because ...'
T[202] = 'In my view, the company should ...'
T[203] = 'To negotiate and agree'
T[204] = 'I see your point, but ...'
T[205] = 'That is a fair concern. However, ...'
T[206] = 'Could we agree to ... by ...?'
T[207] = 'Let us make ... responsible for ...'

# ── PEER ASSESSMENT ─────────────────────────────────────────────────────────
T[213] = '1. Vocabulary. Used 6 or more words from the glossary correctly'
T[215] = '2. Accuracy. Facts, rates, and deadlines match the text'
T[217] = '3. Reasoning. Explained risks and supported recommendations'
T[219] = '4. Interaction. Asked questions and responded to the partner'
T[221] = '5. Clarity. Clear structure and professional tone'

assert len(orig) == 227
build(TPL, T, OUT, glossary=GLOSS, glossary_widths=[2800, 3100, 3460])
