# first view function (in the app package)
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'random':'Dora'}
    posts = [
        {
            'author': {'name':'Dorika'},
            'body': 'This looks promising'
        },
        {
            'author':{'name':'Dorika'},
            'body': 'Even more promising'
        }
    ]

    # arguments after your index.html should be all dynamic content variables
    return render_template('index.html', title='Home', user=user,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
