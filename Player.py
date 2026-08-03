from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board):
        """Return the (row, col) — each in [0, 2] — this player wants to play next."""
        raise NotImplementedError
