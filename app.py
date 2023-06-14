from flask import Flask, render_template
from flask_migrate import Migrate
from db import db

app = Flask(__name__)

@app.route('/')
def weather():
    return render_template('index.html')

if __name__ == '__main__':
    app.run