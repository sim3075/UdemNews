from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.posts import post
from routes.auth import auth
from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/udemnews'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ClaveUltraSecreta'

db.init_app(app)


app.register_blueprint(auth)

app.register_blueprint(post)

app.add_url_rule('/', endpoint='index')

