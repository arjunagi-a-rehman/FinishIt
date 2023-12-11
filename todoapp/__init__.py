from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app1=Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost:3306/finishit'
app1.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app1)
bcrypt = Bcrypt(app1)
login_manager = LoginManager(app1)
login_manager.login_view = "user_login"
login_manager.login_message_category = "info"

app1.config['MAIL_SERVER']='smtp.gmail.com'
app1.config['MAIL_PORT'] = 465
app1.config['MAIL_USERNAME'] = 'abdul123arj@gmail.com'
app1.config['MAIL_PASSWORD'] = "gsto fpyg lwyu jsuk"
app1.config['MAIL_USE_TLS'] = False
app1.config['MAIL_USE_SSL'] = True




from .services.schedular_services import *
print("starting")
scheduler.start()
from todoapp.controller import todoController
