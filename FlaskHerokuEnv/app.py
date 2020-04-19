import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    greeting = "Hello"
    try:
        excited = os.environ['EXCITED']
        greeting = greeting + "!!!!!"
    except:
        pass

    return render_template("index.html", greeting=greeting)
