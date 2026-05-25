# Swedish Daily-Life Scenario Classifier — Final Report

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

Dataset: CC BY 4.0

See `LICENSE` for project licensing details.

---
For the full academic write-up, see `report/final_report.md` and the submitted PDF in `report/`.
# Swedish Daily-Life Scenario Classifier — Final Report

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

<<<<<<< HEAD
- `data/scenario_dataset.csv`: custom dataset with Swedish text, English translation, Chinese translation, label, lecture theme, source, and review status.
- `src/run_experiment.py`: main experiment script for embedding-based classifier comparison.
- `src/train_tool_model.py`: trains a lightweight local classifier for Assignment 2 tool demonstrations.
- `src/predict_scenario.py`: predicts a scenario label for one input sentence.
- `report/assignment1_report_draft.md`: report draft.
=======
- Linear SVM — Accuracy: 0.8667, Macro-F1: 0.8712
- Logistic Regression — Accuracy: 0.8667, Macro-F1: 0.8689
- Random Forest — Accuracy: 0.8667, Macro-F1: 0.8682
- kNN — Accuracy: 0.8667, Macro-F1: 0.8648
>>>>>>> 8c890e5 (docs: replace README with final assignment report summary)

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

Dataset: CC BY 4.0

See `LICENSE` for project licensing details.

---
For the full academic write-up, see `report/final_report.md` and the submitted PDF in `report/`.
