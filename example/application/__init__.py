from flask import Flask

from .extensions import database, login_manager, api
from .routes import resource_blp, user_blp
from flask_flaat import current_userinfo, current_user


def create_app(config="settings.DefaultConfig"):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    api.init_app(app)
    database.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    api.register_blueprint(resource_blp, url_prefix='/resource')
    api.register_blueprint(user_blp, url_prefix='/user')
