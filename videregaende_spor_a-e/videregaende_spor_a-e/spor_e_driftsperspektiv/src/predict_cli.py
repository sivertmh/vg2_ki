import argparse
import os
import joblib
import logging
import pandas as pd

def ensure_dirs():
    os.makedirs("logs", exist_ok=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timer_lekser", type=float, required=True)
    parser.add_argument("--fravaer", type=float, required=True)
    parser.add_argument("--soevn", type=float, required=True)
    args = parser.parse_args()

    ensure_dirs()
    logging.basicConfig(
        filename="logs/predict.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    model = joblib.load("models/model.pkl")

    X_new = pd.DataFrame([{
        "timer_lekser": args.timer_lekser,
        "fravaer": args.fravaer,
        "soevn": args.soevn
    }])

    pred = int(model.predict(X_new)[0])
    msg = "BESTÅTT (1)" if pred == 1 else "IKKE BESTÅTT (0)"

    logging.info("Predict input=%s pred=%s", X_new.to_dict(orient="records")[0], pred)
    print("=== Spor E: Prediksjon ===")
    print("Input:", X_new.to_dict(orient="records")[0])
    print("Prediksjon:", msg)
    print("Logg: logs/predict.log")

if __name__ == "__main__":
    main()
