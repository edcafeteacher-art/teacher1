# Case Challenge dashboard (pair work)

When the teacher gives cases for pair work, or a worksheet needs a role play with several cases, build an HTML dashboard by adapting `assets/case_challenge_template.html` (Tax Risk Case Challenge, Year 3 Finance). Never design a new page: change content only.

## Fixed format

- Interface in English. Sapphire design: navy masthead #0b2545, accent #0f2f57, gold #c9a24a, grid background #e9eef4, Spectral and IBM Plex Sans, dark theme toggle (dark #050b16, gold #e2c06d). All data stays in the student's browser (localStorage, wrapped in try/catch).
- Tabs: Brief, one tab per case, Peer rubric, Glossary. Timer in the header (prep 15 or 20 min, talk 3 or 5 min, custom, sound signal).
- Brief: steps of the lesson, presentation requirements, pair A/B and group, the case assigned by the teacher (marked Ours), retelling notes for the lesson text.
- Case tab: situation, roles, tasks with checkboxes, success condition, target vocabulary (tap inserts into the field), glossary counter with word forms (target 8), requirements checklist, fields Main problem / Reason 1 and 2 / Recommendation 1 to 3 / Expected result / Success condition, each with who speaks (A or B), language kit (useful phrases and mini glossary), copy plan button.
- Levels: each case has Level A (with support: key facts box and sentence starters as placeholders, simpler tasks) and Level B (standard tasks, no starters). Year 3 always gets two levels.
- Peer rubric: Vocabulary heard box (active vocabulary of the case, full glossary with search, a word outside the active list moves into the box marked added, counter to 8), 5 criteria 0 to 5 with total out of 25, One strength and One suggestion with grey example placeholders, the teacher's final mark block, copy assessment.
- Glossary tab: search EN and RU, marks words already used, copy.

## How to adapt the template

1. Copy `assets/case_challenge_template.html`.
2. Replace everything between `/* ---------- Data ---------- */` and `/* ---------- State ---------- */` with new `GLOSSARY`, `CASES`, `FIELDS`, `PHRASES`, `CRITERIA`, `BANDS`, `ILLO`. Keep the same object shape:
   `{id, title, tags[], situation, role, tasksA[], tasksB[], facts[], starters{problem, reason1, reason2, rec1, rec2, rec3, result, sc}, vocab[], sc, scField}`.
3. Every item in `vocab` must be exactly an English term from `GLOSSARY`.
4. Update `SPECIAL` regex patterns for terms with brackets, apostrophes, or abbreviations, for example `"value added tax (VAT)":"value[\\s-]+added[\\s-]+tax|VAT"`. A term with brackets and no SPECIAL entry breaks the counter.
5. Change the title, masthead eyebrow, h1, intro, Brief steps and requirements, retelling labels and placeholders, rubric placeholders, footer, and `const KEY = "..."` (a new storage key per dashboard).
6. Illustrations in `ILLO` are inline SVGs built from the `--il-*` colour tokens; draw one simple scene per case.
7. No em-dashes in case texts.

## Test before delivery

Open the page in a headless browser (Playwright). Check: no console errors (a blocked Google Fonts request in an offline sandbox is fine), every tab opens, Level A shows facts and starters and Level B hides them, typing glossary terms raises the counter (including word forms and terms inside longer terms, longest match wins), rubric total updates, glossary search finds Russian words, theme toggle works, no horizontal scroll at 390 px width. When testing a bare file, wrap it in a page that sets `[hidden]{display:none!important}`, which the hosting platform adds.

## Delivery

If you can publish it as a hosted page, do so and give the link; otherwise deliver the .html file. Say that the page is private until the teacher shares it.
