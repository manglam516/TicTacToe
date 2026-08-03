from Player import Player


class Sudhanshu(Player):
    def __init__(self):
        super().__init__(name="Sudhanshu", symbol="X")

    def get_move(self, board):
        # TODO(Sudhanshu): implement move-picking logic here, return (row, col).
        raise NotImplementedError("Sudhanshu's move logic is not implemented yet")
