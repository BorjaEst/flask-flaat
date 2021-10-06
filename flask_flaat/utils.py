""" flask_flaat.utils
----------------------
General utilities.
"""
import functools

import flask_login
from flaat import ensure_is_list
from flask import abort, current_app, has_request_context, request, session
from werkzeug.local import LocalProxy


def login_user(**kwargs):
    flaat = current_app.login_manager._flaat
    user_info = flaat._get_all_info_from_request(request)
    if not user_info:
        abort(401)

    user = current_app.login_manager._user_callback(user_info)
    result = flask_login.login_user(user, **kwargs) if user else abort(401)

    # WARNING Dirty code: Patch '_user_id' with what we really want to store
    session['_user_id'] = user_info    # Save user information
    return result


request_userinfo = LocalProxy(lambda: _get_userinfo())


def _get_userinfo():
    if has_request_context():
        flaat = current_app.login_manager._flaat
        if '_user_id' in session:
            return session.get('_user_id')
        else:
            return flaat._get_all_info_from_request(request)


def group_required(**flaat_kwargs):
    def wrapper(func):
        @functools.wraps(func)
        def decorated_view(*args, **kwargs):
            flaat = current_app.login_manager._flaat
            _group_required(flaat, request_userinfo, **flaat_kwargs)
            return func(*args, **kwargs)
        return flask_login.login_required(decorated_view)
    return wrapper


def _group_required(flaat, user_info, group=[], claim=None, match='all'):
    if user_info is None:
        abort(401)

    group = ensure_is_list(group)
    required_matches = flaat._determine_number_of_required_matches(
        match, group)
    if not required_matches:
        raise RuntimeError(
            f"Error interpreting the 'match' parameter: {match}")

    # copy entries from incoming claim
    (avail_group_entries, user_message) = flaat._get_entitlements_from_claim(
        user_info, claim)

    if not avail_group_entries:
        abort(403)

    # now we do the actual checking
    matches_found = 0
    for entry in avail_group_entries:
        for g in group:
            if entry == g:
                matches_found += 1

    if matches_found < required_matches:
        abort(403)

    return True
