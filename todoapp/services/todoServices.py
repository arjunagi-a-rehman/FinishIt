from todoapp.repository.data import getAllTodo,save,get_by_id,delete
from todoapp.models.todo import Todo,TodoStatus
from todoapp.models.user import Users


def getAll():
    return getAllTodo()

def save_todo(title,descrition,target_date,table_id):
    save(Todo(title=title,description=descrition,status=TodoStatus.PENDING,todo_table_id=table_id,target_date=target_date))

def updater_status(id,status):
    todo1=get_by_id(id)
    if(todo1 is None):
        return None
    new_status = TodoStatus(status)
    todo1.set_status(new_status)
    save(todo1)
    return todo1.todo_table_id

def update_todo(todo_id,title,description,target_date):
    todo=get_by_id(todo_id)
    if(todo is None):
        return None
    todo.title=title
    todo.set_description(description)
    todo.target_date=target_date
    save(todo)
    return todo.todo_table_id


def delete_todo(id):
    todo=get_by_id(id)
    table_id= todo.todo_table_id
    if(todo is None):
        return None
    delete(todo)
    return table_id


def register_user_service(name,email,password):
    user=Users()
    user.name=name
    user.email=email
    user.set_password(password)
    save(user)

def get_verified_user(email,password):
    user=Users.query.filter_by(email=email).first()
    if(user and user.check_password(password)):
        return user
    return None


