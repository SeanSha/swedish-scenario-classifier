---
license: cc-by-4.0
task_categories:
- text-classification
language:
- sv
- en
- zh
size_categories:
- n<1K
pretty_name: Swedish Pre-A1 Scenario Classification Dataset
tags:
- swedish
- language-learning
- sentence-embeddings
- text-classification
- pre-a1
---

# Swedish Pre-A1 Scenario Classification Dataset

This dataset contains 150 short Swedish learner sentences for text classification. It is designed for absolute beginner / pre-A1 learners and aligned with beginner Swedish lecture themes.

## Labels

- `food_shop`
- `family_school`
- `health_places`
- `transport`
- `home_places`
- `social_intro`

Each label has 25 examples.

## Columns

- `id`: unique example id
- `text`: Swedish learner sentence used as model input
- `english`: English translation
- `chinese`: Chinese translation
- `label`: classification label
- `lecture_theme`: topic group used during dataset design
- `source`: creation source
- `review_status`: review flag

## Intended Use

This dataset is intended for a course project on embedding-based text classification and for prototyping Swedish learning tools.

## Creation Process

The dataset was created through AI-assisted drafting and manual structuring. The vocabulary and themes were aligned with beginner Swedish lecture materials, but the public dataset contains newly written example sentences, not copied lecture content.

## Citation

If used, cite the accompanying GitHub repository for this assignment.
