from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask import Flask
from flask_login import LoginManager
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()
# initializes the object of Flask
app = Flask(__name__)
# sets the config for the object
app.config['SECRET_KEY'] = os.getenv("secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("db-uri")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=1)


# initializes a SQLAlchemy object with the flask app object
database = SQLAlchemy(app)


try:
        # db.session.execute('SELECT 1')
        database.session.execute(text('SELECT 1'))
        print('\n\n----------- Connection successful !')
except Exception as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)
login = LoginManager(app)



# this prevents a circular import and imports the routes so they are all used
from flaskblog import routes