from Création_personnage.classe import Classe
from Création_personnage.sous_classe import SousClasse
from Création_personnage.race import Race

import time

# Races
humain = Race(nom="Humain",age_min=18, age_max=120)
ogre = Race(nom="Ogre",age_min=18, age_max=150)
nain = Race(nom="Nain", age_min=15, age_max=250)
elf = Race(nom="Elf", age_min=16, age_max=500)

liste_races = [humain, ogre, nain, elf]
# Sous-classes
prince = SousClasse(nom="Prince",arme="Poignard",pv=200, degats=[20,15], atts_spe=[60,40])
princesse = SousClasse(nom="Princesse",arme="Dague",pv=175,degats=[30,10],atts_spe=[50])
roi = SousClasse(nom="Roi",arme="Épée",pv=250,degats=[50,40,20,20],atts_spe=[75])
reine = SousClasse(nom="Reine",arme="Épée",pv=225,degats=[60,30,30,10],atts_spe=[70])
fermier = SousClasse(nom="Fermier",arme="Houe",pv=100,degats=[10,8,8,5],atts_spe=[20])
forgeron = SousClasse(nom="Forgeron",arme="Marteau",pv=120,degats=[12,9,8,8],atts_spe=[25])
boucher = SousClasse(nom="Boucher",arme="Couteau",pv=110,degats=[10,10,8,6],atts_spe=[20])
pecheur = SousClasse(nom="Pêcheur",arme="Morue",pv=110,degats=[10,10,8,6],atts_spe=[20])
mage = SousClasse(nom="Mage",arme="Livre de sort",pv=250,degats=[40,30],atts_spe=[100])
sorcier = SousClasse(nom="Sorcier",arme="Baguette magique",pv=250,degats=[50,35,25],atts_spe=[110])
alchimiste = SousClasse(nom="Alchimiste",arme="Potions magiques",pv=250,degats=[50,35,25],atts_spe=[110])
shaman = SousClasse(nom="Shaman",arme="Invocation d'esprit",pv=230,degats=[60,40,20],atts_spe=[125,90])
archer = SousClasse(nom="Archer",arme="Arc",pv=150,degats=[100,40,40,40],atts_spe=[115,110])
cavalier = SousClasse(nom="Cavalier",arme="Lance",pv=300,degats=[40,20,20,10],atts_spe=[80,75])
infanterie = SousClasse(nom="Infantrie",arme="Fusil",pv=275,degats=[60,40,30,20],atts_spe=[100,90])
mercenaire = SousClasse(nom="Mercenaire",arme="Double dague",pv=200,degats=[75,40,30,30],atts_spe=[125,90])
# Classes
royaute = Classe(nom="Royauté",sous_classes=[prince,princesse,roi,reine])
villageois = Classe(nom="Villageois",sous_classes=[fermier,forgeron,boucher,pecheur])
magicien = Classe(nom="Magicien",sous_classes=[mage,sorcier,alchimiste,shaman])
armee = Classe(nom="Armée",sous_classes=[archer,cavalier,infanterie,mercenaire])

liste_classes = [royaute,villageois,magicien,armee]

def choisir_nom():
    """
    Permet au joueur de choisir son nom
    :return: Le nom, complet du joueur
    """
    p_prenom = input("Quel est votre prénom, aventurier?\n"
                     "Pénom: ").capitalize().strip()
    while not p_prenom.isalpha():
        print("\nEntrez un prénom correcte")
        time.sleep(1)
        p_prenom = input("\nQuel est votre prénom, aventurier?\n"
                         "Pénom: ").capitalize().strip()
    p_nom = input("\nQuel est votre nom de famille, aventurier?\n"
                    "Nom de famille: ").capitalize().strip()
    while not p_nom.isalpha():
        print("\nEntrez un nom de famille correcte")
        time.sleep(1)
        p_nom = input("\nQuel est votre nom de famille, aventurier?\n"
                      "Nom de famille: ").capitalize().strip()
    print("\nExcellent !\n")
    time.sleep(1)
    p_nom_complet = p_prenom + " " + p_nom

    return p_nom_complet

