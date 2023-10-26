#https://github.com/kshitizrohilla/iris-flower-classification-using-k-nearest-neighbor-algorithm/blob/main/notebook.ipynb

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris

# Load the Iris dataset from scikit-learn
iris = load_iris()
# Extract features (X) and target variable (y)
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(y_pred)
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)
