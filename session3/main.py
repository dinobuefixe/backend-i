from typer import Typer, echo, style, colors
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Meeting:
    title : str
    owner : str
    date : str

cli = Typer()

@cli.command()
def greetings(name: str = "X"):
    echo(style(f"Greetings", fg=colors.BLUE))

@cli.command()
def goodbye():
    echo(style("Goodbye", fg=colors.RED))


@cli.command()
def create_meeting(
    title: str,
    date: str,
    owner: str
):
    
    meeting= Meeting(
        title=title,
        date=date,
        owner=owner
    )

    echo(style(f"""
    =========================
    {title}
    =========================           
    created by {owner} on {date}
    """,fg=colors.BRIGHT_CYAN, bold=True))



if __name__ == "__main__":
    cli()