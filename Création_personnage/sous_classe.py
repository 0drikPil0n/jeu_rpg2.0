from Générale.Attaque import Attaque

class SousClasse:
    """
    Une sous-catégorie de classe procurant au joueur ses statistiques
    """
    def __init__(self, nom: str, arme: str, pv: int, attaque: Attaque, attaque_speciale: Attaque):
        """
        Initialize le nom de la classe et les autres paramètres
        :param nom: Le nom de la sous-classe
        :param arme: L'arme utilisée par cette sous-classe
        :param pv: Les points de vie de cette sous-classe
        :param attaque: L'attaque de base de cette sous-classe
        :param attaque_speciale: L'attaque spéciale de cette sous-classe
        """
        self.nom = nom
        self.arme = arme
        self.pv = pv
        self.attaque = attaque
        self.attaque_speciale = attaque_speciale

    @property # Nom
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("Le nom de la sous-classe doit être de type str")
        self._nom = nom

    @property # Arme
    def arme(self):
        return self._arme

    @arme.setter
    def arme(self, arme):
        if not isinstance(arme, str):
            raise TypeError("L'arme doit être de type str")
        self._arme = arme

    @property # Point de vie
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, pv: int):
        if pv < 1:
            raise ValueError("Les points de vie doivent être au moins de 1")
        self._pv = pv

    @property # Dégats
    def attaque(self):
        return self._attaque

    @attaque.setter
    def attaque(self, attaque):
        for degat in attaque:
            if degat <= 0:
                raise ValueError("Un dégat doit être au minimum de 1")
        self._attaque = attaque

    @property # Attaques spéciales
    def attaque_speciale(self):
        return self._attaque_speciale

    @attaque_speciale.setter
    def attaque_speciale(self, attaque_speciale):
        for degat in attaque_speciale:
            if degat <= 0:
                raise ValueError("Une attaque spéciale doit être au minimum de 1")
        self._attaque_speciale = attaque_speciale
