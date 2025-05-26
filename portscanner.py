# -*-coding:Latin-1 -*
python

import socket
import subprocess
import sys
from datetime import datetime
import errno
subprocess.call('clear',shell=True) #nettoyer le terminal.
remote_server= raw_input('enter the domain name : ')
remote_server_IP=socket.gethostbyname(remote_server)
print ('IPv4 : ',remote_server_IP)
#afficher l'adresse IPv4 de la cible.
print ("-"*60)
print ('please wait while scanning',remote_server_IP)
print ("-"*60)
t1=datetime.now()
try :
for port in range (79,85) :
connexion=
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
resultat=connexion.connect_ex((remote_server_IP,port))
if resultat == 0 : # si aucune erreur n'est rencontrée
print ('Port {}: open'.format(port)
else :
print ('port {}: closed'.format(port)
connexion.close()
# clore la connexion
except KeyboardInterrupt :
print ('you pressed Ctrl+C !!')
sys.exit()
# arreter l'exécution du script
except :
print ('something wrong !!!')
sys.exit()
#
t2=datetime.now()
Ttotal=t2-t1
print ('-'*60)
print ('scan done in ',Ttotal,'second') # afficher le temps total du scan 
