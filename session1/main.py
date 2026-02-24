import typer
from datetime import datetime

def invalid():
    typer.echo("Data inválida!")

def create_meeting():
    month = typer.prompt("Insere o mês da reunião", type=int)
    if month < 1 or month > 12:
        invalid()
        raise typer.Exit()

    day = typer.prompt("Insere o dia da reunião", type=int)
    if day < 1 or day > 31:
        invalid()
        raise typer.Exit()

    year = datetime.now().year

    date_str = f"{year}/{month}/{day}"
    date_styled = typer.style(date_str, fg=typer.colors.BLUE, bold=True)

    owner = typer.prompt("Qual é o teu nome?")
    owner_styled = typer.style(owner, fg=typer.colors.GREEN)

    title = typer.prompt("Qual é o título da reunião?")
    title_styled = typer.style(title, fg=typer.colors.GREEN)

    typer.echo(f"Meeting: {title_styled}")
    typer.echo(f"Owner: {owner_styled}")
    typer.echo(f"Date: {date_styled}")


if __name__ == "__main__":
    typer.run(create_meeting)
