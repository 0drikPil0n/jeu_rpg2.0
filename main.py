import time
import random


# Création du personnage
def verifier_nom(p_prenom: str, p_nom: str) -> str:
    """
    Vérifie si le nom et le prénom sont correcte et retourne le nom complet
    :param p_prenom: Le prénom
    :param p_nom: Le nom de famille
    :return: Le nom complet
    """
    while not p_prenom.isalpha():
        p_prenom = input("Entrer un prénom correcte: ").capitalize().strip()
    while not p_nom.isalpha():
        p_nom = input("Entrer un nom de famille correcte: ").capitalize().strip()
    p_nom_complet = p_prenom + " " + p_nom

    return p_nom_complet


races: list[dict] = [{"Race": "Humain", "Âge_permis": [18, 120]},
                     {"Race": "Ogre", "Âge_permis": [18, 150]},
                     {"Race": "Nain", "Âge_permis": [15, 200]},
                     {"Race": "Elfe", "Âge_permis": [16, 500]}
                     ]


def verifier_race(numero: int) -> dict:
    """
    Vérifie si le numéro choisis correspond à une race
    :param numero: Le numéro de race choisis
    :return: La race choisis
    """
    while True:
        if numero not in range(1, len(races) + 1):
            print(f"\nEntrer un numero de 1 à {len(races)}\n")
            time.sleep(1)
            for p_position, p_race in enumerate(races):
                print(f"{p_position + 1} - {p_race['Race']}")
            numero: int = int(input("Veuillez choisir une race par son numéro: ").strip())
        else:
            break
    race_choisi = races[numero - 1]

    return race_choisi


genres: list = ["Homme","Femme","Autre"]


def verifier_genre(p_genre: str) -> str:
    """
    Vérifie si le genre choisis est correcte
    :param p_genre: Le genre choisis
    :return: Le genre choisis
    """
    while True:
        if p_genre not in genres:
            print("\nEntrer un genre correcte")
            time.sleep(1)
            p_genre = input("\nQuel est votre genre? (Homme/Femme/Autre): ").capitalize().strip()
        else:
            break
    return p_genre


classes:list = ["Royauté","Villageois","Magicien","Armée"]


if __name__ == '__main__':
    # Choix du nom du personnage
    prenom: str = input("Veuillez entrer le prénom de votre personnage: ").capitalize().strip()
    nom: str = input("Veuillez choisir votre nom de famille: ").capitalize().strip()
    nom_complet = verifier_nom(prenom, nom)

    # Choix de la race du personnage
    print(f"\nVoici les races disponibles:")
    for position, race in enumerate(races):
        print(f"{position + 1} - {race['Race']}")
    num_race_choisi: int = int(input("Veuillez choisir une race par son numéro: ").strip())
    race = verifier_race(num_race_choisi)

    # Choix du genre du personnage
    genre: str = input("\nQuel est votre genre? (Homme/Femme/Autre): ").capitalize().strip()
    genre = verifier_genre(genre)
    print(f"\nVoici les races disponibles:")

    # Choix de la classe du personnage


