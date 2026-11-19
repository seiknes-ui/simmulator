"""Beskjærer DSB-faresedlene fra NDLA til selve ruta og fjerner «Nr. x»-teksten over.
Bruk: python -I beskjaer-faresedler.py <inn-mappe> <ut-mappe>"""
import re
import sys
from pathlib import Path

inn, ut = Path(sys.argv[1]), Path(sys.argv[2])
ut.mkdir(parents=True, exist_ok=True)
# filnavn hos NDLA -> navn på siden
NAVN = {'1': '1', '1.4': '1.4S', '2.1': '2.1', '2.2': '2.2', '2.3': '2.3', '3': '3', '4.1': '4.1', '4.2': '4.2',
        '4.3': '4.3', '5.1': '5.1', '5.2': '5.2', '6.1': '6.1', '6.2': '6.2', '7A': '7', '8': '8', '9': '9'}

for src, dst in NAVN.items():
    s = (inn / f'{src}.svg').read_text(encoding='utf-8')
    assert not re.search(r'<script|<foreignObject|\bon\w+=|javascript:|href="http', s, re.I), src
    # største rute = ytterkanten av fareseddelen
    best = None
    for pts in re.findall(r'<(?:polygon|polyline)[^>]*points="([^"]+)"', re.sub(r'<defs>.*?</defs>', '', s, flags=re.S)):
        xy = [float(v) for v in re.findall(r'-?\d+(?:\.\d+)?', pts)]
        xs, ys = xy[0::2], xy[1::2]
        if len(xs) < 4:
            continue
        box = (min(xs), min(ys), max(xs), max(ys))
        if best is None or (box[2] - box[0]) > (best[2] - best[0]):
            best = box
    x0, y0, x1, y1 = best
    side = max(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = f'{cx - side / 2:.2f} {cy - side / 2:.2f} {side:.2f} {side:.2f}'
    s = re.sub(r'width="300px" height="300px" viewBox="0 0 300 300" style="[^"]*"', f'viewBox="{vb}"', s, count=1)
    assert f'viewBox="{vb}"' in s, src
    # fjern «Nr. x» (én eller to tekstnoder øverst, y < 40)
    s = re.sub(r'\s*<text transform="matrix\(1 0 0 1 [\d.]+ (\d+\.?\d*)\)"[^>]*>[^<]*</text>',
               lambda m: '' if float(m.group(1)) < 40 else m.group(0), s)
    # Illustrator-fontnavn finnes ikke i nettleseren
    s = s.replace("font-family:'Helvetica-Bold';", "font-family:Helvetica,Arial,sans-serif;font-weight:bold;")
    s = s.replace("font-family:'Helvetica';", "font-family:Helvetica,Arial,sans-serif;")
    if dst == '1.4S':
        s, n = re.subn(r'>G</text>', '>S</text>', s)
        assert n == 1
    s = s.replace('<!-- Generator:', f'<!-- DSB via NDLA (CC BY-SA 4.0), beskåret{" og endret til 1.4S" if dst == "1.4S" else ""}. Generator:', 1)
    (ut / f'{dst}.svg').write_text(s, encoding='utf-8')
    print(dst, vb)
