""" flask_flaat.login_manager
-----------------------------
The LoginManager class.
"""

import flask_login


class UserMixin(flask_login.UserMixin):
    """This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    """

    def get_id(self):
        """Patched at flask_flaat.utils:30"""
        return None
