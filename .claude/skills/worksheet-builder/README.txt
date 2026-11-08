worksheet-builder  (skill for Claude Code)

Install
  Personal:  copy the folder worksheet-builder to ~/.claude/skills/
  Project:   copy it to <your project>/.claude/skills/
Requirements
  python3 with lxml (pip install lxml); for page checks also LibreOffice (soffice), poppler (pdftoppm), Pillow.
Use
  Ask Claude Code, for example: "Сделай рабочий лист для 1 курса банковского дела, уровень A2, по этому тексту".
  The agent reads SKILL.md, asks its questions, then builds the .docx in the current folder.
Test
  cd to an empty folder and run:  python3 <path>/worksheet-builder/examples/example_A1-A2_two_texts_banking_y1.py
