from Player import Player


class Manglam(Player):
    def __init__(self):
        super().__init__(name="Manglam", symbol="O")

    def get_move(self, board):
        # TODO(Manglam): implement move-picking logic here, return (row, col).
        raise NotImplementedError("Manglam's move logic is not implemented yet")
