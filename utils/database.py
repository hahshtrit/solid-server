from pymongo import MongoClient
from utils.authentication import hash_password, create_auth_token
import bcrypt

mongo_client = MongoClient("mongo")
db = mongo_client["cse312"]

userinfo = db["userinfo"]


# username could be in plaintext

# db['userinfo'] should be
# {
# username: _               (in bytes)
# hash_salt_password: _     (in bytes)
# hash_salt_auth_token: _   (in bytes)
# }

def register_user(entered_username: str, entered_password: str, auth_token: str = ""):
    userinfo.insert_one({"username": entered_username, "password": hash_password(entered_password), "auth_token": b""})


# only need to query a user by username or auth_token
def find_user(username: str = "", auth_token: str = "") -> bool:
    if not username and not auth_token:
        print("At least one argument should be given")
        # and also, this stops exploits from getting access using empty auth_tokens
        return False

    if username:
        return True if userinfo.find_one({"username": username}, {"_id": 0}) else False
    elif auth_token:
        return True if userinfo.find_one({"auth_token": hash_token(auth_token)}, {"_id": 0}) else False

# db['messages'] should be
# {
# username: _               (in bytes)
# message: _                (in bytes)  <- this is multimedia content
# }
