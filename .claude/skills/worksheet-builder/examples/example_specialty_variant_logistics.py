"""Financial Independence for Year 1 Logistics: both versions (A1-A2 two texts, and Version 2 A2).
Texts and glossaries are those of the Banking sheets; only the professional context changes."""
import sys, pathlib
SKILL = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))

import re
from hob_fill import build

def load(path):
    src = open(path, encoding='utf-8').read()
    src = src[:src.rindex('build(TPL')]
    ns = {'__name__': 'loaded', '__file__': path}
    exec(compile(src, path, 'exec'), ns)
    return ns

COMMON = {
    5: ('You are a first-year student at a logistics college. Today your group is talking about money. '
        'Your teacher asks a simple question, "Who is financially independent in this room?"'),
    6: ('Your teacher says, "Financial independence is not about a lot of money. It is about knowing how to use '
        'money. A good logistics specialist plans costs and budgets every day, so you need to learn it first."'),
    115: 'Works at a warehouse on Saturdays',
    125: 'Delivers food as a courier after college',
    158: ('Imagine you work at a logistics company. A school asks you to give a short talk, "How to start managing '
          'your money."'),
    170: 'Option 4   Role Play   Job Interview||   [3 min, pairs]',
    171: ('Student A is an HR manager at a logistics company. Student B is a student who says, "I want a '
          'part-time job at your warehouse."'),
    173: 'Then change roles.',
}
V1 = dict(COMMON)
V1.update({
    177: ('Use income from a part-time job, for example at a warehouse or as a courier. Show 5 expenses marked as '
          'needs or wants, one saving goal with the amount and the date, and 2 steps from the text. Then show '
          'your product to the group and explain it in 2 minutes.'),
    2: '90 min   •   Level A1–A2   •   Year 1   •   Logistics',
    100: 'b)  Pavel delivers parcels on Saturdays. He has a __________________ .',
    172: ('Student A asks 3 questions about the student’s free time, experience, and plans for the money. '
          'Student B answers and names a saving goal. Student A gives 2 simple tips.'),
    174: 'Requirements   Use 4 glossary words each   •   Be polite   •   Speak in full sentences',
})
V2 = dict(COMMON)
V2.update({
    177: ('Use income from a part-time job at a warehouse or in delivery. Show monthly income and expenses, a chart '
          'that compares needs and wants, a saving goal with the amount, and how many months you need to reach it. '
          'Add 3 steps from the text. Present your product to the group in 2 minutes.'),
    2: 'Version 2   •   90 min   •   Level A2   •   Year 1   •   Logistics',
    100: 'b)  Pavel works at a warehouse on Saturdays. He earns money and __________________ .',
    172: ('Student A asks at least 4 questions about the student’s schedule, experience, expenses, and saving '
          'goal. Student B answers. Student A gives 3 tips and explains them.'),
    174: 'Requirements   Use 6 glossary words each   •   Be polite   •   Ask and answer follow-up questions',
})

JOBS = [
    (str(SKILL / 'examples' / 'example_A1-A2_two_texts_banking_y1.py'), V1,
     str(pathlib.Path.cwd() / 'Financial_Independence_A1-A2_Logistics_Y1.docx')),
    (str(SKILL / 'examples' / 'example_A2_version2_harder_banking_y1.py'), V2,
     str(pathlib.Path.cwd() / 'Financial_Independence_A2_Version2_Logistics_Y1.docx')),
]
for src, over, out in JOBS:
    ns = load(src)
    T = ns['T']
    T.update(over)
    flat = ' '.join(x for v in T.values() for x in (v if isinstance(v, list) else [v]) if isinstance(x, str))
    left = re.findall(r'\b(?:bank\w*|banker|café|Banking)\b', flat, re.I)
    # "bank account" and "bank card" are general money vocabulary and stay
    left = [w for w in left if w.lower() not in ('bank',)]
    print(out.rsplit('/', 1)[1], 'context words left:', left)
    build(ns['TPL'], T, out, glossary=ns['GLOSS'], glossary_widths=[2700, 2900, 3760])
