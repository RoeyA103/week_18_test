from mongo_connection import get_collection
from pymongo import ASCENDING
from pymongo.errors import BulkWriteError
from datetime import datetime

def create_unique_index(index:str):
    collection = get_collection()
    collection.create_index(index,unique=True)

def inser_data(data:dict) -> int:
    collection = get_collection()
    try:

        data["insertion_time"] = datetime.utcnow()

        res = collection.insert_one(data)
        
        print("data inserted to mongo")

        
    except BulkWriteError:
        print("Duplicate order_id")
    except Exception as e:
        print(e)