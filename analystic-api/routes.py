from fastapi import APIRouter


route = APIRouter(prefix="/analytics")


@route.get("/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    pass

@route.get("/top-urgent-zones")
def top_urgent_zones():
    pass

@route.get("/distance-distribution")
def distance_distribution():
    pass

@route.get("/low-visibility-high-activity")
def low_visibility_high_activity():
    pass
