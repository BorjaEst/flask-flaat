""" flask_flaat.login_manager
-----------------------------
The LoginManager class.
"""
from flask_login import LoginManager
from flaat import Flaat


class MyFlaat(Flaat):
    def __init__(self, app, *args, **kwargs):
        self.app = app
        super().__init__(*args, **kwargs)

    @property
    def trusted_op_list(self):
        return self.app.config['TRUSTED_OP_LIST']

    @trusted_op_list.setter
    def trusted_op_list(self, value):
        self.app.config['TRUSTED_OP_LIST'] = value

    @property
    def client_id(self):
        return self.app.config['CLIENT_ID']

    @client_id.setter
    def client_id(self, value):
        self.app.config['CLIENT_ID'] = value

    @property
    def client_secret(self):
        return self.app.config['CLIENT_SECRET']

    @client_secret.setter
    def client_secret(self, value):
        self.app.config['CLIENT_SECRET'] = value


class FlaatLoginManager(LoginManager):
    """[summary]

    :param object: [description]
    :type object: [type]
    """

    def __init__(self, *args, **kwargs):
        LoginManager.__init__(self, *args, **kwargs)

    def init_app(self, app, **kwargs):
        app.flaat = MyFlaat(app)
        app.flaat.set_web_framework('flask')
        LoginManager.init_app(self, app, **kwargs)
