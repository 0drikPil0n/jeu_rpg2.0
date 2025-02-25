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
        self.nom = nom
        self.sous_classes = sous_classes

    @property
    def nom(self):
        return self.nom

    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("Le nom de la classe doit être de type str")
        self._nom = nom

    @property
    def sous_classes(self):
        return self.sous_classes

    @sous_classes.setter
    def sous_classes(self, sous_classes):
        if not isinstance(sous_classes, list):
            raise TypeError("Les sous-classes doivent être dans une liste (list[SousClasse])")
        self._sous_classes = sous_classes

