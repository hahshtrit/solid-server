import sys

from pymongo import MongoClient
from utils.authentication import hash_password, hash_token

mongo_client = MongoClient("mongo")
db = mongo_client["cse312"]

userinfo = db["userinfo"]


# db['userinfo'] is
# {
# username: _               (in string)
# hash_salt_password: _     (in bytes)
# hash_salt_auth_token: _   (in bytes)
# dog:                      (in bool)
# }

# TODO: session IDs can be used instead of authentication tokens

def register(entered_username: str, entered_password: str, auth_token: str = "", profile_pic: bytes = None,
             dog: bool = True):
    userinfo.insert_one({"username": entered_username, "password": hash_password(entered_password), "auth_token": b"",
                         "profile_pic": profile_pic, "dog": dog})
    # print(list(userinfo.find()))
    sys.stdout.flush()


def change_animal(username: str, dog_person: bool):
    # reverse pref
    dog_person = False if dog_person else True
    userinfo.update_one({"username": username}, {'$set': {"dog": dog_person}})


def add_auth_token(username: str, auth_token):
    userinfo.update_one({"username": username}, {'$set': {"auth_token": hash_token(auth_token)}})


def remove_auth_token(username: str):
    userinfo.update_one({"username": username}, {'$set': {"auth_token": ""}})


def update_profile_picture(username: str, profile_pic):
    userinfo.update_one({"username": username}, {'$set': {"profile_pic": profile_pic}})


# only need to query a user by username or auth_token
def authenticate(username: str = "", auth_token: str = "") -> dict:
    if not username and not auth_token:
        print("At least one argument should be given")
        # and also, this stops exploits using empty auth_tokens
        return {}

    if username:
        return userinfo.find_one({"username": username}, {"_id": 0})
    elif auth_token:
        return userinfo.find_one({"auth_token": hash_token(auth_token)}, {"_id": 0})

# db['messages'] should be
# {
# username: _               (in bytes)
# message: _                (in bytes)  <- this is multimedia content
# }
