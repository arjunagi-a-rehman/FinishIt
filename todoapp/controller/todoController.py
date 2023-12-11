from todoapp import app1 as app
from todoapp.services.todoServices import getAll ,save_todo, updater_status,update_todo,delete_todo,register_user_service,get_verified_user
from flask import request,render_template,url_for,redirect,flash
from flask_login import login_user, logout_user, login_required,current_user
from todoapp.services.table_services import *
from todoapp.services.mail_service import *
from todoapp.forms.forms import *
import asyncio
from concurrent.futures import ThreadPoolExecutor
import threading

executor = ThreadPoolExecutor()
@app.route('/')
@app.route('/tables')
@login_required
def render_tables():
    return render_template('todo_tables.html',tables=current_user.all_todo_tables())
@app.route('/table',methods=['GET','POST'])
def post_table():
    save_table(request.form.get('title'),request.form.get('description'),current_user)
    return redirect(url_for('render_tables'))

@app.route('/table/delete/<int:id>',methods=['POST'])
def delete_table_api(id):
    delete_table(id)
    return redirect(url_for('render_tables'))

@app.route('/table/update',methods=['POST'])
def update_table_api():
    table_id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    update_table(table_id,title,description)
    return redirect(url_for('render_tables'))

@app.route('/table/share',methods=['POST'])
def add_user_to_table():
    table_id = request.form.get('id')
    email = request.form.get('email')
    add_user(table_id,email,current_user)
    return redirect(url_for('render_tables'))

@app.route('/todos/<int:id>')
@login_required
def renderindex(id):
    todos=getAll()
    return render_template('index.html',todos=get_by_id(id).get_todos(),table_name=get_by_id(id).title)


# @app.route('/todos')
# @login_required
# def get_all():
#     return current_user.all_todos()

@app.route('/todo',methods=['GET','POST'])
def post_todo():
    save_todo(request.form.get('title'),request.form.get('description'),request.form.get('target_date'),request.form.get('table_id'))
    return redirect(url_for('renderindex',id=request.form.get('table_id')))

@app.route('/todo/status/<int:id>',methods=['PUT','POST'])
@login_required
def update_status(id):
    new_status_str =  request.form['status']
    table_id=updater_status(id,new_status_str)
    return redirect(url_for('renderindex',id=table_id))

@app.route('/todo/update',methods=['POST','PUT'])
@login_required
def update_todo_api():
    todo_id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    target_date=request.form.get('target_date')
    table_id=update_todo(todo_id,title,description,target_date)
    return redirect(url_for('renderindex',id=table_id))

@app.route('/todo/<int:id>', methods=['POST', 'DELETE'])
@login_required
def delete_todo_api(id):
    table_id=delete_todo(id)
    return redirect(url_for('renderindex',id=table_id))

@app.route('/register',methods=['POST','GET'])
async def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        email=form.email_address.data
        register_user_service(name=form.username.data,
                              email=form.email_address.data,
                              password=form.password1.data)
        flash(f"Account created successfully!", category='success')
        thread = threading.Thread(
            target=send_mail,
            args=("Welcome", "your_email@example.com", [email], "Thanks for joining finish it")
        )
        thread.start()        
        return redirect(url_for('user_login'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)



@app.route('/login',methods=['POST','GET'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_verified_user(email=form.email.data,password=form.password.data)
        if user:
            login_user(user=user)
            return redirect(url_for('render_tables'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)
    

# need to make page
@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for("user_login"))


    

    


   