from __future__ import annotations

import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Train four lightweight local scenario classifiers for Assignment 2 tool demos. "
            "The final Assignment 1 experiment should use run_experiment.py with "
            "sentence-transformer embeddings when the package and model are available."
        )
    )
    parser.add_argument("--data", default="data/scenario_dataset.csv")
    parser.add_argument("--output-dir", default="models")
    return parser.parse_args()


def build_pipeline(classifier) -> Pipeline:
    """Build a pipeline with TF-IDF preprocessing and a classifier."""
    return Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
            ("svd", TruncatedSVD(n_components=50, random_state=42)),
            ("normalizer", Normalizer(copy=False)),
            ("classifier", classifier),
        ]
    )


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.data)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    classifiers = {
        "logistic_regression": LogisticRegression(
            max_iter=2000, class_weight="balanced", random_state=42
        ),
        "linear_svm": LinearSVC(class_weight="balanced", random_state=42),
        "random_forest": RandomForestClassifier(
            n_estimators=300, class_weight="balanced", random_state=42
        ),
        "knn": KNeighborsClassifier(n_neighbors=5, metric="cosine"),
    }

    for model_name, classifier in classifiers.items():
        pipeline = build_pipeline(classifier)
        pipeline.fit(df["text"], df["label"])

        output_path = output_dir / f"{model_name}.joblib"
        joblib.dump(pipeline, output_path)
        print(f"Saved {model_name} model to {output_path.resolve()}")

    # Keep backward compatibility: also save the default logistic regression as scenario_classifier.joblib
    default_pipeline = build_pipeline(classifiers["logistic_regression"])
    default_pipeline.fit(df["text"], df["label"])
    default_output_path = output_dir / "scenario_classifier.joblib"
    joblib.dump(default_pipeline, default_output_path)
    print(f"Saved default model (logistic_regression) to {default_output_path.resolve()}")


if __name__ == "__main__":
    main()
