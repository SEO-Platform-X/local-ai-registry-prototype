"""Apply the brand layer (docs/brand.css, brand.js) to every browsable screen in docs/.
Idempotent: safe to re-run after build_site.py regenerates the pages.
Usage: python3 generators/apply_brand.py [docs_dir]"""
import re, sys, glob, os
D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'docs')
MARK = '<!--lr-brand-->'

def serif_rules(s):
    # keep each screen's own serif (Cormorant) headings serif under the brand font reset
    sels = set()
    for st in re.findall(r'<style[^>]*>(.*?)</style>', re.sub(r'<!--lr-brand-->.*?<!--/lr-brand-->', '', s, flags=re.S), flags=re.S):
        for m in re.finditer(r'(?:^|[}\s])([^{}@]+)\{([^{}]*)\}', st):
            sel, body = m.group(1).strip(), m.group(2)
            if 'Cormorant' in body and 'font-family' in body and '#dc-root' not in sel and 'Cormorant' not in sel:
                for one in sel.split(','):
                    one = one.strip()
                    if len(one) > 2 and one not in ('h1', 'h2', 'h3') and not one.startswith(('@', '/*')) and len(one) < 90:
                        sels.add(one)
    if not sels:
        return ''
    return '<style>' + ','.join('#dc-root ' + x for x in sorted(sels)) + '{font-family:"Cormorant Garamond",Georgia,serif !important}</style>'

for f in sorted(glob.glob(os.path.join(D, '*.html'))):
    s = open(f, encoding='utf-8').read()
    s = re.sub(r'<!--lr-brand-->.*?<!--/lr-brand-->', '', s, flags=re.S)
    if 'id="dc-root"' not in s:
        continue
    head = MARK + '<link rel="stylesheet" href="brand.css?v=12">' + serif_rules(s) + '<!--/lr-brand-->'
    s = s.replace('</head>', head + '</head>', 1)
    s = s.replace('<div id="dc-root">', MARK + '<div class="lr-street" aria-hidden="true"></div><!--/lr-brand--><div id="dc-root">', 1)
    tail = MARK + '<script src="brand.js?v=12"></script>' + ('<script src="brand-photos.js?v=12"></script>' if os.path.basename(f) in ('Main.html', 'MProfile.html') else '') + '<!--/lr-brand-->'
    k = s.rfind('</body>')
    s = s[:k] + tail + s[k:]
    open(f, 'w', encoding='utf-8').write(s)
    print('branded', os.path.basename(f))
