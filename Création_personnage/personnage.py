from Création_personnage.race import Race
from Création_personnage.classe import Classe
from Création_personnage.sous_classe import SousClasse

import jsonpickle
from pathlib import Path
import random
import time

CHEMIN_PERSO = Path("Création_personnage/personnage.json")

class Personnage:
    """
    Un avatar créé par le joueur
    """

    def __init__(self, nom: str, age: int, genre: str, race: Race, classe: Classe, sous_classe: SousClasse,
                 esquive: bool = False):
        self.nom = nom
        self.age = age
        self.genre = genre
        self.race = race
        self.classe = classe
        self.sous_classe = sous_classe
        self.esquive = esquive
        self.pv = sous_classe.pv
        self.degats = sous_classe.degats
        self.atts_spe = sous_classe.atts_spe
        self.arme = sous_classe.arme

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

    def enregistrer_personnage(self):
        with open(file=CHEMIN_PERSO, mode='r') as fichier_perso:
            liste_personnage = jsonpickle.decode(fichier_perso.read())
        liste_personnage.append(self)
        with open(file=CHEMIN_PERSO, mode="w", encoding="utf-8") as fichier_perso:
            fichier_perso.write(jsonpickle.encode(liste_personnage, indent=4))

    def attaquer(self, ennemi, choix):
        match choix:
            case "1":
                attaque = random.choice(self.degats)
                print(f"Vous utiliser {}")
                ennemi.pv -=
            case "2":
                attaque = random.choice(self.atts_spe)


    def esquiver(self):
        """
        Permet au joueur d'esquiver la prochaine attaque. A une chance d'échouer.
        :return: True s'il esquive, False sinon.
        """
        chance = [5,1]
        esquive = random.choices([True,False],chance)
        if esquive:
            self.esquive = True
            print("\nVous esquiver la prochaine attaque!")
            time.sleep(0.5)
        else:
            print("\nVous n'avez pas réussis à esquiver l'attaque...")
            time.sleep(0.5)

