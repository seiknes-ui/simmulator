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
