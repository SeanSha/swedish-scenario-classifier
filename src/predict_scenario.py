from __future__ import annotations

import argparse
from pathlib import Path

import joblib


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Predict a daily-life scenario label for a Swedish sentence."
    )
    parser.add_argument("text", help="A Swedish sentence or short learner utterance.")
    parser.add_argument("--model-path", default="models/scenario_classifier.joblib")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model_path = Path(args.model_path)
    if not model_path.exists():
        raise SystemExit(
            f"No saved classifier found at {model_path}. Run train_tool_model.py first."
        )

    model = joblib.load(model_path)
    prediction = model.predict([args.text])[0]
    probabilities = getattr(model, "predict_proba", None)

    print(f"label: {prediction}")
    if probabilities is not None:
        proba = model.predict_proba([args.text])[0]
        labels = model.classes_
        ranked = sorted(zip(labels, proba), key=lambda item: item[1], reverse=True)
        for label, score in ranked:
            print(f"{label}: {score:.3f}")


if __name__ == "__main__":
    main()
