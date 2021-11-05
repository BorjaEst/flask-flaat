""" flask_flaat.login_manager
-----------------------------
The LoginManager class.
"""
from flaat import Flaat
from flask import abort
from flask_login import LoginManager

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
        self._flaat = None
        self._request_callback = lambda request: self.request_callback(request)

    def init_app(self, app, **kwargs):
        LoginManager.init_app(self, app, **kwargs)
        self._flaat = MyFlaat(app)
        self._flaat.set_web_framework('flask')
        app.config.setdefault('TRUSTED_OP_LIST', TRUSTED_OP_LIST)

    def request_loader(self, callback):
        raise RuntimeError("You should not use this method")

    def request_callback(self, request):
        try:
            userinfo = self._flaat._get_all_info_from_request(request)
            return self._user_callback(userinfo) if userinfo else None
        except TypeError:
            return None
