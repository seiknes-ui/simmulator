---
name: sjekk-oppgave
description: Sjekker en ADR-oppgave fra et bilde (for eksempel fra en oppgavesamling eller en prøve) mot ADR/RID 2025 og forskriften fra DSB. Finner riktig svar i boka med sidetall og sitat, sier om svaret på bildet er riktig, og forklarer hva som er feil. Bruk når brukeren sender bilde av en ADR-oppgave eller ber om å sjekke en oppgave.
---

# Sjekk en ADR-oppgave mot boka

Brukeren sender et bilde av én eller flere oppgaver, ofte med et svar som er krysset av eller skrevet inn. Svar på norsk bokmål, kort og presist. Følg også `adr-kurs/CLAUDE.md` (ordlyden fra boka, fotnoter, sammenhenger, norske regler).

## 1. Les oppgaven
- Skriv av oppgaveteksten og alle svaralternativene ordrett fra bildet. Marker hvilket svar som er valgt eller oppgitt som fasit, hvis det synes.
- Er noe uleselig, si det og gjett ikke. Er det flere oppgaver på bildet, ta én og én.

## 2. Hent boka
- Teksten ligger i `$ADR_BOK/adr.txt` (standard `/tmp/adr-bok/adr.txt`). Finnes den ikke, kjør `bash adr-kurs/verktoy/hent_bok.sh`. Den henter ADR/RID 2025 fra www.dsb.no og lager tekst med én side per PDF-side, så sidetallene blir de samme som i boka.
- Svikter nedlastingen (nettverket tillater ikke www.dsb.no), si det til brukeren og svar ikke fra hukommelsen.

## 3. Finn svaret i boka
Bruk `python3 -I adr-kurs/verktoy/sok_i_boka.py <adr.txt> …`:
- `ord ord …` finner linjer med alle ordene, med side og avsnitt
- `--avsnitt 7.5.5.3` viser hele avsnittet og fotnotene nederst på sidene det står på
- `--un 1203` viser radene i Tabell A (husk at en rad er delt på to sider: kolonne (1)–(9b) og (10)–(20))
- `--side 1605` viser en hel side

Les alltid:
- hele avsnittet, ikke bare treffet, og merknadene (ANM)
- fotnotene: i tabellcellene (a), b)), i kolonneoverskriftene (for eksempel «Tank (l)c») og nederst på siden (små tall i teksten)
- unntakene som kan endre svaret: 1.1.3.1, 1.1.3.5, 1.1.3.6 og listen i 1.1.3.6.2, 3.4 (LQ), 3.5 (EQ), spesielle bestemmelser i kolonne (6) og S-, V- og CV-koder
- forskriften om landtransport av farlig gods (først i boka) når oppgaven gjelder norske regler, for eksempel §§ 4–6, § 9, § 12, § 18 a, § 30
Står svaret ikke i boka eller forskriften (for eksempel brannklasser fra EN 2, førstehjelp eller DSBs veiledninger), si det tydelig.

## 4. Svar slik
**Oppgaven:** oppgaveteksten og alternativene, kort.

**Riktig svar:** alternativet eller svaret, med bokas ordlyd.

**Vurdering:** ✅ Riktig / ❌ Feil / ⚠️ Delvis riktig eller oppgaven er uklar.

**Hva er feil:** hvorfor det valgte svaret er feil, og hva som gjør det riktige svaret riktig. Er oppgaven selv feil, utdatert (eldre ADR-utgave) eller tvetydig, si det og forklar hvorfor.

**Kilde:** avsnitt og side, med et kort ordrett sitat fra boka. Ta med fotnoten eller merknaden hvis den avgjør svaret.

**Henger sammen med:** andre avsnitt eleven bør kjenne (én linje).

Er du usikker, si hva du er usikker på og hva som skal til for å avgjøre det. Foreslå til slutt, på én linje, om oppgaven bør legges inn i ADR-kurset (`adr-kurs/index.html`) og hvor.
