# Modellforklaring – hva gjør modellene, og hva er forskjellen?
*(Denne teksten hører til videregående spor A–E og kan brukes i elevheftet/README.)*

## Hva er en «modell» i maskinlæring?
En **modell** er et program som prøver å lære en sammenheng mellom:
- **X (features)** = input (kolonner/variabler)
- **y (target/label)** = fasiten vi vil forutsi

Når du trener modellen (`fit`), lærer den et mønster fra treningsdata.
Når du predikerer (`predict`), bruker den mønsteret til å gjette svar på nye data.

---

## Klassifisering vs regresjon vs clustering
### 1) Klassifisering (Spor A og D)
Du forutsier en **kategori** (klasse).
- Eksempel: bestått (1) / ikke bestått (0)

### 2) Regresjon (Spor C)
Du forutsier et **tall**.
- Eksempel: karakter (1–6)

### 3) Clustering (Spor B)
Du finner **grupper** uten fasit (ingen label-kolonne).
- Modellen finner mønstre og grupper selv

---

# Spor A – Modellene dere sammenligner (klassifisering)

## A1) Decision Tree (beslutningstre)
**Tenk på det som if/else-regler som modellen lager selv.**

Hvordan den «tenker» (forenklet):
- «Hvis fravær > 12 → sannsynlig ikke bestått»
- «Ellers hvis timer_lekser > 4 → sannsynlig bestått»

**Fordeler**
- Lett å forklare
- Rask å trene

**Ulemper**
- Kan lett bli for tilpasset treningsdata (**overfitting**)
- Resultatet kan endre seg mye hvis data endres litt

**Hva du skal se etter**
- Er score stabil mellom kjøringer?
- Gir logikken mening?

---

## A2) Random Forest (mange trær som «stemmer»)
**En Random Forest er mange beslutningstrær som tar en flertallsavgjørelse.**

Hvordan den «tenker»:
- Mange trær gir hver sin prediksjon
- Skogen velger det svaret flest trær mener

**Fordeler**
- Ofte bedre score enn ett enkelt tre
- Mer robust (mindre overfitting)
- Tåler støy i data bedre

**Ulemper**
- Vanskeligere å forklare enn ett tre
- Mer «black box»

**Hva du skal se etter**
- Får du bedre og mer stabil score enn Decision Tree?
- Husk: høy score betyr ikke automatisk rettferdig modell

---

## A3) Logistic Regression (lineær klassifisering)
Navnet er litt misvisende: den brukes ofte til **klassifisering**.

**Tenk på den som en modell som lager en «grense» mellom klassene.**
Den finner en formel som gir en sannsynlighet for 0/1.

**Fordeler**
- Enkel og stabil «baseline»
- Ofte lett å forklare som «formel/grense»
- God når sammenhengen er ganske «rettlinjet»

**Ulemper**
- Fanger ikke opp kompliserte mønstre like godt som Random Forest
- Kan være dårlig hvis virkeligheten er «kronglete»

**Hva du skal se etter**
- Stabilitet (lignende score ved flere kjøringer)
- Ikke bli stresset av litt lavere score: dette er baseline

---

## Hvorfor gir modellene ulike svar?
Fordi de lærer på ulike måter:
- Decision Tree lager regler (kan overfitte)
- Random Forest bruker mange trær (mer robust)
- Logistic Regression lager en enkel grense (stabil baseline)

**Poenget er ikke bare å finne «vinneren», men å kunne begrunne valget ditt.**

---

# Spor B – KMeans (clustering)
I clustering finnes det ingen fasit.

## KMeans: «Finn k grupper»
KMeans deler data i **k grupper** slik at punkter i samme gruppe ligner mest på hverandre.

Hvordan den «tenker»:
- Lager k «sentrum»
- Flytter sentrum til de passer best
- Hvert punkt får cluster = nærmeste sentrum

**Viktige poeng**
- Du velger **k** selv (2, 3, 4…)
- Det finnes ikke alltid «riktig» svar – du må tolke

**Hva du skal gjøre**
- Test ulike k
- Beskriv hva som kjennetegner hver gruppe
- Vurder om gruppene gir mening

---

# Spor C – Linear Regression (regresjon)
Her predikerer du et **tall**, ikke en kategori.

## Linear Regression: «formel for tall»
Den prøver å finne en sammenheng som:
- karakter = a·timer_lekser + b·søvn + c·fravær + konstant

**Evalueringsmål**
- **MAE**: gjennomsnittlig absolutt feil (hvor mye bommer vi i snitt)
- **RMSE**: straffer store feil mer
- **R²**: hvor mye modellen forklarer (0 = dårlig, 1 = perfekt)

**Hva du skal gjøre**
- Noter MAE/RMSE/R²
- Prøv å fjerne/legge til en feature og se endring
- Forklar hvilken type feil som er «verst»

---

# Spor D – Forklarbar KI (feature importance)
Her prøver vi å forstå *hvorfor* modellen predikerer som den gjør.

## Feature importance (enkelt forklart)
- «Hvilke kolonner bruker modellen mest når den tar beslutninger?»

**Hva du skal gjøre**
- Finn de viktigste variablene
- Diskuter om dette er rettferdig
- Koble til bias/personvern:
  - Hvilke variabler burde vi *ikke* bruke i et ekte system?

---

# Spor E – Driftsperspektiv (KI som «system»)
Her gjør du løsningen mer «produksjonsnær».

Du lærer å:
1) trene og lagre modell til fil (`model.pkl`)
2) kjøre prediksjon fra kommandolinje (CLI)
3) logge hva som skjer (drift)

**Hva du skal reflektere over**
- Hvilke data er sensitive?
- Hvem skal ha tilgang til loggene?
- Hva skjer hvis input er feil/mangler?

---

## Klar elev-setning (til README/rapport)
> «Jeg valgte denne modellen fordi den lærer mønstre fra treningsdata, og jeg testet den på data den ikke har sett før. Resultatet viser både styrker og svakheter ved modellen.»
