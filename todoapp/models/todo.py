from typing import Any
from todoapp import db
from enum import Enum
from datetime import datetime
from .todo_table import Todo_table


class TodoStatus(Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'inprogress'
    DONE = 'done'
    DELAYED = 'delayed'




class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=500), nullable=False)
    status = db.Column(db.Enum(TodoStatus), nullable=False)
    target_date = db.Column(db.Date, default=None, nullable=True)
    todo_table_id=db.Column(db.Integer(), db.ForeignKey('todo_table.id'))

    def __init__(self, title, description, status,todo_table_id,target_date=None):
        self.title = title
        self.description = description
        self.set_status(status)
        self.target_date = target_date
        self.todo_table_id=todo_table_id

    def set_status(self, status):
        self.status = status

    def set_description(self,description):
        self.description=description

    def set_title(self,title):
        self.title=title

    def set_target_date(self,target_date):
        self.target_date=target_date
    def set_todo_table_id(self,todo_table_id):
        self.todo_table_id=todo_table_id

    def serialize(self):
        return {

            'id': self.id,
            'name': self.title,
            'description': self.description,
            'target_date':self.target_date,
            'status': self.status,
            'todo_table_id':self.todo_table_id
        }
