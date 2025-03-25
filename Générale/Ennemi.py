from . import Attaque
from Création_personnage import Personnage

import random
import time


class Ennemi:
    def __init__(self, nom: str, pv: int, atts: list[Attaque], chances: list[int]):
        self.nom = nom
        self.pv = pv
        self.atts = atts
        self.chances = chances
        self.attaque_reussite = True
        if pv <= 0:
            raise TypeError("Les points de vie doivent être un nombre entier plus grand que 0")

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise ValueError("Le nom doit être un str")
        self._nom = nom

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, pv):
        if not isinstance(pv, int):
            raise TypeError("Les points de vie doivent être un nombre entier")
        self._pv = pv

    @property
    def atts(self):
        return self._atts

    @atts.setter
    def atts(self, atts):
        if not isinstance(atts, list):
            raise ValueError("Les attaques doivent être dans une liste")
        self._atts = atts

    @property
    def chances(self):
        return self._chances

    @chances.setter
    def chances(self, chances):
        if not isinstance(chances, list):
            raise ValueError("Les chances doivent être dans une liste.")
        for chance in chances:
            if not isinstance(chance, int):
                raise ValueError("Une chnace doit être un int.")
        self._chances = chances

    @property
    def attaque_reussite(self):
        return self._attaque_reussite

    @attaque_reussite.setter
    def attaque_reussite(self, attaque_reussite):
        if not isinstance(attaque_reussite, bool):
            raise TypeError("L'attaque peut sois réusir, sois ne pas réussir (bool).")
        self._attaque_reussite = attaque_reussite


    def reussite_attaque(self):
        """
        Définis si l'attaque réussie ou non.
        :return: True si elle réussit, False sinon.
        """
        reussite = random.choices([True, False], weights=[1, 2], k=1)
        self.attaque_reussite = reussite[0]

    def attaque_choisis(self):
        """
        Choisis une attaque au hasard que l'ennemi va effectuer
        :return: L'attaque choisie
        """
        attaque = random.choices(self.atts, weights=self.chances, k=1)
        return attaque[0]

    def attaquer(self, p_perso: Personnage):
        """
        Lance une attaque choisit au hasard dans la liste d'attaque
        :return: None
        """

        attaque = self.attaque_choisis()
        degats = attaque.degat_infliger()
        if not p_perso.esquive:
            if self.attaque_reussite:
                print(f"\n{self.nom} utilise {attaque.nom} et vous inflige {degats} dégats")
                p_perso.pv -= degats
                time.sleep(0.5)
            else:
                print(f"\n{self.nom} tente {attaque.nom}, mais il échoue...")
                time.sleep(0.5)
        else:
            print(f"\n{self.nom} utilise {attaque.nom}, mais il vous a manqué...")
            time.sleep(0.5)
