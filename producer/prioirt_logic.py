def set_priority(event:dict):
    if event["weapons_count"] > 0:
        return "URGENT"
    if event["distance_from_fence_m"] <= 50:
        return "URGENT"
    if event["people_count"] >= 8:
        return "URGENT"
    if event["vehicle_type"] == "trock":
        return "URGENT"
    if event["distance_from_fence_m"] <= 150 and event["people_count"] >= 4:
        return "URGENT"
    if event["vehicle_type"] == "jeep" and event["people_count"] >=3:
        return "URGENT"
    return "NORMAL"

def priority_log(events:list):
    for event in events:
        event["priority"] = set_priority(event)
    return events