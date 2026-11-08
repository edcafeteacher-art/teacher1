"""How to Find Your Way in an Unknown Town  |  CEFR A2  |  Year 1 Logistics  |  Hobbies design.

Variant of HW15_Find_Your_Way_A2_Banking_Y1.py. Text, glossary, and all answer-bearing tasks (Part 3,
Part 5 Tasks 1 and 3, Option 2, Option 5 numbers) come from the Banking base unchanged, so
Find_Your_Way_A2_Y1_KEY.docx works for both sheets. Only the professional context is overridden.

Facts used (Option 5), Moscow public transport, central zone, fares from 2 January 2026, per trip
  Troika card (Wallet) 75 roubles, bank card 83 roubles, biometric payment 71 roubles
  Sources  Interfax    https://www.interfax.ru/moscow/1060092
           Kommersant  https://www.kommersant.ru/doc/8336906

Usage   python3 HW15_Find_Your_Way_A2_Logistics_Y1.py <source HW15.docx> <output folder>
"""
import sys, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
BASE = str(HERE / 'HW15_Find_Your_Way_A2_Banking_Y1.py')


def load(path):
    src = open(path, encoding='utf-8').read()
    src = src[:src.rindex('build(TPL')]          # content only, no build and no key
    ns = {'__name__': 'loaded', '__file__': path}
    exec(compile(src, path, 'exec'), ns)
    return ns


ns = load(BASE)
T = ns['T']
OUT = str(pathlib.Path(sys.argv[2]) / 'Find_Your_Way_A2_Logistics_Y1.docx')

T.update({
    1: 'Getting Around a New Place for a Future Logistics Worker',
    2: '90 min   •   Level A2   •   Year 1   •   Logistics',
    5: ('You are a first-year student at a logistics college. Next Monday you start your practice at a warehouse '
        'of a logistics company in a part of Moscow that you do not know. Work starts at 8 a.m., and the first '
        'trucks arrive at 8.'),
    6: ('The logistics manager says, "In logistics, time is money. If one worker is late, the trucks wait. '
        'Plan your way to work before your first day."'),
    12: 'Guess. What can happen to Denis on his first morning at the warehouse? Give 1 idea.',
    110: 'Case   Three Students, Three Ways to Get to the Warehouse',
    125: 'Works as a courier',
    126: 'Delivers parcels on foot',
    127: 'Never looks at a map',
    128: 'Asks 4 or 5 people a day',
    129: 'Wants to be a dispatcher.',
    139: ('Give your opinion. Who is the best prepared for the first day at the warehouse? Give 2 reasons. '
          'Use the word because.'),
    151: 'How can a new worker find the way to a warehouse and come on time?',
    155: 'Why a logistics worker must be on time (trucks, deliveries, couriers)',
    158: ('Imagine you work as a dispatcher at a logistics company in Moscow. A new courier calls and asks, '
          '"How do I get from the underground station to our warehouse?"'),
    170: 'Option 4   Role Play   At the Warehouse||   [3 min, pairs]',
    171: ('Student A is a new courier. He or she is lost near the warehouse and calls the office. '
          'Student B is a dispatcher at a logistics company.'),
    175: 'Option 5   Product   Weekly Transport Budget||   [15 min, then 2 min presentation]',
    176: ('You are a logistics manager. A new employee starts work at your warehouse next week. He works 5 days '
          'a week, and every day he makes 4 trips by public transport in the central zone. You plan his weekly '
          'transport budget.'),
    196: 'Why must couriers know the city well?',
})

flat = ' '.join(x for v in T.values() for x in (v if isinstance(v, list) else [v]) if isinstance(x, str))
left = re.findall(r'\b(?:banker\w*|banking|teller\w*|loan\w*|bank branch\w*|branch\w*|client\w*)\b', flat, re.I)
print('Banking context words left:', left)
ns['build'](ns['TPL'], T, OUT, glossary=ns['GLOSS'], glossary_widths=[3000, 2900, 3460])
