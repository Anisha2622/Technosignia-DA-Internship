"""Day 14 — Machine Learning Fundamentals
Install: python -m pip install pandas scikit-learn
Keep this script and day14_customer_churn_sample.csv in the same folder.
Run: python day14_machine_learning_fundamentals.py
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_absolute_error

df = pd.read_csv("day14_customer_churn_sample.csv")
X = df[["TenureMonths", "MonthlyCharge", "SupportCalls", "ContractType"]]
y = df["Churn"]

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
X_valid, X_test, y_valid, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
)

numeric_features = ["TenureMonths", "MonthlyCharge", "SupportCalls"]
categorical_features = ["ContractType"]
preprocess = ColumnTransformer([
    ("numeric", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]), numeric_features),
    ("categorical", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical_features)
])

def report(name, actual, predicted):
    print(f"\n{name}")
    print(f"Accuracy : {accuracy_score(actual, predicted):.3f}")
    print(f"Precision: {precision_score(actual, predicted, zero_division=0):.3f}")
    print(f"Recall   : {recall_score(actual, predicted, zero_division=0):.3f}")
    print(f"F1-score : {f1_score(actual, predicted, zero_division=0):.3f}")
    print(f"MAE      : {mean_absolute_error(actual, predicted):.3f}")

baseline = Pipeline([
    ("preprocess", preprocess),
    ("model", DummyClassifier(strategy="most_frequent"))
])
baseline.fit(X_train, y_train)
report("Baseline — validation data", y_valid, baseline.predict(X_valid))

model = Pipeline([
    ("preprocess", preprocess),
    ("model", LogisticRegression(max_iter=1000, random_state=42))
])
model.fit(X_train, y_train)
report("Logistic Regression — validation data", y_valid, model.predict(X_valid))
report("Logistic Regression — test data", y_test, model.predict(X_test))
