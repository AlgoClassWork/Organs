#pip install flask
from flask import Flask, render_template, request
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    organs = get_all_organs()
    return render_template('index.html', organs=organs)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        description = request.form.get('description')
        price = request.form.get('price')
        image = request.form.get('image')

        add_organ(name, category, description, price, image)

    return render_template('admin.html')

app.run()
