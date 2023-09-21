from flask import Flask

app = Flask(__name__)
tmp = 'Hello {name}! \n{message}'

@app.route('/')
def home():
    return tmp

@app.route('/about')
def about():
    return 'About'
