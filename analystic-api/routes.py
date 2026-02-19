from fastapi import APIRouter
import dal
import redis_service

route = APIRouter(prefix="/analytics")


@route.get("/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    res = redis_service.get_key("alerts_by_border_and_priority")
    if res:
        return res
    res =  dal.alerts_by_border_and_priority()
    redis_service.save_key(key="alerts_by_border_and_priority",val=res)
    return res

@route.get("/top-urgent-zones")
def top_urgent_zones():
    res = redis_service.get_key("top_urgent_zones")
    if res:
        return res
    res =  dal.top_urgent_zones()
    redis_service.save_key(key="top_urgent_zones",val=res)
    return res

@route.get("/distance-distribution")
def distance_distribution():
    res = redis_service.get_key("distance_distribution")
    if res:
        return res
    res =  dal.distance_distribution()
    redis_service.save_key(key="distance_distribution",val=res)
    return res

@route.get("/low-visibility-high-activity")
def low_visibility_high_activity():
    return {}
