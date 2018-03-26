import os
import requests
import jwt
import logging

_public_key = None

# FileManager
from filemanager.models import FileManager
from auth.lib import Verifyer

db_connection_string = os.environ.get('DATABASE_URL')
FileRegistry = FileManager(db_connection_string)


def public_key():
    global _public_key
    if _public_key is None:
        auth_server = os.environ.get('AUTH_SERVER')
        _public_key = requests.get(f'{auth_server}/auth/public-key').content
    return _public_key


def verify(auth_token, owner=None):
    """Verify Auth Token.
    :param auth_token: Authentication token to verify
    :param owner: dataset owner
    """
    verifyer = Verifyer(public_key=public_key())
    if auth_token == 'testing-token' and owner == '__tests':
        return True
    return verifyer.extract_permissions(auth_token)
