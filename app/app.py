from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template

from dotenv import load_dotenv

load_dotenv('./.flaskenv')

app = Flask(__name__)

@app.route("/")
def index():
    name = 'Jhon Smith'
    return render_template('index.html', name = name)

if __name__ == '__main__':
    app.run()