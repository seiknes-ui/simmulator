# Sjekker at «minst/høyst/over/under …» + tall i riktige svar står likt i boka.
# Bruk: python3 -I verktoy/ordlyd.py <adr.txt> index.html
import re, sys
bok = re.sub(r'\s+', ' ', open(sys.argv[1], encoding='utf-8').read().lower()).replace('­','')
html = open(sys.argv[2], encoding='utf-8').read()
ss = lambda x: x.replace("\\'", "'")
qs = re.findall(r"^\s*\['([a-z]+)', '[a-z]', '((?:[^'\\]|\\.)*)', '((?:[^'\\]|\\.)*)', \['((?:[^'\\]|\\.)*)'", html, re.M)
pat = re.compile(r'\b(minst|høyst|over|under|mer enn|mindre enn|inntil|maksimalt|ikke over|opptil)\s+(\d[\d ]*(?:,\d+)?)', re.I)
for st, src, q, a in qs:
    a = ss(a)
    for w, n in pat.findall(a):
        n = n.strip(); nn = n.replace(' ', '')
        variants = {n, nn, nn.replace(',', '.')}
        if len(nn) > 3: variants.add(nn[:-3] + '.' + nn[-3:]); variants.add(nn[:-3] + ' ' + nn[-3:])
        if not any((w.lower() + ' ' + v) in bok for v in variants):
            print(f'{w} {n} | {ss(src)} | {ss(q)[:90]} | {a}')

# Sitater: alt i «…» i svaralternativer og forklaringer (også i oppslagsmalene) skal stå ordrett i boka.
# Linjeskift med bindestrek i boka slås sammen. Korte ord og navn på merker eller kolonner er med, de finnes også i boka.
rå = open(sys.argv[1], encoding='utf-8').read().replace('­', '')
rå = re.sub(r'(\w)[-‐]\s*\n\s*(\w)', r'\1\2', rå)
bok2 = re.sub(r'\s+', ' ', rå.lower())
norm = lambda t: re.sub(r'\s+', ' ', t.lower().replace("\\'", "'")).strip(' .,;:')
# Malene for oppslag: alle alternativer er sitater fra boka. Faste spørsmål: riktig svar og forklaring
# (feilalternativer kan med vilje sitere tekst som ikke står i boka, for eksempel en feil erklæring).
start = html.index('const OPPSLAG'); slutt = html.index('const QS = [')
biter = [(t, 'mal') for t in re.findall(r'«([^«»]{4,})»', html[start:slutt])]
qx = re.findall(r"^\s*\['[a-z]+', '[a-z]', '(?:[^'\\]|\\.)*', '(?:[^'\\]|\\.)*', \['((?:[^'\\]|\\.)*)'.*?\], '((?:[^'\\]|\\.)*)'", html, re.M)
for svar, ex in qx:
    for t in re.findall(r'«([^«»]{4,})»', svar + ' ' + ex): biter.append((t, svar[:70]))
bok2_ut = bok2.replace(' ', '')
feil = 0
for t, hvor in biter:
    if '${' in t or '<' in t or re.match(r'UN \d{4} |TOMT KOLLI, |Spesiell bestemmelse 640[A-H]$', t): continue  # linjer i transportdokumentet laget etter mønsteret i boka
    n = norm(t.replace('…', '').replace('¹', '').replace('²', ''))
    if n not in bok2 and n.replace(' ', '') not in bok2_ut:
        feil += 1; print(f'SITAT IKKE I BOKA: «{t}» | {hvor}')
print(f'{feil} sitater i riktige svar og forklaringer som ikke står ordrett i boka')
