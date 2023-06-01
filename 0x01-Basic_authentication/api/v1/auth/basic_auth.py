#!/usr/bin/env python3
'''Module for Basic User authentication
'''
import base64
from .auth import Auth


class BasicAuth(Auth):
    '''Basic Authorization Protocal Implementation
    '''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''Scoopes Base64 section of the
        Authorization header
        '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        trancate = authorization_header.split(" ")[-1]
        return trancate

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        '''Determines if the header is to be decode/encode
        '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoding = base64_authorization_header.encode('utf-8')
            decoding = base64.b64decode(decoding)
            return decoding.decode('utf-8')
        except Exception:
            return None
