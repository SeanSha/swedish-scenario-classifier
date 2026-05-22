from __future__ import annotations

import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Train a lightweight local scenario classifier for Assignment 2 tool demos. "
            "The final Assignment 1 experiment should use run_experiment.py with "
            "sentence-transformer embeddings when the package and model are available."
        )
    )
    parser.add_argument("--data", default="data/scenario_dataset.csv")
    parser.add_argument("--output", default="models/scenario_classifier.joblib")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.data)

    pipeline = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
            ("svd", TruncatedSVD(n_components=50, random_state=42)),
            ("normalizer", Normalizer(copy=False)),
            (
                "classifier",
                LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42),
            ),
        ]
    )
    pipeline.fit(df["text"], df["label"])

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, output_path)
    print(f"Saved tool model to {output_path.resolve()}")


if __name__ == "__main__":
    main()
