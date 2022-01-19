from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from datetime import timedelta
# initializes the object of Flask
app = Flask(__name__)
# sets the config for the object
app.config['SECRET_KEY'] = "dev"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=1)
# initializes a SQLAlchemy object with the flask app object
database = SQLAlchemy(app)
login = LoginManager(app)



# this prevents a circular import and imports the routes so they are all used
from flaskblog import routes