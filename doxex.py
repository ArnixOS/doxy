from rich.console import Console
from rich.panel import Panel
from os import system
from os.path import isfile

heading = Panel('''
[red]██████[/red]   [yellow]██████[/yellow]   [green]██  ██[/green]   [blue]██████[/blue]    [magenta]██  ██[/magenta]
[red]██   ██[/red]  [yellow]██  ██[/yellow]     [green]██[/green]     [blue]████[/blue]        [magenta]██[/magenta]
[red]██████[/red]   [yellow]██████[/yellow]   [green]██  ██[/green]   [blue]██████[/blue]    [magenta]██  ██[/magenta]

A simple script to export to manage exports from your distrobox container

[bold]Select an operation:-[/bold]
[[green bold]e[/green bold]] export application/binary
[[yellow bold]r[/yellow bold]] remove the exported stuff
[[red bold]x[/red bold]] exit doxex''')

console = Console()
console.print(heading)
