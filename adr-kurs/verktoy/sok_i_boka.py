# Søk i ADR/RID 2025 (tekst fra hent_bok.sh). Viser sidetall (PDF-side = sidetallet i boka).
# Bruk:
#   python3 -I sok_i_boka.py <adr.txt> ord [ord ...]      linjer der alle ordene finnes, med side og avsnitt
#   python3 -I sok_i_boka.py <adr.txt> --avsnitt 7.5.5.3  hele avsnittet, med fotnoter nederst på sidene det står på
#   python3 -I sok_i_boka.py <adr.txt> --side 1605        hele siden
#   python3 -I sok_i_boka.py <adr.txt> --un 1203          radene for UN-nummeret i Tabell A
import re, sys
if len(sys.argv) < 3: sys.exit(__doc__ or 'Se toppen av fila')
sider = open(sys.argv[1], encoding='utf-8').read().split('\f')
args = sys.argv[2:]
head = re.compile(r'^(\d\.\d+(?:\.\d+)*|§ ?\d+ ?[a-z]?\.?)\s+\S')
def avsnitt_paa(side_nr, linje_nr):
    for s in range(side_nr, max(side_nr - 6, -1), -1):
        ls = sider[s].split('\n')
        rng = range(linje_nr if s == side_nr else len(ls) - 1, -1, -1)
        for i in rng:
            m = head.match(ls[i])
            if m and '....' not in ls[i]: return m.group(1)
    return '?'
def fotnoter(side_nr):
    ls = [l for l in sider[side_nr].split('\n') if l.strip()]
    return [l for l in ls[-12:] if re.match(r'^([1-9]|[a-e][.)])\s+[A-ZÆØÅ«]', l)]
if args[0] == '--side':
    n = int(args[1]); print(f'--- side {n} ---'); print(sider[n - 1])
elif args[0] == '--avsnitt':
    sec = args[1]; pat = re.compile(r'^' + re.escape(sec) + r'\s+\S'); nxt = re.compile(r'^\d\.\d+(?:\.\d+)*\s+\S')
    funnet = False
    for s, txt in enumerate(sider):
        ls = txt.split('\n')
        for i, l in enumerate(ls):
            if pat.match(l) and '....' not in l:
                funnet = True; out = [f'--- {sec}, side {s + 1} ---']; ss, ii, n = s, i, 0
                while n < 120:
                    lines = sider[ss].split('\n')
                    if ii >= len(lines):
                        fn = fotnoter(ss)
                        if fn: out.append(f'[fotnoter nederst på side {ss + 1}: ' + ' | '.join(fn) + ']')
                        ss += 1; ii = 0
                        if ss >= len(sider): break
                        out.append(f'--- side {ss + 1} ---'); continue
                    l2 = lines[ii]
                    m = nxt.match(l2)
                    if n > 0 and m and not m.group(0).startswith(sec) and '....' not in l2: break
                    out.append(l2); ii += 1; n += 1
                fn = fotnoter(ss)
                if fn: out.append(f'[fotnoter nederst på side {ss + 1}: ' + ' | '.join(fn) + ']')
                print('\n'.join(out)); print()
    if not funnet: print('Fant ikke avsnittet', sec)
elif args[0] == '--un':
    un = args[1]
    for s, txt in enumerate(sider):
        ls = txt.split('\n')
        for i, l in enumerate(ls):
            if re.match(r'^' + un + r'\s+[A-ZÆØÅ]', l) or re.search(r'\s' + un + r'$', l):
                print(f'side {s + 1}: ' + ' | '.join(ls[max(0, i - 6):i + 8]))
else:
    ord_ = [a.lower() for a in args]; n = 0
    for s, txt in enumerate(sider):
        ls = txt.split('\n')
        for i, l in enumerate(ls):
            blokk = ' '.join(ls[i:i + 2]).lower()
            if all(o in blokk for o in ord_) and all(o in l.lower() for o in ord_[:1]):
                print(f'side {s + 1} · {avsnitt_paa(s, i)}: {l.strip()} {ls[i + 1].strip() if i + 1 < len(ls) else ""}'[:240]); n += 1
                if n >= 60: print('… flere treff, bruk flere ord'); sys.exit()
