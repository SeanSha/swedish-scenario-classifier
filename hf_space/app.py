from __future__ import annotations

from pathlib import Path

import gradio as gr
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.svm import LinearSVC


DATA_PATH = Path("scenario_dataset.csv")
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
LABEL_DESCRIPTIONS = {
    "food_shop": "Food, fika, and shop situations",
    "family_school": "Family, child, school, and teacher communication",
    "health_places": "Health expressions and health-related places",
    "transport": "Public transport, travel, and directions",
    "home_places": "Home, rooms, furniture, and prepositions",
    "social_intro": "Introductions, clarification, and everyday small talk",
}


def softmax(values: np.ndarray) -> np.ndarray:
    shifted = values - np.max(values)
    exp = np.exp(shifted)
    return exp / exp.sum()


def load_classifier() -> tuple[SentenceTransformer, LinearSVC, pd.DataFrame]:
    data = pd.read_csv(DATA_PATH)
    embedder = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = embedder.encode(
        data["text"].tolist(),
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    classifier = LinearSVC(class_weight="balanced", random_state=42)
    classifier.fit(embeddings, data["label"])
    return embedder, classifier, data


EMBEDDER, CLASSIFIER, DATA = load_classifier()


def predict(text: str) -> tuple[str, dict[str, float]]:
    if not text or not text.strip():
        return "Please enter a Swedish sentence.", {}

    embedding = EMBEDDER.encode([text.strip()], normalize_embeddings=True)
    prediction = CLASSIFIER.predict(embedding)[0]
    scores = CLASSIFIER.decision_function(embedding)[0]
    probabilities = softmax(scores)
    score_map = {
        label: float(score)
        for label, score in sorted(
            zip(CLASSIFIER.classes_, probabilities),
            key=lambda item: item[1],
            reverse=True,
        )
    }
    description = LABEL_DESCRIPTIONS.get(prediction, "")
    label_text = f"{prediction} — {description}"
    return label_text, score_map


examples = [
    "Jag är på bussen.",
    "Jag vill ha kaffe.",
    "Kan jag prata med läraren?",
    "Var är apoteket?",
    "Boken är på bordet.",
    "Vad heter du?",
]


demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(
        label="Swedish sentence",
        placeholder="Type a short Swedish learner sentence...",
    ),
    outputs=[
        gr.Textbox(label="Predicted label"),
        gr.Label(label="Model scores"),
    ],
    examples=examples,
    title="Lecture-Aligned Swedish Scenario Classifier",
    description=(
        "Classifies pre-A1 Swedish learner sentences into six lecture-aligned "
        "daily-life scenarios using multilingual sentence embeddings and Linear SVM."
    ),
)


if __name__ == "__main__":
    demo.launch()
