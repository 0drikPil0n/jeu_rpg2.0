from Générale import Ennemi, Attaque


class Dragon(Ennemi):
    # Attaque du dragon
    coup_queue = Attaque(nom="Coup de queue", degats=[50, 55], chances=[2, 1])
    lance_flamme = Attaque(nom="Lance flamme", degats=[75, 80], chances=[2, 1])
    coup_griffe = Attaque(nom="Coup de griffe", degats=[30, 35], chances=[2, 1])

    def __init__(self, nom: str, pv: int):
        self.atts = [Dragon.coup_queue, Dragon.lance_flamme, Dragon.coup_griffe]
        self.chances = [4,2,3]
        super().__init__(nom, pv, self.atts, self.chances)
