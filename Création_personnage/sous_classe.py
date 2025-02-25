class SousClasse:
    """
    Une sous-catégorie de classe procurant au joueur ses statistiques
    """
    def __init__(self, nom: str, arme: str, pv: int, degats: list[int], atts_spe: list[int]):
        """
        Initialize le nom de la classe et les autres paramètres
        :param nom: Le nom de la sous-classe
        :param arme: L'arme utilisée par cette sous-classe
        :param pv: Les points de vie de cette sous-classe
        :param degats: Les dégats que cette sous-classe peut infligé
        :param atts_spe: Les attaques spéciales de cette sous-classe
        """
        self.nom = nom
        self.arme = arme
        self.pv = pv
        self.degats = degats
        self.atts_spe = atts_spe

    @property # Nom
    def nom(self):
        return self.nom

    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("Le nom de la sous-classe doit être de type str")
        self._nom = nom

    @property # Arme
    def arme(self):
        return self.arme

    @arme.setter
    def arme(self, arme):
        if not isinstance(arme, str):
            raise TypeError("L'arme doit être de type str")
        self._arme = arme

    @property # Point de vie
    def pv(self):
        return self.pv

    @pv.setter
    def pv(self, pv: int):
        if pv < 1:
            raise ValueError("Les points de vie doivent être au moins de 1")
        self._pv = pv

    @property # Dégats
    def degats(self):
        return self.degats

    @degats.setter
    def degats(self, degats):
        for degat in degats:
            if degat < 0:
                raise ValueError("Un dégat doit être au minimum de 1")
        self._degats = degats

    @property # Attaques spéciales
    def atts_spe(self):
        return self._atts_spe

    @atts_spe.setter
    def atts_spe(self, atts_spe):
        for att_spe in atts_spe:
            if att_spe < 0:
                raise ValueError("Une attaque spéciale doit être au minimum de 1")
        self._atts_spe = atts_spe
