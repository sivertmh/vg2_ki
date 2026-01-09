# Spor B – Clustering (usupervised)
Her finnes **ingen fasit** (ingen label). Modellen prøver å finne grupper selv.

## Læringsmål
- forstå forskjellen på supervised og unsupervised læring
- lære å tolke om grupper gir mening (ikke bare “score”)
- se at dataskala kan påvirke resultat

## Hva skal jeg få til? (kort)
- Kjør clustering og få en **cluster-label** (gruppe) for hver rad.
- Test minst **to ulike k-verdier** (f.eks. 2 og 4) og sammenlign.
- Beskriv hva som kjennetegner gruppene og om de **gir mening**.

## Datasett
`data/clustering.csv`
Kolonner: alder, forbruk, besok_per_uke

## Kjøring
```bash
python src/spor_b.py
```

## Oppgave
1. Kjør skriptet og se hvor mange elever/objekter som havner i hver cluster.
2. Endre `k` (antall grupper) og observer endringer.
3. Svar i README:
   - Hvilket k ga mest mening, og hvorfor?
   - Hvorfor må vi ofte skalere data før clustering?
