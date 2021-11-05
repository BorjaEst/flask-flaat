from flask_flaat import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api


login_manager = LoginManager()
database = SQLAlchemy()
api = Api()
