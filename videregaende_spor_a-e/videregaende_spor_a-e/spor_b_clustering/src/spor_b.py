import argparse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, default=3, help="Antall clustere (k)")
    args = parser.parse_args()

    data = pd.read_csv("data/clustering.csv")
    X = data.values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(n_clusters=args.k, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)

    data_out = data.copy()
    data_out["cluster"] = labels
    print("=== Spor B: Clustering ===")
    print(data_out["cluster"].value_counts().sort_index())

    # enkel 2D-plot: alder vs forbruk (fargelagt per cluster)
    plt.figure()
    plt.scatter(data_out["alder"], data_out["forbruk"], c=data_out["cluster"])
    plt.xlabel("alder")
    plt.ylabel("forbruk")
    plt.title(f"KMeans clustering (k={args.k}) – alder vs forbruk")
    plt.tight_layout()
    plt.show()

    print("\nTips: Kjør igjen med f.eks. --k 2 eller --k 4 og sammenlign.")
    print("Merk: Clustering har ingen fasit – tolkning er en del av jobben.")

if __name__ == "__main__":
    main()
