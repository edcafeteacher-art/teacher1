"""Quality check for a worksheet built with hob_fill.py.

Usage
  python check_docx.py OUTPUT.docx [--forbid word1,word2] [--render]

Checks
  1. em-dashes (never allowed) and en-dashes (allowed only in a level range such as A1–A2)
  2. colons in prose (allowed only in the table labels 'Strong point:' and 'Improve:')
  3. forbidden leftovers from the template or from another specialty (--forbid)
  4. the file opens as a valid zip with well-formed XML
  5. --render: converts to PDF with LibreOffice and writes a contact sheet PNG of all pages
Exit code 1 if any check fails.
"""
import re, sys, zipfile, subprocess, pathlib, argparse
from lxml import etree

ALLOWED_COLON = {'Strong point:', 'Improve:'}
DEFAULT_FORBID = ['hobby', 'hobbies', 'Misha', 'Sofia']   # Hobbies template leftovers

ap = argparse.ArgumentParser()
ap.add_argument('docx')
ap.add_argument('--forbid', default='', help='comma-separated words that must not appear')
ap.add_argument('--render', action='store_true')
a = ap.parse_args()
path = pathlib.Path(a.docx)
ok = True

with zipfile.ZipFile(path) as z:
    bad = z.testzip()
    xml = z.read('word/document.xml')
etree.fromstring(xml)
x = xml.decode('utf-8')
if bad:
    print('FAIL corrupt zip member', bad); ok = False

paras = [''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p)) for p in re.findall(r'<w:p[ >].*?</w:p>', x, re.S)]
paras = [p for p in paras if p.strip()]
text = ' '.join(paras)

em = [p for p in paras if '—' in p]
if em:
    ok = False; print('FAIL em-dash in', len(em), 'paragraphs'); [print('   ', p[:110]) for p in em]
en = [p for p in paras if '–' in p and not re.search(r'[ABC][12]–[ABC][12]|\d–\d', p)]
if en:
    ok = False; print('FAIL en-dash outside a range'); [print('   ', p[:110]) for p in en]
col = [p for p in paras if ':' in p and p.strip() not in ALLOWED_COLON]
if col:
    ok = False; print('FAIL colon in prose'); [print('   ', p[:110]) for p in col]
forbid = DEFAULT_FORBID + [w.strip() for w in a.forbid.split(',') if w.strip()]
hits = sorted({m for w in forbid for m in re.findall(rf'\b{re.escape(w)}\w*', text, re.I)})
if hits:
    ok = False; print('FAIL forbidden words found', hits)

print(f'{path.name}: {len(paras)} paragraphs,', 'ALL CHECKS PASSED' if ok else 'CHECKS FAILED')

if a.render:
    out = path.with_suffix('')
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', str(path.parent), str(path)],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    pdf = path.with_suffix('.pdf')
    subprocess.run(['pdftoppm', '-jpeg', '-r', '50', str(pdf), str(out) + '-page'], check=False)
    try:
        from PIL import Image
        pages = sorted(path.parent.glob(out.name + '-page-*.jpg'))
        ims = [Image.open(p) for p in pages]
        w, h = ims[0].size; cols = 6; rows = (len(ims) + cols - 1) // cols
        sheet = Image.new('RGB', (w * cols, h * rows), 'white')
        for i, im in enumerate(ims):
            sheet.paste(im, ((i % cols) * w, (i // cols) * h))
        sheet_path = path.parent / (out.name + '-contact-sheet.png')
        sheet.save(sheet_path)
        for p in pages:
            p.unlink()
        print(f'rendered {len(ims)} pages -> {sheet_path}  (open it and look at every page)')
    except Exception as e:  # noqa: BLE001
        print('render skipped:', e)

sys.exit(0 if ok else 1)
