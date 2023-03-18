from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from os import system

heading1 = Panel('''
[red]██████[/red]   [yellow]██████[/yellow]   [green]██  ██[/green]   [blue]██  ██[/blue]
[red]██   ██[/red]  [yellow]██  ██[/yellow]     [green]██[/green]      [blue]████[/blue]
[red]██████[/red]   [yellow]██████[/yellow]   [green]██  ██[/green]     [blue]██[/blue]

A simple script to manage your distrobox containers

[bold]Select an operation[/bold]:-
[[magenta bold]e[/magenta bold]] enter into a container
[[cyan bold]c[/cyan bold]] create a new container
[[blue bold]r[/blue bold]] remove a container
[[green bold]v[/green bold]] view containers
[[yellow bold]s[/yellow bold]] stop a container
[[red bold]x[/red bold]] exit doxy'''
)
                 
heading2 = '''
[bold]Select an operation:-[/bold]
[[magenta bold]e[/magenta bold]] enter into a container
[[cyan bold]c[/cyan bold]] create a new container
[[blue bold]r[/blue bold]] remove a container
[[yellow bold]v[/yellow bold]] view containers
[[green bold]s[/yellow bold]] stop a container
[[red bold]x[/red bold]] exit doxy
'''

def enter():
    console.print("Showing all the containers you have:-")
    system("distrobox list")
    container = Prompt.ask("Enter the container you want to start:-")
    console.print(f"[yellow bold]NOTE:-[/yellow bold] In order to exit [blue]{container}[/blue] type [red bold]exit[/red bold]")
    console.print(f"Staring [blue]{container}[/blue]...")
    p1 = system(f"distrobox enter {container}")
    if p1 != 0:
        console.print(f"[red]error:- [/red] [blue]{container}[/blue] not started")
        exit(p1)
    else:
        pass

def remove():
    console.print("Showing all the containers you have:-")
    system("distrobox list")
    container = Prompt.ask("Enter the container you want to delete")
    yn = Prompt.ask("[yellow bold]NOTE:-[/yellow bold] Deleting this container can remove the apps installed on the container\nAre you sure you want to delete?" , choices=["y" , "n"])
    if yn == "y":
        console.print(f"Stopping [blue]{container}[/blue]")
        p1 = system(f"distrobox stop {container}")
        if p1 != 0:
            console.print(f"Please close the container in order to stop it")
            exit(p1)
        else:
            pass

        console.print(f"Deleting [blue]{container}[/blue]..")
        system(f"distrobox rm {container}")
    else:
        console.print(f"[red]error:-[/red] container [blue]{container}[/blue] not deleted")

#ef stop():
    

console = Console()
console.print(heading1)

choice = str(Prompt.ask("Select your choice" , choices=["e","c","r","v","s","x"]))
if choice == str("x"):
    console.print("[red]doxy exited with exit code[/red] 0")
    exit(0)
elif choice == str("r"):
    remove()
elif choice == str("e"):
    enter()
