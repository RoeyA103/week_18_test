from pymongo import MongoClient , errors
import os

mongo_host = os.getenv("MONGO_URI","mongodb://mongo:27017")
mongo_db = os.getenv("MONGO_DB_NAME","test")
mongo_collection = os.getenv("MONGO_COLLECTION","events")


def get_collection():
    try:
        clinet = MongoClient(mongo_host)
        db =clinet[mongo_db]

        collection = db[mongo_collection]
        return collection
    except errors as e:
        raise e


