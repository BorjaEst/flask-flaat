from flask import Flask

from .extensions import database, login_manager
from .routes import resource_blp, user_blp


def create_app(config="settings.DefaultConfig"):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    database.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(resource_blp, url_prefix='/resource')
    app.register_blueprint(user_blp, url_prefix='/user')
