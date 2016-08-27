import os

#
# Get the folder that the script lives in
#
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
WTF_CSRF_ENABLED = True
DEBUG = True
SECRET_KEY = 'my_precious'

#
# Define the full path for the database
#
DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
