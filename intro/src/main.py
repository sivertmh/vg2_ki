from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([X[0]]))
