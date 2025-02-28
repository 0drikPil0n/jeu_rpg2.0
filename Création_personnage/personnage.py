import jsonpickle
from Création_personnage.race import Race
from Création_personnage.classe import Classe
from Création_personnage.sous_classe import SousClasse
from pathlib import Path

CHEMIN_PERSO = Path("Création_personnage/personnage.json")
class Personnage:
    """
    Un avatar créé par le joueur
    """
    def __init__(self,nom:str, age:int, genre: str,race: Race, classe: Classe, sous_classe: SousClasse):
        self._nom = nom
        self._age = age
        self._genre = genre
        self._race = race
        self._classe = classe
        self._sous_classe = sous_classe

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        if nom is not isinstance(nom, str):
            raise TypeError("Le nom doit être un string")
        self._nom = nom

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age is not isinstance(age, int):
            raise TypeError("Ça prend un int")
        self._age = age

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if genre is not isinstance(genre, str):
            raise TypeError("Cela doit être un str")
        self._genre = genre

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        if race is not isinstance(race, Race):
            raise TypeError("Pas la bonne classe")
        self._race = race

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, classe):
        if classe is not isinstance(classe, Classe):
            raise TypeError("Pas la bonne classe")
        self._classe = classe

    @property
    def sous_classe(self):
        return self._sous_classe

    @sous_classe.setter
    def sous_classe(self, sous_classe):
        if sous_classe is not isinstance(sous_classe, SousClasse):
            raise TypeError("Pas la bonne classe")
        self._sous_classe = sous_classe


    def enregistrer_personnage(self):
        with open(file=CHEMIN_PERSO, mode='r') as fichier_perso:
            liste_personnage = jsonpickle.decode(fichier_perso.read())
        liste_personnage.append(self)
        with open(file=CHEMIN_PERSO, mode="w", encoding="utf-8") as fichier_perso:
            fichier_perso.write(jsonpickle.encode(liste_personnage, indent=4))






