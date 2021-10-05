""" flask_flaat.utils
----------------------
General utilities.
"""
import functools

import flask_login
from flaat import tokentools
from flask import abort, current_app, request, session


def login_user(**kwargs):
    at = tokentools.get_access_token_from_request(request)
    ti = tokentools.get_accesstoken_info(at) if at else abort(401)
    user = current_app.login_manager._user_callback(ti)
    result = flask_login.login_user(user, **kwargs) if user else abort(401)

    # WARNING Dirty code: Patch '_user_id' with what we really want to store
    session['_user_id'] = ti    # Save user information
    return result


def group_required(**flaat_kwargs):
    def wrapper(func):
        @functools.wraps(func)
        def decorated_view(*args, **kwargs):
            flaat = current_app.login_manager._flaat
            decorator = flaat.group_required
            return decorator(**flaat_kwargs)(func)(*args, **kwargs)
        return flask_login.login_required(decorated_view)
    return wrapper


def aarc_g002_group_required(**flaat_kwargs):
    def wrapper(func):
        @functools.wraps(func)
        def decorated_view(*args, **kwargs):
            flaat = current_app.login_manager._flaat
            decorator = flaat.aarc_g002_group_required
            return decorator(**flaat_kwargs)(func)(*args, **kwargs)
        return flask_login.login_required(decorated_view)
    return wrapper


def aarc_g002_entitlement_required(**flaat_kwargs):
    def wrapper(func):
        @functools.wraps(func)
        def decorated_view(*args, **kwargs):
            flaat = current_app.login_manager._flaat
            decorator = flaat.aarc_g002_entitlement_required
            return decorator(**flaat_kwargs)(func)(*args, **kwargs)
        return flask_login.login_required(decorated_view)
    return wrapper
