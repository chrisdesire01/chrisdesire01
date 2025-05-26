from scapy.all import IP, TCP, sr1
import pyfiglet
from colorama import Fore, Style, init
import requests
# Initialisation de Colorama
init()

def afficher_banniere():
    ascii_art = pyfiglet.figlet_format("CTECH-IT")
    print(Fore.GREEN + ascii_art + Style.RESET_ALL)
    print(Fore.GREEN + "=" * 40)
    print("VULNERABILITY SCAN ")
    print("=" * 40 + "\n" + Style.RESET_ALL)

def scanner_ports(cible, ports):
    print(Fore.GREEN + f" Scan des ports sur {cible}...\n" + Style.RESET_ALL)

    for port in ports:
        paquet = IP(dst=cible)/TCP(dport=port, flags="S")
        reponse = sr1(paquet, timeout=1, verbose=False)

        if reponse and reponse.haslayer(TCP) and reponse[TCP].flags == 0x12:
            print(Fore.GREEN + f" Port {port} ouvert" + Style.RESET_ALL)
        else:
            print(Fore.RED + f" Port {port} fermé ou filtré" + Style.RESET_ALL)

def detecter_os(cible):
    print(Fore.GREEN + f" Détection du système d'exploitation de {cible}...\n" + Style.RESET_ALL)
    
    paquet = IP(dst=cible)/TCP(dport=80, flags="S")
    reponse = sr1(paquet, timeout=1, verbose=False)

    if reponse and reponse.haslayer(TCP):
        ttl = reponse[IP].ttl
        if ttl <= 64:
            print(Fore.GREEN + " Système probable : Linux/Unix" + Style.RESET_ALL)
        elif ttl <= 128:
            print(Fore.GREEN + " Système probable : Windows " + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + " Système inconnu" + Style.RESET_ALL)

def rechercher_vulnerabilites(service):
    print(Fore.GREEN + f" Recherche de vulnérabilités pour {service}...\n" + Style.RESET_ALL)
    url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={service}"
    
    try:
        response = requests.get(url)
        data = response.json()
        for vuln in data.get("result", {}).get("CVE_Items", [])[:5]:
            print(Fore.RED + f" {vuln['cve']['CVE_data_meta']['ID']} - {vuln['cve']['description']['description_data'][0]['value']}" + Style.RESET_ALL)
    except:
        print(Fore.YELLOW + " aucune vulnerabilite detecter" + Style.RESET_ALL)

if __name__ == "__main__":
    afficher_banniere()
    cible = input(Fore.GREEN + " Entrez l'IP ou domaine à scanner : " + Style.RESET_ALL)
    ports_input = input(Fore.GREEN + " Entrez les ports à scanner (ex: 22,80,443) : " + Style.RESET_ALL)
    ports = [int(p) for p in ports_input.split(",")]

    scanner_ports(cible, ports)
    detecter_os(cible)

    service = input(Fore.GREEN + " Entrez un service à vérifier (ex: Apache, OpenSSH) : " + Style.RESET_ALL)
    rechercher_vulnerabilites(service)

