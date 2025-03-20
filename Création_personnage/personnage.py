from Création_personnage.race import Race
from Création_personnage.classe import Classe
from Création_personnage.sous_classe import SousClasse
from Générale.Attaque import Attaque

import jsonpickle
from pathlib import Path
import random
import time




class Personnage:
    """
    Un avatar créé par le joueur
    """
    CHEMIN_PERSO = Path("Création_personnage/personnage.json")

    def __init__(self, nom: str, age: int, genre: str, race: Race, classe: Classe, sous_classe: SousClasse):
        self.nom = nom
        self.age = age
        self.genre = genre
        self.race = race
        self.classe = classe
        self.sous_classe = sous_classe
        self.esquive = False
        self.pv = sous_classe.pv
        self.attaque = sous_classe.attaque
        self.attaque_speciale = sous_classe.attaque_speciale
        self.arme = sous_classe.arme
        self.tour_avant_recharge: int = 0

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être une string")
        self._nom = nom

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError("Ça prend un int")
        self._age = age

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if not isinstance(genre, str):
            raise TypeError("Cela doit être un str")
        self._genre = genre

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        if not isinstance(race, Race):
            raise TypeError("Pas la bonne classe")
        self._race = race

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, classe):
        if not isinstance(classe, Classe):
            raise TypeError("Pas la bonne classe")
        self._classe = classe

    @property
    def sous_classe(self):
        return self._sous_classe

    @sous_classe.setter
    def sous_classe(self, sous_classe):
        if not isinstance(sous_classe, SousClasse):
            raise TypeError("Pas la bonne classe")
        self._sous_classe = sous_classe

    @property
    def esquive(self):
        return self._esquive

    @esquive.setter
    def esquive(self, esquive):
        if not isinstance(esquive, bool):
            raise TypeError("L'esquive doit être sois True ou False")
        self._esquive = esquive

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, pv):
        self._pv = pv

    @property
    def attaque(self):
        return self._attaque

    @attaque.setter
    def attaque(self, attaque):
        if not isinstance(attaque, Attaque):
            raise TypeError("Une attaque doit être de la classe 'Attaque'.")
        self._attaque = attaque

    @property
    def attaque_speciale(self):
        return self._attaque_speciale

    @attaque_speciale.setter
    def attaque_speciale(self, attaque_speciale):
        if not isinstance(attaque_speciale, Attaque):
            raise TypeError("Une attaque doit être de la classe 'Attaque'.")
        self._attaque_speciale = attaque_speciale

    @property
    def arme(self):
        return self._arme

    @arme.setter
    def arme(self, arme):
        if not isinstance(arme, str):
            raise TypeError("L'arme doit être une string.")
        self._arme = arme

    @property
    def tour_avant_recharge(self):
        return self._tour_avant_recharge

    @tour_avant_recharge.setter
    def tour_avant_recharge(self, tour_avant_recharge):
        if not isinstance(tour_avant_recharge, int):
            raise TypeError("Le nombre de tour avant la recharge doit être un int.")
        self._tour_avant_recharge = tour_avant_recharge


    def enregistrer_personnage(self):
        with open(file=Personnage.CHEMIN_PERSO, mode='r') as fichier_perso:
            liste_personnage = jsonpickle.decode(fichier_perso.read())
        liste_personnage.append(self)
        with open(file=Personnage.CHEMIN_PERSO, mode="w", encoding="utf-8") as fichier_perso:
            fichier_perso.write(jsonpickle.encode(liste_personnage, indent=4))

    def attaquer(self, ennemi, choix):
        if self.tour_avant_recharge > 0:
            self.tour_avant_recharge -= 1
        match choix:
            case "1":
                p_attaque: int = self.attaque.degat_infliger()
                print(f"Vous utiliser {self.attaque.nom} et infligé {p_attaque} dégats.")
                ennemi.pv -= p_attaque
            case "2":
                if self.tour_avant_recharge > 0:
                    print(f"\nVous devez attendre {self.tour_avant_recharge} tour pour recharger cette attaque...")
                    time.sleep(0.5)
                else:
                    p_attaque: int = self.attaque_speciale.degat_infliger()
                    print(f"\nVous utiliser {self.attaque.nom} et infligé {p_attaque} dégats.")
                    time.sleep(0.5)
                    ennemi.pv -= p_attaque
                    self.tour_avant_recharge += 3


    def esquiver(self):
        """
        Permet au joueur d'esquiver la prochaine attaque. A une chance d'échouer.
        :return: True s'il esquive, False sinon.
        """
        chance = [4, 1]
        esquive = random.choices([True, False], chance, k=1)
        esquive = esquive[0]
        if esquive is True:
            self.esquive = True
            print("\nVous esquiver la prochaine attaque!")
            time.sleep(0.5)
        else:
            self.esquive = False
            print("\nVous n'avez pas réussis à esquiver l'attaque...")
            time.sleep(0.5)
