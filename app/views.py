# first view function (in the app package)

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'random':'Hello random stuff'}
    return ''' <html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['random'] + '''</h1>
  </body>
</html>
'''
