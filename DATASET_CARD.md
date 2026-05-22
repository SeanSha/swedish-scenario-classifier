# Dataset Card: Swedish Pre-A1 Scenario Classification Dataset

## Dataset Description

This dataset contains 150 short Swedish learner sentences for text classification. It is designed for absolute beginner / pre-A1 learners and aligned with beginner lecture themes such as introductions, clarification phrases, food and shops, family and school, health-related places, transport, and home/location prepositions.

## Labels

- `food_shop`
- `family_school`
- `health_places`
- `transport`
- `home_places`
- `social_intro`

Each label has 25 examples.

## Fields

- `id`: unique example id
- `text`: Swedish learner sentence used as model input
- `english`: English translation
- `chinese`: Chinese translation
- `label`: classification label
- `lecture_theme`: topic group used during dataset design
- `source`: creation source
- `review_status`: review flag

## Intended Use

The dataset is intended for a course project on embedding-based text classification and for prototyping Swedish learning tools. It is not intended as a production dataset.

## Creation Process

The dataset was created through AI-assisted drafting and manual structuring. The vocabulary and themes were aligned with beginner Swedish lecture materials, but the public dataset contains newly written example sentences, not copied lecture content.

## License

Dataset license: CC BY 4.0.
