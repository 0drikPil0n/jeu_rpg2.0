import sys
import time
from textwrap import dedent
import jsonpickle

from Générale.Attaque import Attaque

from Création_personnage import (Personnage, choisir_nom, choisir_race, liste_races, choisir_genre,
                                 choisir_age, choisir_classe, liste_classes, choisir_sous_classe)

from Quete_dragon import Dragon, afficher_dragon, combat, resultat_dragon




liste_aventure = ["Tuer le dragon de la grotte", "Récupérer le crystal magique"]


def choisir_personnage():
    """
    Permet au joueur de choisir son personnage, sois une sauvegarde déjà existante ou alors créer un nouveau personnage.
    :return: Le personnage choisi
    """
    while True:
        while True:
            try:
                sauvegarde = int(input("\nSouhaitez-vous commencer une nouvelle partie ou en reprendre une ancienne?\n"
                                       "Commencer (1) | Reprendre (2) : "))
                if sauvegarde not in [1, 2]:
                    raise ValueError
            except ValueError:
                print("\nVeuillez choisir un nombre entier entre 1 et 2\n")
                time.sleep(1)
            else:
                break

        match sauvegarde:
            case 1:
                nom = choisir_nom()
                race = choisir_race(liste_races)
                genre = choisir_genre()
                age = choisir_age(race)
                classe = choisir_classe(liste_classes)
                sous_classe = choisir_sous_classe(classe)
                print("\n" * 15)
                print(dedent(f"**********************************************************************************\n"
                             f"Bonjour cher aventurier, voici votre personnage:\n"
                             f"Nom: {nom}\n"
                             f"Âge: {age} ans\n"
                             f"Race: {race.nom}\n"
                             f"Genre: {genre}\n"
                             f"Classe choisis: {classe.nom}\n"
                             f"Sous-classe choisis: {sous_classe.nom}\n"
                             f"**********************************************************************************"))
                personnage = Personnage(nom=nom, race=race, genre=genre, age=age, classe=classe,
                                        sous_classe=sous_classe)
                p_perso_joueur: Personnage = commencer_quete(sauvegarde, personnage)
                if p_perso_joueur is not None:
                    return p_perso_joueur
            case 2:
                with open(file=Personnage.CHEMIN_PERSO, mode="r") as perso_json:
                    liste_personnage: list[Personnage] = jsonpickle.decode(perso_json.read())
                if not liste_personnage:
                    print("\nVous n'avez aucune sauvegarde. . .")
                    time.sleep(1)
                    continue
                else:
                    while True:
                        try:
                            for i, perso in enumerate(liste_personnage, start=1):
                                print(f"{i} - {perso.nom}\n"
                                      f"    - {perso.race.nom}\n"
                                      f"    - {perso.genre}\n"
                                      f"    - {perso.age}\n"
                                      f"    - {perso.classe.nom}\n"
                                      f"    - {perso.sous_classe.nom}\n")
                            numero = int(input("Quel sauvegarde voulez-vous prendre?\n"
                                               "Sélectionnez le numéro correspondant: "))
                            if numero not in range(1, len(liste_personnage) + 1):
                                raise IndexError
                        except (ValueError, IndexError):
                            print("\nVeuillez choisir une sauvegarde valide\n")
                            time.sleep(1)
                        else:
                            break
                personnage: Personnage = liste_personnage[numero - 1]
                p_perso_joueur: Personnage = commencer_quete(sauvegarde, personnage)
                if p_perso_joueur is not None:
                    return p_perso_joueur


def choisir_aventure() -> tuple[int, str]:
    """
    Permet au joueur de choisir l'aventure qu'il souhaite faire.
    :return: L'aventure choisi par le joueur
    """
    while True:
        try:
            print("\nVoici les missions disponibles:")
            for p_pos, p_mission in enumerate(liste_aventure):
                print(f"{p_pos + 1} - {p_mission}")
                time.sleep(0.3)
            p_numero = int(input(f"\nQuelle aventure souhaitez-vous faire?\n"
                                 f"Choisissez le numéro correspondant de 1 à {(len(liste_aventure))}: "))
            if p_numero not in range(1, len(liste_aventure) + 1):
                raise IndexError
        except (ValueError, IndexError):
            print("\nVeuillez choisir un nombre correspondant à une mission.\n")
            time.sleep(1)
        else:
            return p_numero, liste_aventure[p_numero - 1]


def commencer_quete(p_sauvegarde: int, p_perso: Personnage = None, ):
    """
    Permet au joueur de décider si il veut commencer une quête ou s'il change d'idée
    :param p_perso: Le personnage créer (s'il y a lieu, sinon None)
    :param p_sauvegarde: La décision du joueur de prendre une suavegarde existente ou non.
    :return: Le personnage utilisé
    """
    while True:
        p_debut_aventure = input("\nÊtes-vous prêt(e) à commencer votre aventure? (oui/non): ").lower().strip()
        if p_debut_aventure not in ["oui", "non"]:
            print("\nVeuillez choisir entre oui ou non")
            time.sleep(1)
        else:
            match p_debut_aventure:
                case "non":
                    print("\n")
                    return None
                case "oui":
                    p_personnage = p_perso
                    if p_sauvegarde == 1:
                        p_personnage.enregistrer_personnage()
                    return p_personnage


