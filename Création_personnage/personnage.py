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
        self._prenom = prenom
        self._nom = nom
        self._age = age
        self._genre = genre
        self._race = race
        self._classe = classe
        self._sous_classe = sous_classe
        self.nom_complet = prenom + " " + nom

    @age.setter

    def enregistrer_personnage(self):
        with open('personnage.json', 'r') as fichier_perso:
            liste_personnage = jsonpickle.decode(fichier_perso.read())
        liste_personnage.append(self)
        with open("personnage.json", "w", encoding="utf-8") as fichier_perso:
            fichier_perso.write(jsonpickle.encode(liste_personnage, indent=4))


nain = Race(nom="nain", age_min=12, age_max=250)

mage = SousClasse(nom="Mage", arme="Baguette magique", pv=200, degats=[100,110],atts_spe=[150])
sorcier = SousClasse(nom="Sorcier", arme="Livre de sorts", pv=180, degats=[120,125],atts_spe=[135])
druide = SousClasse(nom="Druide", arme="Potions", pv=150, degats=[150],atts_spe=[200,50])
shaman = SousClasse(nom="Shaman", arme="Invocation d'esprit", pv=200, degats=[110,135],atts_spe=[145])

magicien = Classe("Magicien",[mage, sorcier, druide, shaman])

perso = Personnage("Arnold Astérix", 34, "Homme", race=nain, classe=magicien, sous_classe=druide)
perso.enregistrer_personnage()




