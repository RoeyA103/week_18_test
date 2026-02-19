import redis
import json

def get_r():
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    return r


    
