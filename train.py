import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)

with open("model/iris_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model got completed and saved")
