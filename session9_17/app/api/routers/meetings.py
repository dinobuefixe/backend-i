# app/api/routers/meetings.py
from fastapi import APIRouter, Query, HTTPException, status
from app.api.schemas import MeetingCreate, MeetingRead

router = APIRouter(prefix="/meetings", tags=["meetings"])

# DB em memória: id -> meeting
DB: dict[str, dict] = {}


@router.post("", status_code=status.HTTP_201_CREATED, response_model=MeetingRead)
def create_meeting(payload: MeetingCreate):
    new_id = str(len(DB) + 1)
    item = {"id": new_id, **payload.model_dump()}
    DB[new_id] = item
    return item


@router.get("", response_model=dict)
def list_meetings(
    owner: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    items = list(DB.values())

    # filtro por owner (Session 12)
    if owner:
        items = [m for m in items if m["owner"] == owner]

    # ordenação estável por data (Session 12 – stable ordering)
    items = sorted(items, key=lambda x: x["date"])

    # paginação
    total = len(items)
    paginated = items[offset : offset + limit]

    return {"total": total, "items": paginated}
