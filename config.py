WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


import os
basedir = os.path.abspath(os.path.dirname(__file__))
print os.path.dirname(__file__)
print basedir

# the URI just creates an identifier for the file, this is not equal to the locator (URL)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')  # here its a path to our DB file
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')  # folder for the SQL migrate files

