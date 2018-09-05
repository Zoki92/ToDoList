from flask import render_template, url_for, redirect, flash, request
from todolist import app, db
from todolist.forms import AddToDoItem
from todolist.models import ToDoItem


@app.route("/")
def index():
	return render_template('index.html', title="Index")


@app.route("/addpost", methods=['GET', 'POST'])
def add_post():
	form = AddToDoItem()
	if form.validate_on_submit():
		td = ToDoItem(name=form.name.data, task=form.task.data, content=form.content.data)
		db.session.add(td)
		db.session.commit()
		flash("You have successfully submitted a task.", 'danger')
		return redirect(url_for('list_items'))	
	return render_template('addpost.html', title="Add Post", form=form)


@app.route("/list")
def list_items():
	items = ToDoItem.query.all()
	return render_template('list.html', title="List of Items", items=items)


@app.route("/delete", methods=['GET','POST'])
def delete_item():
	task = request.form.get("task")
	item= ToDoItem.query.filter_by(task=task).first()
	db.session.delete(item)
	db.session.commit()
	flash("Congrats! You have successfuly finished a task", 'success')
	return	redirect(url_for('list_items'))

