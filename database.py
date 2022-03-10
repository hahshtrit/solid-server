from pymongo import MongoClient


class database:
    mongo_client = MongoClient("mongo")
    db = mongo_client["cse312"]

    def __init__(self, request):
        self.request = request
