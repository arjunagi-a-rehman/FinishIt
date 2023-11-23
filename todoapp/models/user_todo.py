from todoapp import db


Todo_table_User=db.Table('Todo_table_User',
         db.Column('user_id',db.Integer(), db.ForeignKey('users.id')),
         db.Column('todo_table_id',db.Integer(), db.ForeignKey('todo_table.id'))
        )