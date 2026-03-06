from fastapi import FastAPI
from .models import MeetingResponse, Meeting, MeetingRequest
from datetime import datetime

api = FastAPI()

@api.get("/",response_model=list[Meeting])
def list_meetings(title:str="", owner:str="", date:datetime | None = None) -> list[Meeting]:
    return []

@api.post("/", response_model=MeetingResponse)
def create_meeting(meeting:MeetingRequest):
    ...

@api.get("/{meeting_id}", response_model=Meeting)
def get_meeting(meeting_id:str):
    ...