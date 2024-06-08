from flask import Flask
from flask_sqlAlchemy import SQLAlchemy
db = SQLAlchemy

def creat_app:
  app = flask(__name__)
  
  app.config['SECRET_KEY'] = 'screat-key-goes-here'
  app.config['SQLAlchemy_DATABASE_URL']='sqlite:///db.sqlite'
  
  db.init_app(app)
  
  from .auth import auth as auth_blueprint
  app.register_blueprint (auth_blueprint)
  
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  return app