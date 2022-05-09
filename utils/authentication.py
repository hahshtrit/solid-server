import bcrypt
from hashlib import sha1
from secrets import token_urlsafe


def hash_password(entered_pass: str) -> bytes:
    byte_pass = entered_pass.encode()
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(byte_pass, salt)
    return hashed_pass  # hash_password in bytes


def create_auth_token() -> str:
    auth_token: str = token_urlsafe(256)
    return auth_token


def hash_token(auth_token: str) -> bytes:
    # feel free to salt this if y'all like that kind of stuff ;0
    auth_token_hash: hash = sha1(auth_token.encode())
    return auth_token_hash.digest()
