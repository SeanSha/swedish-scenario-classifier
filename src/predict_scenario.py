from __future__ import annotations

import argparse
from pathlib import Path

import joblib


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Predict a daily-life scenario label for a Swedish sentence."
    )
    parser.add_argument("text", help="A Swedish sentence or short learner utterance.")
    parser.add_argument(
        "--model-type",
        choices=["logistic_regression", "linear_svm", "random_forest", "knn"],
        default="logistic_regression",
        help="Choose which classifier model to use.",
    )
    parser.add_argument(
        "--model-dir", default="models", help="Directory where trained models are stored."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model_dir = Path(args.model_dir)
    model_path = model_dir / f"{args.model_type}.joblib"

    if not model_path.exists():
        raise SystemExit(
            f"No saved classifier found at {model_path}. "
            f"Run train_tool_model.py first to train and save the models."
        )

    model = joblib.load(model_path)
    prediction = model.predict([args.text])[0]

    print(f"Model: {args.model_type}")
    print(f"label: {prediction}")

    # Try to get probabilities if available
    classifier = model.named_steps["classifier"]
    if hasattr(classifier, "predict_proba"):
        try:
            # Transform the text through the pipeline preprocessing steps
            feature_vector = model.named_steps["tfidf"].transform([args.text])
            feature_vector = model.named_steps["svd"].transform(feature_vector)
            feature_vector = model.named_steps["normalizer"].transform(feature_vector)
            proba = classifier.predict_proba(feature_vector)[0]
            labels = classifier.classes_
            ranked = sorted(zip(labels, proba), key=lambda item: item[1], reverse=True)
            for label, score in ranked:
                print(f"{label}: {score:.3f}")
        except Exception:
            pass


if __name__ == "__main__":
    main()
