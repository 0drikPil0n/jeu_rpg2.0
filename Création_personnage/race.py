class Race:
    """
    La race fantastique d'un personnage (ex: Cyclope, ogre, elf, etc).
    """
    def __init__(self, nom: str, age_min: int, age_max: int):
        """
        Initialise le nom de la race et sa limite d'âge.
        :param nom: Le nom de la race.
        :param age_min: L'âge minimum pour atteindre l'autonomie.
        :param age_max: L'âge maximum qu'une race peut atteindre avant de mourir.
        """
        self.nom = nom
        self.age_min = age_min
        self.age_max = age_max
        self._limite_age = [age_min, age_max]

    @property
    def nom(self) -> str:
        """
        :return: Le nom de la race
        """
        return self._nom

    @nom.setter
    def nom(self, nom: str):
        if not isinstance(nom, str):
            raise TypeError("Le nom de la race doit être de type str")
        self._nom = nom

    @property
    def age_min(self) -> int:
        """
        :return: L'âge minimum de la race
        """
        return self._age_min

    @age_min.setter
    def age_min(self, age_min: int) -> None:
        if age_min < 1:
            raise ValueError("L'âge minimum dois être d'au moins 1 ans")
        self._age_min = age_min

    @property
    def age_max(self) -> int:
        """
        :return: L'âge maximum de la race
        """
        return self._age_max

    @age_max.setter
    def age_max(self, age_max: int) -> None:
        """
        Permet de modifier l'âge maximum d'une race
        :param age_max: L'âge choisis
        :return: None
        """
        if age_max <= self._age_min:
            raise ValueError("L'âge maximum doit être supérieur à l'âge minimum")
        self._age_max = age_max



