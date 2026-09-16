"""TF-IDF + Logistic Regression baseline for the demo dataset."""

from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from .preprocessing import normalize_text


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "sample_sentiment.csv"


def train_baseline() -> tuple[Pipeline, float, str]:
    """Train the reproducible demonstration classifier."""
    df = pd.read_csv(DATA)
    df["text"] = df["text"].map(normalize_text)
    x_train, x_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=0.25, random_state=42, stratify=df["label"]
    )

    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, zero_division=0)
    return model, accuracy, report


if __name__ == "__main__":
    _, accuracy, report = train_baseline()
    print(f"Accuracy: {accuracy:.3f}")
    print(report)
