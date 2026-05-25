# Swedish Daily-Life Scenario Classifier

Lecture-Aligned Swedish Scenario Classification with Sentence Embeddings

This repository contains the final experiment and materials for Assignment 1: an embedding-based text classification system for absolute-beginner / pre-A1 Swedish learner sentences. The task is to classify short Swedish learner utterances into one of six lecture-aligned daily-life scenarios.

## Labels

- `food_shop`
- `family_school`
- `health_places`
- `transport`
- `home_places`
- `social_intro`

## Summary

This project created a small, curated dataset of 150 Swedish learner sentences (25 examples per class) and compared several classifiers on top of sentence embeddings. The final reported experiment used `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` to produce multilingual sentence embeddings, then trained and evaluated four classifiers: Logistic Regression, Linear SVM, Random Forest, and kNN. Evaluation used an 80/20 stratified train/test split with accuracy and macro-F1 as primary metrics.

### Key Result

All four classifiers achieved similar accuracy on the small test set (30 examples). The reported metrics were:

- Linear SVM — Accuracy: 0.8667, Macro-F1: 0.8712
- Logistic Regression — Accuracy: 0.8667, Macro-F1: 0.8689
- Random Forest — Accuracy: 0.8667, Macro-F1: 0.8682
- kNN — Accuracy: 0.8667, Macro-F1: 0.8648

Linear SVM had the highest macro-F1 and was used in the Hugging Face demo. The repository also includes a lightweight TF-IDF+SVD+LogisticRegression pipeline saved as a local tool model for Assignment 2 demonstrations.

## Contents

- `data/scenario_dataset.csv`: the curated dataset with Swedish text, English and Chinese translations, labels, and metadata.
- `src/run_experiment.py`: reproducible experiment script — generates embeddings (sentence-transformer or tfidf-svd), trains four classifiers, and saves results and confusion matrices to `results/`.
- `src/train_tool_model.py`: trains and saves local TF-IDF+SVD pipelines for four classifiers (now saved separately under `models/`).
- `src/predict_scenario.py`: command-line prediction tool; choose which saved local model to use via `--model-type`.
- `hf_space/`: Hugging Face Space demo that trains a `SentenceTransformer` + `LinearSVC` on startup and serves a Gradio interface.
- `report/`: write-ups and the final report used for submission.

## Reproducibility

Install dependencies and run the final experiment with the sentence-transformer embedding:

```bash
python3 -m venv .venv --system-site-packages
source .venv/bin/activate
pip install -r requirements.txt
python src/run_experiment.py --embedding sentence-transformer
```

For an offline smoke test without sentence-transformers:

```bash
python src/run_experiment.py --embedding tfidf-svd
```

To train and save the local tool models (now saves four model files in `models/`):

```bash
python src/train_tool_model.py
```

To run a local prediction using one of the saved models:

```bash
python src/predict_scenario.py "Jag är på bussen." --model-type linear_svm
```

## Hugging Face Demo

The demo in `hf_space/` uses `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` embeddings and a `LinearSVC` classifier trained at app startup. The Space is available at the repository HF link.

## Notes and Limitations

- Dataset size is small (150 examples); results are for a course project prototype, not production.
- Many examples were AI-assisted and manually checked; further human validation and dataset expansion are recommended.

## License
# Swedish Daily-Life Scenario Classifier

Concise final README for the course assignment. This project classifies short Swedish learner sentences (pre-A1) into six lecture-aligned daily-life scenarios using sentence embeddings and lightweight classifiers.

## Labels

- `food_shop`
- `family_school`
- `health_places`
- `transport`
- `home_places`
- `social_intro`

## What this repo contains

- `data/scenario_dataset.csv` — curated dataset (150 examples, 25 per class)
- `src/run_experiment.py` — reproducible experiment script (sentence-transformer or tfidf-svd embeddings); trains and evaluates four classifiers and saves metrics to `results/`
- `src/train_tool_model.py` — trains and saves local TF-IDF+SVD pipelines (now saves four classifier pipelines under `models/`)
- `src/predict_scenario.py` — CLI prediction tool; choose model with `--model-type`
- `hf_space/` — Hugging Face Space demo (embeddings + `LinearSVC`), served with Gradio
- `report/UU_Assignment_1.pdf` — final submitted PDF report

## Quick start

Create and activate a venv, install requirements, and run the final experiment with sentence-transformer embeddings:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/run_experiment.py --embedding sentence-transformer
```

If you cannot install `sentence-transformers`, run a local smoke test:

```bash
python src/run_experiment.py --embedding tfidf-svd
```

Train and save local TF-IDF pipelines for each classifier (saved under `models/`):

```bash
python src/train_tool_model.py
```

Predict with a saved local model (choose `--model-type`):

```bash
python src/predict_scenario.py "Jag är på bussen." --model-type linear_svm
```

## Notes

- The Hugging Face demo trains a `SentenceTransformer` + `LinearSVC` at startup and does not use the local `models/*.joblib` files.
- This is a course prototype with a small dataset; expand and validate the dataset before any production use.

## License

Dataset: CC BY 4.0. See `LICENSE` for full project license.

---
For the full academic write-up, see `report/UU_Assignment_1.pdf`.

## License

Dataset: CC BY 4.0

See `LICENSE` for project licensing details.

---
For the full academic write-up, see `report/final_report.md` and the submitted PDF in `report/`.
