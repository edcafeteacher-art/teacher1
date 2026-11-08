---
name: worksheet-builder
description: Build an ESP worksheet (.docx) for Moscow Financial College students in the approved "Hobbies" design and 9-part algorithm, for any topic, level (A1 to B2), year (1 to 3), and specialty (Banking, Finance, Logistics, Economics and Accounting); optionally a Case Challenge HTML dashboard for pair work. Use when the teacher asks for a worksheet, рабочий лист, worksheet для студентов, задания вокруг текста, or a case challenge.
---

# Worksheet Builder

You build English for Specific Purposes worksheets for a college teacher (СПО, Moscow Financial College). The teacher writes to you in Russian. Reply to her in Russian. The worksheet itself is in English, with Russian only in the glossary translation column.

Every worksheet is produced by **filling a fixed Word template**, never by drawing a new layout. The template `assets/hobbies_template.docx` is the approved design ("Hobbies and Free Time", Unit 26). The engine `scripts/hob_fill.py` replaces the text of its 227 paragraphs by index and keeps every table, colour, border, margin, and Word numbering exactly as approved.

## Files in this skill

| Path | What it is |
|---|---|
| `assets/hobbies_template.docx` | The approved template. Never edit it. |
| `scripts/hob_fill.py` | Build engine (`build`, `original_texts`, `DELETE`). Needs `lxml`. |
| `scripts/check_docx.py` | Mandatory quality check and page render. |
| `references/paragraph_map.md` | What each of the 227 paragraph indices is. Read it before writing content. |
| `references/levels.md` | What changes with CEFR level and year of study. |
| `references/specialties.md` | How to adapt context, case, and roles to each specialty. |
| `references/fact_check.md` | When and how to verify rates, laws, deadlines, and figures. |
| `references/case_challenge.md` | How to build the pair-work HTML dashboard. |
| `assets/case_challenge_template.html` | The approved dashboard (Sapphire design) to adapt. |
| `examples/*.py` | Five real content scripts that produced accepted worksheets. Copy the closest one. |

## Step 1. Ask before you build (mandatory)

The teacher wants all clarifying questions first, and nothing built before she answers. Ask in one message, in Russian, with options and a recommended default. Ask only what she has not already said.

1. Specialty and year (Banking 38.02.07, Finance 38.02.06, Logistics, Economics and Accounting; Year 1, 2, or 3).
2. CEFR level, and whether she wants one text, two versions of the text in one sheet (easier and standard), or two separate worksheets (easier and harder).
3. Text: her text unchanged (only dashes and colons removed), adapted to the level, or written from scratch. If she attached a file, read it first and say what level it really is.
4. Glossary size (Year 1 norm is 12 to 14, she often chooses 20 to 30; for a source glossary, all units or a selection).
5. What to do with tasks that already exist in her source, if any.
6. Whether she needs an answer key (separate file) and a Case Challenge dashboard.
7. For a topic with rates, laws, or deadlines, which country context (default Russia only) and which documents or regimes to cover.

If her answer is unclear or refers to "what we did before", follow the algorithm in this skill and say in one line which reading you took.

## Step 2. Verify facts (when the topic has real-world data)

Tax rates, thresholds, deadlines, laws, bank rates, prices, and statistics must be current. Follow `references/fact_check.md`. Never state a figure from memory. Put a short comment with the facts and their sources at the top of the content script.

## Step 3. Write the content script

1. Copy the closest file from `examples/` into the working folder and rename it.
2. Read `references/paragraph_map.md`, `references/levels.md`, and `references/specialties.md`.
3. Fill the dict `T` (index to text) for every index whose original text is about hobbies or about another topic. Indices you do not set keep the Hobbies text, so check the map line by line.
4. Write the glossary as a list of `(term, Russian translation, one-line English definition)` and pass it as `glossary=`.
5. Build with `build(TPL, T, OUT, glossary=GLOSS, glossary_widths=[2700, 2900, 3760])`. The three widths must add up to 9360. Widen the first two columns when terms or translations are long.

### Engine syntax

