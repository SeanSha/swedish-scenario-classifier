from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterable

_cache_dir = Path("results/.cache").resolve()
_cache_dir.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(_cache_dir / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(_cache_dir))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Normalizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer


LABEL_ORDER = [
    "food_shop",
    "family_school",
    "health_places",
    "transport",
    "home_places",
    "social_intro",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run embedding-based scenario classification experiments."
    )
    parser.add_argument("--data", default="data/scenario_dataset.csv")
    parser.add_argument("--output-dir", default="results")
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument(
        "--embedding",
        choices=["sentence-transformer", "tfidf-svd"],
        default="tfidf-svd",
        help=(
            "Use sentence-transformer for the final assignment experiment. "
            "Use tfidf-svd for an offline smoke test when the embedding model is not installed."
        ),
    )
    parser.add_argument(
        "--model-name",
        default="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    )
    return parser.parse_args()


def load_dataset(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    expected = {"id", "text", "english", "label"}
    missing = expected.difference(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
    if df["text"].isna().any() or df["label"].isna().any():
        raise ValueError("Dataset contains empty text or label values.")
    unknown_labels = set(df["label"]) - set(LABEL_ORDER)
    if unknown_labels:
        raise ValueError(f"Unknown labels found: {sorted(unknown_labels)}")
    return df


def make_sentence_transformer_embeddings(
    train_texts: Iterable[str], test_texts: Iterable[str], model_name: str
) -> tuple[np.ndarray, np.ndarray, str]:
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise SystemExit(
            "sentence-transformers is not installed. Install requirements or run with "
            "--embedding tfidf-svd for a local smoke test."
        ) from exc

    model = SentenceTransformer(model_name)
    train_embeddings = model.encode(
        list(train_texts), normalize_embeddings=True, show_progress_bar=True
    )
    test_embeddings = model.encode(
        list(test_texts), normalize_embeddings=True, show_progress_bar=True
    )
    return np.asarray(train_embeddings), np.asarray(test_embeddings), model_name


def make_tfidf_svd_embeddings(
    train_texts: Iterable[str], test_texts: Iterable[str]
) -> tuple[np.ndarray, np.ndarray, str]:
    pipeline = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
            ("svd", TruncatedSVD(n_components=50, random_state=42)),
            ("normalizer", Normalizer(copy=False)),
        ]
    )
    train_embeddings = pipeline.fit_transform(list(train_texts))
    test_embeddings = pipeline.transform(list(test_texts))
    return np.asarray(train_embeddings), np.asarray(test_embeddings), "tfidf-svd-50"


def build_classifiers() -> dict[str, object]:
    return {
        "logistic_regression": LogisticRegression(max_iter=2000, class_weight="balanced"),
        "linear_svm": LinearSVC(class_weight="balanced", random_state=42),
        "random_forest": RandomForestClassifier(
            n_estimators=300, class_weight="balanced", random_state=42
        ),
        "knn": KNeighborsClassifier(n_neighbors=5, metric="cosine"),
    }


def save_confusion_matrix(
    y_true: pd.Series, y_pred: np.ndarray, classifier_name: str, output_dir: Path
) -> None:
    matrix = confusion_matrix(y_true, y_pred, labels=LABEL_ORDER)
    fig, ax = plt.subplots(figsize=(8, 6))
    display = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=LABEL_ORDER)
    display.plot(ax=ax, cmap="Blues", values_format="d", colorbar=False)
    ax.set_title(f"Confusion matrix: {classifier_name}")
    plt.xticks(rotation=35, ha="right")
    fig.tight_layout()
    fig.savefig(output_dir / f"confusion_matrix_{classifier_name}.png", dpi=180)
    plt.close(fig)


def main() -> None:
    args = parse_args()
    data_path = Path(args.data)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_dataset(data_path)
    train_df, test_df = train_test_split(
        df,
        test_size=args.test_size,
        random_state=args.random_state,
        stratify=df["label"],
    )

    if args.embedding == "sentence-transformer":
        x_train, x_test, embedding_name = make_sentence_transformer_embeddings(
            train_df["text"], test_df["text"], args.model_name
        )
    else:
        x_train, x_test, embedding_name = make_tfidf_svd_embeddings(
            train_df["text"], test_df["text"]
        )

    results = []
    reports = {}
    prediction_columns = [
        column
        for column in ["id", "text", "english", "chinese", "lecture_theme", "label"]
        if column in test_df.columns
    ]
    predictions = test_df[prediction_columns].copy()

    for name, classifier in build_classifiers().items():
        classifier.fit(x_train, train_df["label"])
        y_pred = classifier.predict(x_test)
        predictions[f"pred_{name}"] = y_pred

        accuracy = accuracy_score(test_df["label"], y_pred)
        macro_f1 = f1_score(test_df["label"], y_pred, average="macro")
        results.append(
            {
                "classifier": name,
                "embedding": embedding_name,
                "accuracy": round(float(accuracy), 4),
                "macro_f1": round(float(macro_f1), 4),
            }
        )
        reports[name] = classification_report(
            test_df["label"], y_pred, labels=LABEL_ORDER, output_dict=True, zero_division=0
        )
        save_confusion_matrix(test_df["label"], y_pred, name, output_dir)

    results_df = pd.DataFrame(results).sort_values(
        by=["macro_f1", "accuracy"], ascending=False
    )
    results_df.to_csv(output_dir / "metrics_summary.csv", index=False)
    predictions.to_csv(output_dir / "test_predictions.csv", index=False)
    with (output_dir / "classification_reports.json").open("w", encoding="utf-8") as f:
        json.dump(reports, f, indent=2, ensure_ascii=False)

    metadata = {
        "dataset": str(data_path),
        "rows": int(len(df)),
        "label_counts": df["label"].value_counts().sort_index().to_dict(),
        "embedding": embedding_name,
        "test_size": args.test_size,
        "random_state": args.random_state,
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
    }
    with (output_dir / "experiment_metadata.json").open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(results_df.to_string(index=False))
    print(f"\nSaved outputs to {output_dir.resolve()}")


if __name__ == "__main__":
    main()
