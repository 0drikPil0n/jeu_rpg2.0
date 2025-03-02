import random
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
        if pv is not isinstance(pv, int):
            raise TypeError("Les points de vie doivent être un nombre entier")
        self._pv = pv

    @property
    def atts(self):
        return self.atts

    @atts.setter
    def atts(self, atts):
        if atts is not isinstance(atts, list):
            raise ValueError("Les")

    def attaquer(self,p_perso: Personnage):
        """
        Lance une attaque choisit au hasard dans la liste d'attaque
        :return: L'attaque lancé
        """
        chance_reussite
        attaque = random.choice(self.atts)
        degat = attaque.degat_infliger()
        if not p_perso.esquive:
            print(f"Le dragon utilise {attaque.nom} et vous inflige {degat} dégats")
            p_perso.pv -= degat
        else:
            print(f"Le dragon tente")

