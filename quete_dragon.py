import random
import time
from typing import Any


def afficher_dragon():
    """
    Affiche la description et l'introduction à la mission
    :return: Rien
    """
    print("*" * 30)
    print("Dans cette mission, l'objectif est de traquer et de tuer un dragon redoutable qui\n"
          "terrorise un village voisin. Le dragon, qui vis dans une grotte profonde\n"
          "et obscure, est hostile et crache du feu sur quiconque ose pénétrer son domaine.\n")
    # time.sleep(10)
    # print("Les aventuriers doivent se préparer en rassemblant des armes. Après une des longues\n "
    #       "semaines de préparation, vous décidez de vous mettre en marche vers cette grotte\n "
    #       "hostile dans les montagnes. Une fois arriver à cette grotte, vous êtes incapable\n "
    #       "de vaincre votre peur.\n")
    # time.sleep(10)
    # print("Des frissons parcours votre corps, vos dents se met à claquer,\n"
    #       "vos jambes se met à trembler. C'est alors que vous prenez une grande inspiration et\n "
    #       "vous prenez votre courage à deux mains. En entrant dans la grotte une odeur nauséabonde \n"
    #       "s'empare de votre corps, vous n'avez jamais senti quelque chose d'aussi mauvais.\n")
    # time.sleep(10)
    # print("C'est alors qu'un craquement se fait surgir comme quelqu'un qui marche sur une branche.\n "
    #       "Vous décidez de baisser le regard et c'est à ce moment que vous remarquez que vous\n "
    #       "marchez sur les cadavres de vos camarades qui, eux aussi, avaient essayé de vaincre se\n "
    #       "fameux dragons. C'est alors qu'un bruit se fait entendre dans le fond de la grotte.\n")
    # time.sleep(10)
    # print("Au fur et à mesure que le bruit se rapproche, vous distinguez une silhouette énorme\n "
    #       "se dirigeant vers vous. C'est alors que le dragon apparait et sans même vous laissez le temps\n"
    #       "de réagir, vous envoie au sol d'un bref coup circulaire avec sa queue. Vous vous relever,\n "
    #       "adrenaline dans le sang, vengeance dans l'esprit et vous vous élancer arme dans la main pour\n "
    #       "peut être la dernière fois!\n")

    return None


def choisir_decision_combat(stats: dict, role: str,p_tour:int) -> tuple[int | None | Any, bool | Any, int]:
    """
    Permet au joueur de choisir quoi faire avant le combat
    :param stats: Les statistiques du role choisis
    :param role: La sous-classe choisis
    :param p_tour: Le nombre de tours avant de pouvoir utiliser l'attaque
    :return: Les points de vie du joueur et du dragon
    """
    # Attaques
    attaques: list[int] = stats[role]["Dégats"]
    p_attaque = None # Par défaut
    attaques_speciale = stats[role]["Att.Spé."]
    # Chance attaque/esquive
    chance_esquive = [True,True,False]
    p_esquive = False # Par défaut
    # Choix combat
    if p_tour > 0:
        p_tour -= 1
    while type(p_attaque) != int:
        decision = input(f"\nLe dragon se prépare à attaquer. Que voulez-vous faire?\n"
              f"Attaquer (1) ou esquiver (2): ")
        while decision not in ["1","2"]:
            print(f"\nVeuillez choisir une action valide")
            time.sleep(0.5)
            decision = input(f"\nLe dragon se prépare à attaquer. Que voulez-vous faire?\n"
                                f"Attaquer (1) ou esquiver (2): ")
        match decision:
            case "1": # Le joueur attaque
                choix_attaque = input(f"\nSouhaitez-vous faire une attaque normale ou une attaque spéciale?\n"
                  f"Attaque (1) ou attaque spéciale (2): ")
                while choix_attaque not in ["1","2"]:
                    print(f"\nVeuillez sélectionner un choix valide")
                    time.sleep(0.5)
                    choix_attaque = input(f"\nSouhaitez-vous faire une attaque normale ou une attaque spéciale?\n"
                                          f"Attaque (1) ou attaque spéciale (2): ")
                match choix_attaque:
                    case "1":
                        p_attaque = random.choice(attaques)
                    case "2":
                        if p_tour != 0:
                            print(f"\nVous ne pouvez pas utiliser votre attaque spéciale!\n"
                                  f"Attendez {p_tour} tour")
                            time.sleep(1)
                        else:
                            p_attaque = random.choice(attaques_speciale)
                            p_tour += 3
            case "2": # Le joueur esquive
                p_esquive = random.choice(chance_esquive)
                p_attaque = 0
    return p_attaque,p_esquive,p_tour


def combat_dragon(stats:dict, role:str, p_attaque:int, p_esquive:bool,pv_dragon:int,pv_joueur:int):
    """
    Combat entre le joueur et le dragon. Détermine comment un tour se déroule
    en fonction des choix du joueur.
    :param stats: Les statistiques du joueur.
    :param role: La sous-classe du joueur.
    :param p_attaque: Les dégats que le joueur inflige.
    :param p_esquive: True si il réussit à esquiver, False sinon.
    :param pv_dragon: Les points de vie restant du dragon.
    :param pv_joueur: Les points de vie restant du joueur.
    :return: Les points de vie du joueur et du dragon.
    """
    # Attaque dragon
    attaques_dragon = [120,90]
    chance_att_dragon = [True,False]
    arme = stats[role]["Arme"] # Arme utilisée
    if p_esquive:
        print("\nVous esquiver l'attaque du dragon")
    else:
        if p_attaque > 0:
            print(f"\nVous attaquer le dragon! Vous utilisez {arme} et lui infligé {p_attaque} dégats!")
            pv_dragon -= p_attaque
            time.sleep(1)
            if pv_dragon > 0:
                print(f"\nIl lui reste {pv_dragon} point de vie")
                time.sleep(1)
            if pv_dragon <= 0:
                print(f"\nLe dragon n'a plus de point de vie")
            time.sleep(1)
        else:
            print(f"\nVous n'avez pas réussis à esquiver à temps")
            time.sleep(0.5)
        if pv_dragon > 0:
            chance = random.choice(chance_att_dragon)
            if chance:
                attaque_dragon = random.choice(attaques_dragon)
                print(f"\nLe dragon attaque! Il vous inflige {attaque_dragon} dégats.")
                pv_joueur -= attaque_dragon
                time.sleep(1)
                if pv_joueur > 0:
                    print(f"Il vous reste {pv_joueur} points de vie")
            if not chance:
                print(f"\nLe dragon à échouer son attaque!")
                time.sleep(1)

    return pv_dragon,pv_joueur


def resultat_dragon(pv_dragon:int,pv_joueur:int) -> bool:
    """
    Indique si le joueur a gagné ou a perdu.
    :param pv_dragon: Les points de vie du dragon.
    :param pv_joueur: Les points de vie du joueur
    :return: True si le joueur gagne, False sinon.
    """
    p_victoire = False
    if pv_dragon <= 0:
        print(f"\nFélicitation! Vous avez vaincu le dragon!\n"
              f"Il vous reste {pv_joueur} PV.\n")
        p_victoire = True
    elif pv_joueur <= 0:
        print("\nVous êtes mort. Le dragon vous a tuer\n")
    time.sleep(1)
    return p_victoire