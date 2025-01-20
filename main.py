#pip install flask
from flask import Flask, render_template
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    organs = get_all_organs()
    return render_template('index.html', organs=organs)

app.run()