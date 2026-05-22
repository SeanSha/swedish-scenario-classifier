# Lecture-Aligned Swedish Scenario Classification with Sentence Embeddings

**GitHub repository:** https://github.com/SeanSha/swedish-scenario-classifier  
**Hugging Face dataset:** https://huggingface.co/datasets/SeanSha30/swedish-pre-a1-scenario-classifier-dataset  
**Working demo:** https://huggingface.co/spaces/SeanSha30/swedish-scenario-classifier-demo

## 1. Introduction

This project builds an embedding-based text classification system for absolute beginner / pre-A1 Swedish learners. The task is to classify a short Swedish learner sentence into one of six lecture-aligned daily-life scenario labels: `food_shop`, `family_school`, `health_places`, `transport`, `home_places`, and `social_intro`. The motivation is to create a small but useful domain dataset for Swedish language learning, where a later tutoring agent could detect the learner's situation and select suitable practice material.

## 2. Dataset Creation

The custom dataset contains 150 examples, balanced across six labels with 25 examples per class. Each row includes a Swedish sentence, English translation, Chinese translation, label, lecture theme, source, and review status. The model uses only the Swedish `text` field as input; the translation and lecture-theme fields are metadata for review and explanation.

The dataset was created through AI-assisted drafting and manual structuring. Its vocabulary and themes were aligned with beginner Swedish lecture materials, including introductions, clarification phrases, food and shops, family and school words, health-related places, transport, and home/location prepositions. To avoid publishing course materials, the public dataset contains newly written example sentences rather than copied lecture text. This follows the assignment's requirement to create a useful text classification dataset in a domain. It is also inspired by synthetic-data methodology where generated text is paired with labels, manually screened, embedded, and evaluated using standard machine-learning models (Moëll & Sand Aronsson, 2026).

## 3. Method

Sentence embeddings were generated with `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, a lightweight multilingual sentence embedding model suitable for Swedish learner sentences. Four classifiers were trained and compared on the same embeddings: Logistic Regression, Linear SVM, Random Forest, and kNN. Evaluation used a stratified 80/20 train/test split with 120 training examples and 30 test examples. The main metrics were accuracy, macro-F1, per-label classification reports, and confusion matrices.

## 4. Results

| Classifier | Accuracy | Macro-F1 |
| --- | ---: | ---: |
| Linear SVM | 0.8667 | 0.8712 |
| Logistic Regression | 0.8667 | 0.8689 |
| Random Forest | 0.8667 | 0.8682 |
| kNN | 0.8667 | 0.8648 |

All four classifiers reached the same accuracy because the test set is small: each model correctly classified 26 out of 30 examples. Macro-F1 still differs slightly because the models made different errors across labels. The strongest model by macro-F1 was Linear SVM. Error analysis showed that very short beginner sentences can be ambiguous. For example, `Jag bor i Stockholm` can be interpreted as either a home/place sentence or a social introduction, and `Är det långt?` can be a transport question but lacks explicit transport vocabulary. This suggests that future dataset expansion should add more minimal context while keeping the language pre-A1.

## 5. Demo and Reflection on AI Use

The Hugging Face demo uses a Gradio interface. At startup it loads the dataset, generates multilingual sentence embeddings, trains a Linear SVM classifier, and predicts a label for user input. This makes the system testable as a working prototype rather than only an offline experiment.

AI assistance was useful for quickly drafting beginner-level examples, restructuring labels, writing reproducible experiment code, and preparing documentation. However, the work still required human judgement: deciding that the original labels were too broad, aligning the dataset with lecture content, checking that the Swedish level was closer to pre-A1, interpreting suspiciously similar classifier results, and avoiding publication of copyrighted lecture text. The main lesson is that AI can accelerate dataset and code creation, but the student still needs to define the task, inspect the data, question results, and make responsible publication decisions.

## References

Moëll, B., & Sand Aronsson, F. (2026). High-accuracy prediction of mental health scores from English BERT embeddings trained on LLM-generated synthetic self-reports: a synthetic-only method development study. *Frontiers in Digital Health, 7*. https://doi.org/10.3389/fdgth.2025.1694464
