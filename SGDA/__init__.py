from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_user import UserManager, UserMixin
from flask_login import LoginManager
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface


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
client = MongoClient('localhost', 27017)
db = client['sgda']
bcrypt = Bcrypt(app)
db = MongoEngine(app)

class User(db.Document, UserMixin):
        active = db.BooleanField(default=True)

        # User authentication information
        username = db.StringField(default='')
        password = db.StringField()

        # User information
        first_name = db.StringField(default='')
        last_name = db.StringField(default='')

        # Relationships
        roles = db.ListField(db.StringField(), default=[])

user_manager = UserManager(app, db, User)
app.session_interface = MongoEngineSessionInterface(db)


from SGDA import routes