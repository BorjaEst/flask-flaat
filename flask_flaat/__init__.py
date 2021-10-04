""" flask_flaat
---------------
This module provides user session management for Flask using oidc tokens. 
It lets you log your users in and out in a database-independent manner.
:copyright: (c) 2021 Borja Esteban.
:license: MIT, see LICENSE for more details.
"""

from .login_manager import FlaatLoginManager as LoginManager
from .mixins import UserMixin
from flask_login import login_user, logout_user


__all__ = ["LoginManager", "UserMixin", "login_user", "logout_user"]
