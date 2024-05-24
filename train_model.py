import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
import joblib
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("surrey-nlp/PLOD-CW")

# Extract text and labels from the dataset
train_texts = [" ".join(item["tokens"]) for item in dataset["train"]]
train_labels = [item["ner_tags"] for item in dataset["train"]]

# Flatten the list of sentences and corresponding labels for training
flattened_train_texts = [word for sentence in train_texts for word in sentence.split()]
flattened_train_labels = [label for sublist in train_labels for label in sublist]

# Encode the labels
label_encoder = LabelEncoder()
encoded_train_labels = label_encoder.fit_transform(flattened_train_labels)

# Convert the dataset into a DataFrame
train_df = pd.DataFrame({"text": flattened_train_texts, "labels": encoded_train_labels})

# Build the model pipeline with TF-IDF and SVM
pipeline = make_pipeline(TfidfVectorizer(), SVC(kernel='linear', probability=True))

# Train the model
pipeline.fit(train_df['text'], train_df['labels'])

# Save the model and label encoder
joblib.dump(pipeline, 'svm_tfidf_model.joblib')
joblib.dump(label_encoder, 'label_encoder.joblib')

print("Model training and saving completed successfully.")
