import socket
import requests
import whois
from scapy.all import IP, TCP, sr1
import pyfiglet
from colorama import Fore, Style, init

# Initialisation de Colorama
init()

def afficher_banniere():
    ascii_art = pyfiglet.figlet_format("CTECH-IT")
    print(Fore.GREEN + ascii_art + Style.RESET_ALL)
    print(Fore.GREEN + "=" * 40)
    print("🔥 Scanner de Vulnérabilités 🔥")
    print("=" * 40 + "\n" + Style.RESET_ALL)

def detecter_serveur(nom_domaine):
    try:
        ip_serveur = socket.gethostbyname(nom_domaine)
        print(Fore.GREEN + f"🌐 IP du serveur : {ip_serveur}" + Style.RESET_ALL)
        
        url = f"http://{nom_domaine}"
        response = requests.get(url, timeout=300)
        serveur = response.headers.get("Server", "Inconnu")
        print(Fore.GREEN + f"🖥️ Serveur Web : {serveur}" + Style.RESET_ALL)
        
        return ip_serveur
    except Exception as e:
        print(Fore.RED + f"❌ Erreur lors de la détection : {e}" + Style.RESET_ALL)
        return None

def detecter_os(ip_serveur):
    print(Fore.GREEN + f"🖥️ Détection du système d'exploitation de {ip_serveur}...\n" + Style.RESET_ALL)
    
    paquet = IP(dst=ip_serveur)/TCP(dport=80, flags="S")
    reponse = sr1(paquet, timeout=1, verbose=False)

    if reponse and reponse.haslayer(TCP):
        ttl = reponse[IP].ttl
        if ttl <= 64:
            print(Fore.GREEN + "🟢 Système probable : **Linux/Unix**" + Style.RESET_ALL)
        elif ttl <= 128:
            print(Fore.GREEN + "🟢 Système probable : **Windows**" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "⚠️ Système inconnu" + Style.RESET_ALL)

def rechercher_vulnerabilites(service):
    print(Fore.GREEN + f"🔎 Recherche de vulnérabilités pour **{service}**...\n" + Style.RESET_ALL)
    url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={service}"
    
    try:
        response = requests.get(url)
        data = response.json()
        for vuln in data.get("result", {}).get("CVE_Items", [])[:5]:
            print(Fore.RED + f"⚠️ {vuln['cve']['CVE_data_meta']['ID']} - {vuln['cve']['description']['description_data'][0]['value']}" + Style.RESET_ALL)
    except:
        print(Fore.YELLOW + "⚠️ Impossible de récupérer les vulnérabilités actuellement." + Style.RESET_ALL)

def trouver_localisation(ip_serveur):
    print(Fore.GREEN + f"🌍 Localisation du serveur ({ip_serveur})...\n" + Style.RESET_ALL)
    
    try:
        info = whois.whois(ip_serveur)
        pays = info.get("country", "Inconnu")
        ville = info.get("city", "Inconnue")
        print(Fore.GREEN + f"🌍 Pays : {pays}, Ville : {ville}" + Style.RESET_ALL)
    except Exception:
        print(Fore.YELLOW + "⚠️ Impossible de récupérer la localisation." + Style.RESET_ALL)

if __name__ == "__main__":
    afficher_banniere()
    nom_domaine = input(Fore.GREEN + "🔍 Entrez le nom de domaine à scanner : " + Style.RESET_ALL)
    ip_serveur = detecter_serveur(nom_domaine)

    if ip_serveur:
        detecter_os(ip_serveur)
        trouver_localisation(ip_serveur)

        service = input(Fore.GREEN + "🔎 Entrez un service à vérifier (ex: Apache, OpenSSH) : " + Style.RESET_ALL)
        rechercher_vulnerabilites(service)

