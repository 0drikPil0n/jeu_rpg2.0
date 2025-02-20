from Création_personnage.race import Race
from Création_personnage.classe import Classe
from Création_personnage.sous_classe import SousClasse


class Personnage:
    """
    Un avatar créé par le joueur
    """
    def __init__(self, nom:str, age:int, genre: str,race: Race, classe: Classe, sous_classe: SousClasse):
        self._nom = nom
        self._age = age
        self._genre = genre
        self._race = race
        self._classe = classe
        self._sous_classe = sous_classe


    def enregistrer_personnage(self):
        """
        Enregistre le personnage dans le fichier de sauvegarde
        :return:
        """
        with open