def resultat_quete(p_victoire: bool, p_joueur: Personnage):
    """
    Permet à l'utilisateur de choisir ce qu'il veut faire après sa quête, selon s'il a réussi ou s'il a échoué
    :param p_victoire: True si le joueur a réussi sa quête, False sinon.
    :param p_joueur: Le joueur
    :return:
    """
    if p_victoire:
        print(f"\nVous avez compléter cette quête!")
        time.sleep(0.5)
    if not p_victoire:
        print(f"\nVous avez échouer cette quête...")
        time.sleep(0.5)
        p_choix2 = input("\nVoulez-vous recommencer? (oui/non): ")
        while p_choix2 not in ["oui", "non"]:
            print("\nVeuillez choisir 'oui' ou 'non'! ")
            time.sleep(1)
            p_choix2 = input("\nVoulez-vous recommencer? (oui/non): ")
        if p_choix2 == "oui":
            return True
        elif p_choix2 == "non":
            pass
    p_choix3 = input("\nSouhaitez-vous en faire une autre? (oui/non): ").strip().lower()
    while p_choix3 not in ["oui", "non"]:
        print("\nVeuillez choisir 'oui' ou 'non'! ")
        time.sleep(1)
        p_choix3 = input("Souhaitez-vous en faire une autre? (oui/non): ").strip().lower()
    if p_choix3 == "oui":
        return False
    elif p_choix3 == "non":
        print(f"Au revoir, {p_joueur.classe} {p_joueur.nom}!")
        sys.exit()


if __name__ == '__main__':
    print("Saluation ! Bienvenu(e) au jeu!")
    time.sleep(1)
    # Choix du pesonnage
    perso_joueur = choisir_personnage()
    # Début de l'aventure
    while True:
        aventure = choisir_aventure()
        num_aventure = aventure[0]
        match num_aventure:
            case 1:
                while True:
                    # Attaque du dragon
                    coup_queue = Attaque(nom="Coup de queue", degats=[50, 55], chances=[2, 1])
                    lance_flamme = Attaque(nom="Lance flamme", degats=[75, 80], chances=[2, 1])
                    coup_griffe = Attaque(nom="Coup de griffe", degats=[30, 35], chances=[2, 1])
                    # Le dragon
                    dragon = Dragon(pv=600, atts=[coup_queue, lance_flamme, coup_griffe], chances=[2, 1, 1])
                    afficher_dragon()
                    while perso_joueur.pv > 0 and dragon.pv > 0:
                        combat(perso_joueur, dragon)
                    victoire = resultat_dragon(perso_joueur, dragon)



                    # afficher_dragon()
                    # pv_dragon = 600
    #                 pv_joueur = stats_role[sous_classe]["PV"]
    #                 tour = 0
    #                 while pv_dragon > 0 and pv_joueur > 0:
    #                         attaque,esquive,tour = choisir_decision_combat(stats_role, sous_classe, tour)
    #                         pv_dragon,pv_joueur = combat_dragon(stats_role, sous_classe, attaque, esquive, pv_dragon, pv_joueur)
    #                     victoire = resultat_dragon(pv_dragon, pv_joueur)
    #                     result = resultat_quete(victoire)
    #                     if not result:
    #                         break
    #         case "2":
    #             while True:
    #                 survie = None
    #                 pv_joueur = stats_role[sous_classe]["PV"]
    #                 quete_crystal.afficher_crystal()
    #                 carte_sc = quete_crystal.creer_carte_pilier() # sc = sans crystal
    #                 carte = quete_crystal.choisir_spot_crystal(carte_sc)
    #                 position, largeur, hauteur, coordonnees = quete_crystal.position_depart(carte)
    #                 while position != "C" and survie is not False:
    #                     attaques_joueur = stats_role[sous_classe]["Dégats"]
    #                     while True:
    #                         choix = input(f"-------------------------\n"
    #                                       f"Que voulez-vous faire?\n"
    #                                       f"1 - Voir la carte\n"
    #                                       f"2 - Voir vos coordonées\n"
    #                                       f"3 - Avancer sur un pilier\n"
    #                                       f"-------------------------\n"
    #                                       f"Choisissez une option: ")
    #                         if choix not in ["1", "2", "3"]:
    #                             print("Veuillez choisir un choix valide")
    #                         else:
    #                             break
    #                     match choix:
    #                         case "1":
    #                             quete_crystal.afficher_map(carte)
    #                         case "2":
    #                             quete_crystal.afficher_coordonnees(coordonnees[0], coordonnees[1])
    #                         case "3":
    #                             position, largeur, hauteur, coordonnees= quete_crystal.avancer_map(carte, largeur, hauteur)
    #                             survie = quete_crystal.situation_piliers(position, pv_joueur, attaques_joueur)
    #                 victoire = quete_crystal.resultat_crystal(survie, position)
    #                 result = resultat_quete(victoire)
    #                 if not result:
    #                     break
    #
    #
    #
    #
    #
    # case "3":
    #     pass
    # case "4":
    #     pass
