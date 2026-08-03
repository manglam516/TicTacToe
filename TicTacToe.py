from CurrentState import CurrentState
from Manglam import Manglam
from Sudhanshu import Sudhanshu


class Game:
    def __init__(self, players):
        self.board = CurrentState()
        self.players = players

    def play(self):
        self.board.display()
        while True:
            for player in self.players:
                row, col = player.get_move(self.board)
                self.board.apply_move(row, col, player.symbol)
                self.board.display()

                winner = self.board.get_winner()
                if winner:
                    print(f"{player.name} ({winner}) wins!")
                    return

                if self.board.is_full():
                    print("It's a draw!")
                    return


def main():
    print("TicTacToe Game : (Sudhanshu vs Manglam)")
    game = Game([Sudhanshu(), Manglam()])
    game.play()


if __name__ == "__main__":
    main()
