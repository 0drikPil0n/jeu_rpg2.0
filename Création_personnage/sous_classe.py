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
        self._nom = nom
        self._arme = arme
        self._pv = None
        self.set_pv(pv)
        self._degats = None
        self.set_degats(degats)
        self._atts_spe = None
        self.set_atts_spe(atts_spe)

    def get_pv(self):
        return self._pv

    def set_pv(self, pv: int):
        if pv < 1:
            raise ValueError("Les points de vie doivent être au moins de 1")
        self._pv = pv

    def get_degats(self):
        return self._degats

    def set_degats(self, degats):
        for degat in degats:
            if degat < 0:
                raise ValueError("Un dégat doit être au minimum de 1")
        self._degats = degats

    def get_att_spe(self):
        return self._atts_spe

    def set_atts_spe(self, atts_spe):
        for att_spe in atts_spe:
            if att_spe < 0:
                raise ValueError("Une attaque spéciale doit être au minimum de 1")
        self._atts_spe = atts_spe
