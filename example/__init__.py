from flask import Flask

from .extensions import login_manager
from .routes import resource_blp, user_blp


def create_app(test_config={}):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.update(test_config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    login_manager.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(resource_blp,  url_prefix='/resource')
    app.register_blueprint(user_blp, url_prefix='/user')
