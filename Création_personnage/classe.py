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
        self._sous_classes = None

    def get_sous_classes(self):
        return self._sous_classes

    def set_sous_classes(self, sous_classes):
        self._sous_classes = sous_classes
