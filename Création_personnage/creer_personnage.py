from Création_personnage.classe import Classe
from Création_personnage.sous_classe import SousClasse
from Création_personnage.race import Race

import time

from Générale.Attaque import Attaque

# Races
humain = Race(nom="Humain", age_min=18, age_max=120)
ogre = Race(nom="Ogre", age_min=18, age_max=150)
nain = Race(nom="Nain", age_min=15, age_max=250)
elf = Race(nom="Elf", age_min=16, age_max=500)

liste_races = [humain, ogre, nain, elf]
## Sous-classes
# Prince
poignard = Attaque("Poignard", [25, 15], [1, 1])
poignard_s = Attaque("Poignard", [60, 40], [1, 2])
prince = SousClasse(nom="Prince", arme="Poignard", pv=200, attaque=poignard, attaque_speciale=poignard_s)
# Princesse
dague = Attaque("Dague", [30, 10], [2, 1])
dague_s = Attaque("Dague", [50], [1])
princesse = SousClasse(nom="Princesse", arme="Dague", pv=175, attaque=dague, attaque_speciale=dague_s)
# Roi
epee1 = Attaque("Épée", [50, 40, 20, ], [1, 1, 2])
epee1_s = Attaque("Épée", [75], [1])
roi = SousClasse(nom="Roi", arme="Épée", pv=250, attaque=epee1, attaque_speciale=epee1_s)
# Reine
epee2 = Attaque("Épée", [60, 30, 10], [1, 2, 1])
epee2_s = Attaque("Épée", [70], [1])
reine = SousClasse(nom="Reine", arme="Épée", pv=225, attaque=epee2, attaque_speciale=epee2_s)
# Fermier
houe = Attaque("Houe", [10, 8, 5], [1, 2, 1])
houe_s = Attaque("Houe", [20], [1])
fermier = SousClasse(nom="Fermier", arme="Houe", pv=100, attaque=houe, attaque_speciale=houe_s)
# Forgeron
marteau = Attaque("Marteau", [12, 9, 8], [1, 1, 2])
marteau_s = Attaque("Marteau", [25], [1])
forgeron = SousClasse(nom="Forgeron", arme="Marteau", pv=120, attaque=marteau, attaque_speciale=marteau_s)
# Boucher
couteau = Attaque("Couteau", [10, 8, 6], [2, 1, 1])
couteau_s = Attaque("Couteau", [20], [1])
boucher = SousClasse(nom="Boucher", arme="Couteau", pv=110, attaque=couteau, attaque_speciale=couteau_s)
# Pêcheur
morue = Attaque("Morse", [12, 8, 6], [1, 2, 1])
morue_s = Attaque("Morse", [20], [1])
pecheur = SousClasse(nom="Pêcheur", arme="Morue", pv=110, attaque=morue, attaque_speciale=morue_s)
# Mage
livre_sort = Attaque("Livre de sort", [40, 30], [4, 3])
livre_sort_s = Attaque("Livre de sort", [100], [1])
mage = SousClasse(nom="Mage", arme="Livre de sort", pv=250, attaque=livre_sort, attaque_speciale=livre_sort_s)
# Sorcier
baguette_magique = Attaque("Baguette magique", [50, 35, 25], [2, 3, 1])
baguette_magique_s = Attaque("Baguette magique", [110], [1])
sorcier = SousClasse(nom="Sorcier", arme="Baguette magique", pv=250, attaque=baguette_magique,
                     attaque_speciale=baguette_magique_s)
# Alchimiste
potions = Attaque("Potions", [50, 35, 25], [3, 4, 2])
potions_s = Attaque("Potions", [110], [1])
alchimiste = SousClasse(nom="Alchimiste", arme="Potions magiques", pv=250, attaque=potions, attaque_speciale=potions_s)
# Shaman
invocation_esprit = Attaque("Invocation esprit", [60, 40, 20], [3, 2, 1])
invocation_esprit_s = Attaque("Invocation esprit", [125, 90], [1, 2])
shaman = SousClasse(nom="Shaman", arme="Invocation d'esprit", pv=230, attaque=invocation_esprit,
                    attaque_speciale=invocation_esprit_s)
# Archer
arc = Attaque("Arc", [100,40], [1, 3])
arc_s = Attaque("Arc", [115, 110], [1, 2])
archer = SousClasse(nom="Archer", arme="Arc", pv=150, attaque=arc, attaque_speciale=arc_s)
# Cavalier
lance = Attaque("Lance", [40, 20, 10], [2, 3, 1])
lance_s = Attaque("Lance", [80, 75], [3, 4])
cavalier = SousClasse(nom="Cavalier", arme="Lance", pv=300, attaque=lance, attaque_speciale=lance_s)
# Infanterie
fusil = Attaque("Fusil", [60, 40, 30, 20], [2, 3, 1])
fusil_s = Attaque("Fusil", [100, 90], [1, 2])
infanterie = SousClasse(nom="Infantrie", arme="Fusil", pv=275, attaque=fusil, attaque_speciale=fusil_s)
# Mercenaire
double_dague = Attaque("Double Dague", [75, 40, 30], [1, 1, 2])
double_dague_s = Attaque("Double Dague", [125, 90], [1, 3])
mercenaire = SousClasse(nom="Mercenaire", arme="Double dague", pv=200, attaque=double_dague,
                        attaque_speciale=double_dague_s)
# Classes
royaute = Classe(nom="Royauté", sous_classes=[prince, princesse, roi, reine])
villageois = Classe(nom="Villageois", sous_classes=[fermier, forgeron, boucher, pecheur])
magicien = Classe(nom="Magicien", sous_classes=[mage, sorcier, alchimiste, shaman])
armee = Classe(nom="Armée", sous_classes=[archer, cavalier, infanterie, mercenaire])

liste_classes = [royaute, villageois, magicien, armee]


def choisir_nom():
    """
    Permet au joueur de choisir son nom
    :return: Le nom complet du joueur
    """
    p_prenom = input("\nQuel est votre prénom, aventurier?\n"
                     "Prénom: ").capitalize().strip()
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
    p_nom_complet = f"{p_prenom} {p_nom}"

    return p_nom_complet


def choisir_race(p_races: list[Race]):
    """
    Permet au joueur de choisir sa race
    :param p_races: La liste des races disponibles
    :return: La race choisis
    """
    while True:
        print("\nVoici les races disponibles:")
        for i, race in enumerate(p_races):
            print(f"{i + 1} - {race.nom}")
            time.sleep(0.5)
        try:
            race_choisis: int = int(input(f"De quelle race êtes vous, aventurier?\n"
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
            p_age: int = int(input(f"\nQuel est votre age, aventurier?\n"
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
        for i, cla in enumerate(p_classes, start=1):
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
        for i, sous in enumerate(p_sous_classes, start=1):
            print(f"{i} - {sous.nom}")
            time.sleep(0.5)
        try:
            p_sous: int = int(input("\nQuel est votre sous-classe, aventurier?\n"
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
