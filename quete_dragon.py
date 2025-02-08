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
    time.sleep(10)
    print("Les aventuriers doivent se préparer en rassemblant des armes. Après une des longues\n "
          "semaines de préparation, vous décidez de vous mettre en marche vers cette grotte\n "
          "hostile dans les montagnes. Une fois arriver à cette grotte, vous êtes incapable\n "
          "de vaicre votre peur.\n")
    time.sleep(10)
    print("Des frissons parcours votre corps, vos dents se met à claquer,\n"
          "vos jambes se met à trembler. C'est alors que vous prennez une grande inspiration et\n "
          "vous penez votre courage à deux mains. En entrant dans la grotte une odeur nauséabonde \n"
          "s'empare de votre corps, vous n'avez jamais senti quelque chose d'aussi mauvais.\n")
    time.sleep(10)
    print("C'est alors qu'un craquement se fait surgir comme quelqu'un qui marche sur une branche.\n "
          "Vous décidez de baisser le regard et c'est à ce moment que vous remarquez que vous\n "
          "marchez sur les cadavres de vos camarades qui eux aussi avaient essayé de vaincre se\n "
          "fameux dragons. C'est alors qu'un bruit se fait entendre dans le fond de la grotte.\n")
    time.sleep(10)
    print("Au fur et à mesure que le bruit se rapproche, vous distinguez une silouhette énorme\n "
          "se dirigeant vers vous. C'est alors que le dragon apparait et sans même vous laissez le temps\n"
          "de réagir, vous envoies au sol d'un bref coup circulaire avec sa queue. Vous vous relever,\n "
          "adrenaline dans le sang, vengeance dans l'esprit et vous vous élencer arme dans la main pour\n "
          "peut être la dernière fois!\n")

    return None


def choisir_decision_combat(stats: dict, role: str) -> tuple[int | Any, bool | Any] | None:
    """
    Permet au joueur de choisir quoi faire avant le combat
    :param stats: Les statistiques du role choisis
    :param role: La sous-classe choisis
    :return: Les points de vie du joueur et du dragon
    """
    tour: int = 0
    # Attaques
    attaques: list[int] = stats[role]["Dégats"]
    attaque = 0 # Par défaut
    attaques_speciale = stats[role]["Att.Spé."]
    # Chance attaque/esquive
    chance_esquive = [True,True,False]
    esquive = False # Par défaut
    # Choix combat
    while pv_dragon > 0 and pv_joueur > 0:
        if tour > 0:
            tour -= 1
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
                        attaque = random.choice(attaques)
                    case "2":
                        if tour != 0:
                            print(f"\nVous ne pouvez pas utiliser votre attaque spéciale!\n"
                                  f"Attendez {tour} tour")
                            time.sleep(1)
                            continue
                        else:
                            attaque = random.choice(attaques_speciale)
                            tour += 3
            case "2": # Le joueur esquive
                esquive = random.choice(chance_esquive)
        return attaque,esquive


def combat_dragon(stats:dict,role:str,attaque:int,esquive:bool):
    # Point de vie
    pv_dragon: int = 600
    pv_joueur: int = stats[role]["PV"]
    arme = stats[role]["Arme"] # Arme utilisé
    if esquive:
        print("\nVous esquiver l'attaque du dragon")
    else:
        print(f"\nVous attaquer le dragon! Vous utilisez {arme} et lui infligé {attaque} dégats!")



