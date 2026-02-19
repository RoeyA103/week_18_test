from mongo_connection import get_collection


def alerts_by_border_and_priority():
    collection = get_collection()
    pipline3 = [
            {"$group":{
                "_id":{
                    "border":"$border","priority":"$priority"} ,
                    "total" : {"$sum":1}
            }},
            { "$project": {
            "_id": 0,
            "border": "$_id.border",
            "priority": "$_id.priority",
            "total": "$total"
        }},
        {
            "$sort":{"priority":-1}
        }
        ]
    res =list(collection.aggregate(pipline3))

    return res

def top_urgent_zones()->list:
    collection = get_collection()
    pipline3 = [{
        "$match":{"priority":"URGENT"}
    },
            {"$group":{
                "_id":"$border" ,
                    "total" : {"$sum":1}
            }},
            { "$project": {
            "_id": 0,
            "border": "$_id",
            "priority":1,
            "total": "$total"
        }},
        {
            "$sort":{"total":-1}
        }
        ]

    return list(collection.aggregate(pipline3))

def distance_distribution()-> list:
    collection = get_collection()
    pipline1 = [{
            "$match": {"distance_from_fence_m":{"$lte":300}}
    },
            {"$group":{
                "_id":"null" ,
                "close" : {"$sum":1}
            }},

            { "$project": {
            "_id": 0,
            "close":1
        }}
        ]

    pipline2 = [{
            "$match": {"distance_from_fence_m":{"$lte":800,
                                                "$gte":301}}
    },
            {"$group":{
                "_id":"null" ,
                "mid" : {"$sum":1}
            }},

            { "$project": {
            "_id": 0,
            "mid":1
        }}
        ]

    pipline3 = [{
            "$match": {"distance_from_fence_m":{"$lte":1500,
                                                "$gte":801}}
    },
            {"$group":{
                "_id":"null" ,
                "far" : {"$sum":1}
            }},

            { "$project": {
            "_id": 0,
            "far":1
        }}
        ]

    close = list(collection.aggregate(pipline1))[0]["close"]
    mid = list(collection.aggregate(pipline2))[0]["mid"]
    far = list(collection.aggregate(pipline3))[0]["far"]

    return {"total-close":close,"total_mid":mid,"total_far":far}


