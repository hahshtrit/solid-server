import bcrypt
from hashlib import sha1
from secrets import token_urlsafe


def hash_password(entered_pass: str) -> bytes:
    hashed_pass = bcrypt.hashpw(entered_pass.encode(), bcrypt.gensalt())
    return hashed_pass  # hash_password in bytes


def generate_auth_token() -> str:
    auth_token: str = token_urlsafe(256)
    return auth_token


def hash_token(auth_token: str) -> bytes:
    # this part has to be consistent, therefore no salting
    auth_token_hash: hash = sha1(auth_token.encode())
    return auth_token_hash.digest()
