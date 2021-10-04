""" flask_flaat
---------------
This module provides user session management for Flask using oidc tokens. 
It lets you log your users in and out in a database-independent manner.
:copyright: (c) 2021 Borja Esteban.
:license: MIT, see LICENSE for more details.
"""

from flask_login import (AnonymousUserMixin, current_user, login_required,
                         logout_user)

from .login_manager import FlaatLoginManager as LoginManager
from .mixins import UserMixin
from .utils import login_user

__all__ = [
    "LoginManager",
    "UserMixin",
    "AnonymousUserMixin",
    "login_user",
    "logout_user",
    "login_required",
    "current_user",
]
