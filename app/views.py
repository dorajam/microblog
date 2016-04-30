# first view function (in the app package)
from flask import render_template
from app import app

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
    return render_template('index.html', title='Home', user=user['random'],posts=posts)
