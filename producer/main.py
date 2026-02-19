import json
from prioirt_logic import priority_log
from redis_service import insert_many


def load_json_file():
    with open("border_alerts.json") as f:
        file = json.load(f)
        return file
    
def main():
    events = load_json_file()

    events = priority_log(events=events)

    insert_many(events)


main()