from todoapp.repository.data import save,get_table_by_id,delete
from todoapp.models.todo_table import Todo_table
from todoapp.models.user import Users
from todoapp.services.todoServices import update_status_time,get_all_next_day
from .mail_service import send_mail
import threading
from todoapp import app1


def save_table(title,description,user):
    save(Todo_table(title,description,user=user))

def get_by_id(id):
    table=get_table_by_id(id)
    update_tables_todo(table)
    return table

def delete_table(id):
    table=Todo_table.query.get(id)
    if table:
        table.users=[]
        delete(table)

def update_table(table_id,title,description):
    table=Todo_table.query.get(table_id)
    if not table:
        return None
    table.set_title(title)
    table.set_description(description)
    save(table)


def update_tables_todo(table):
    for todo in table.todos:
        update_status_time(todo1=todo)

def add_user(table_id,email,current_user):
    print('------------',table_id)
    table=Todo_table.query.get(table_id)
    print('---------',table)
    if not table:
        return None
    user=Users.query.filter_by(email=email).first()
    print(user)
    if not user:
        return None
    table.add_user(user)
    print('-----------',table.serialize())
    save(table)
    thread = threading.Thread(
                    target=send_mail,
                    args=("Notification", "abdul123arj@gmail.com", [user.email], f"{table.title} Hasbeen shred with you by {current_user.email} ")
                )
    thread.start()
    

def sen_reminder_day_before():
    with app1.app_context():
        todos_one_day_from_current_date = get_all_next_day()
        for todo in todos_one_day_from_current_date:
            table =get_table_by_id(todo.todo_table_id)
            for user in table.users:
                thread = threading.Thread(
                    target=send_mail,
                    args=("Rminder", "abdul123arj@gmail.com", [user.email], "Your {todo.title} is pendding for tommorow")
                )
                thread.start()