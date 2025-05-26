from fernet import Fernet

# Clé de cryptage (à remplacer par la vôtre)
key = b"votre_cle_de_cryptage_ici"

# Fonction pour crypter des données
def crypter(data):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Fonction pour décrypter des données
def decrypter(data):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()

# Exemple d'utilisation
data = "Ceci est un message à crypter"
data_cryptee = crypter(data)
print(f"Données cryptées : {data_cryptee}")

data_decryptee = decrypter(data_cryptee)
print(f"Données décryptées : {data_decryptee}")
