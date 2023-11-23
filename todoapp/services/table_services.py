from todoapp.repository.data import save,get_table_by_id,delete
from todoapp.models.todo_table import Todo_table
from todoapp.models.user import Users

def save_table(title,description,user):
    save(Todo_table(title,description,user=user))

def get_by_id(id):
    return get_table_by_id(id)

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

def add_user(table_id,email):
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
    

