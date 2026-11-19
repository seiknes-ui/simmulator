"""Lager sidetallene som ADR-siden viser når eleven svarer feil («Slå opp i boka»).

Leser teksten fra DSBs ADR/RID 2025 og finner siden der hvert avsnitt og hver paragraf
som brukes som kilde i index.html, begynner. Resultatet skrives inn mellom
// BOK-START og // BOK-SLUTT i index.html.

Bruk:
  1. Last ned https://www.dsb.no/siteassets/rapporter-og-publikasjoner/veileder/adrrid-2025.pdf
  2. pdftotext -raw -enc UTF-8 adrrid-2025.pdf adr.txt
  3. python bokreferanser.py adr.txt ../index.html

Sidetallene gjelder 1. opplag 2025, der sidetallet i PDF-en er det samme som i boka.
"""
import json, re, sys

# Avsnitt der overskriften i teksten ikke begynner med nummeret
ALIAS = {'3.2.2': r'Tabell B: Alfabetisk'}
SEC = re.compile(r'\b\d{1,2}\.\d{1,2}(?:\.\d{1,2}){0,4}\b')
PAR = re.compile(r'§\s*(\d+a?)')


def main(txt_path, html_path):
    pages = open(txt_path, encoding='utf-8').read().split('\f')
    html = open(html_path, encoding='utf-8').read()

    # Alle kilder: tredje felt i spørsmålene, src i labene og faste «Kilde:»-tekster
    srcs = set(re.findall(r"^\s*\['\w+', '[a-o]', '([^']*)'", html, re.M))
    srcs |= set(re.findall(r"src: '([^']*)'", html))
    srcs |= set(re.findall(r"kildeHTML\('([^']*)'", html))

    # Kapitler fra innholdsfortegnelsen: «Kapittel 8.3. Tittel......1614»
    chapters = {}
    # Lange titler går over flere linjer
    for m in re.finditer(r'^Kapittel (\d{1,2}\.\d{1,2})\. ((?:(?!Kapittel )[^.\f]|\.(?!\.\.))+?)\.{3,}\s*(\d+)\s*$', '\f'.join(pages[:12]), re.M):
        # Fjern kontrolltegn fra PDF-en, og slå sammen linjeskift
        title = ' '.join(''.join(c if c >= ' ' else ' ' for c in m.group(2)).split())
        chapters.setdefault(m.group(1), (title, int(m.group(3))))
    # Innholdslister med prikker gir sidetallet når overskriften ikke står på egen linje i teksten
    toc_pages = {}
    for m in re.finditer(r'^(\d{1,2}\.\d{1,2}(?:\.\d{1,2})*) [^\n]*?\.{3,}\s*(\d+)\s*$', '\f'.join(pages), re.M):
        toc_pages.setdefault(m.group(1), int(m.group(2)))

    # En ekte overskrift følges av brødtekst eller av et av sine egne underavsnitt. I tabeller og
    # lister som bare ramser opp avsnitt, følges den av et annet avsnittsnummer.
    def first_page(pattern, start=1, end=len(pages), sec=None):
        fallback = None
        for i in range(start - 1, min(end, len(pages))):
            lines = [l for l in pages[i].split('\n') if l.strip()]
            for j, line in enumerate(lines):
                if '....' in line or not re.match(pattern, line):
                    continue
                fallback = fallback or i + 1
                nxt = lines[j + 1] if j + 1 < len(lines) else ''
                m = re.match(r'(\d{1,2}\.\d{1,2}(?:\.\d{1,2})*)(\s|$)', nxt)
                if sec is None or not m or m.group(1).startswith(sec + '.'):
                    return i + 1
        return fallback

    bok, kap = {}, {}
    for src in srcs:
        for sec in SEC.findall(src):
            ch = '.'.join(sec.split('.')[:2])
            if ch not in chapters:
                continue
            kap[ch] = chapters[ch][0]
            # Avsnittet letes etter fra kapittelets første side, så henvisninger i løpende tekst
            # tidligere i boka ikke blir tatt for overskriften
            p = chapters[ch][1] if sec == ch else first_page(ALIAS.get(sec, re.escape(sec) + r'(\s|$)'), chapters[ch][1], sec=sec) or toc_pages.get(sec)
            if p:
                bok[sec] = p
            else:
                print('fant ikke', sec, 'i', src, file=sys.stderr)
        for par in PAR.findall(src):
            p = first_page(r'§ ' + re.escape(par) + r'\. ', 15, 46)
            if p:
                bok['§' + par] = p
            else:
                print('fant ikke §', par, file=sys.stderr)

    block = ('// BOK-START (lages av verktoy/bokreferanser.py – ikke rediger for hånd)\n'
             'const BOK = ' + json.dumps(dict(sorted(bok.items())), ensure_ascii=False) + ';\n'
             'const KAP = ' + json.dumps(dict(sorted(kap.items())), ensure_ascii=False) + ';\n'
             '// BOK-SLUTT')
    new = re.sub(r'// BOK-START.*?// BOK-SLUTT', lambda _: block, html, flags=re.S)
    if new == html and '// BOK-START' not in html:
        sys.exit('fant ikke // BOK-START i ' + html_path)
    open(html_path, 'w', encoding='utf-8').write(new)
    print(len(bok), 'sidetall og', len(kap), 'kapitler skrevet')


if __name__ == '__main__':
    main(*sys.argv[1:3])
