""" flask_flaat.utils
----------------------
General utilities.
"""
import functools

import flask_login
from flask import abort, current_app, has_request_context, request, session
from werkzeug.local import LocalProxy


def login_user(**kwargs):
    flaat = current_app.login_manager._flaat
    userinfo = flaat._get_all_info_from_request(request)
    if not userinfo:
        abort(401)

    user = current_app.login_manager._user_callback(userinfo)
    result = flask_login.login_user(user, **kwargs) if user else abort(401)

    # WARNING Dirty code: Patch '_user_id' with what we really want to store
    session['_user_id'] = userinfo    # Save user information
    return result


current_userinfo = LocalProxy(lambda: _get_userinfo())


def _get_userinfo():
    if has_request_context():
        flaat = current_app.login_manager._flaat
        if '_user_id' in session:
            return session.get('_user_id')
        else:
            return flaat._get_all_info_from_request(request)


def scope_required(scope):
    def wrapper(func):
        @functools.wraps(func)
        def decorated_view(*args, **kwargs):
            if current_userinfo._get_current_object() is None:
                abort(401, f"Invalid or missing authentication token")
            if scope not in current_userinfo:
                abort(403, f"No scope '{scope}' available at user info")
            return func(*args, **kwargs)
        return decorated_view
    return wrapper
