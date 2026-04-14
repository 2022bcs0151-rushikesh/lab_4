import os
import json
import joblib
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

def train_model():
    # ✅ CREATE FOLDERS (IMPORTANT FIX)
    os.makedirs("app", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    data = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    f1 = f1_score(y_test, preds, average="macro")

    # Save model
    joblib.dump(model, "app/model.pkl")

    # Save metrics
    metrics = {"f1": float(f1)}   # 👈 convert to float (important for JSON)
    with open("results/metrics.json", "w") as f:
        json.dump(metrics, f)

    print("Training completed. F1 =", f1)

if __name__ == "__main__":
    train_model()
