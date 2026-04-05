# app/api/main.py
from fastapi import FastAPI
from app.api.routers import meetings_router, action_items_router

app = FastAPI(
    title="Meeting Note Assistant API",
    version="0.2.0",
    description="Meetings, notes, and action items management",
)


@app.get("/health")
def health():
    return {"status": "ok"}


# incluir routers
app.include_router(meetings_router)
app.include_router(action_items_router)


# Session 14 – Challenge: GET /dashboard/summary
@app.get("/dashboard/summary")
def dashboard_summary():
    """
    Endpoint de agregados simples:
    - total de meetings
    - total de action items
    - total de action items 'open' vs 'closed'
    """
    from app.api.routers.meetings import DB as MEETINGS_DB
    from app.api.routers.action_items import ACTION_DB

    total_meetings = len(MEETINGS_DB)

    all_action_items = []
    for items in ACTION_DB.values():
        all_action_items.extend(items)

    total_action_items = len(all_action_items)
    open_items = sum(1 for a in all_action_items if a.get("status", "open") == "open")
    closed_items = sum(1 for a in all_action_items if a.get("status") == "closed")

    return {
        "total_meetings": total_meetings,
        "total_action_items": total_action_items,
        "open_action_items": open_items,
        "closed_action_items": closed_items,
    }
