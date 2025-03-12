import random
import time
from Création_personnage.personnage import Personnage
from Quete_dragon.attaque_dragon import Attaque

class Dragon:
    def __init__(self,pv:int, atts:list[Attaque], chances:list[int]):
        self.pv = pv
        self.atts = atts
        self.chances = chances

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self,pv):
        if not isinstance(pv, int) or pv <= 0:
            raise TypeError("Les points de vie doivent être un nombre entier plus grand que 0")
        self._pv = pv

    @property
    def atts(self):
        return self._atts

    @atts.setter
    def atts(self, atts):
        if not isinstance(atts, list):
            raise ValueError("Les")
        self._atts = atts

    @property
    def chances(self):
        return self._chances

    @chances.setter
    def chances(self, chances):
        if not isinstance(chances,list):
            raise ValueError("Les chances doivent être dans une liste.")
        for chance in chances:
            if not isinstance(chance, int):
                raise ValueError("Une chnace doit être un int.")
        self._chances = chances

    def attaquer(self,p_perso: Personnage):
        """
        Lance une attaque choisit au hasard dans la liste d'attaque
        :return: None
        """
        reussite = random.choices([True,False], weights=[2,1], k=1)
        attaque = random.choices(self.atts,weights=self.chances,k=1)
        degat = attaque.degat_infliger()
        if not p_perso.esquive:
            if reussite:
                print(f"\nLe dragon utilise {attaque.nom} et vous inflige {degat} dégats")
                p_perso.pv -= degat
                time.sleep(0.5)
            else:
                print(f"\nLe dragon tente {attaque.nom}, mais il échoue...")
                time.sleep(0.5)

