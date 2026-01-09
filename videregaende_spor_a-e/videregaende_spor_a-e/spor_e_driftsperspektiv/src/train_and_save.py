import os
import joblib
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def ensure_dirs():
    os.makedirs("models", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

def main():
    ensure_dirs()
    logging.basicConfig(
        filename="logs/train.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    data = pd.read_csv("data/klassifisering.csv")
    X = data.drop("besto", axis=1)
    y = data["besto"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(random_state=42, n_estimators=300)
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)

    joblib.dump(model, "models/model.pkl")

    logging.info("Model trained. Test accuracy=%.3f", acc)
    print("=== Spor E: Trening ferdig ===")
    print(f"Test accuracy: {acc:.3f}")
    print("Lagret modell: models/model.pkl")
    print("Logg: logs/train.log")

if __name__ == "__main__":
    main()
