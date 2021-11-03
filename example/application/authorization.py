import flask_flaat
from flask import current_app
from flask_flaat import login_required

from .extensions import login_manager
from .models import User

__all__ = ['login_required', 'admin_required']


@login_manager.user_loader
def load_user(user_info):
    return User.query.get((
        user_info['body']['sub'],
        user_info['body']['iss'],
    ))


@flask_flaat.scope_required('eduperson_entitlement')
def admin_required(entitlements):
    any_of = current_app.config['ADMIN_ENTITLEMENTS']
    return not set(any_of).isdisjoint(entitlements)
