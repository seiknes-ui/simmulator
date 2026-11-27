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
- Står svaret ikke i ADR-boka eller forskriften, men i DSBs læreplan, på dsb.no, hos Statens vegvesen eller i en standard (for eksempel brannklassene i EN 2), skal spørsmålet merkes i `UTENFOR_BOKA` med kilden, for eksempel «Ikke i boka – fra DSBs læreplan (2.5)». Eleven skal se at svaret ikke kan slås opp i boka.
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

## Ordlyden fra boka i svaret
Spørsmålene kan skrives om til situasjoner fra jobben, men når ordlyden er viktig for å finne riktig svar, skal svaret bruke nøyaktig samme ord som boka. Det gjelder særlig:
- tall og grenser: «minst», «høyst», «over», «ikke over», «mer enn» skal stå slik boka sier det, med samme tall og enhet
- plikt og valg: «skal», «får ikke», «kan» og «så vidt mulig» skal ikke byttes med hverandre eller med «må» og «bør»
- faste uttrykk og definerte ord: «transportenhet», «kolli», «tom, ikke rengjort», «TOMT KOLLI», «OVERPAKNING», «MILJØFARLIG» og andre ord fra 1.2.1 eller teksten som skal stå på merker og i dokumenter
Sjekk svaret mot avsnittet i boka før det skrives inn, og kjør `verktoy/ordlyd.py`, som finner grenser og tall i svarene som ikke står likt i boka. Feilalternativene kan gjerne ligge nær ordlyden, så eleven må lese nøye.

## Fotnoter og merknader
Les alltid fotnotene under tabellene og merknadene (ANM) i avsnittet før en regel skrives inn. De endrer ofte hovedregelen for bestemte UN-numre, klasser eller mengder. Fotnotehenvisningen kan stå i kolonneoverskriften (for eksempel «Tank (l)c» og «Bulk (kg)d» i 1.10.3.1.2), i selve cellene (for eksempel «a)» og «b)»), eller som et lite tall i teksten med fotnoten helt nederst på siden (for eksempel «Øyeskyllemiddel¹» og «spade²» i 8.1.5). I tekstutgaven av boka havner fotnotene fra bunnen av siden midt i teksten, rett før sidetallet, så se etter dem der. Eksempler:
- 1.1.3.6.3 fotnote a): UN 0081, 0082, 0084, 0241, 0331, 0332, 0482, 1005 og 1017 har største samlede mengde 50 kg, og ganges med 20 ved blandet last (1.1.3.6.4)
- 1.10.3.1.2: a) «Ikke relevant» og b) «Bestemmelsene i 1.10.3 gjelder ikke, uansett mengde» i cellene (for eksempel bensin og propan i kolli), c) og d) i overskriftene for tank og bulk: verdien gjelder bare når Tabell A tillater tank eller bulk
- 7.5.2.1 fotnote 1/–4/: når klasse 1 likevel kan samlastes
- 8.1.5.2 og 8.1.5.3 fotnotene: hvilke faresedler som krever øyeskyllemiddel, spade, tetning for sluk og oppsamlingsbeholder
Kjør `verktoy/fotnoter.py`, som finner fotnoter i boka som nevner UN-numre og viser hvor kurset bruker de samme UN-numrene sammen med avsnittet. Les treffene og sjekk at fotnoten er tatt med. Fotnoter uten UN-nummer må sjekkes for hånd.

## Entydige spørsmål og alternativer
- Spør du om en tabell, kolonne eller fotnote, skal spørsmålet si hvilken: for eksempel «tabell 1.10.3.1.2 (liste over farlig gods med høy risiko), kolonnen «Kolli (kg)»», «kolonne (15) i Tabell A» eller «fotnote 1 til «Øyeskyllemiddel» i 8.1.5.2». Bruk ordene fra fotnoten («ikke nødvendig», «bare nødvendig») i spørsmål og svar.
- Spørsmålet skal ha alle opplysningene som trengs for ett riktig svar, for eksempel at beholderen brukes til farlig gods, eller at lasten har flere transportkategorier.
- Alternativene skal være av samme slag som det det spørres om: spørres det om poeng, skal alle alternativene være poeng, ikke blandet med liter og kg.
- Et feilalternativ skal ikke være riktig i et unntak eller en fotnote (for eksempel 50 kg for dynamitt etter fotnote a) i 1.1.3.6.3). Bruk et annet tall, eller still spørsmålet slik at unntaket er med.

## Signalord
Signalordene må, skal, alltid, aldri, påbudt og forbudt markeres automatisk med farge (funksjonen `sig()`), og sterkere når to står i samme setning. I fagstoffet vises markeringen hele tiden. I spørsmål og svaralternativer skal de ikke markeres før svaret er avslørt (`flaggSignal()` i `answer()`). Bruk dem bevisst i spørsmål og svar, og la ikke alternativer med «alltid» eller «aldri» alltid være de gale, så elevene må lese og tenke.
