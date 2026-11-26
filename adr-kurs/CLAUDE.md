# ADR grunnkurs – retningslinjer for innhold

Kurset er for sjåfører som tar ADR grunnkurs, og for bedriftene de jobber i.
Vurder alltid hva som er aktuelt for en sjåfør eller en bedrift når du lager spørsmål, fagstoff og laber.

## Hva som tas med
- **Sjåføren:** det sjåføren møter på jobben: lasting og lossing, merking og skilt, dokumenter og utstyr i bilen, kjøring og parkering, tunneler, kontroll på vegen og ulykker.
- **Bedriften:** det avsender, transportør, laster eller sikkerhetsrådgiver trenger: plikter, opplæring, emballasje, klassifisering, avfall, varsling og godkjenning av kjøretøy.
- Skriv spørsmålene som situasjoner fra jobben («Du skal kjøre bensin i tank …»), ikke som rene oppslagsøvelser.
- Kurset handler om transport i Norge. Ta ikke med internasjonale regler (transport over grensen, multilaterale avtaler, språk på merking over grensen, regler for sjø, fly og bane). Unntak: dokumenter, som språk i transportdokument og skriftlige instruksjoner. Emne l (multimodal transport) dekkes kort, med kjøring til og fra havna.
- Ta ikke med boktrivia som verken sjåføren eller bedriften har praktisk nytte av, som hvordan et kapittel er nummerert innvendig eller koder for multimodale tanker og bulk.

## Merking av målgruppe
Spørsmål i `QS` kan ha et sjuende felt for målgruppe:
- ingen verdi: først og fremst for sjåføren
- `'b'`: mest for bedriften (vises som «For bedriften»)
- `'sb'`: for både sjåfør og bedrift

## Kilder og sidetall
- Alt skal bygge på ADR/RID 2025 og forskrift om landtransport av farlig gods fra DSB. Sjekk fakta i boka før de skrives inn.
- Sidetall lages med `verktoy/bokreferanser.py`. Kjør den etter hver endring av kilder eller fagstoff, og ikke skriv sidetall for hånd.

## Sjekk sammenhenger i andre kapitler
Når noe nytt legges inn, skal du alltid se etter hvordan det henger sammen med andre kapitler i boka, og ta det med:
- **Tabell A:** hvilke kolonner viser til regelen (for eksempel (6) → 3.3, (7a) → 3.4, (7b) → 3.5, (15) → 1.1.3.6 og 8.6, (18) → 7.5.11, (19) → 8.5, (20) → 5.3.2.3)?
- **Unntakene:** gjelder regelen innenfor 1000 poeng (listen i 1.1.3.6.2), for LQ (3.4.1), for EQ (3.5.1.1), for privatpersoner og firma (1.1.3.1) og for tom emballasje (1.1.3.5)?
- **Spesielle bestemmelser:** endrer en S-kode (8.5), en V-, VC- eller CV-kode (7.2.4, 7.3.3, 7.5.11) eller en spesiell bestemmelse (3.3) regelen?
- **Sikring:** gjelder 1.10 og høy risiko (1.10.3), og når gjelder 1.10 ikke (1.10.4)?
- **Dokumenter og instruksjoner:** hva skal stå i transportdokumentet (5.4.1), og hva sier de skriftlige instruksjonene (5.4.3.4)?
- **Forskriften:** har den en norsk særregel (for eksempel §§ 4–6, § 9, § 12, § 15, § 18 a, § 30)?
- **Kurset:** finnes det fagstoff, spørsmål eller laber om det samme fra før? Oppdater dem, så de ikke sier noe annet.

Skriv sammenhengene inn i fagstoffet («Henger sammen med …»), og lag gjerne spørsmål som krever at eleven bruker to kapitler.

## Signalord
Signalordene må, skal, alltid, aldri, påbudt og forbudt markeres automatisk med farge (funksjonen `sig()`), og sterkere når to står i samme setning. Bruk dem bevisst i spørsmål og svar, og la ikke alternativer med «alltid» eller «aldri» alltid være de gale, så elevene må lese og tenke.
