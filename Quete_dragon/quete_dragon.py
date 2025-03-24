
import time
from textwrap import dedent

from Quete_dragon import Dragon
from Création_personnage import Personnage


def afficher_dragon():
    """
    Affiche la description et l'introduction à la mission
    :return: None
    """
    print("*" * 30)
    print(dedent(
        "Dans cette mission, l'objectif est de traquer et de tuer un dragon redoutable qui\n"
        "terrorise un village voisin. Le dragon, qui vis dans une grotte profonde et obscure,\n"
        "est hostile, et crache du feu sur quiconque ose pénétrer son domaine.\n"))
    input("Appuyer sur entrée pour continuer\n")
    print(dedent(
        "Les aventuriers doivent se préparer en rassemblant des armes. Après une longue\n"
        "semaine de préparation, vous décidez de vous mettre en marche vers cette grotte\n"
        "hostile située dans les montagnes. Une fois arrivé à cette grotte, vous êtes incapable\n"
        "de vaincre votre peur.\n"))
    input("Appuyer sur entrée pour continuer\n")
    print(dedent(
        "Des frissons parcourent votre corps, vos dents se mettent a claquées,\n"
        "vos jambes se mettent a tremblées. C'est alors que vous prenez une grande inspiration, et\n"
        "vous prenez votre courage à deux mains. En entrant dans la grotte, une odeur nauséabonde \n"
        "s'empare de votre corps, vous n'avez jamais senti quelque chose d'aussi mauvais.\n"))
    input("Appuyer sur entrée pour continuer\n")
    print(dedent(
        "C'est alors qu'un craquement se fait surgir comme quelqu'un qui marche sur une branche.\n"
        "Vous décidez de baisser le regard, et c'est à ce moment que vous remarquez que vous\n"
        "marchez sur les cadavres de vos camarades qui, eux aussi, avaient essayés de vaincre ce\n"
        "fameux dragon. C'est alors qu'un bruit se fait entendre dans le fond de la grotte.\n"))
    input("Appuyer sur entrée pour continuer\n")
    print(dedent(
        "Au fur et à mesure que le bruit se rapproche, vous distinguez une silhouette énorme\n"
        "se dirigeant vers vous. C'est alors que le dragon apparait et sans même vous laissez le temps\n"
        "de réagir, vous envoie au sol d'un bref coup circulaire avec sa queue. Vous vous relever,\n"
        "adrénaline dans le sang, vengeance dans l'esprit et vous vous élancer arme dans la main pour\n"
        "peut être la dernière fois!\n"))
    input("Appuyer sur entrée pour continuer\n")
    return None


def combat(joueur: Personnage, p_dragon: Dragon):
    """
    Le combat entre le joueur et le draogn. Permet au joueur de choisir que faire avant le combat.
    :param joueur: Le personnage du joueur
    :param p_dragon: Le dragon
    :return: None
    """
    # Tour du joueur
    joueur.esquive = False
    while True:
        p_choix = input("\nLe dragon se prépare à attaquer... Que voulez-vous faire?\n"
                        "Attaquer (1) ou esquiver (2): ")
        while p_choix not in ["1", "2"]:
            print("\nVeuillez sélectionner un choix valide...")
            time.sleep(0.5)
            p_choix = input("\nLe dragon se prépare à attaquer... Que voulez-vous faire?\n"
                            "Attaquer (1) ou esquiver (2): ")
        match p_choix:
            case "1":
                choix_atts = input("\nQuelle attaque voulez-vous utilisée?\n"
                                   "Attaque normale (1) | Attaque spéciale (2): ")
                while choix_atts not in ["1", "2"]:
                    print("\nVeuillez sélectionner un choix valide...")
                    time.sleep(0.5)
                    choix_atts = input("\nQuelle attaque voulez-vous utilisée?\n"
                                       "Attaque normale (1) | Attaque spéciale (2): ")
                if choix_atts == "2":
                    if joueur.tour_avant_recharge > 0:
                        print(f"\nVous devez attendre {joueur.tour_avant_recharge} tour pour recharger cette attaque...")
                        time.sleep(1)
                        continue
                joueur.attaquer(p_dragon, choix_atts)
                if p_dragon.pv > 0:
                    print(f"\nIl reste {p_dragon.pv} PV au dragon.")
                time.sleep(1)
                break
            case "2":
                joueur.esquiver()
                break
    if joueur.tour_avant_recharge > 0:
        joueur.tour_avant_recharge -= 1
    if p_dragon.pv > 0:
        # Tour du dragon
        reussite = p_dragon.reussite_attaque()
        attaque = p_dragon.attaque_choisis()
        p_dragon.attaquer(p_perso=joueur, attaque=attaque, reussite=reussite)
        if joueur.pv > 0:
            print(f"\nIl vous reste {joueur.pv} point de vie")
        time.sleep(0.5)


def resultat_dragon(joueur, dragon) -> bool:
    """
    Détermine si la quête est réussit ou non.
    :param joueur: Le joueur
    :param dragon: Le dragon
    :return: True si la mission est réussi, False sinon.
    """
    if joueur.pv <= 0:
        print("\nVous avez été vaincu(e)...")
        time.sleep(1)
        return False
    elif dragon.pv <= 0:
        print("\nVous avez vaincu le dragon, félicitation !")
        time.sleep(1)
        return True
