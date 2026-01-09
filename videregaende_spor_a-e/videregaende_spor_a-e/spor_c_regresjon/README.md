# Spor C – Regresjon (tallprediksjon)
Her predikerer vi et **tall** (karakter), ikke en kategori.

## Læringsmål
- skille mellom klassifisering og regresjon
- lære evalueringsmål for regresjon: MAE/RMSE/R²
- forstå at “feil” måles som avvik

## Hva skal jeg få til? (kort)
- Tren en regresjonsmodell som predikerer et **tall** (karakter).
- Noter **MAE, RMSE og R²**.
- Endre features (fjern/legg til en kolonne) og forklar hvordan det påvirker feil.

## Datasett
`data/regresjon.csv`
- X: timer_lekser, soevn, fravaer
- y: karakter (1.0–6.0)

## Kjøring
```bash
python src/spor_c.py
```

## Oppgave
1. Kjør og noter MAE, RMSE og R².
2. Fjern/legg til en feature (kolonne) og se hvordan resultat endrer seg.
3. Refleksjon:
   - Hvilken type feil er “verst” i dette eksempelet?
   - Hvilke data ville gjort modellen mer rettferdig/robust?
