#!/usr/bin/env python3
"""Module for the API's session authentication
"""

from uuid import uuid4

from .auth import Auth


class SessionAuth(Auth):
    """A Session authentication class that Inherits from the AUTH class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creating a session id fo the user
        """
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
