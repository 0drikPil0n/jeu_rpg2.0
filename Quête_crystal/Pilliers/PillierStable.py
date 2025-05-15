from Pillier import Pillier

class PillierStable(Pillier):
    def __init__(self, sorte: str, stable: bool):
        super().__init__(sorte="Pillier stable", stable=True)
