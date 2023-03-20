from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from os import system
import container_list

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

distab = Table(title="Supported Linux Distros:-")
distab.add_column("s.no")
distab.add_column("distro")
distab.add_row("i","[blue]Alpine Linux[/blue]")
distab.add_row("ii","[cyan]Arch Linux[/cyan]" )
distab.add_row("iii" , "[red]Debian Linux[/red]")
distab.add_row("iv", "[blue]Fedora Linux[/blue]")
distab.add_row("v","[green]OpenSuse Linux[/green]" )
distab.add_row("vi","[red]Ubuntu Linux[/red]" )

def enter():
    console.print("Showing all the containers you have:-")
    system("distrobox list")
    container = Prompt.ask("Enter the container you want to enter:-")
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

class ShowDistroContainers():
    def alpine():
        tabubu = Table(title="Supported Alpine Versions")
        tabubu.add_column("s.no:-")
        tabubu.add_column("versions:-")
        tabubu.add_row("i" , "[blue]3.15[/blue]")
        tabubu.add_row("ii" , "[blue]3.16[/blue]")
        tabubu.add_row("iii" , "[blue]latest[/blue]")
        console.print(Panel("These alpine versions are supported:-" and tabubu))

    def fedora():
        tabubu = Table(title="Supported Fedora Versions")
        tabubu.add_column("s.no:-")
        tabubu.add_column("versions:-")
        tabubu.add_row("i" , "[blue]36[/blue]")
        tabubu.add_row("ii" , "[blue]37[/blue]")
        tabubu.add_row("iii" , "[blue]38 Rawhide[/blue]")
        console.print(Panel(tabubu))

    def arch():
        tabar = Table(title="Supported Arch Versions")
        tabar.add_column("s.no:-")
        tabar.add_column("version:-")
        tabar.add_row("i" , "[cyan]latest[/cyan]")
        console.print(Panel(tabar))
        option = Prompt.ask("select version" , choices=["i"])
        if option == "i":
            create("archlinux:latest")

    def osuse():
        tabos = Table(title="Supported OpenSuse Versions")
        tabos.add_column("s.no:-")
        tabos.add_column("version:-")
        tabos.add_row("i" , "[green]leap(stable)[/green]")
        tabos.add_row("ii" , "[green]tumbleweed(rolling)[/green]")
        console.print(Panel(tabos))

    def ubuntu():
        tabubu = Table(title="Supported Ubuntu Versions")
        tabubu.add_column("s.no:-")
        tabubu.add_column("versions:-")
        tabubu.add_row("i" , "[red]14.04 trusty[/red]")
        tabubu.add_row("ii" , "[red]16.04 xenial[/red]")
        tabubu.add_row("iii" , "[red]18.04 bionic[/red]")
        tabubu.add_row("iv" , "[red]20.04 focal[/red]")
        tabubu.add_row("v" , "[red]22.04 jammy[/red]")
        console.print(Panel("These ubuntu versions are supported:-" and tabubu))


    def debian():
        tabubu = Table(title="Supported Debian Versions")
        tabubu.add_column("s.no:-")
        tabubu.add_column("versions:-")
        tabubu.add_row("i" , "[red]9 Stretch[/red]")
        tabubu.add_row("ii" , "[red]10 Buster[/red]")
        tabubu.add_row("iii" , "[red]11 Bullseye[/red]")
        tabubu.add_row("iv" , "[red]12 Bookworm(Testing)[/red]")
        tabubu.add_row("v" , "[red]Sid(rolling)[/red]")
        console.print(Panel(tabubu))

        
def list_containers():
    console.print(Panel(distab))
    prompt = Prompt.ask("Enter the distro's serial number in order to make the container", choices=["i" , "ii" , "iii" , "iv" , "v" , "vi"])
    if prompt == "vi":
        ShowDistroContainers.ubuntu()
    elif prompt == "i":
        ShowDistroContainers.alpine()
    elif prompt == "ii":
        ShowDistroContainers.arch()
    elif prompt == "iii":
        ShowDistroContainers.debian()
    elif prompt == "iv":
        ShowDistroContainers.fedora()
    elif prompt == "v":
        ShowDistroContainers.osuse()

def create(id: str):
    hname = Prompt.ask("[green]>[/green] Enter the name of your container?") 
    console.print("creating your container...")
    prcs = system(f"distrobox-create --name doxybox-{hname} --image {id}")
    if prcs != 0:
        console.print("[red]error:-[/red] creating container failed")
    else:
        pass

def view():
    console.print("here is the list of all of your distrobox containers:-")
    system("distrobox list")

def stop():
    view()
    cont = Prompt.ask("[green]>[/green] enter the container you want to stop")
    prcs = system(f"distrobox stop {cont}")
    if prcs != 0:
        console.print(f"[red]error:-[/red] [blue]{cont}[/blue] failed to stop")
    else:
        pass 

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
elif choice == str("v"):
    view()
elif choice == str("s"):
    stop()
elif choice == str("c"):
    list_containers()
