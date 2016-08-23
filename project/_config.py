import os

#
# Get the folder that the script lives in
#
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

#
# Define the full path for the database
#
DATABASE_PATH = os.path.join(basedir, DATABASE)
