#!/usr/bin/python3
from colorama import Back , Fore
from os import system 
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
    pacman = "/usr/bin/pacman"
    zypper = "/usr/bin/zypper"
    apt = "/usr/bin/apt"
    dnf = "/usr/bin/dnf"
    yum = "/usr/bin/yum"
    apk = "/usr/bin/apk"
    xbps = "/usr/bin/xbps"

print(f"{Fore.YELLOW}[i] checking system...{Fore.RESET}")
ensure_cont = ensure_container(gethostname())

print("Checking that this box is running under doxy:" , ensure_cont)
if "no" in ensure_cont == True:
    exit(1)
else:
    pass

print("Checking package manager:- ")
