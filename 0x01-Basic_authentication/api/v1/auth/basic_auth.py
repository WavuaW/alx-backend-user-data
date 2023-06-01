#!/usr/bin/env python3
'''Module for Basic User authentication
'''

from .auth import Auth


class BasicAuth(Auth):
    '''Basic Authorization Protocal Implementation
    '''
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''Scoopes Base64 section of the Authorization header
        '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        trancate = authorization_header.split(" ")[-1]
        return trancate     
