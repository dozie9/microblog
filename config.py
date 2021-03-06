WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-no-go-know-am'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'https://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'https://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

import os
basedir = os.path.abspath(os.path.dirname(__file__))
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
#MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'dozie.steve'#os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = 'chidiogo'#os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['dozie.steve@gmail.com']

# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

