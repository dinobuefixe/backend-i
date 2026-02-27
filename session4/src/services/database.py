from data.models import Meeting
from uuid import uuid4


BASE_PATH = "src/data/meetings_files"

def create(meeting:Meeting):
    filename = f"{BASE_PATH}/{uuid4()}.md"
    with open(filename, "w") as file:
        file.writelines(str(meeting))