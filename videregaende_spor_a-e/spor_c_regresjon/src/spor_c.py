import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import math

def main():
    data = pd.read_csv("data/regresjon.csv")
    X = data.drop("karakter", axis=1)
    y = data["karakter"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, pred)
    rmse = math.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)

    print("=== Spor C: Regresjon ===")
    print(f"MAE  = {mae:.3f}")
    print(f"RMSE = {rmse:.3f}")
    print(f"R^2  = {r2:.3f}")
    print("\nTips: Sjekk koeffisientene (viktighet i lineær modell):")
    for name, coef in zip(X.columns, model.coef_):
        print(f"  {name:12s}: {coef:+.3f}")

if __name__ == '__main__':
    main()