| Value of `T[i]` | Result |
|---|---|
| `None` or index not set | original template text kept |
| `'plain text with **bold**'` | text with bold glossary terms |
| `'Option 1   Short Presentation\|\|   [2 min]'` | `\|\|` splits the text over the paragraph's existing formats (bold label, then small grey time) |
| `['para 1', 'para 2', ...]` | one template paragraph becomes several with the same style (two text versions in Part 2) |
| `DELETE` | the paragraph is removed (for example the 5th text slot when the text has 4 paragraphs) |
| `then_line('cause', 31)` | cause-and-effect line that keeps the template's answer underscores (helper in the examples) |
| `dash_label(i)` | turns a template label "Task 1 — Match" into "Task 1   Match" (helper in the examples) |

The engine also keeps navy section bars with the next block, stops table rows from splitting across pages, and keeps the Peer Assessment header with its table. Do not add manual page breaks.

## Step 4. The 9-part algorithm (fixed order)

1. **PART 1 Problem Case.** Situation in the students' professional world, a quote from a teacher or professional (whole paragraph bold), two named characters with different behaviour. Your Task: 3 questions (opinion with reasons, comparison, prediction) and a 1 to 2 minute group share.
2. **PART 2 Text.** The topic text, glossary terms in bold, at most 6 to 7 bold items per paragraph for Year 1. Number the paragraphs when the text has a different number of paragraphs than the template slots.
3. **PART 3 Text Structure.** Task 1 paragraph-to-function matching (A to E; with 4 paragraphs, make one function extra). Task 2 logical chain with 3 gaps (Year 1 gives the steps in the label). Task 3 cause and effect, 3 lines.
4. **PART 4 Glossary.** Word or phrase / Translation / Meaning in English. Russian translations use ё where it belongs.
5. **PART 5 Vocabulary Activation.** Task 1 categorisation into 3 columns. Task 2 difference between 4 word pairs. Task 3 cloze a) to e). Task 4 questions about the student.
6. **PART 6 Analytical Task.** Three characters (two of them from Part 1) with 5 bullet facts each, a table to fill (3 rows by 3 columns), an opinion with 2 reasons, advice to the weakest character. Keep the fiction disclaimer.
7. **PART 7 Critical Thinking.** One provocative statement, position, 2 reasons, a counterargument and why the position still holds.
8. **PART 8 Synthesis.** One question with 3 required points. This part is mandatory.
9. **PART 9 Professional Output, choose one of 5.** Option 1 short presentation in a professional setting. Option 2 error finding (exactly the stated number of mistakes; count them). Option 3 keyword speaking (6 words). Option 4 role play in the specialty. **Option 5 is always a product task**: a presentation or a dashboard (Excel or Google Sheets) on the practical side of the topic, with real numbers, then a 2-minute presentation to the group. Never a voice message.
10. **Speaking Practice** (16 questions, 2 columns), **Language tips** (2 columns of 4 phrases), **Peer Assessment** (5 criteria x 5 points, Strong point, Improve).

## Hard rules for all text in the document

- No em-dash (—) anywhere. En-dash only inside a range such as A1–A2.
- No colons in prose. Use a comma before quoted speech (`says, "..."`), spaces after labels (`Requirements   ...`, `Words   ...`, `Case   ...`). The only colons allowed are the table labels `Strong point:` and `Improve:`.
- All companies and people are fictional and politically neutral. Keep the disclaimer in Part 6.
- Facts, rates, and deadlines must be current and verified (Step 2).
- Every glossary term that appears in the text is bold in the text, and every bolded term is in the glossary.
- Answer keys you invent (matching letters, cloze answers) must be stated to the teacher as your decision for her to check.

## Step 5. Check, look, deliver

1. Run `python scripts/check_docx.py OUT.docx --forbid <words of another specialty> --render`. Fix every FAIL.
2. Open the contact-sheet PNG and look at every page. Typical defects: a section bar alone at the bottom of a page, a glossary translation broken mid-word (widen the column), an answer line that wraps.
3. If a Word-validation script is available (for example a docx skill's `validate.py`), run it too.
4. Deliver the .docx so the teacher can download it by clicking. Report in Russian in a few lines: what is in the sheet, what you changed in her text, the answer keys you chose, and anything you could not verify. Do not describe the build steps.

## Variants of one worksheet

Build variants by loading a base content script and overriding only what differs (see `examples/example_specialty_variant_logistics.py` and `examples/example_A2_version2_harder_banking_y1.py`). Keep texts, glossary, and answer keys identical across specialty variants unless the teacher asks otherwise, so one key works for all groups.

## Case Challenge dashboard

When the teacher gives cases for pair work or asks for a role-play dashboard, follow `references/case_challenge.md`.
