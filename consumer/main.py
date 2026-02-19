from redis_connection import get_r
import json
import mongo_service

def main():
    r = get_r()
    mongo_service.create_unique_index('timestamp')
    while True:
        print("try read msg")
        try:
            message_id = r.brpop("URGENT",timeout=5)[1]

            full_message_hash = r.hgetall(f"message:{message_id}")

            data = json.loads(full_message_hash["data"])
            
            print(f"Full message details: {data}")

            mongo_service.inser_data(data=data)

            continue

        except TypeError:
            try:
                print("no data in URGENT trying in NORMAL")
                message_id = r.brpop("NORMAL",timeout=5)[1]

                full_message_hash = r.hgetall(f"message:{message_id}")

                data = json.loads(full_message_hash["data"])
                
                print(f"Full message details: {data}")

                mongo_service.inser_data(data=data)
            except TypeError:
                print("no data in NORMAL wetimg for new msg")
                continue


if __name__=="__main__":
    main()