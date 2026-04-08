from maths.operations import addition, soustraction, multiplication
from maths.statistiques import moyenne, maximum, minimum
from utils.string_utils import inverser_chaine, compter_mots
import requests

# Maths
print("Addition:", addition(5, 3))
print("Soustraction:", soustraction(10, 4))
print("Multiplication:", multiplication(6, 7))

# Statistiques
liste = [10, 20, 30, 40, 50]
print("Moyenne:", moyenne(liste))
print("Max:", maximum(liste))
print("Min:", minimum(liste))

# String
texte = "Bonjour tout le monde"
print("Inverse:", inverser_chaine(texte))
print("Nombre de mots:", compter_mots(texte))



def tester_requete(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Requête réussie !")
            print(response.text[:300])
        else:
            print("Erreur HTTP :", response.status_code)
    except Exception as e:
        print("Erreur :", e)

tester_requete("https://example.com")