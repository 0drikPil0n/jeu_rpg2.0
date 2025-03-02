import random
import time
from Création_personnage.personnage import Personnage
from Quete_dragon.attaque_dragon import Attaque

class Dragon:
    def __init__(self,pv:int, atts:list[Attaque]):
        self.pv = pv
        self.atts = atts

    @property
    def pv(self):
        return self.pv

    @pv.setter
    def pv(self,pv):
        if not isinstance(pv, int) or pv <= 0:
            raise TypeError("Les points de vie doivent être un nombre entier plus grand que 0")
        self._pv = pv

    @property
    def atts(self):
        return self.atts

    @atts.setter
    def atts(self, atts):
        if not isinstance(atts, list):
            raise ValueError("Les")

    def attaquer(self,p_perso: Personnage):
        """
        Lance une attaque choisit au hasard dans la liste d'attaque
        :return: None
        """
        reussite = random.choice([True,False])
        attaque = random.choice(self.atts)
        degat = attaque.degat_infliger()
        if not p_perso.esquive:
            if reussite:
                print(f"\nLe dragon utilise {attaque.nom} et vous inflige {degat} dégats")
                p_perso.pv -= degat
                time.sleep(0.5)
            else:
                print(f"\nLe dragon tente {attaque.nom}, mais il échoue...")
                time.sleep(0.5)
