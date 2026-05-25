# Swedish Daily-Life Scenario Classifier

## Lecture-Aligned Swedish Scenario Classification with Sentence Embeddings

This repository contains the final experiment and materials for Assignment 1. The project builds an embedding-based text classification system for absolute-beginner / pre-A1 Swedish learner sentences. The task is to classify short Swedish learner utterances into one of six lecture-aligned daily-life scenario labels.

## Links

- GitHub repository: https://github.com/SeanSha/swedish-scenario-classifier
- Hugging Face dataset: https://huggingface.co/datasets/SeanSha30/swedish-pre-a1-scenario-classifier-dataset
- Working demo: https://huggingface.co/spaces/SeanSha30/swedish-scenario-classifier-demo
- Final report: `report/UU_Assignment_1.pdf`

## Task

The project classifies short Swedish learner sentences into six daily-life scenarios:

- `food_shop`
- `family_school`
- `health_places`
- `transport`
- `home_places`
- `social_intro`

These labels are designed to match common beginner-level Swedish learning situations, such as shopping, family and school, health and places, transport, home-related topics, and social introductions.

## Dataset

The dataset contains 150 short Swedish learner sentences, with 25 examples for each class. The sentences are designed for absolute-beginner / pre-A1 Swedish learners and are aligned with daily-life classroom topics.

The dataset was created as a small course-project dataset. Many examples were AI-assisted during drafting and then manually checked before use. Because the dataset is small, the results should be understood as prototype results rather than production-level performance.

The dataset file is available at:

```text
data/scenario_dataset.csv
```

The dataset is also available on Hugging Face:

```text
https://huggingface.co/datasets/SeanSha30/swedish-pre-a1-scenario-classifier-dataset
```

Dataset license:

```text
CC BY 4.0
```

## Method

The main experiment uses multilingual sentence embeddings and lightweight classifiers.

The final embedding model is:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

The embeddings are used as input features for four classifiers:

- Logistic Regression
- Linear SVM
- Random Forest
- kNN

These classifiers were selected because they provide simple and common baselines for small text classification tasks. They also make it possible to compare linear, tree-based, and instance-based classification methods.

The evaluation uses an 80/20 stratified train/test split. Accuracy and macro-F1 are used as the main evaluation metrics. Macro-F1 is important because the task has multiple classes and each class should be treated equally.

## Key Results

| Model | Accuracy | Macro-F1 |
|---|---:|---:|
| Linear SVM | 0.8667 | 0.8712 |
| Logistic Regression | 0.8667 | 0.8689 |
| Random Forest | 0.8667 | 0.8682 |
| kNN | 0.8667 | 0.8648 |

Linear SVM obtained the highest macro-F1 score and is therefore used in the Hugging Face demo.

## Repository Structure

```text
data/
  scenario_dataset.csv

src/
  run_experiment.py
  train_tool_model.py
  predict_scenario.py

hf_space/
  app.py
  requirements.txt

report/
  UU_Assignment_1.pdf

results/
  experiment results and saved metrics

models/
  saved local TF-IDF + SVD classifier pipelines
```

## How to Reproduce the Main Experiment

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the main experiment with sentence-transformer embeddings:

```bash
python src/run_experiment.py --embedding sentence-transformer
```

The script trains and evaluates the classifiers and saves the result files in the `results/` folder.

## Offline Smoke Test

If `sentence-transformers` is not available, an offline smoke test can be run with TF-IDF + SVD features:

```bash
python src/run_experiment.py --embedding tfidf-svd
```

This is mainly used to check that the experiment pipeline works without downloading the sentence-transformer model.

## Train Local Prediction Models

To train and save local TF-IDF + SVD classifier pipelines, run:

```bash
python src/train_tool_model.py
```

This saves four classifier pipelines under the `models/` folder.

## Command-Line Prediction

After training the local models, a sentence can be classified from the command line:

```bash
python src/predict_scenario.py "Jag är på bussen." --model-type linear_svm
```

The `--model-type` argument can be used to choose the saved classifier.

## Hugging Face Demo

The working demo is available here:

```text
https://huggingface.co/spaces/SeanSha30/swedish-scenario-classifier-demo
```

The Hugging Face Space code is located in:

```text
hf_space/
```

The demo uses:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

and a LinearSVC classifier trained at app startup. Users can enter a short Swedish sentence and receive a predicted daily-life scenario label.

## Notes and Limitations

This project is a small course-project prototype. The dataset contains only 150 examples, so the reported results should not be interpreted as strong evidence of general performance on real Swedish learner data.

The dataset examples are short, controlled, and scenario-focused. Real learner input may contain spelling mistakes, grammar errors, mixed languages, or more complex sentences. Further data collection, human validation, and testing on real learner sentences would be needed before using this system in a practical language-learning tool.

The experiment also uses a single train/test split. More robust evaluation, such as cross-validation, would give a more reliable estimate of model performance.

## AI Use and Reflection

AI tools were used during the assignment to support dataset drafting, code debugging, README improvement, and report editing. However, the dataset was manually checked, the experiment was run and reviewed by the author, and the final analysis was written based on the actual results.

Using AI was helpful for quickly building a working prototype and improving the structure of the project. At the same time, the process showed that AI-generated content still needs careful checking, especially for dataset quality, code correctness, and academic explanation. A fuller reflection is included in the PDF report.

## License

The dataset is released under CC BY 4.0.

See `LICENSE` for the full project license details.

## Report

For the full academic write-up, see:

```text
report/UU_Assignment_1.pdf
```
