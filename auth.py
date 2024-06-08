from flask import blueprints

from . import db

auth = Blueprints('auth', __name__)

@auth.route('/login')
def login():
  return 'login'

@auth.route('/signup')
def signup():
  return 'Signup'

@auth.route('/logout')
def logout():
  return 'Logout'

