from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '776766d63eecce38ccea4f3ebb68c69b'
client = MongoClient('localhost', 27017)
db = client['sgda']
bcrypt = Bcrypt(app)


from SGDA import routes