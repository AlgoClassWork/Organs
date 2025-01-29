#pip install flask
from flask import Flask, render_template, request, redirect, url_for
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    organs = get_all_organs()
    return render_template('index.html', organs=organs)

@app.route('/detail/<int:id>') 
def detail(id):
    organ = get_organ(id)
    return render_template('detail.html', organ=organ)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        action = request.form.get('action')
        id = request.form.get('id')
        name = request.form.get('name')
        category = request.form.get('category')
        description = request.form.get('description')
        price = request.form.get('price')
        image = request.form.get('image')

        if action == 'add':
            add_organ(name, category, description, price, image)
        if action == 'edit':
            update_organ(name, category, description, price, image, id)
        if action == 'delete':
            delete_organ(id)

    organs = get_all_organs()
    return render_template('admin.html', organs=organs)

app.run()
