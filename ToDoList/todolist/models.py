from todolist import db
from datetime import datetime




class ToDoItem(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique = False, nullable=False)
	task = db.Column(db.String(120), unique = True, nullable=False)
	content = db.Column(db.Text ,nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	


	def __repr__(self):
		return '<User %r>' % self.name