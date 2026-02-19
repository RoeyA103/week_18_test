from fastapi import APIRouter
import dal

route = APIRouter(prefix="/analytics")


@route.get("/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    return dal.alerts_by_border_and_priority()

@route.get("/top-urgent-zones")
def top_urgent_zones():
    return dal.top_urgent_zones()

@route.get("/distance-distribution")
def distance_distribution():
    return dal.distance_distribution()

@route.get("/low-visibility-high-activity")
def low_visibility_high_activity():
    pass
