from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from todolist.models import ToDoItem




class AddToDoItem(FlaskForm):
	name = StringField('Username:', validators=[DataRequired()])
	task = StringField('Task:', validators=[DataRequired()])
	content = TextAreaField('Content:', validators=[DataRequired()])
	submit = SubmitField('Submit')


	def validate_task(self, task):
		task = ToDoItem.query.filter_by(task=task.data).first()
		if task:
			raise ValidationError("Please enter a task that is not on the list")
	

	# def validate_title(self, title):
	# 	title = ToDoItem.query.filter_by(title=form.title.data).first()
	# 	if title:
	# 		raise ValidationError("Please Enter a To Do Task which is not existing")

