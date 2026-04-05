# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.api.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def sample_meeting(client):
    payload = {"title": "Demo", "date": "2026-01-01", "owner": "Alice"}
    r = client.post("/meetings", json=payload)
    assert r.status_code == 201
    return r.json()


@pytest.fixture
def sample_action_item(client, sample_meeting):
    meeting_id = sample_meeting["id"]
    payload = {
        "description": "Prepare slides",
        "owner": "Alice",
        "due_date": "2026-02-01",
    }
    r = client.post(f"/meetings/{meeting_id}/action-items", json=payload)
    assert r.status_code == 201
    return r.json()
