import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
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

    print("=== Spor D: Forklarbar KI ===")
    print(f"Test accuracy: {acc:.3f}\n")

    importances = model.feature_importances_
    pairs = sorted(zip(X.columns, importances), key=lambda x: x[1], reverse=True)

    print("Feature importance (høyere = større påvirkning):")
    for name, imp in pairs:
        print(f"  {name:12s}: {imp:.3f}")

    print("\nTips: Forklar hvorfor dette kan gi bias hvis dataene er skjeve.")

if __name__ == "__main__":
    main()
