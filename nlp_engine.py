import pickle
import numpy as np
import os

# Define paths to the pre-trained models (Ensure these are generated in your local environment)
MODEL_PATH = 'models/logistic_regression_model.pkl'
VECTORIZER_PATH = 'models/tfidf_vectorizer.pkl'

# Load models safely into memory once on startup to reduce latency
try:
    with open(MODEL_PATH, 'rb') as f:
        clf = pickle.load(f)
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
    MODELS_LOADED = True
except FileNotFoundError:
    MODELS_LOADED = False
    print("Warning: ML models not found. Please run training script first.")

def analyze_payload(payload):
    """
    Vectorizes the incoming HTTP payload and predicts if it is malicious.
    """
    if not MODELS_LOADED:
        return {"is_malicious": False, "confidence": 0.0, "error": "Models not loaded"}
        
    try:
        # Transform the raw text payload into a mathematical vector
        vectorized_payload = vectorizer.transform([payload])
        
        # Predict probability (0 = Benign, 1 = Malicious)
        prediction = clf.predict(vectorized_payload)[0]
        probability = clf.predict_proba(vectorized_payload)[0][prediction]
        
        return {
            "is_malicious": bool(prediction == 1),
            "confidence": round(float(probability), 4),
            "engine": "TF-IDF + Logistic Regression"
        }
    except Exception as e:
        return {"is_malicious": False, "confidence": 0.0, "error": str(e)}