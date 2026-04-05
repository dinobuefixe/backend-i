# tests/test_meetings.py
from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_health_ok() -> None:
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_create_meeting_ok() -> None:
    payload = {"title": "Planning", "date": "2026-03-10", "owner": "Jorge"}
    r = client.post("/meetings", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == payload["title"]
    assert body["owner"] == payload["owner"]


def test_create_meeting_missing_title() -> None:
    payload = {"date": "2026-03-10", "owner": "Jorge"}
    r = client.post("/meetings", json=payload)
    assert r.status_code == 422  # erro de validação


def test_create_meeting_invalid_date_format() -> None:
    payload = {"title": "Bad Date", "date": "not-a-date", "owner": "Jorge"}
    r = client.post("/meetings", json=payload)
    assert r.status_code == 422
