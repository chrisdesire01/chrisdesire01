>>> # -*- coding: utf-8 -*
>>> import socket
>>>  #port d'ecoute
>>> PORT = 8080
>>>  #creation de socket
>>> server = socket.socket()
>>> print("[*]socket cree...")
[*]socket cree...
>>> # bind avec le PORT
>>> #sert a binder le socker sur une adresse et un port.
>>> # quand un client n'appelle pas bind, c'est le system qui choisira l'adresse et le port a utiliser.
>>> server.bind((", PORT))
  File "<stdin>", line 1
    server.bind((", PORT))
                 ^
SyntaxError: unterminated string literal (detected at line 1)
>>>
>>> server.bind(('', PORT))
>>> print('[*]bind avec le port %s'%(PORT))
[*]bind avec le port 8080
>>>
>>>
>>>
>>> #Ecoute de connexion iverse
>>> server.listen(5)
>>> print('[*]socket listeing....')
[*]socket listeing....
>>> # creation de loop en attente de connexion.
>>> while True:
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after 'while' statement on line 1
>>> while True:
... c, addresse = server.accept()
  File "<stdin>", line 2
    c, addresse = server.accept()
    ^
IndentationError: expected an indented block after 'while' statement on line 1
>>> c, addresse = server.accept()
