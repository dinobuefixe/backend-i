from data import insert,remove
from dataclasses import dataclass
import random 
from pathlib import Path
import json
import typer

path = Path("albums_database/index.json")

@dataclass
class class_album:
    artist: str
    album: str

    def __str__(self):
        return f"""---
artist: {self.artist}
album: {self.album}
---
# Album
"""
    
def create(artist : str,album : str):
    if not artist:
        raise ValueError("Campo do Artista está vazio")
    if not album:
        raise ValueError("Campo do Álbum está vazio")

    album = class_album(artist=artist, album=album)
    insert(album)


def choose_album():
    if not path.exists():
        raise ValueError("Não existe nenhum album")
    else:
        try:
            json.loads(path.read_text())
        except:
            raise ValueError("Não existe nenhum album")

    with open(path, "r") as file:
        index_content: list = json.loads(file.read())

    if not index_content: 
        raise ValueError("Não existem álbuns na base de dados.") 
    
    album_escolhido = random.choice(index_content) 
    artist = typer.style(album_escolhido.get('artist'), fg=typer.colors.BLUE, bold=True)
    album_name = typer.style(album_escolhido.get('album'), fg=typer.colors.GREEN, bold=True)
    print(f"- {album_name} de {artist}")
    remove(album_escolhido)

def list_albums():
    if not path.exists():
        raise ValueError("Não existe nenhum album")
    else:
        try:
            json.loads(path.read_text())
        except:
            raise ValueError("Não existe nenhum album")

    with open(path, "r") as file:
        index_content: list = json.loads(file.read())

    if not index_content:
        raise ValueError("Não existem álbuns na base de dados.")

    for album in index_content:
        artist = typer.style(album.get('artist'), fg=typer.colors.BLUE, bold=True)
        album_name = typer.style(album.get('album'), fg=typer.colors.GREEN, bold=True)
        print(f"- {album_name} de {artist}")