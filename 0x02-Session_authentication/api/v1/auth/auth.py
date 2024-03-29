#!/usr/bin/env python3
""" Module for authentication
"""
import os
import re
from flask import request
from typing import List, TypeVar


class Auth:
    '''API authentication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Checks the path and determines if it requiree authentication
        or not'''
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for y in excluded_paths:
                if y.startswith(path):
                    return False
                if path.startswith(y):
                    return False
                if y[-1] == '*':
                    if path.startswith(y[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        '''Returns a header - authorization header
        '''
        if request is None:
            return None
        auth_head = request.headers.get('Authorization')
        if auth_head is None:
            return None
        return auth_head

    def current_user(self, request=None) -> TypeVar('User'):
        '''Returns a header - authorization header
        '''
        return None

    def session_cookie(self, request=None) -> str:
        """Returns SESSION_NAME cookie's value
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
