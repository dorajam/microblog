# you need this file to specify that the "app" folder is a package

from flask import Flask

app = Flask(__name__)     # this is an instance -> different from the app package (folder)
from app import views