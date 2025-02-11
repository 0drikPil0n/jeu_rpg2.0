import random
import time

def afficher_crystal():
    """
    Affiche un message d'introduction et de description
    :return: None
    """
    print("*" * 30)
    print("Dans un désert loins de la civilisation, se trouve un temple ancien en ruine depuis des années.\n"
          "Le temple était autrefois un sanctuaire pour les dieux, des shaman se réunissaient pour les vénérés.\n"
          "Ils s'agenouilaient autour du centre du temple, duquel jaïssait un vaisseau de lumière très intense.\n")
    # time.sleep(10)
    print("Ce vaisseau de lumière, portait avec lui la puissance nécessaire pour alimenter toute une ville en électricité,\n"
          "cependant, les shamans n'avait absolument aucune idée d'où cette puissance pouvait bien provenir.\n"
          "Aujourd'hui, nous possédons la technologie pour allerexplorer ces ruines, mais ça ne se passe pas comme prévu.\n")
    # time.sleep(10)
    print("Tout au fin fond des ruines du temples, se trouve une oasis, avec au milieu, un crystal.\n"
          "Le problème, est que cette oasis est isolé du reste du temple, malgé qu'elle sois situé en son centre.\n"
          "Elle est entouré de pilier de roche, certain stable, d'autre tombe lorsque qu'on met les pieds dessus.\n")
    # time.sleep(10)
    print("Pour une raison inconnu, les piliers reviennent toujours, et ne sont jamais les mêmes à chaque fois.\n"
          "Votre but est d'aller chercher le crystal et le ramener au royaume, sans tomber dans le vide inconnu,\n"
          "vous pourriez mourir de votre chute...\n")
    # time.sleep(5)
    print("ou pire")
    return None

# Création de la carte
piliers = ["S", "S", "S", "T", "T", "E"] # S pour solide, T pour tombant et E pour ennemi


def creer_carte_pilier(p_piliers:list):
    """
    Crée la carte de pilier que le joueur devra traverser
    :param p_piliers: La liste des types de piliers
    :return: La carte de pilier
    """
    carte_pilier = {}
    for i in range(10):
        rangee_pilier = []
        for j in range(10):
            pilier = random.choice(p_piliers)
            rangee_pilier.append(pilier)
        carte_pilier[i] = rangee_pilier
    return carte_pilier


def choisir_spot_crystal(p_map:dict):
    """
    Choisis aléatoirement l'emplacement du crystal secret que le joueur devra trouver
    :param p_map: La carte de base
    :return: La carte avec le crystal
    """
    rangee_choisi = random.choice(p_map)
    spot_choisi = random.choice([0,1,2,3,4,5,6,7,8,9])
    rangee_choisi.pop(spot_choisi)
    rangee_choisi.insert(spot_choisi, "C")

    return p_map


def position_depart(map_):
    """
    Choisis la position de départ du joueur sur la carte
    :param map_: La carte
    :return: La position du joueur sur la carte
    """
    p_position_depart = None
    while p_position_depart != "S":
        hauteur = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        largeur = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        p_position_depart = map_[hauteur][largeur]

    return position_depart, int(hauteur), int(largeur)


def avancer_map(map_:dict,hauteur:int,largeur:int):
    """
    Permet au joueur d'avancer sur la carte dans la direction de son choix
    :param map_: La carte
    :param hauteur: La position en Y du joueur
    :param largeur: La positiion en X du joueur
    :return: Sa nouvele position
    """
    position_map = map_[hauteur][largeur]
    while True:
        try:
            direction = int(input(f"Dans quelle directions voulez-vous aller?\n"
                              f"Haut(0), Bas(1), Gauche(2), Droite(3): "))
            if direction not in (0, 1, 2, 3):
                raise ValueError
        except ValueError:
            print("Veuillez écrire un numéro valide.")
        else:
            break
    if direction == 0:
        try:
            hauteur = hauteur - 1
            position_map = map_[hauteur][largeur]
        except (IndexError,KeyError):
            hauteur = hauteur + 1
            position_map = map_[hauteur][largeur]
            print("Vous ne pouvez pas aller dans cette direction")
        else:
            pass
    if direction == 1:
        try:
            hauteur = hauteur + 1
            position_map = map_[hauteur][largeur]
        except (IndexError,KeyError):
            hauteur = hauteur - 1
            position_map = map_[hauteur][largeur]
            print("Vous ne pouvez pas aller dans cette direction")
        else:
            pass
    if direction == 2:
        try:
            largeur = largeur - 1
            position_map = map_[hauteur][largeur]
        except (IndexError,KeyError):
            largeur = largeur + 1
            position_map = map_[hauteur][largeur]
            print("Vous ne pouvez pas aller dans cette direction")
        else:
            pass
    if direction == 3:
        try:
            largeur = largeur + 1
            position_map = map_[hauteur][largeur]
        except (IndexError,KeyError):
            largeur = largeur - 1
            position_map = map_[hauteur][largeur]
            print("Vous ne pouvez pas aller dans cette direction")
        else:
            pass
    return position_map, hauteur, largeur


