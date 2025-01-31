import time
import random

# Création du personnage
def verifier_nom(p_prenom:str, p_nom:str) -> str:
    """
    Vérifie si le nom et le prénom sont correcte et retourne le nom complet
    :param p_prenom: Le prénom
    :param p_nom: Le nom de famille
    :return: Le nom complet
    """
    while not p_prenom.isalpha():
        p_prenom = input("Entrer un prénom correcte: ").capitalize()
    while not p_nom.isalpha():
        p_nom = input("Entrer un nom de famille correcte: ").capitalize()
    p_nom_complet = p_prenom + " " + p_nom

    return p_nom_complet

races: list[dict] = [{"Race": "Humain",
                      "Âge_permis": [18,120]},
                     {"Race": "Ogre",
                      "Âge_permis": [18, 150]},
                     {"Race": "Nain",
                      "Âge": [15, 200]},
                     {"Race": "Elfe",
                      "Âge": [16, 500]}
                     ]
def verifier_race(numero:int) -> str:
    liste_nom_race: list = []
    for nom_race in races:
        liste_nom_race.append(nom_race)
    race_choisi = liste_nom_race[numero] in len(liste_nom_race)
    if not race_choisi:
        numero = input("Veuillez choisir une race valide: ")
    return liste_nom_race[numero]





if __name__ == '__main__':
    # Choix du nom du personnage
    prenom: str = input("Veuillez entrer le prénom de votre personnage: ").capitalize()
    nom: str = input("Veuillez choisir votre nom de famille: ").capitalize()
    nom_complet = verifier_nom(prenom, nom)
    # Choix de la race du personnage
    print(f"Voici les races disponibles:")
    for position, race in enumerate(races):
        print(f"{position + 1} - {race}")
    num_race_choisi: int = int(input("Veuillez choisir une race par son numéro: "))
    verifier_race(num_race_choisi)







