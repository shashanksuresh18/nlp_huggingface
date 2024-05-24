
import joblib
import re
from flask import Flask, request, jsonify, render_template
import logging
import datetime

app = Flask(__name__)

logging.basicConfig(filename='model_logs.log', level=logging.INFO)

# Load the trained model and label encoder
model = joblib.load('svm_tfidf_model.joblib')
label_encoder = joblib.load('label_encoder.joblib')

def tokenize(text):
    # Split text into words and punctuation
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    return tokens

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form['text']
        words = tokenize(text)
        
        # Predict labels for each word
        predictions = model.predict(words)
        decoded_predictions = label_encoder.inverse_transform(predictions)
        
        results = [{"word": word, "prediction": pred} for word, pred in zip(words, decoded_predictions)]
        
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "input": text,
            "predictions": results
        }
        logging.info(log_entry)
        
        return render_template('result.html', results=results, text=text)
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/testpredict', methods=['POST'])
def testpredict():
    try:
        data = request.get_json()
        text = data['text']
        words = tokenize(text)
        
        # Predict labels for each word
        predictions = model.predict(words)
        decoded_predictions = label_encoder.inverse_transform(predictions)
        
        results = [{"word": word, "prediction": pred} for word, pred in zip(words, decoded_predictions)]
        
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "input": text,
            "predictions": results
        }
        logging.info(log_entry)
        
        return jsonify(results)
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
