"""
hob_fill.py  |  Template engine for the "Hobbies" worksheet design (standard since Oct 2026).

Takes the reference DOCX as a template and replaces the text of non-empty
paragraphs by their running index (same order as in the source). All tables,
fills, borders, margins and Word numbering stay exactly as in the template.

Text syntax per paragraph
  None              keep the original text
  "plain **bold**"  base run format = first non-bold run, bold = first bold run
  "seg1||seg2"      map pieces onto the paragraph's consecutive format groups
                    (e.g. Option labels: bold label || small time note)
"""
import copy, re, sys, zipfile, shutil, os
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q = lambda t: f'{{{W}}}{t}'
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'


def _text_runs(p):
    return [r for r in p.findall(q('r')) if r.find(q('t')) is not None]


def _is_bold(rpr):
    return rpr is not None and rpr.find(q('b')) is not None


def _make_run(rpr, text):
    r = etree.Element(q('r'))
    if rpr is not None:
        r.append(copy.deepcopy(rpr))
    t = etree.SubElement(r, q('t'))
    t.text = text
    t.set(XML_SPACE, 'preserve')
    return r


def _bold_from(base):
    rpr = copy.deepcopy(base) if base is not None else etree.Element(q('rPr'))
    if rpr.find(q('b')) is None:
        idx = 0
        for i, ch in enumerate(rpr):
            if ch.tag in (q('rStyle'), q('rFonts')):
                idx = i + 1
        rpr.insert(idx, etree.Element(q('bCs')))
        rpr.insert(idx, etree.Element(q('b')))
    return rpr


def _groups(runs):
    out = []
    for r in runs:
        rpr = r.find(q('rPr'))
        key = etree.tostring(rpr) if rpr is not None else b''
        if out and out[-1][0] == key:
            continue
        out.append((key, rpr))
    return [g[1] for g in out]


def fill_paragraph(p, new_text):
    runs = _text_runs(p)
    if not runs:
        return
    anchor = runs[0]
    parent = anchor.getparent()
    pos = list(parent).index(anchor)

    if '||' in new_text:
        pieces = new_text.split('||')
        grp = _groups(runs)
        new_runs = [_make_run(grp[min(i, len(grp) - 1)], s) for i, s in enumerate(pieces)]
    else:
        rprs = [r.find(q('rPr')) for r in runs]
        base = next((x for x in rprs if not _is_bold(x)), rprs[0])
        bold = next((x for x in rprs if _is_bold(x)), None)
        bold = bold if bold is not None else _bold_from(base)
        new_runs = []
        for seg in re.split(r'(\*\*[^*]+\*\*)', new_text):
            if not seg:
                continue
            if seg.startswith('**') and seg.endswith('**'):
                new_runs.append(_make_run(bold, seg[2:-2]))
            else:
                new_runs.append(_make_run(base, seg))

    for r in runs:
        r.getparent().remove(r)
    for pe in p.findall(q('proofErr')):
        p.remove(pe)
    for i, r in enumerate(new_runs):
        parent.insert(pos + i, r)


def text_paragraphs(root):
    res = []
    for p in root.iter(q('p')):
        txt = ''.join(''.join(r.itertext()) for r in _text_runs(p))
        if txt.strip():
            res.append(p)
    return res


DELETE = '\x00DELETE'   # texts[i] = DELETE removes that paragraph completely


def _set_widths(tbl, widths):
    grid = tbl.find(q('tblGrid'))
    for gc, w in zip(grid.findall(q('gridCol')), widths):
        gc.set(q('w'), str(w))
    for tr in tbl.findall(q('tr')):
        for tc, w in zip(tr.findall(q('tc')), widths):
            tcw = tc.find(f"{q('tcPr')}/{q('tcW')}")
            if tcw is not None:
                tcw.set(q('w'), str(w)); tcw.set(q('type'), 'dxa')


def _rebuild_glossary(root, rows, widths=None):
    """Replace the data rows of the glossary table (header contains 'Word or phrase')
    with one row per (term, translation, meaning), cloned from the first data row."""
    for tbl in root.iter(q('tbl')):
        trs = tbl.findall(q('tr'))
        head = ''.join(trs[0].itertext()) if trs else ''
        if 'Word or phrase' not in head:
            continue
        proto = trs[1]
        for tr in trs[1:]:
            tbl.remove(tr)
        for entry in rows:
            tr = copy.deepcopy(proto)
            cells = tr.findall(q('tc'))
            for tc, val in zip(cells, entry):
                p = next(x for x in tc.iter(q('p')) if _text_runs(x))
                fill_paragraph(p, val)
            tbl.append(tr)
        if widths:
            assert sum(widths) == 9360, widths
            _set_widths(tbl, widths)
        return len(rows)
    raise ValueError('glossary table not found')


