from pymongo import MongoClient
from utils.authentication import hash_password, create_auth_token
import bcrypt

mongo_client = MongoClient("mongo")
db = mongo_client["cse312"]

# db['userinfo'] should be
# {
# username: _               (in bytes)
# hash_salt_password: _     (in bytes)
# hash_salt_auth_token: _   (in bytes)
# }

def register_user(entered_username: str, entered_password: str):
    # hash+salt pass, store
    pass

def validate_login(entered_username: str, entered_password: str):
    return False

# db['messages'] should be
# {
# username: _               (in bytes)
# message: _                (in bytes)  <- this is multimedia content
# }