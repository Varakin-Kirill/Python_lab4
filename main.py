from flask import Flask, request, render_template, url_for
import string
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    text = file.read().decode('utf-8')
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    counter = Counter(words)
    most_common_word = counter.most_common(1)[0][0]
    return render_template('result.html', word=most_common_word)

if __name__ == '__main__':
    app.run(debug=True)