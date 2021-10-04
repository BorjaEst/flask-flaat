""" flask_flaat.login_manager
-----------------------------
The LoginManager class.
"""
import functools
from flask import request, abort

from flaat import Flaat, tokentools
from flask_login import LoginManager
import flask_login

from .config import TRUSTED_OP_LIST


class MyFlaat(Flaat):
    def __init__(self, app, *args, **kwargs):
        self.app = app
        super().__init__(*args, **kwargs)

    @property
    def trusted_op_list(self):
        return self.app.config['TRUSTED_OP_LIST']

    @trusted_op_list.setter
    def trusted_op_list(self, value):
        pass

    @property
    def client_id(self):
        return self.app.config['CLIENT_ID']

    @client_id.setter
    def client_id(self, value):
        pass

    @property
    def client_secret(self):
        return self.app.config['CLIENT_SECRET']

    @client_secret.setter
    def client_secret(self, value):
        pass


class FlaatLoginManager(LoginManager):
    """[summary]

    :param object: [description]
    :type object: [type]
    """

    def __init__(self, *args, **kwargs):
        LoginManager.__init__(self, *args, **kwargs)
        self._request_callback = lambda request: self.request_callback(request)

    def init_app(self, app, **kwargs):
        LoginManager.init_app(self, app, **kwargs)
        app.flaat = MyFlaat(app)
        app.flaat.set_web_framework('flask')
        app.config.setdefault('TRUSTED_OP_LIST', TRUSTED_OP_LIST)

    def login(self, route):
        @functools.wraps(route)
        def decorated(*args, **kwargs):
            at = tokentools.get_access_token_from_request(request)
            ti = tokentools.get_accesstoken_info(at) if at else abort(401)
            user_subiss = (ti['body']['sub'], ti['body']['iss'])
            user = self._user_callback(user_subiss)
            flask_login.login_user(user) if user else abort(401)
            return route(user, *args, **kwargs)
        return decorated

    def logout(self, route):
        @functools.wraps(route)
        def decorated(*args, **kwargs):
            user = flask_login.current_user
            return_val = route(user, *args, **kwargs)
            flask_login.logout_user()
            return return_val
        return flask_login.login_required(decorated)

    def request_loader(self, callback):
        raise RuntimeError("You should not use this method")

    def request_callback(self, request):
        at = tokentools.get_access_token_from_request(request)
        ti = tokentools.get_accesstoken_info(at) if at else abort(401)
        user_subiss = (ti['body']['sub'], ti['body']['iss'])
        return self._user_callback(user_subiss)
