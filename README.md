# KI, Maskinlæring og LLM - Uke 2

## Introduksjonsoppgave

1) Dette er ikke maskinlæring fordi det er blitt satt regler for maskinen av oss mennesker, og på forhånd. Det er ingen KI som har blitt trent på data, resultatene er basert på regler vi satt og variabler som settes inn.

2) "fit" og "predict" er to metoder som brukes til maskinlæring. Fit er metoden som trener maskinen opp på data, mens predict brukes til å lage et nytt svar som den baserer på tidligere mønstre.

3) 

### Problem

Modellen (fra csv_modell.py) vi har laget med python forsøker å forutsi om man består eller ikke består på skolen. Den bestemmer dette utifra de tre ulike faktorene søvn, fravær og antall timer brukt på lekser.

### Data
Datasettet består av disse kolonnene:
- **timer_lekser**: Hvor mange timer eleven har brukt på lekser
- **fravaer**: Hvor mange dager eleven har vært borte fra skolen
- **soevn**: Hvor mange timer søvn eleven har fått
- **besto**: Om eleven besto eller ikke (boolean)

### Resultat
Modellen deles i treningsdata og testdata, og resultatet måles med en test score (accuracy). Test scoren viser hvor ofte modellen gjetter riktig på testdataene, og jeg fikk en score på 1.0.

### Begrensninger
Datasettet er veldig lite, så modellen kan lett bli unøyaktig. Derfor kan resultatet være upålitelig, men funker i dette eksempelet for å lære hvordan maskinlæring fungerer.

---

## Spor E - Driftsperspektiv

### Hvilke data er sensitive?

Det er visse data i dette sporet som ikke bør deles fordi den er personlig, og slike data finner vi i predict.log og klassifisering.csv. Disse filene inneholder data om elever som ikke bør deles. Selv om train.log også er logg-fil, inneholder den bare data som viser test score-tall.

### Hvem skal ha tilgang til loggene?

God sikkerhet er å følge "least privelege principle" og bare gi tilgang til de som trenger det, spesielt på filer som dette. Det vil si utviklere som trener modellen og eventuelle medutviklere som trenger å kvalitetsjekke arbeidet deres. Dette gjelder da for predict.log som inneholder sensetiv data, mens train.log kan vises i dokumentasjon på Github for eksempel, altså alle (eller firmaet).

### Hva skjer hvis input-data er feil eller mangler?

Hvis input-data er feil eller mangler, kan modellen gi feil eller en dårlig prediksjon.
