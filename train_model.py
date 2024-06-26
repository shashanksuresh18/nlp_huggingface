import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
import joblib
from datasets import load_dataset

dataset = load_dataset("surrey-nlp/PLOD-CW")

train_texts = [" ".join(item["tokens"]) for item in dataset["train"]]
train_labels = [item["ner_tags"] for item in dataset["train"]]

flattened_train_texts = [word for sentence in train_texts for word in sentence.split()]
flattened_train_labels = [label for sublist in train_labels for label in sublist]

label_encoder = LabelEncoder()
encoded_train_labels = label_encoder.fit_transform(flattened_train_labels)

train_df = pd.DataFrame({"text": flattened_train_texts, "labels": encoded_train_labels})

pipeline = make_pipeline(TfidfVectorizer(), SVC(kernel='linear', probability=True))

pipeline.fit(train_df['text'], train_df['labels'])

joblib.dump(pipeline, 'svm_tfidf_model.joblib')
joblib.dump(label_encoder, 'label_encoder.joblib')

print("Model training and saving completed successfully.")