def choisir_race(p_races: list[Race], p_nom):
    """
    Permet au joueur de choisir sa race
    :param p_races: La liste des races disponibles
    :param p_nom: Le nom du joueur
    :return: La race choisis
    """
    while True:
        print("\nVoici les races disponibles:")
        for i,race in enumerate(p_races):
            print(f"{i + 1} - {race.nom}")
            time.sleep(0.5)
        try:
            race_choisis:int = int(input(f"De quelle race êtes vous, aventurier?\n"
                                        f"Choisissez un numéro entre 1 et {len(p_races)}: "))
        except ValueError:
            print(f"\nVeuillez écrire un nombre entre 1 et {len(p_races)}")
            time.sleep(1)
        else:
            if race_choisis not in range(1, (len(p_races) + 1)):
                print(f"\nVeuillez écrire un nombre entre 1 et {len(p_races)}")
                time.sleep(1)
            else:
                print("\nExcellent !\n")
                time.sleep(1)
                return p_races[race_choisis - 1]

def choisir_genre():
    """
    Permet au joueur de choisir son genre
    :return: Le genre du joueur
    """
    while True:
        p_genre = input("\nQuel est votre genre, aventurier?\n"
                        "(Homme/femme/autre): ").capitalize().strip()
        if p_genre not in ["Homme", "Femme", "Autre"]:
            print("\nVeuillez choisir un genre entre Homme/Femme/Autre")
            time.sleep(1)
        else:
            print("\nExcellent !\n")
            time.sleep(1)
            return p_genre

def choisir_age(p_race: Race):
    """
    Permet au joueur de choisir son âge.
    :param p_race: La race choisis
    :return: L'âge du joueur
    """
    while True:
        try:
            p_age:int = int(input(f"\nQuel est votre age, aventurier?\n"
                          f"Limite d'âges: {p_race.limite_age}\n"
                                  f"Votre âge: "))
            if p_age < p_race.age_min or p_age > p_race.age_max:
                raise ValueError
        except ValueError:
            print(f"Veuillez écrire écrire un nombre entre {p_race.age_min} et {p_race.age_max}")
            time.sleep(1)
        else:
            print("\nExcellent !\n")
            time.sleep(1)
            return p_age

def choisir_classe(p_classes: list[Classe]):
    """
    Permet au joueur de choisir sa classe
    :param p_classes: La liste de classe diponibles
    :return: La classe choisit
    """
    while True:
        print("\nVoici les classes disponibles:")
        for i, cla in enumerate(p_classes,start=1):
            print(f"{i} - {cla.nom}")
            time.sleep(0.5)
        try:
            p_classe: int = int(input("\nQuel est votre classe, aventurier?\n"
                             "Classe choisi: "))
            if p_classe not in range(1, (len(p_classes) + 1)):
                raise ValueError
        except ValueError:
            print("\nVeuillez choisir une classe valide")
            time.sleep(1)
        else:
            print("\nExcellent !\n")
            time.sleep(1)
            return p_classes[p_classe - 1]

def choisir_sous_classe(p_classe: Classe):
    """
    Permet au joueur de choisir sa sous-classe
    :param p_classe: La classe choisi
    :return: La sous-classe choisi
    """
    while True:
        p_sous_classes = p_classe.sous_classes
        print("\nVoici les sous-classes disponibles:")
        for i, sous in enumerate(p_sous_classes,start=1):
            print(f"{i} - {sous.nom}")
            time.sleep(0.5)
        try:
            p_sous:int = int(input("\nQuel est votre sous-classe, aventurier?\n"
                           "Classe choisi: "))
            if p_sous not in range(1, (len(p_sous_classes) + 1)):
                raise ValueError
        except ValueError:
            print("\nVeuillez choisir une sous-class valide")
            time.sleep(1)
        else:
            print("\nExcellent !\n")
            time.sleep(1)
            return p_sous_classes[p_sous - 1]



