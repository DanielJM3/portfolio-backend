from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask('__name__', template_folder='./website/templates', static_folder='./website/static')

app.config['SECRET_KEY'] = '333333333333333333333333333333333'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website/database_name.db'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'email@gmail.com',
    "MAIL_PASSWORD": 'password'
}

app.config.update(mail_settings)
mail=Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'devLogin'

from website import routes