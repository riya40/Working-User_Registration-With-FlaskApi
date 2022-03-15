from flask import Flask
from flask_jwt_extended.config import config
from flask_mongoengine import MongoEngine
from flask_restful import Api, Resource
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_bcrypt import generate_password_hash, check_password_hash, Bcrypt
from flask_mail import Mail



app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'login_record_db',
    'host': 'localhost',
    'port': 27017
}

app.config['MONGODB_SETTINGS'] = {
'host': 'mongodb://localhost/login_record_db'
}


db = MongoEngine(app)
db = MongoEngine()
db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mail = Mail(app)
app.config.from_envvar('E:\cfppython\testusermain\.env')


