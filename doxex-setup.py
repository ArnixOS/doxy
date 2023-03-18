#!/usr/bin/python3
from colorama import Back , Fore
from os import system , chdir , mkdir
from os.path import isfile
from socket import gethostname
from shutil import move
from requests import get

def ensure_container(hostname: str):
    hostcheck = list(hostname)
    if hostcheck[0] == "d" and hostcheck[1] == "o" and hostcheck[2] == "x" and hostcheck[3] == "y" and hostcheck[4] == "b" and hostcheck[5] == "o" and hostcheck[6] == "x":
        return f"{Fore.GREEN}yes{Fore.RESET}"
    else:
        return f"{Fore.RED}no{Fore.RESET}" 
    
def package_manager():
    if isfile("/usr/bin/pacman") == True:
        return f"{Fore.CYAN}/usr/bin/pacman{Fore.RESET}"
    elif isfile("/usr/bin/zypper") == True:
        return f"{Fore.CYAN}/usr/bin/zypper{Fore.RESET}"
    elif isfile("/usr/bin/apt") == True:
        return f"{Fore.CYAN}/usr/bin/apt{Fore.RESET}"
    elif isfile("/usr/bin/dnf") == True:
        return f"{Fore.CYAN}/usr/bin/dnf{Fore.RESET}"
    elif isfile("/usr/bin/xbps") == True:
        return f"{Fore.CYAN}/usr/bin/xbps{Fore.RESET}"
    else:
        return f"{Fore.RED}unsupported package manger{Fore.RESET}"

print(f"{Fore.LIGHTYELLOW_EX}[i]{Fore.YELLOW} checking system...{Fore.RESET}")
ensure_cont = ensure_container(gethostname())

print(f"Checking that this box is running under doxy: {ensure_cont}")
if "no" in ensure_cont:
    exit(1)
else:
    pass

print(f"Checking package manager:- {package_manager()}")
print(f"{Fore.LIGHTYELLOW_EX}[ii]{Fore.YELLOW} installing dependencies...{Fore.RESET}")
pm = package_manager()
if pm == f"{Fore.CYAN}/usr/bin/pacman":
    prcs = system(f"sudo pacman -Sy python-rich python-requests")
    if prcs != 0:
        print(f"Installation of dependencies:- {Fore.RED}failed{Fore.RESET}")
        exit(1)
    else:
        print(f"Installation of dependencies:- {Fore.GREEN}passed{Fore.RESET}")
        pass
elif pm == f"{Fore.CYAN}/usr/bin/apt{Fore.RESET}":
    prcs = system(f"sudo apt install python3-rich python3-requests git")
    if prcs != 0:
        print(f"Installation of dependencies:- {Fore.RED}failed{Fore.RESET}")
        exit(1)
    else:
        print(f"Installation of dependencies:- {Fore.GREEN}passed{Fore.RESET}")
        pass
print(f"{Fore.LIGHTYELLOW_EX}[iii]{Fore.YELLOW} installing doxex...{Fore.RESET}")
print(f"cloning the git repo")
p = system("git clone https://github.com/ArnixOS/doxy")
if p != 0 :
    print(f"{Fore.RED}git clone failed")
    exit(1)
else:
    chdir("doxy")
    mkdir("~/.local/doxex")
    move("doxex.py" , "~/.local/share/doxex")
    chdir("~/.local/share/doxex")
    system("ln -sf doxex.py ../bin/doxex")
