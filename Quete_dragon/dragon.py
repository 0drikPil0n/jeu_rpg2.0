from Générale import Ennemi, Attaque


class Dragon(Ennemi):
    def __init__(self, nom: str, pv: int, atts: list[Attaque], chances: list[int]):
        super().__init__(nom, pv, atts, chances)


