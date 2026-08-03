class CurrentState:
    SIZE = 3

    def __init__(self):
        self.grid = [["" for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def display(self):
        rows = []
        for row in self.grid:
            cells = [cell if cell else " " for cell in row]
            rows.append(" " + " | ".join(cells) + " ")
        separator = "\n" + "-" * (4 * self.SIZE - 1) + "\n"
        print(separator.join(rows))

    def is_valid_move(self, row, col):
        return 0 <= row < self.SIZE and 0 <= col < self.SIZE and self.grid[row][col] == ""

    def apply_move(self, row, col, symbol):
        if not self.is_valid_move(row, col):
            raise ValueError(f"Invalid move: ({row}, {col})")
        self.grid[row][col] = symbol

    def is_full(self):
        return all(cell != "" for row in self.grid for cell in row)

    def get_winner(self):
        lines = list(self.grid)
        lines.extend([[self.grid[r][c] for r in range(self.SIZE)] for c in range(self.SIZE)])
        lines.append([self.grid[i][i] for i in range(self.SIZE)])
        lines.append([self.grid[i][self.SIZE - 1 - i] for i in range(self.SIZE)])

        for line in lines:
            if line[0] != "" and all(cell == line[0] for cell in line):
                return line[0]
        return None
