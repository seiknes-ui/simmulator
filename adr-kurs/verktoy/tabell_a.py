# Leser radene for et UN-nummer i Tabell A (ADR/RID 2025, tekst fra hent_bok.sh).
# Hver rad står på to sider i boka: kolonne (1)–(9b) til venstre og (10)–(20) til høyre.
# Bruk: python3 -I tabell_a.py <adr.txt> 1203 1017 ...   (skriver radene som JSON)
import re, sys, json
L = open(sys.argv[1], encoding='utf-8').read().split('\n')
A0 = next(i for i, l in enumerate(L) if l.startswith('0004 AMMONIUMPIKRAT') and i > 15000)
A1 = next(i for i, l in enumerate(L) if l.startswith('Tabell B: Alfabetisk liste'))
RAD = re.compile(r'^(\d{4})\s+\S')
SLUTT = re.compile(r'(?:^|\s)(\d{4})$')
STOPP = re.compile(r'^(Tabell A|Kapittel 3\.2|Del 3|UN$|Nr\.|\(1\)|3\.1\.2|\d+ \d+ \d+$)')

def venstre(un):
    ut = []
    for i in range(A0, A1):
        if L[i].startswith(un + ' ') and RAD.match(L[i]):
            blokk = [L[i]]
            for j in range(i + 1, min(i + 14, A1)):
                if RAD.match(L[j]) or STOPP.match(L[j]) or SLUTT.search(L[j]) and re.search(r'\b(CE\d+|S\d+|CV\d+|V\d+)\b', L[j]): break
                blokk.append(L[j])
            ut.append(' '.join(blokk))
    return ut

def hoyre(un):
    ut = []
    for i in range(A0, A1):
        l = L[i]
        if l.endswith(' ' + un) or l == un and i > A0:
            if RAD.match(l): continue  # venstre rad som slutter med tallet
            blokk = [l]
            for j in range(i - 1, max(i - 16, A0), -1):
                k = L[j]
                if SLUTT.search(k) and not RAD.match(k) or STOPP.match(k) or k.startswith('Ikke tillatt'): break
                blokk.insert(0, k)
            ut.append(' '.join(blokk))
    return ut

def tolk(v, h):
    r = {'venstre': v, 'hoyre': h}
    m = re.search(r'\s(1|2|3|4\.[123]|5\.[12]|6\.[12]|7|8|9)\s+([A-Z]{1,4}\d{0,2}|\d\.\d[A-Z]|\d[A-Z]{1,4})\s+(?:(I{1,3})\s+)?([\d.]+(?:\s*\+\s*[\d.]+)*)?', v)
    if m: r.update(klasse=m.group(1), kode=m.group(2), eg=m.group(3) or '', sedler=(m.group(4) or '').replace(' ', ''))
    m = re.search(r'\s(0|\d+ ?(?:ml|L|kg|g))\s+(E\d)\s', ' ' + v.replace('\n', ' ') + ' ')
    if m: r.update(lq=m.group(1), eq=m.group(2))
    m = re.search(r'\s([0-4])\s+\(([A-E0-9/\-]+)\)', ' ' + h)
    if m: r.update(tk=m.group(1), tunnel=m.group(2))
    etter = h[h.index('(' + m.group(2) + ')') + len(m.group(2)) + 2:] if m else h
    r['koder'] = re.findall(r'\b((?:VC|CV|AP|V|S)\d+)\b', etter)
    m = re.search(r'(?:CE\d+\s+)?(X?\d{2,3})\s+\d{4}$', h)
    r['farenr'] = m.group(1) if m else ''
    return r

if __name__ == '__main__':
    ut = {}
    for un in sys.argv[2:]:
        v, h = venstre(un), hoyre(un)
        ut[un] = [tolk(v[i] if i < len(v) else '', h[i] if i < len(h) else '') for i in range(max(len(v), len(h)))]
    print(json.dumps(ut, ensure_ascii=False, indent=1))
