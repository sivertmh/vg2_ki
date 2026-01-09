# VG2 KI – Elevguide for videregående spor (A–E)

## (WSL + Debian + Python + scikit-learn)

Når du er ferdig med **Introduksjonsoppgaven** og **Ollama-oppgaven** jobber du jobbe videre med Spor A-E.
Du velger **to** spor. Sporene er uavhengige, men bygger på samme grunnidé:
**data → train/test → modell → evaluering → refleksjon**.

---

## Før du starter (gjelder alle spor)

1. Åpne Debian (WSL) og gå til mappen for denne pakken.
2. Lag/aktiver virtuelt miljø:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Installer pakker:

```bash
pip install -r requirements.txt
```

---

## Hvordan kjøre et spor

Hvert spor har en egen mappe med `README.md`, `src/` og `data/`.

Eksempel (spor A):

```bash
cd spor_a_modellsammenligning
python src/spor_a.py
```

Hvis et spor støtter parametre:

```bash
python src/spor_x.py --help
```

---

## Hva du skal levere (for et videregående spor)

I prosjekt-repoet ditt skal du i tillegg levere:

- koden du brukte (filer i `src/`)
- kort beskrivelse i `README.md` (problem, metode, resultat, begrensninger)
- refleksjon: _hva lærte du, hva kan gå galt, bias/personvern_

**Viktig:** Du blir ikke vurdert på “høyest score”, men på forståelse og dokumentasjon.

---

## Sporoversikt

### Spor A – Modellsammenligning (supervised)

Du sammenligner 2–3 modeller på samme datasett, og forklarer forskjellene.

### Spor B – Clustering (unsupervised)

Du grupperer data uten fasit (ingen label). Målet er å tolke om gruppene gir mening.

### Spor C – Regresjon (tallprediksjon)

Du predikerer et tall (ikke kategori) og evaluerer med MAE/RMSE/R².

### Spor D – Forklarbar KI (XAI light)

Du finner hvilke features som påvirker prediksjonen mest og diskuterer rettferdighet.

### Spor E – Driftsperspektiv (IT-drift)

Du gjør modellen mer “produksjonsnær”: logging, kommando-linje, enkel prediksjonskøyring
og refleksjon om datahåndtering/personvern.

---

## Tips når du står fast

- Har du `(venv)`? → `source venv/bin/activate`
- Er du i riktig mappe? → `pwd` og `ls`
- Mangler pakker? → `pip install -r requirements.txt`

## Modellforklaring (anbefalt å lese)

For å forstå hva du faktisk gjør i sporene A–E, les denne teksten først:

- **MODELLFORKLARING_MODELLER_OG_FORSKJELLER.md**

Kort sagt:

- Spor A/D = **klassifisering** (kategori 0/1)
- Spor C = **regresjon** (tall)
- Spor B = **clustering** (grupper uten fasit)
- Spor E = **drift** (modell som system: lagring, CLI, logging)

Tips: bruk modellforklaringen når du skriver refleksjon i README.
