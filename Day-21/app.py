# Day21_Intro_to_ML

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load Dataset
data = pd.read_csv(r"C:\Users\sushs\OneDrive\Desktop\DS_internship\Day-21\Iris.csv")
# Step 3: Remove unnecessary column (Id if present)
if "Id" in data.columns:
    data = data.drop("Id", axis=1)

# Step 4: Define Features and Target
X = data.drop("Species", axis=1)
y = data["Species"]

# Step 5: Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 6: Train Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 7: Predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate Model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))