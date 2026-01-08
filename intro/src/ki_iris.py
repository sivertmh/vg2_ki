from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)

model = DecisionTreeClassifier()
model.fit(X, y)

print("Prediksjon:", model.predict([X[0]]))
print("Ekte klasse:", y[0])

iris = load_iris()
print(iris.target_names[model.predict([X[0]])])