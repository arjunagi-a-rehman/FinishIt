from todoapp.models.todo import Todo
from todoapp.models.user import Users
from todoapp.models.todo_table import Todo_table
from todoapp import db

def getAllTodo():
    obj_list = Todo.query.all()
    return [ obj.serialize() for obj in obj_list]

def save(data):
    try:
        db.session.add(data)
        print(data.serialize())
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def get_by_id(id):
    return Todo.query.get(id)

def get_table_by_id(id):
    return Todo_table.query.get(id)

def delete(todo):
    db.session.delete(todo)
    db.session.commit()
