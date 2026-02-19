from redis_connection import get_r
import json

def get_key(key:str):
    r = get_r()
    val = r.get(key)
    if val:
        val = json.loads(val)
        print("data loded from redis")
    r.close()
    return val

def save_key(key:str,val):
    try:
        r = get_r()
        res = r.setex(name=key,value=json.dumps(val),time=300)
        print("data inserted to redis")
        r.close()
        return res
    except Exception as e:
        raise e
    
