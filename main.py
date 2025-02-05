import time
import random
from textwrap import dedent

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


def verifier_age(p_age:int, p_race:dict) -> int:
    """
    Vérifie si l'âge est dans la limite d'âge
    :param p_age: L'âge entrée
    :param p_race: la race choisis
    :return: L'âge choisis
    """
    range_age = p_race["Âge_permis"]
    while True:
        if p_age not in range(range_age[0], range_age[1] + 1):
            if p_age < range_age[0]:
                print(f"\nCet âge est trop petit\n"
                      f"La tranche d'âge permise pour cette race est de {range_age[0]} à {range_age[1]}")
                time.sleep(1)
                p_age = int(input("\nIndiquer votre âge: ").strip())
            elif p_age > range_age[1]:
                print(f"\nCet âge est trop grand\n"
                      f"La tranche d'âge permise pour cette race est de {range_age[0]} à {range_age[1]}")
                time.sleep(1)
                p_age = int(input("\nIndiquer votre âge: ").strip())
        else:
            break
    age_choisis = p_age

    return age_choisis


# Création de la classe
classes:list = ["Royauté","Villageois","Magicien","Armée"]


def verifier_classe(numero: int, p_classes) -> str:
    """
    Vérifie si la classe choisis est correcte
    :param numero: Le numéro de la classe choisis
    :param p_classes: La liste de classes
    :return: La classe choisis
    """
    while True:
        if numero not in range(1, len(p_classes) + 1):
            print("\nVeuillez choisir un numéro de classe correcte")
            time.sleep(1)
            print("\n")
            for p_position, p_classe in enumerate(p_classes):
                print(f"{p_position + 1} - {p_classe}")
            numero: int = int(input("Veuillez choisir votre classe: ").strip())
        else:
            break
    classe_choisi = p_classes[numero - 1]

    return classe_choisi


list_sous_classes:dict[str, list[str]] = {"Royauté": ["Prince","Princesse","Roi","Reine"],
                                     "Villageois": ["Fermier","Forgeron","Boucher","Pêcheur"],
                                     "Magicien": ["Mage","Sorcier","Alchimiste","Shaman"],
                                     "Armée": ["Archer","Cavalier","Infanterie","Mercenaire"]}


Stats_role = {
        "Prince":{    "Arme": "Poignard",           "PV": 200,  "Dégats": [20,15],         "Att.Spé.": [60,40]},
        "Princesse":{ "Arme": "Dague",              "PV": 175,  "Dégats": [30,10],         "Att.Spé.": [50]},
        "Roi":{       "Arme": "Épée",               "PV": 250,  "Dégats": [50,40,20,20],   "Att.Spé.": [75]},
        "Reine":{     "Arme": "Épée",               "PV": 225,  "Dégats": [60,30,30,10],   "Att.Spé.": [70]},
        "Fermier":{   "Arme": "Houe",               "PV": 100,  "Dégats": [10,8,8,5],      "Att.Spé.": [20]},
        "Forgeron":{  "Arme": "Marteau",            "PV": 120,  "Dégats": [12,9,8,8],      "Att.Spé.": [25]},
        "Boucher":{   "Arme": "Couteau",            "PV": 110,  "Dégats": [10,10,8,6],     "Att.Spé.": [20]},
        "Pêcheur":{   "Arme": "Morue",              "PV": 110,  "Dégats": [10,10,8,6],     "Att.Spé.": [20]},
        "Mage":{      "Arme": "Livre de sort",      "PV": 250,  "Dégats": [40,30],         "Att.Spé.": [100]},
        "Sorcier":{   "Arme": "Baguette magique",   "PV": 250,  "Dégats": [50,35,25],      "Att.Spé.": [110]},
        "Alchimiste":{"Arme": "Potions magiques",   "PV": 250,  "Dégats": [50,35,25],      "Att.Spé.": [110]},
        "Shaman":{    "Arme": "Invocation d'esprit","PV": 230,  "Dégats": [60,40,20],      "Att.Spé.": [125,90]},
        "Archer":{    "Arme": "Arc",                "PV": 150,  "Dégats": [100,40,40,40],  "Att.Spé.": [115,110]},
        "Cavalier":{  "Arme": "Lance",              "PV": 300,  "Dégats": [40,20,20,10],   "Att.Spé.": [80,75]},
        "Infantrie":{ "Arme": "Fusil",              "PV": 275,  "Dégats": [60,40,30,20],   "Att.Spé.": [100,90]},
        "Mercenaire":{"Arme": "Double dague",       "PV": 200,  "Dégats": [75,40,30,30],   "Att.Spé.": [125,90]}}

if __name__ == '__main__':
    # Choix du nom du personnage
    prenom: str = input("Veuillez entrer le prénom de votre personnage: ").capitalize().strip()
    nom: str = input("Veuillez choisir votre nom de famille: ").capitalize().strip()
    nom_complet = verifier_nom(prenom, nom)

    # Choix de la race du personnage
    while True:
        try:
            print(f"\nVoici les races disponibles:")
            for position, r in enumerate(races):
                print(f"{position + 1} - {r['Race']}")
            num_race_choisi: int = int(input("Veuillez choisir une race par son numéro: ").strip())
            race = verifier_race(num_race_choisi)
        except ValueError:
            print("\nVeuillez écrire un nombre entier\n")
            time.sleep(1)
        else:
            break

    # Choix du genre du personnage
    genre: str = input("\nQuel est votre genre? (Homme/Femme/Autre): ").capitalize().strip()
    genre = verifier_genre(genre)

    # Choix de l'âge du personnage
    while True:
        try:
            age:int = int(input("\nQuel âge avez-vous?\n"
                                "Indiquer vôtre âge: ").strip())
            age = verifier_age(age, race)
        except ValueError:
            print("\nVeuillez écrire un nombre entier\n")
            time.sleep(1)
        else:
            break

    # Choix de la classe du personnage
    while True:
        try:
            print(f"\nVoici les classes disponibles:")
            for pos, c in enumerate(classes):
                print(f"{pos + 1} - {c}")
            num_classe:int = int(input("Veuillez choisir votre classe: ").strip())
            classe = verifier_classe(num_classe, classes)
        except ValueError:
            print("\nVeuillez écrire un nombre entier\n")
            time.sleep(1)
        else:
            break

    # Choix de la sous-classe du personnage
    while True:
        try:
            sous_classes = list_sous_classes[classe]
            print(f"\nVoici les sous-classes disponibles:")
            for position, sous_class in enumerate(sous_classes):
                print(f"{position + 1} - {sous_class}")
            num_sous_classe:int = int(input("Veuillez choisir votre sous-classe: ").strip())
            sous_classe = verifier_classe(num_sous_classe, sous_classes)
        except ValueError:
            print("\nVeuillez écrire un nombre entier\n")
            time.sleep(1)
        else:
            break

    print("\n" * 15)
    print(dedent(f"**********************************************************************************\n"
                 f"Bonjour cher aventurier, voici votre personnage:\n"
                 f"Nom: {nom_complet}\n"
                 f"Âge: {age}\n"
                 f"Race: {race["Race"]}\n"
                 f"Genre: {genre}\n"
                 f"Classe choisis: {classe}\n"
                 f"Sous-classe choisis: {sous_classe}\n"
                 f"**********************************************************************************"))



