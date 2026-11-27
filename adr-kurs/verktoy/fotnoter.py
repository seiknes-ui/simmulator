# Finner fotnoter i boka som nevner UN-numre, og viser hvor kurset bruker de samme UN-numrene
# sammen med avsnittet fotnoten hører til. Treffene må leses for hånd: står fotnoten riktig i kurset?
# Bruk: python3 -I verktoy/fotnoter.py <adr.txt> index.html
import re, sys
bok = open(sys.argv[1], encoding='utf-8').read().split('\n')
html = open(sys.argv[2], encoding='utf-8').read()
head = re.compile(r'^(\d\.\d+(?:\.\d+)+)\s+\S')
fot = re.compile(r'^(\d/|[a-e]\)|\d) ')
sec, notes = None, []
for i, l in enumerate(bok):
    m = head.match(l)
    if m and not re.search(r'\.{5}', l): sec = m.group(1)
    if sec and fot.match(l) and 'UN' in l:
        txt = ' '.join(bok[i:i + 3])
        uns = set(re.findall(r'\b(\d{4})\b', txt)) - {'2025', '2023', '2019'}
        if uns: notes.append((sec, l[:110], uns))
items = re.findall(r"^\s*(\['[a-z]+', '[a-z]', .*|\{ st: '[a-z]+', .*)$", html, re.M)
for sec, l, uns in notes:
    top = '.'.join(sec.split('.')[:3])
    hits = [it for it in items if top in it and any(re.search(r'UN[ -]?(?:nr\.? )?' + u + r'\b', it) for u in uns)]
    if hits:
        print(f'== {sec}: {l}')
        for h in hits: print('   ', h[:200])
