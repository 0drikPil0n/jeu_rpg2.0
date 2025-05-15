import random
import time

from Pillier import Pillier
from Générale import Ennemi
from Générale import Attaque
from Création_personnage import Personnage

class PillierEnnemi(Pillier):
    ### Création des ennemis avec leur attaques
    # Chauve-sourie
    bite = Attaque("Morsure",[5],[1])
    chauve_sourie = Ennemi("Chauve-sourie", 50,[bite],[1])
    # Squelette
    arc = Attaque("Arc",[10],[1])
    squelette = Ennemi("Squelette",75,[arc], [1])
    # Zombie
    spit = Attaque("Crachat",[15],[1])
    zombie = Ennemi("Zombie",100,[spit],[1])
    ennemis = [chauve_sourie, squelette, zombie]
    def __init__(self, sorte: str, stable: bool):
        super().__init__(sorte="Pillier ennemi", stable=True)

    @classmethod
    def combat_ennemi(cls, joueur: Personnage):
        """
        Fait attaquer un ennemi aléatoire.
        :param joueur: Le joueur
        :return: None
        """
        victoire = False
        ennemi = random.choice(cls.ennemis)
        print(f"\nVous tomber sur {ennemi.nom}")
        time.sleep(0.5)
        while joueur.pv > 0 and ennemi.pv > 0:
            choix = int(input(f"\nQue voulez-vous faire? Attaquer ou essayer de pousser l'ennemi dans le vide?\n"
                              f"Attaquer(0) ou Pousser(1): "))
            while choix not in [0, 1]:
                choix = int(input(f"\nVeuillez sélectionner un choix valide.\n"
                                  f"Attaquer(0) ou Pousser(1): "))
            if choix == 0:
                # Tour de l'ennemi
                ennemi.attaquer(joueur)
                # Tour du joueur
                choix = "1"
                joueur.attaquer(ennemi,choix)
            elif choix == "2":
                if ennemi == cls.chauve_sourie:
                    pousser = False
                else:
                    pousser = random.choice([False,True])
                if pousser:
                    print("Vous poussez l'ennemi dans le vide.")
                    ennemi.pv -= ennemi.pv
                    time.sleep(0.5)
                if not pousser:
                    print("\nVous n'avez pas réussis a pousser l'ennemi dans le vide.")
                    time.sleep(0.5)


