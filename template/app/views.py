from flask import render_template, url_for, redirect
from app import app
from forms import TaskForm

@app.route('/', methods = ['GET', 'POST'])
def index():
	form = TaskForm()
	if form.validate_on_submit():
		task = Task(label = form.label.data)
		task.save()
		return redirect(url_for('index'))

	return render_template('index.html', form = form)
