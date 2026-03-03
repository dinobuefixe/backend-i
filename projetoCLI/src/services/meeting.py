from data.models import Meeting
from services import database

def create(title : str,owner : str,date : str):
    if not title:
        raise ValueError("Title is Empty")

    new_meeting = Meeting(
        title=title,
        owner=owner,
        date=date
    )
    database.create(meeting=new_meeting)

def list():
    ...