from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  


model = pickle.load(open(r'..\saved_models\phishing_model.pkl', 'rb'))
vectorizer = pickle.load(open(r'..\saved_models\tfidf_vectorizer.pkl', 'rb'))

@app.route('/detect-phishing', methods=['POST'])
def detect_phishing():
    email_text = request.json['text']
    email_vectorized = vectorizer.transform([email_text])
    prediction = model.predict(email_vectorized)
    return jsonify({'phishing': bool(prediction[0])})

if __name__ == "__main__":
    app.run()
