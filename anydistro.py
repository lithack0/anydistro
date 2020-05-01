import requests
import os
from pprint import pprint
from termcolor import cprint
from pyfiglet import figlet_format
cprint(figlet_format("\t    ANYDISTRO"),"yellow",attrs=["bold"])
cprint("\tWhich distribution you want to download ","yellow",attrs=["bold"])
print("\033[33;1m")
print("[1].Ubuntu       [2].Kali     [3].Frdora")
print("[4].KaliNet       [5].Debian     [6].Alpine")
print("[7].BackBox       [8].CentOs     ")
c=input("Enter Your choice: ")
if c=="1":
	print("\033[33;1m")
	o=os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
	print("\033[33;1m[*]To start type [./start-ubuntu.sh]")
elif c=="2":
	print("\033[33;1m")
	o=os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
	print("\033[33;1m[*]To start type [./start-kali.sh]")
elif c=="3":
	print("\033[33;1m")
	o=os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
	print("\033[33;1m[*]To start type [./start-fedora.sh]")
elif c=="4":
	print("\033[33;1m")
	o=os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
	print("\033[33;1m[*]To start type [./start-nethunter.sh]")
elif c=="5":
	print("\033[33;1m")
	o=os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
	print("\033[33;1m[*]To start type [./start-debian.sh]")
elif c=="6":
	print("\033[33;1m")
	o=os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")
	print("\033[33;1m[*]To start type [./start-alpine.sh]")
elif c=="7":
	print("\033[33;1m")
	o=os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
	print("\033[33;1m[*]To start type [./start-backbox.sh]")
elif c=="8":
	print("\033[33;1m")
	o=os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
	print("\033[33;1m[*]To start type [./start-centos.sh]")
