import sys
import time
from textwrap import dedent

from Création_personnage.creer_personnage import (choisir_nom,choisir_age,choisir_genre,choisir_race,choisir_classe,
                                                  choisir_sous_classe,liste_classes,liste_races)
from Création_personnage.personnage import Personnage

# Choix de la mission
liste_aventure = ["Tuer le dragon de la grotte", "Récupérer le crystal magique"]


def verifier_aventure(numero:int, p_list_aventure) -> tuple[int, str]:
    """
    Vérifie si le numéro correspond à une aventure
    :param numero: Le numéro entré
    :param p_list_aventure: Liste des aventures disponibles
    :return: L'aventure choisi par le joueur
    """
    while True:
        if numero not in range(len(p_list_aventure) + 1):
            print("\nVeuillez choisir un numéro de missions valide")
            time.sleep(1)
            print("\nVoici les missions disponibles:")
            for p_pos, p_mission in enumerate(liste_aventure):
                print(f"{p_pos + 1} - {p_mission}")
                time.sleep(0.3)
            numero = int(input(f"\nQuelle aventure souhaitez-vous faire?\n"
                                            f"Choisissez le numéro correspondant de 1 à {(len(liste_aventure))}: "))
        else:
            break
    return numero, liste_aventure[numero - 1]


def resultat_quete(p_victoire:bool):
    """
    Permet à l'utilisateur de choisir ce qu'il veut faire après sa quête, selon s'il a réussi ou s'il a échoué
    :param p_victoire: True si le joueur a réussi sa quête, False sinon.
    :return:
    """
    if p_victoire:
        print(f"\nVous avez compléter cette quête!")
        time.sleep(0.5)
    if not p_victoire:
        print(f"\nVous avez échouer cette quête...")
        time.sleep(0.5)
        p_choix2 = input("\nVoulez-vous recommencer? (oui/non): ")
        while p_choix2 not in ["oui","non"]:
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
        print(f"Au revoir, {classe} {nom}!")
        sys.exit()

if __name__ == '__main__':
    while True:
        nom = choisir_nom()
        race = choisir_race(liste_races, nom)
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
        while True:
            debut_aventure = input("\nÊtes-vous prêt(e) à commencer votre aventure? (oui/non): ").lower().strip()
            if debut_aventure not in ["oui", "non"]:
                print("\nVeuillez choisir entre oui ou non")
                time.sleep(1)
            else:
                if debut_aventure == "non":
                    print("\n")
                break
        if debut_aventure == "oui":
            personnage = Personnage(nom=nom, race=race, genre=genre, age=age, classe=classe, sous_classe=sous_classe)
            personnage.enregistrer_personnage()
            break
    # # Début aventure
    # while True:
    #     while True:
    #         try:
    #             print("\nVoici les missions disponibles:")
    #             for pos, mission in enumerate(liste_aventure):
    #                 print(f"{pos + 1} - {mission}")
    #                 time.sleep(0.3)
    #             num_aventure_choisi = int(input(f"\nQuelle aventure souhaitez-vous faire?\n"
    #                                             f"Choisissez le numéro correspondant de 1 à {(len(liste_aventure))}: "))
    #             aventure = verifier_aventure(num_aventure_choisi, liste_aventure)
    #         except ValueError:
    #             print("\nVeuillez choisir un nombre entier\n")
    #             time.sleep(1)
    #         else:
    #             break
    #
    #     match str(aventure[0]):
    #         case "1":
    #             while True:
    #                 quete_dragon.afficher_dragon()
    #                 pv_dragon = 600
    #                 pv_joueur = stats_role[sous_classe]["PV"]
    #                 tour = 0
    #                 while pv_dragon > 0 and pv_joueur > 0:
    #                     attaque,esquive,tour = quete_dragon.choisir_decision_combat(stats_role, sous_classe, tour)
    #                     pv_dragon,pv_joueur = quete_dragon.combat_dragon(stats_role, sous_classe, attaque, esquive, pv_dragon, pv_joueur)
    #                 victoire = quete_dragon.resultat_dragon(pv_dragon, pv_joueur)
    #                 result = resultat_quete(victoire)
    #                 if not result:
    #                     break
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
    #         case "3":
    #             pass
    #         case "4":
    #             pass


