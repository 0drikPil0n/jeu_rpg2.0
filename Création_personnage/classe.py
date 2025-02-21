from Création_personnage.sous_classe import SousClasse


class Classe:
    """
    Catégorie de combattant (ex: Royauté, Magicien)
    """

    def __init__(self, nom: str, sous_classes: list[SousClasse]):
        """
        Initialize le nom ainsi que les sous-classes d'une classe
        :param nom: Le nom de la classe
        :param sous_classes: Les sous-classes
        """
        self._nom = nom
        self._sous_classes = sous_classes

    @property
    def nom(self):
        return self._nom

    @property
    def sous_classes(self):
        return self._sous_classes

