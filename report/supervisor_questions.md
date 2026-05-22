# Questions for Supervisor

Dear Supervisor,

I am planning to build an embedding-based text classification system for Assignment 1.

The project idea is a Swedish daily-life scenario classifier for absolute beginner / pre-A1 learners. Given a Swedish learning sentence or short dialogue, the system predicts one of six lecture-aligned daily-life scenario labels: food_shop, family_school, health_places, transport, home_places, or social_intro.

I plan to create a small custom dataset of around 150-300 Swedish learner sentences. The dataset is aligned with vocabulary and themes from our Swedish beginner lecture materials, such as introductions, clarification phrases, food and shops, family words, places and prepositions, transport words, and simple health/place expressions. The dataset will be AI-assisted at the first draft stage, then manually checked for Swedish quality, English/Chinese translation, lecture-level appropriateness, and label correctness. Each item will contain Swedish text, English translation, Chinese translation, label, and lecture theme metadata.

For the embedding part, I plan to use a multilingual sentence embedding model such as `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`. I will compare multiple classifiers on top of the embeddings: Logistic Regression, SVM, Random Forest, and kNN. Evaluation will use an 80/20 train/test split, accuracy, macro-F1, classification reports, and confusion matrices.

My questions are:

1. Is this topic suitable for Assignment 1 as an embeddings system?
2. Does creating a small custom Swedish daily-life scenario dataset aligned with course lecture vocabulary meet the dataset creation expectation for pass with distinction?
3. Are the six labels reasonable, or would you recommend reducing or changing them?
4. Is comparing multilingual sentence embeddings with Logistic Regression, SVM, Random Forest, and kNN sufficient for the modelling part?
5. Is it acceptable to connect this classifier to Assignment 2, where a SisuTutor Agent uses the classifier as a tool to choose suitable Swedish practice material?

Best regards,

Maoxuan
