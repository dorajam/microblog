# you need this file to specify that the "app" folder is a package

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)     # this is an instance -> different from the app package (folder)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
