from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

X, y = load_iris(return_X_y=True)

model = DecisionTreeClassifier()

params = {"max_depth": [2, 3, 4, 5]}

grid = GridSearchCV(model, params, cv=5)
grid.fit(X, y)

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)
