# Swedish Daily-Life Scenario Classifier

Embedding-based text classification system for absolute beginner / pre-A1 learners of Swedish.

## Links

- Hugging Face dataset: https://huggingface.co/datasets/SeanSha30/swedish-pre-a1-scenario-classifier-dataset
- Hugging Face demo: https://huggingface.co/spaces/SeanSha30/swedish-scenario-classifier-demo
- GitHub repository: TODO

The system classifies short Swedish learning sentences into six lecture-aligned daily-life scenarios:

- `food_shop`
- `family_school`
- `health_places`
- `transport`
- `home_places`
- `social_intro`

## Project Goal

This project is designed for Assignment 1: Embeddings System. It creates a small custom dataset of lecture-aligned Swedish daily-life learning sentences and compares several classifiers on top of sentence embeddings.

The project is also designed to connect to Assignment 2. A future SisuTutor Agent can use the classifier as a tool: first detect the learner's scenario, then retrieve suitable learning material and generate practice.

## Files

- `data/scenario_dataset.csv`: custom dataset with Swedish text, English translation, Chinese translation, label, lecture theme, source, and review status.
- `src/run_experiment.py`: main experiment script for embedding-based classifier comparison.
- `src/train_tool_model.py`: trains a lightweight local classifier for Assignment 2 tool demonstrations.
- `src/predict_scenario.py`: predicts a scenario label for one input sentence.
- `report/assignment1_report_draft.md`: report draft.
- `report/final_report.md`: concise academic report for submission.
- `report/supervisor_questions.md`: concise questions to send to the supervisor.

## Recommended Final Experiment

Install dependencies:

```bash
python3 -m venv --system-site-packages .venv
.venv/bin/python -m pip install -r requirements.txt
```

Run the final sentence-transformer experiment:

```bash
.venv/bin/python src/run_experiment.py --embedding sentence-transformer
```

This uses:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

## Offline Smoke Test

If `sentence-transformers` is not installed yet, run:

```bash
python3 src/run_experiment.py --embedding tfidf-svd
```

This is only a local pipeline test. The final report should use the sentence-transformer result.

## Verified Result

The final experiment has been run successfully with `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.

| Classifier | Accuracy | Macro-F1 |
| --- | ---: | ---: |
| Linear SVM | 0.8667 | 0.8712 |
| Logistic Regression | 0.8667 | 0.8689 |
| Random Forest | 0.8667 | 0.8682 |
| kNN | 0.8667 | 0.8648 |

## Assignment 2 Tool Demo

Train a small local model:

```bash
python3 src/train_tool_model.py
```

Predict a scenario:

```bash
python3 src/predict_scenario.py "Jag är på bussen."
```

Expected label:

```text
transport
```

Note: the classifier uses the Swedish `text` column as input. The English, Chinese, and lecture theme columns are metadata for review and explanation.
