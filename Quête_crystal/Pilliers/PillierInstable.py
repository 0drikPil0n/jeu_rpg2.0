from Pillier import Pillier

class PillierInstable(Pillier):
    def __init__(self, sorte: str, stable: bool):
        super().__init__(sorte="Pillier instable", stable=False)
