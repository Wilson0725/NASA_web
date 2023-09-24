from flask import render_template

def hello_world():
    return render_template('index.html') 

def index():
    return render_template('index_test.html') 