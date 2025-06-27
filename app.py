from flask import Flask, request, render_template
import joblib
from utils.preprocess import clean_text

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_spam(message):
    cleaned = clean_text(message)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)
    return "Spam" if pred[0] == 1 else "Not Spam"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        msg = request.form['message']
        result = predict_spam(msg)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
