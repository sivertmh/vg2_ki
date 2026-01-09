# Spor E – Driftsperspektiv (IT-drift)
Dette sporet handler om å gjøre løsningen mer “produksjonsnær”:
- tydelig kjøring fra kommandolinje
- logging til fil
- forutsigbar mappestruktur
- refleksjon om personvern og ansvar

## Læringsmål
- forstå at KI er et system som må driftes
- lære enkel logging og parameterstyring (argparse)
- tenke sikkerhet/personvern for data

## Hva skal jeg få til? (kort)
- Kjør `train_and_save.py` slik at det lages `models/model.pkl` og en loggfil.
- Kjør `predict_cli.py` minst **3 ganger** med ulike input-verdier.
- Forklar hva logging er, og skriv en refleksjon om **tilgang/personvern** for data og logger.

## Datasett
`data/klassifisering.csv` (brukes til å trene en modell lokalt)

## Kjøring (to steg)
### 1) Tren og lagre modell
```bash
python src/train_and_save.py
```

Dette lager:
- `models/model.pkl` (lagret modell)
- `logs/train.log` (logg)

### 2) Kjør prediksjon på én “bruker-input”
```bash
python src/predict_cli.py --timer_lekser 4 --fravaer 3 --soevn 7
```

Dette skriver prediksjon og logger til `logs/predict.log`.

## Oppgave
1. Tren modellen og sjekk at filer i `models/` og `logs/` blir laget.
2. Kjør 3 ulike prediksjoner med ulike input.
3. Skriv i README:
   - Hvilke data er sensitive?
   - Hvem skal ha tilgang til loggene?
   - Hva skjer hvis input-data er feil eller mangler?
