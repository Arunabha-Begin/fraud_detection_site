import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = pd.read_csv("creditcard.csv")

X = data.drop("Class", axis=1)
y = data["Class"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Handle null values in all features
imputer = SimpleImputer(strategy="median")
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Standardization for train data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Standardization for test data
X_test = scaler.transform(X_test)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced'
)

# Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, "random_forest_model.pkl")
joblib.dump(imputer, "imputer.pkl")
joblib.dump(scaler, "scaler.pkl")

#  Predictions
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# Accuracy
train_acc = accuracy_score(y_train, train_pred)
test_acc = accuracy_score(y_test, test_pred)

# Print Accuracies
print("Random Forest:")
print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)
print("Precision:", precision_score(y_test, test_pred))
print("Recall:", recall_score(y_test, test_pred))
print("F1 Score:", f1_score(y_test, test_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, test_pred))

# Plot Graph
labels = ['Training Accuracy', 'Testing Accuracy']
values = [train_acc, test_acc]

plt.figure()
plt.bar(labels, values)

plt.xlabel("Dataset")
plt.ylabel("Accuracy")
plt.title("Random Forest: Training vs Testing Accuracy")

plt.show()