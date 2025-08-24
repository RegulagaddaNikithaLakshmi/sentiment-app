from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    subjectivity = None
    text = ""

    if request.method == 'POST':
        # 1. Read the input text from the form
        text = request.form['text']

        # 2. Use TextBlob to calculate polarity and subjectivity
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Determine sentiment category based on polarity score
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

    # 3. Pass results to the HTML template to display on webpage
    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity, text=text)

if __name__ == '__main__':
    app.run(debug=True)
