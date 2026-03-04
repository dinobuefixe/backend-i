import typer
from logic import create, choose_album, list_albums

cli = typer.Typer()

@cli.command()
def create_album():
    artist = typer.prompt("Insere o nome do artista", type=str)
    album = typer.prompt("Insere o nome do album", type=str)    
    
    create(artist=artist, album=album)


@cli.command()
def choose() : 
    choose_album()

@cli.command()
def list():
    list_albums()

option=0
while (option!=4):
    print("1 - Adicionar um álbum")
    print("2 - Escolher um álbum aleatório")
    print("3 - Listar os álbuns disponíveis")
    print("4 - Sair")

    option = int(input("Escolha uma opção: "))

    if option == 1:
        create_album()
    elif option == 2:
        choose()
    elif option == 3:
        list()
    elif option == 4:
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    cli()