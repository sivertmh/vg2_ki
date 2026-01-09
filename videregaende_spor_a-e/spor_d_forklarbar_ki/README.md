# Spor D – Forklarbar KI (XAI light)
Her skal du **forklare hvorfor** modellen predikerer som den gjør.

## Læringsmål
- forstå at modeller kan være “black box”
- hente ut feature importance
- koble forklaring til bias/etikk

## Hva skal jeg få til? (kort)
- Tren modellen og få ut en liste over **feature importance**.
- Forklar hvilke variabler som påvirker prediksjonen mest og om det virker rimelig.
- Skriv en kort refleksjon om **bias/personvern**: hva kan gå galt hvis dataene er skjeve?

## Datasett
`data/klassifisering.csv`
- X: timer_lekser, fravaer, soevn
- y: besto (0/1)

## Kjøring
```bash
python src/spor_d.py
```

## Oppgave
1. Kjør og se “feature importances”.
2. Diskuter: Gir dette mening? Hvilke features dominerer?
3. Refleksjon (skriv i README):
   - Hvilke variabler burde vi *ikke* bruke i en ekte modell, og hvorfor?
   - Hvordan kan forklarbarhet hjelpe oss å oppdage bias?
