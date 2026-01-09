# Spor A – Modellsammenligning (supervised)
Du skal sammenligne flere modeller på **samme datasett** og forklare forskjellene.

## Læringsmål
- forstå at «KI» ikke er én algoritme
- se hvordan modellvalg påvirker resultat (score, stabilitet)
- trene på å argumentere for tekniske valg

## Hva skal jeg få til? (kort)
- Kjør minst **3 modeller** og sammenlign test-resultat (accuracy).
- Endre minst **én ting** (f.eks. parameter eller datasplitt) og noter hva som skjer.
- Forklar i README hva som er forskjellen på modellene, og **hvorfor du ville valgt en av dem**.

## Datasett
`data/klassifisering.csv`
- X: timer_lekser, fravaer, soevn
- y: besto (0/1)

## Kjøring
Fra mappen `spor_a_modellsammenligning`:
```bash
python src/spor_a.py
```

## Oppgave
1. Kjør skriptet og noter test-score for hver modell.
2. Endre én ting (f.eks. test_size, random_state, eller model-parametere) og se hva som skjer.
3. Skriv i README i hovedprosjektet ditt:
   - Hvilken modell var best og hvorfor tror du det?
   - Hva kan være ulempen med «mest nøyaktig» modell?
