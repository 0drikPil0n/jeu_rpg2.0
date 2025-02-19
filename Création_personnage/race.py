class Race:
    def __init__(self, race: str, age_min: int, age_max: int):
        """
        La race fantastique d'un personnage (ex: Cyclope, ogre, elf, etc).
        :param race: Le nom de la race.
        :param age_min: L'âge minimum pour atteindre l'autonomie.
        :param age_max: L'âge maximum qu'une race peut atteindre avant de mourir.
        """
        self._race = None
        self.set_race(race)
        self._age_min = None
        self.set_age_min(age_min)
        self._age_max = None
        self.set_age_max(age_max)
        self.limite_age = [age_min, age_max]
    # get/set nom de la race
    def get_race(self) -> str:
        """
        :return: Le nom de la race
        """
        return self._race

    def set_race(self, race: str) -> None:
        """
        Permet de modifier le nom de la race
        :param race: Le nom de la race
        :return: None
        """
        self._race = race

    # get/set âge minimum
    def get_age_min(self) -> int:
        """
        :return: L'âge minimum de la race
        """
        return self._age_min

    def set_age_min(self, age_min: int) -> None:
        """
        Permet de modifier l'âge minimum d'une race
        :param age_min: L'âge choisis
        :return: None
        """
        if age_min < 1:
            raise ValueError("L'âge minimum dois être d'au moins 1 ans")
        self._age_min = age_min

    # get/set âge maximum
    def get_age_max(self) -> int:
        """
        :return: L'âge maximum de la race
        """

    def set_age_max(self, age_max: int) -> None:
        """
        Permet de modifier l'âge maximum d'une race
        :param age_max: L'âge choisis
        :return: None
        """
        if age_max <= self._age_min:
            raise ValueError("L'âge maximum doit être supérieur à l'âge minimum")
        self._age_max = age_max



