from todoapp import db
from .user_todo import Todo_table_User

class Todo_table(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=500), nullable=False)
    users = db.relationship('Users', secondary=Todo_table_User, back_populates='todo_tables', lazy=True)
    todos = db.relationship('Todo', backref='todo_table', lazy=True, cascade='all, delete-orphan')
    def __init__(self,title,description,user):
        self.title=title
        self.description=description
        self.users=[user]
    def set_title(self,title):
        self.title=title
    def set_description(self,description):
        self.description=description
    def get_todos(self):
        return {"todos":[todo.serialize() for todo in self.todos], "table_id":self.id}
    def add_user(self,user):
        self.users.append(user)    
    def get_users(self):
        return [user.serialize for user in self.users]

    def serialize(self):
        return{
            "id":self.id,
            "title":self.title,
            "description":self.description
        }
