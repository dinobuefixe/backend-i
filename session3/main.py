from typer import Typer, echo, style, colors
from datetime import datetime

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
def create_meeting(meeting: Meeting):
    echo(style(f"""
    =========================
    {meeting.title}
    =========================           
    created by {meeting.owner} on {meeting.date}
    """,fg=colors.BRIGHT_CYAN, bold=True))



if __name__ == "__main__":
    cli()