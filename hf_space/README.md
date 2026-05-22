---
title: Swedish Scenario Classifier
emoji: 📚
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: mit
---

# Swedish Scenario Classifier

Working demo for a lecture-aligned Swedish pre-A1 scenario classifier.

The app classifies a short Swedish learner sentence into one of six labels:

- `food_shop`
- `family_school`
- `health_places`
- `transport`
- `home_places`
- `social_intro`

It uses `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` embeddings and a Linear SVM classifier trained on the included dataset at startup.
