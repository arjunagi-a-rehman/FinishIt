from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app1=Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI']='mysql://abdul:abdul@localhost:3306/todo'
app1.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app1)
bcrypt = Bcrypt(app1)
login_manager = LoginManager(app1)
login_manager.login_view = "user_login"
login_manager.login_message_category = "info"
from todoapp.controller import todoController
