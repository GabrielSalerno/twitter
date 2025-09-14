import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True, instance_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance'))
app.config['SECRET_KEY']='de3ac1bccfc9365936f4f1e168cef1e6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Você precisa estar logado para acessar esta página."
login_manager.login_message_category = 'info'

from twitterflask import routes