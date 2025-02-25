import json
import jsonpickle
from race import Race
from classe import Classe
from sous_classe import SousClasse


class Personnage:
    """
    Un avatar créé par le joueur
    """
    def __init__(self, prenom:str, nom:str, age:int, genre: str,race: Race, classe: Classe, sous_classe: SousClasse):
        self.prenom = prenom
        self._nom = nom
        self._age = age
        self._genre = genre
        self._race = race
        self._classe = classe
        self._sous_classe = sous_classe
        self.nom_complet = prenom + " " + nom

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, prenom):
        self._prenom = prenom

    def enregistrer_personnage(self):
        with open('personnage.json', 'r') as fichier_perso:
            liste_personnage = jsonpickle.decode(fichier_perso.read())
        liste_personnage.append(self)
        with open("personnage.json", "w", encoding="utf-8") as fichier_perso:
            fichier_perso.write(jsonpickle.encode(liste_personnage, indent=4))






