# Swedish Daily-Life Scenario Classifier

Lecture-Aligned Swedish Scenario Classification with Sentence Embeddings

This repository contains the final experiment and materials for Assignment 1: an
embedding-based text classification system for absolute-beginner / pre-A1 Swedish
learner sentences. The task is to classify short Swedish learner utterances into
one of six lecture-aligned daily-life scenarios.

## Labels

- `food_shop`
- `family_school`
- `health_places`
- `transport`
- `home_places`
- `social_intro`

## Summary

This project created a curated dataset of 150 Swedish learner sentences (25
examples per class) and compared several classifiers on top of multilingual
sentence embeddings. The final experiment used
`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` to produce
embeddings, then trained and evaluated four classifiers: Logistic Regression,
Linear SVM, Random Forest, and kNN. Evaluation used an 80/20 stratified
train/test split with accuracy and macro-F1 as the primary metrics.

### Key results

- Linear SVM — Accuracy: 0.8667, Macro-F1: 0.8712
- Logistic Regression — Accuracy: 0.8667, Macro-F1: 0.8689
- Random Forest — Accuracy: 0.8667, Macro-F1: 0.8682
- kNN — Accuracy: 0.8667, Macro-F1: 0.8648

Linear SVM obtained the highest macro-F1 and is used in the Hugging Face demo.

## Repository contents

- `data/scenario_dataset.csv` — curated dataset (150 examples, 25 per class)
- `src/run_experiment.py` — reproducible experiment script (sentence-transformer
  or tfidf-svd embeddings); trains classifiers and saves metrics to `results/`
- `src/train_tool_model.py` — trains and saves local TF-IDF+SVD pipelines (now
  saves four classifier pipelines under `models/`)
- `src/predict_scenario.py` — CLI prediction tool; choose saved model with
  `--model-type`
- `hf_space/` — Hugging Face Space demo (embeddings + `LinearSVC`), served with
  Gradio
- `report/UU_Assignment_1.pdf` — final submitted PDF report

## Quick start

Create and activate a virtual environment, install requirements, and run the
final experiment using sentence-transformer embeddings:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/run_experiment.py --embedding sentence-transformer
```

Offline smoke test (no sentence-transformers):

```bash
python src/run_experiment.py --embedding tfidf-svd
```

Train and save local TF-IDF pipelines for each classifier:

```bash
python src/train_tool_model.py
```

Predict with a saved local model (choose `--model-type`):

```bash
python src/predict_scenario.py "Jag är på bussen." --model-type linear_svm
```

## Hugging Face demo

The Space in `hf_space/` uses `sentence-transformers/paraphrase-multilingual-
MiniLM-L12-v2` embeddings and a `LinearSVC` classifier trained at app startup.

## Notes and limitations

- Dataset is small (150 examples); results are for a course-project prototype
  and should not be used as-is in production.
- Many dataset examples were AI-assisted and manually checked; further human
  validation and expansion are recommended.

## License

Dataset: CC BY 4.0. See `LICENSE` for full project license details.

---
For the full academic write-up, see `report/UU_Assignment_1.pdf`.
