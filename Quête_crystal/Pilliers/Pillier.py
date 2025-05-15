
class Pillier:
    """
    Un pilier de pierre sur lequel un joueur peut marcher.
    """
    def __init__(self, sorte: str, stable: bool = True):
        self._sorte = sorte
        self._stable = stable

    @property
    def sorte(self):
        return self._sorte

    @property
    def stable(self):
        return self._stable

