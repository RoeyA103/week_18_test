from redis_connection import get_r
import json

def insert_event(event:dict,queue:str,message_id:str):
    try:
        r = get_r()

        r.lpush(queue, message_id)

        r.hmset(f"message:{message_id}", mapping=
                {"data":json.dumps(event)})

        print("event inserted to redis successfuly")

    except Exception as e:
        print(e)

def insert_many(events:list[dict]):
    for event in events:
        insert_event(event=event,queue=event["priority"],message_id=event["timestamp"])
