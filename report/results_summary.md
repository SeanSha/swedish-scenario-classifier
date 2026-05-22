# Results Summary

Final embedding model:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

Dataset:

- 150 examples
- 6 labels
- 25 examples per label
- 120 training examples
- 30 test examples
- Stratified 80/20 split

## Metrics

| Classifier | Accuracy | Macro-F1 |
| --- | ---: | ---: |
| Linear SVM | 0.8667 | 0.8712 |
| Logistic Regression | 0.8667 | 0.8689 |
| Random Forest | 0.8667 | 0.8682 |
| kNN | 0.8667 | 0.8648 |

Best model:

`Linear SVM`

## Error Analysis

The strongest model by macro-F1, Linear SVM, correctly classified 26 out of 30 test examples.

Main error patterns:

- Home places and social introduction can overlap when a sentence is also a self-introduction, for example `Jag bor i Stockholm`.
- Very short direction phrases such as `Är det långt?` can be too general.
- Family/school and transport can overlap for short time sentences such as `Jag kommer klockan tre`.
- Short general help sentences such as `Jag behöver hjälp` can be ambiguous without a health-place context.

## Interpretation

The result supports the idea that multilingual sentence embeddings are useful for classifying lecture-aligned beginner Swedish sentences into practical daily-life scenarios. The dataset is small, so the result should be interpreted as a course-project prototype rather than a production-level classifier.
