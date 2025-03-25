
class Pillier:
    """
    Un pilier de pierre sur lequel un joueur peut marcher.
    """
    def __init__(self, sorte: str, stable: bool = True):
        self.sorte = sorte
        self.stable = stable

