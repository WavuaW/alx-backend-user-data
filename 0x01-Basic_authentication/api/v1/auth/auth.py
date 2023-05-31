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
        '''Returns a header - authorization header'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
