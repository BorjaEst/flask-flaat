""" flask_flaat.login_manager
-----------------------------
The LoginManager class.
"""

import flask_login
from flask_login import AnonymousUserMixin

__all__ = ["UserMixin", "AnonymousUserMixin"]


class UserMixin(flask_login.UserMixin):
    '''
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    '''

    def get_id(self):
        try:
            return (self.token_sub, self.token_iss)
        except AttributeError:
            error_msg = 'No `token_sub` or `token_iss` - override `get_id`'
            raise NotImplementedError(error_msg)



