

class Attaque:
    def __init__(self, nom:str, degats:list[int],chances:list[int]):
        self.nom = nom
        self.degats = degats
        self.chances = chances

    @property
    def nom(self):
        return self.nom

    @nom.setter
    def nom(self, nom):
        if nom is not isinstance(nom, str):
            raise TypeError("Le nom de l'attaque doit être une string")
        self._nom = nom

    @property
    def degats(self):
        return self.degats

    @degats.setter
    def degats(self, degats):
        if degats is not isinstance(degats,list):
            raise TypeError("Les dégats de cette attaque doivent être dans une liste")
        for degat in degats:
            if degat is not isinstance(degat, int):
                raise TypeError("Un dégat doit être un nombre entier")
        self._degats = degats

    @property
    def chances(self):
        return self.chances

    @chances.setter
    def chances(self,chances):
        if chances is not isinstance(chances, list):
            raise TypeError("Les chances relatives au dégats doivvent être dans une liste")
        for chance in chances:
            if chance is not isinstance(chance, int):
                raise TypeError("Une chance doit être un nombre entier")
        if chances != self._degats:
            raise ValueError("Il doit y avoir une chance pour chaque dégats")
        self._chances = chances