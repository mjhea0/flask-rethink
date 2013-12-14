from flask import render_template, url_for, redirect, g
from app import app
from forms import TaskForm

@app.route("/")
def index():
    form = TaskForm()
    return render_template('index.html', form=form)
