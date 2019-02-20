from flask import Flask, session
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_user import UserManager, UserMixin
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user, current_user
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
import pymongo


class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = '776766d63eecce38ccea4f3ebb68c69b'

    # Flask-MongoEngine settings
    MONGODB_SETTINGS = {
        'db': 'sgda',
        'host': 'mongodb://localhost:27017/'
    }

    # Flask-User settings
    USER_APP_NAME = "SGDA"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form
    USER_UNAUTHORIZED_ENDPOINT = 'home'
    USER_UNAUTHENTICATED_ENDPOINT = 'login'
    USER_AFTER_LOGIN_ENDPOINT = 'home'
    USER_AFTER_LOGOUT_ENDPOINT = 'home'
    
app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')
app.static_folder = 'static'
db = MongoEngine(app)
bcrypt = Bcrypt(app)
global role
role = 'none'
#Inicializar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
class User(UserMixin, db.Document):
    meta = {'collection': 'usuario'}
    email = db.StringField(max_length=30)
    password = db.StringField()


#Conectar con base de datos
client = MongoClient('localhost', 27017)
db = client['sgda']
#Verificar si DB está inicializada o no
if db.usuarios.count() == 0:
    print("DEBUG: Inicializando usuarios de DB")
    usuarios = db.usuarios
    hashpass1 = bcrypt.generate_password_hash('soyjefe').decode('utf-8')
    hashpass2 = bcrypt.generate_password_hash('soysecretaria').decode('utf-8')
    usuarios_data = [
        {"_id": 1, "email": 'jefedpto@ciens.ucv.ve', "password": hashpass1, "username": 'jefe_dpto'},
        {"_id": 2, "email": 'secretaria@ciens.ucv.ve',"password": hashpass2, "username": 'secretaria'}
    ]
    usuarios.update(usuarios_data[0],usuarios_data[0],upsert=True)
    usuarios.update(usuarios_data[1],usuarios_data[1],upsert=True)
else:
    print("DEBUG: Usuarios de DB ya inicializados")

from SGDA import routes



