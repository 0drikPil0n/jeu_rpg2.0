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

pilier = ["S", "S", "S", "T", "T", "E"] # S pour solide, T pour tombant et E pour ennemi