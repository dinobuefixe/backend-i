# app/api/routers/action_items.py
from fastapi import APIRouter, Query, HTTPException, status
from app.api.schemas import ActionItemCreate, ActionItemRead

router = APIRouter(prefix="/meetings", tags=["action-items"])

# meeting_id -> lista de action items
ACTION_DB: dict[str, list[dict]] = {}


@router.post("/{meeting_id}/action-items", status_code=status.HTTP_201_CREATED,
             response_model=ActionItemRead)
def create_action_item(meeting_id: str, payload: ActionItemCreate):
    items = ACTION_DB.get(meeting_id, [])
    new_id = str(len(items) + 1)

    item = {
        "id": new_id,
        "meeting_id": meeting_id,
        **payload.model_dump(),
    }
    ACTION_DB.setdefault(meeting_id, []).append(item)
    return item


@router.get("/{meeting_id}/action-items", response_model=dict)
def list_action_items(
    meeting_id: str,
    owner: str | None = None,  # exercício: filtro por owner
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    items = ACTION_DB.get(meeting_id, [])

    if owner:
        items = [a for a in items if a["owner"] == owner]

    # ordenação estável por due_date + id (desafio)
    items = sorted(items, key=lambda x: (x["due_date"], x["id"]))

    total = len(items)
    paginated = items[offset : offset + limit]

    return {"total": total, "items": paginated}
