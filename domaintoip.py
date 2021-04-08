import os
import time
from colorama import Fore, Back, Style
from socket import gethostbyname
from pyfiglet import figlet_format

merah = Fore.RED
cyan = Fore.CYAN
biru = Fore.BLUE
ijo = Fore.GREEN
kuning = Fore.YELLOW

def bersih_layar():
	   linux = "clear"
	   windows = "cls"
	   os.system([linux,windows][os.name == "nt"])
bersih_layar()
time.sleep(2.50)
title = figlet_format("DomainToIP")
print(title)
print(cyan+"[+] Author : Wan5550")
print(Style.RESET_ALL)
print(kuning+"[+] Github : github.com/wannazid")
print(Style.RESET_ALL)
def main():
           input_list2 = input(ijo+"[+] List Site (site.txt) > ")
           print(Style.RESET_ALL)
           buka_list2 = open(input_list2,"r").read().splitlines()
           input_save = input(ijo+"[+] Save Name File (1.txt) > ")
           print(Style.RESET_ALL)
           print(ijo+"[!] Procces For > "+input_save)
           time.sleep(3)
           print(Style.RESET_ALL)
           try:
               for site in buka_list2:
                     ke_ip = gethostbyname(site)
                     print(merah+"=> "+site+" : "+ke_ip)
                     savefile = open(input_save, 'a').write(ke_ip+"\n")
           except:
           	print(ijo+"=> "+site+" : Error-Dont Use HTTP:// And HTTPS://")
main()
print(Style.RESET_ALL)
print("[!] File Berhasil Disimpan")

