import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def main():
    data = pd.read_csv("data/klassifisering.csv")
    X = data.drop("besto", axis=1)
    y = data["besto"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "DecisionTree": DecisionTreeClassifier(random_state=42),
        "RandomForest": RandomForestClassifier(random_state=42, n_estimators=200),
        "LogisticRegression": LogisticRegression(max_iter=2000)
    }

    print("=== Spor A: Modellsammenligning ===")
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        acc = accuracy_score(y_test, pred)
        print(f"{name:18s}  accuracy = {acc:.3f}")

    print("\nTips: Endre test_size/random_state eller parametere og kjør igjen.")
    print("Husk: Høy score betyr ikke alltid rettferdig eller robust modell.")

if __name__ == "__main__":
    main()
