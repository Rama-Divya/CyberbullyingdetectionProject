from flask import Flask, render_template, request, session, redirect, url_for
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the stopwords, vectorizer, and model
with open("stopwords.txt", "r") as file:
    stopwords = file.read().splitlines()

vectorizer = pickle.load(open("vectorizer_data.pkl", "rb"))
model = pickle.load(open("classification_model", 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    input_text = None
    
    # Handle form submission (POST request)
    if request.method == 'POST':
        user_input = request.form['text']
        input_text = user_input  # Store the input text for re-rendering
        if user_input:
            transformed_input = vectorizer.transform([user_input])
            prediction = model.predict(transformed_input)[0]
            # Convert prediction to readable result
            prediction = "Cyberbullying" if prediction == 1 else "Not Cyberbullying"
        else:
            prediction = None  # If no input is provided, no prediction

    return render_template('index.html', prediction=prediction, input_text=input_text)

@app.route('/clear', methods=['POST'])
def clear():
    return redirect(url_for('index'))
@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

if __name__ == '__main__':
    app.run(debug=True)
