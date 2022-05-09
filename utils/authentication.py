import bcrypt

def hash_password(entered_pass: str):
    byte_pass = entered_pass.encode()
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(byte_pass, salt)
    return hashed_pass # hash_password in bytes

def create_auth_token():
    return