from flask import Flask, request, jsonify
import tensorflow as tf
from keras.models import load_model
import re
from keras.preprocessing.sequence import pad_sequences
import nltk
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
import pandas as pd

app = Flask(__name__)

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    '''Removes HTML tags: replaces anything between opening and closing <> with empty space'''

    return TAG_RE.sub('', text)

def preprocess_text(sen):
    '''Cleans text data up, leaving only 2 or more char long non-stepwords composed of A-Z & a-z only
    in lowercase'''
    
    sentence = sen.lower()

    # Remove html tags
    sentence = remove_tags(sentence)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)  # When we remove apostrophe from the word "Mark's", the apostrophe is replaced by an empty space. Hence, we are left with single character "s" that we are removing here.

    # Remove multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)  # Next, we remove all the single characters and replace it by a space which creates multiple spaces in our text. Finally, we remove the multiple spaces from our text as well.

    # Remove Stopwords
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    sentence = pattern.sub('', sentence)

    return sentence

# Load the Keras sentiment analysis model
model = load_model('sentiment_LSTM_model.keras')
word_tokenizer = Tokenizer() 

# Function to run when the server starts
def on_start():
    data = pd.read_csv('csv_files/all_reviews.csv', sep=',', encoding='latin-1')
    Notkeep = [d for d in data.columns if d not in ['headline', 'pros', 'cons']]
    data = data.drop(Notkeep, axis=1)
    data['review'] = data['headline'] + '. ' + data['pros'] + '. ' + data['cons']
    data.drop(columns=['headline', 'pros', 'cons'], inplace=True)
    
    # Convert the 'review' column to strings
    data['review'] = data['review'].astype(str)
    
    X = []
    sentences = list(data['review'])
    for sen in sentences:
        X.append(sen)
    
    # Assuming word_tokenizer is defined somewhere in your code
    word_tokenizer.fit_on_texts(X)

# API endpoint to receive headline and predict sentiment
@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    data = request.get_json(force=True)
    review = data['review']
    print(review)
    unseen_processed = []
    unseen_processed.append(preprocess_text(review))
    unseen_tokenized = word_tokenizer.texts_to_sequences(unseen_processed)[0]
    unseen_padded = pad_sequences([unseen_tokenized], padding='post', maxlen=100)

    # Predict sentiment using the loaded Keras model
    unseen_sentiments = model.predict(unseen_padded)

    print(unseen_tokenized[0])
    print(unseen_sentiments)
    new_score = unseen_sentiments.tolist()

    return jsonify({'sentiment': new_score})

on_start()

if __name__ == '__main__':
    app.run(port=9090)
