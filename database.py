from pymongo import MongoClient


class database:
    mongo_client = MongoClient("mongo")
    db = mongo_client["cse312"]
    users = db['users']
    comments = db['comments']

    def __init__(self, request):
        self.request = request

