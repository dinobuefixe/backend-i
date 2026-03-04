from pathlib import Path
import json
from uuid import uuid4

path = Path("albums_database/index.json")

def insert(album):
    # Criar ficheiro se não existir
    if not path.exists():
        path.write_text("[]")
    else:
        try:
            json.loads(path.read_text())
        except:
            path.write_text("[]")

    
    # Ler conteúdo atual
    with open(path, "r") as file:
        index_content: list = json.loads(file.read())

    # Adicionar novo item
    index_content.append({
        "id": str(uuid4()),
        "artist": album.artist,
        "album": album.album
    })

    # Gravar lista atualizada
    with open(path, "w") as file:
        json.dump(index_content, file, indent=4)

def remove(album_escolhido):
    with open(path, "r") as file:
        index_content: list = json.loads(file.read())

    index_content.remove(album_escolhido)

    with open(path, "w") as file:
        json.dump(index_content, file, indent=4)