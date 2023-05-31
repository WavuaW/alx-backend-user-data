#!/usr/bin/env python3
""" Module for authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    '''API authentication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        '''Returns a header - authorization header
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Returns a header - authorization header
        '''
        return None