def build(template, texts, out_path, glossary=None, glossary_widths=None):
    """texts: dict {index: str|None|DELETE} or list aligned with text paragraphs.
    glossary: optional list of (term, translation, meaning) rows of any length."""
    with zipfile.ZipFile(template) as z:
        files = {n: z.read(n) for n in z.namelist()}
    root = etree.fromstring(files['word/document.xml'])
    paras = text_paragraphs(root)
    if isinstance(texts, list):
        if len(texts) != len(paras):
            sys.exit(f'Expected {len(paras)} texts, got {len(texts)}')
        texts = dict(enumerate(texts))
    for i, t in texts.items():
        if t == DELETE:
            paras[i].getparent().remove(paras[i])
        elif isinstance(t, (list, tuple)):
            proto = copy.deepcopy(paras[i])
            fill_paragraph(paras[i], t[0])
            last = paras[i]
            for extra in t[1:]:
                np_ = copy.deepcopy(proto)
                fill_paragraph(np_, extra)
                last.addnext(np_); last = np_
        elif t is not None:
            fill_paragraph(paras[i], t)
    if glossary is not None:
        _rebuild_glossary(root, glossary, glossary_widths)
    # section bars (navy / teal single-row tables) stay on the page with the next block
    def _keep_next(par):
        ppr = par.find(q('pPr'))
        if ppr is None:
            ppr = etree.Element(q('pPr')); par.insert(0, ppr)
        if ppr.find(q('keepNext')) is None:
            idx = 1 if ppr.find(q('pStyle')) is not None else 0
            ppr.insert(idx, etree.Element(q('keepNext')))
    for tbl in root.iter(q('tbl')):
        rows = tbl.findall(q('tr'))
        fills = [sh.get(q('fill')) for sh in tbl.iter(q('shd'))]
        if len(rows) == 1 and fills and fills[0] in ('1B3A5C', '1A6B5F'):
            for par in tbl.iter(q('p')):
                _keep_next(par)
            nxt = tbl.getnext()
            while nxt is not None and nxt.tag == q('p'):
                _keep_next(nxt); nxt = nxt.getnext()
    # tables that start with a navy header row (Peer Assessment) keep header with the next row
    for tbl in root.iter(q('tbl')):
        rows = tbl.findall(q('tr'))
        fills = [sh.get(q('fill')) for sh in rows[0].iter(q('shd'))] if rows else []
        if len(rows) > 2 and fills and fills[0] in ('1B3A5C', '1A6B5F'):
            for tr in rows[:2]:
                for par in tr.iter(q('p')):
                    _keep_next(par)
    # rows of multi-row tables must not split across pages (glossary, case, peer table)
    for tbl in root.iter(q('tbl')):
        rows = tbl.findall(q('tr'))
        grid = tbl.find(q('tblGrid'))
        ncols = len(grid.findall(q('gridCol'))) if grid is not None else 1
        if len(rows) < 3 and not (len(rows) == 2 and ncols >= 3):
            continue
        for tr in rows:
            trpr = tr.find(q('trPr'))
            if trpr is None:
                trpr = etree.Element(q('trPr'))
                tr.insert(1 if tr.find(q('tblPrEx')) is not None else 0, trpr)
            if trpr.find(q('cantSplit')) is None:
                trpr.insert(0, etree.Element(q('cantSplit')))
    files['word/document.xml'] = etree.tostring(root, xml_declaration=True,
                                                encoding='UTF-8', standalone=True)
    tmp = out_path + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as z:
        for n, b in files.items():
            z.writestr(n, b)
    shutil.move(tmp, out_path)
    print('DONE:', out_path, '| paragraphs:', len(paras))


def original_texts(template):
    with zipfile.ZipFile(template) as z:
        root = etree.fromstring(z.read('word/document.xml'))
    return [''.join(''.join(r.itertext()) for r in _text_runs(p)) for p in text_paragraphs(root)]
