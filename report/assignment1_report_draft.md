# Lecture-Aligned Swedish Daily-Life Scenario Classifier

## 1. Introduction

This project builds an embedding-based text classification system for absolute beginner and pre-A1 learners of Swedish. The task is to classify short Swedish learning sentences into lecture-aligned daily-life scenarios such as food and shops, family and school, health-related places, transport, home and places, and social introductions.

The motivation is practical and course-connected. The dataset is aligned with the vocabulary, sentence patterns, and beginner topics from the Swedish course lectures, such as introductions, asking for clarification, food and shops, family words, places and prepositions, transport words, and simple health/place expressions. A scenario classifier can help a learning system understand what kind of situation the learner wants to practise before generating exercises or retrieving learning material.

This project is also designed to support a later agent-based system, SisuTutor Agent. In Assignment 2, the agent can use the classifier as a tool: user input is classified into a daily-life scenario, then the agent retrieves relevant material and generates scenario-specific Swedish practice.

## 2. Dataset

The dataset is a small custom dataset of 150 Swedish learning sentences. It contains six labels, with 25 examples per label. The language level is intentionally simple: most sentences use short main clauses and lecture-level patterns such as `Jag vill...`, `Jag är...`, `Var är...?`, `När går...?`, and `Kan jag...?`.

| Label | Meaning |
| --- | --- |
| food_shop | food, fika, and shop situations |
| family_school | family, child, school, and teacher communication |
| health_places | health expressions and health-related places |
| transport | public transport and travel |
| home_places | home, rooms, furniture, and prepositions |
| social_intro | introductions, clarification, and everyday small talk |

Each row contains:

| Field | Description |
| --- | --- |
| id | unique example id |
| text | Swedish sentence |
| english | English translation |
| chinese | Chinese translation |
| label | scenario label |
| lecture_theme | lecture-based vocabulary or topic group |
| source | data creation source |
| review_status | manual review status |

The dataset was created by first extracting themes and vocabulary from seven Swedish beginner lecture PDFs. The examples were then AI-assisted and manually structured into daily-life scenario labels. The lecture-aligned themes are:

| Lecture-aligned theme | Related label |
| --- | --- |
| `food_and_shop` | `food_shop` |
| `family_and_school` | `family_school` |
| `health_and_places` | `health_places` |
| `transport_and_directions` | `transport` |
| `home_and_prepositions` | `home_places` |
| `intro_and_clarification` | `social_intro` |

The examples are intended for manual checking before final submission. Manual checking focuses on Swedish correctness, English and Chinese translation quality, lecture-level appropriateness, and label consistency.

The classifier uses only the Swedish `text` field as model input. The English and Chinese translations and the `lecture_theme` column are metadata for manual review, annotation consistency, and explanation in the report.

This dataset creation process is part of the contribution of the project. The novelty is not a new embedding model, but a small learner-oriented dataset for practical Swedish scenarios.

## 3. Embedding Method

The planned final embedding model is:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

This model is suitable because it supports multilingual sentence representations, including Swedish and English, and is lightweight enough for a course project.

The code also includes a local `tfidf-svd` option for smoke testing the pipeline without downloading a sentence-transformer model. This option is useful for checking that the data split, classifiers, metrics, and result files work correctly. The final reported experiment should use the multilingual sentence-transformer embeddings.

## 4. Classifiers

The project compares four classifiers on top of the embeddings:

| Classifier | Reason |
| --- | --- |
| Logistic Regression | simple and strong baseline |
| Linear SVM | common classifier for embedding-based text classification |
| Random Forest | non-linear comparison model |
| kNN | similarity-based classifier that directly reflects the embedding space |

Comparing several classifiers makes the system stronger than a single-model baseline and supports a more analytical report.

## 5. Evaluation and Results

The experiment uses a stratified 80/20 train/test split. Stratification keeps the six labels balanced in both training and test sets.

The evaluation metrics are:

| Metric | Purpose |
| --- | --- |
| Accuracy | overall performance |
| Macro-F1 | balanced performance across labels |
| Classification report | per-label precision, recall, and F1 |
| Confusion matrix | error analysis between scenarios |

The final experiment was run with `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`. The dataset contains 150 examples: 120 training examples and 30 test examples.

| Classifier | Accuracy | Macro-F1 |
| --- | ---: | ---: |
| Linear SVM | 0.8667 | 0.8712 |
| Logistic Regression | 0.8667 | 0.8689 |
| Random Forest | 0.8667 | 0.8682 |
| kNN | 0.8667 | 0.8648 |

Linear SVM achieved the best macro-F1, with 0.8667 accuracy and 0.8712 macro-F1. All four classifiers performed similarly after the label names were aligned with the lecture themes. This suggests that the multilingual sentence embeddings are useful for separating the lecture-aligned scenario labels, but also that the small test set makes the differences between classifiers modest.

The main error patterns were:

- home places and social introduction can overlap when a sentence is a general self-introduction, for example `Jag bor i Stockholm`;
- short transport direction phrases such as `Är det långt?` can be confused with social language because they are very general;
- family/school and transport can overlap for short time sentences such as `Jag kommer klockan tre`;
- short general help sentences such as `Jag behöver hjälp` can be ambiguous without a health-place context.

These errors are useful because they show where the dataset could be improved. More context words can be added to very short sentences while still keeping them pre-A1, for example `i affären`, `på bussen`, `i skolan`, or `på apoteket`.

## 6. Reproducibility

The main experiment can be run with:

```bash
python3 src/run_experiment.py --embedding sentence-transformer
```

The script saves:

- `results/metrics_summary.csv`
- `results/classification_reports.json`
- `results/test_predictions.csv`
- `results/confusion_matrix_<classifier>.png`
- `results/experiment_metadata.json`

For local testing without the sentence-transformer dependency, the pipeline can be tested with:

```bash
python3 src/run_experiment.py --embedding tfidf-svd
```

This smoke test should not be presented as the final embedding result if the assignment requires neural sentence embeddings. In this project, the final metrics above come from the multilingual sentence-transformer model.

## 7. Connection to Assignment 2

The classifier can become a tool inside the SisuTutor Agent. For example:

1. The user writes: "I need to talk to my child's teacher."
2. The classifier predicts: `family_school`.
3. The agent retrieves family/school communication material.
4. The agent generates role-play practice, vocabulary, or correction feedback for that scenario.

This makes Assignment 1 and Assignment 2 connected. Assignment 1 provides a focused embedding-based classifier, while Assignment 2 can use the classifier in a broader agent workflow.

## 8. Distinction Angle

The distinction angle is the combination of:

- a custom dataset aligned with the course lecture vocabulary and real-life Swedish learner needs;
- multilingual sentence embeddings;
- comparison of several classifiers;
- clear evaluation with macro-F1 and confusion matrices;
- error analysis connected to lecture-aligned daily-life categories;
- direct integration path into an agent tool for Assignment 2.

## 9. Limitations

The dataset is small and should not be treated as a production dataset. Some examples are AI-assisted and require manual validation. The train/test split is also small, so performance may vary depending on the random seed.

Future work could include increasing the dataset size to 300 examples, adding short dialogues, collecting examples from real learner needs, and testing another multilingual embedding model such as `intfloat/multilingual-e5-small`.
