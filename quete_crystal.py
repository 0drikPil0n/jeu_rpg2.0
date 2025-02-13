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


def creer_carte_pilier():
    """
    Crée la carte de pilier que le joueur devra traverser
    :return: La carte de pilier
    """
    piliers = ["S", "S", "S", "T", "T", "E"]  # S pour solide, T pour tombant et E pour ennemi
    carte_pilier = {}
    for i in range(10):
        rangee_pilier = []
        for j in range(10):
            pilier = random.choice(piliers)
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

# Déplacement sur la map
def position_depart(map_):
    """
    Choisis la position de départ du joueur sur la carte
    :param map_: La carte
    :return: La position du joueur sur la carte
    """
    # Initialize les variable
    p_position_depart = None
    hauteur = None
    largeur = None
    while p_position_depart != "S":
        hauteur = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        largeur = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        p_position_depart = map_[hauteur][largeur]
    p_co_x = largeur + 1
    p_co_y = -(hauteur + 1) + 11

    return p_position_depart, int(p_co_y), int(p_co_x)


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

    p_co_x = largeur + 1
    p_co_y = -(hauteur + 1) + 11
    return position_map, p_co_y, p_co_x


def situation_piliers(position:str, pv_joueur:int,atts_joueur:list,):
    """
    Détermine ce qui arrive au joueur en fonction du type de pilier sur lequel il atterrit
    :param position: La position du joueur
    :param pv_joueur: Les points de vie du joueur
    :param atts_joueur: Les attaques du joueur
    :return: None si le pilier est solide, False si le pilier tombe, retourne la victoire si le joueur croise un ennemi
    """
    if position == "S":
        time.sleep(0.5)
        print("Le pilier ne bouge pas. Vous êtes en sécurité")
        time.sleep(0.5)
        return None
    elif position == "T":
        time.sleep(0.5)
        print("Vous tomber dans le vide")
        time.sleep(0.5)
        return False
    elif position == "E":
        time.sleep(0.5)
        victoire = attaque_ennemi(pv_joueur,atts_joueur)
        return victoire
    elif position == "C":
        time.sleep(0.5)
        print("Vous avez trouver le crystal !")
        time.sleep(0.5)
        return None

# Affichage de la carte
def afficher_map(p_map:dict):
    """
    Affiche la carte
    :param p_map: La carte
    :return: None
    """
    for chiffre,rangee in p_map.items():
        print(f"{rangee}\n")
    return None


def afficher_coordonnees(co_x:int, co_y:int):
    """
    Afficher les coordonnées du joueur sur la carte
    :param co_x: Sa position sur l'axe X
    :param co_y: Sa position sur l'axe Y
    :return: None
    """
    print(f"Coordonnée de l'axe X: {co_x}\n"
          f"Coordonnée de l'axe Y: {co_y}")
    return None

# Combat
def attaque_ennemi(pv_joueur:int, atts_joueur:list):
    victoire = False
    liste_ennemis = [["Chauve-sourie", 50, 5], ["Squelette", 75, 10], ["Zombie", 60, 15]]
    ennemi = random.choice(liste_ennemis)
    pv_ennemi = ennemi[1]
    att_ennemi = ennemi[2]
    print(f"\nVous tomber sur {ennemi[0]}")
    time.sleep(0.5)
    choix = int(input(f"\nQue voulez-vous faire? Attaquer ou essayer de pousser l'ennemi dans le vide?\n"
                  f"Attaquer(0) ou Pousser(1): "))
    while choix not in [0,1]:
        choix = int(input(f"\nVeuillez sélectionner un choix valide.\n"
                      f"Attaquer(0) ou Pousser(1): "))
    if choix == 0:
        while pv_joueur >= 0 and pv_ennemi >= 0:
            att_joueur = random.choice(atts_joueur)
            print(f"\n{ennemi[0]} vous inflige {att_ennemi} dégats")
            pv_joueur = pv_joueur - att_ennemi
            time.sleep(0.5)
            print(f"\nIl vous reste {pv_joueur} PV.")
            time.sleep(0.5)
            print(f"\nVous attaquer {ennemi[0]}. Vous lui infligé {att_joueur} dégats.")
            pv_ennemi = pv_ennemi - att_joueur
            time.sleep(0.5)
            if pv_ennemi > 0:
                print(f"Il reste {pv_ennemi} PV à {ennemi[0]}.")
            time.sleep(0.5)
        if pv_ennemi <= 0:
            print(f"Vous avez vaincu {ennemi[0]}.")
            victoire = True
            time.sleep(0.5)
        if pv_joueur <= 0:
            print(f"{ennemi[0]} vous à vaincu.")
            time.sleep(0.5)
            victoire = False
    if choix == 1:
        if ennemi[0] == "Chauve-Sourie":
            pousser = False
        else:
            pousser = random.choice([False,True])
        if pousser:
            print("Vous poussez l'ennemi dans le vide.")
            pv_ennemi -= pv_ennemi
            time.sleep(0.5)
        if not pousser:
            print("\nVous n'avez pas réussis a pousser l'ennemi dans le vide.")
            time.sleep(0.5)

    return victoire
