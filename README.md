# TicTacToe

A two-player Tic Tac Toe game, built as a small exercise in low-level design (LLD)
and as a shared playground for learning Git/GitHub — Sudhanshu and Manglam each
own their own player logic and collaborate via branches and PRs.

## Design

The game is split into four small pieces, each with a single responsibility:

| File               | Role                                                                 |
|---------------------|-----------------------------------------------------------------------|
| `Player.py`         | Abstract base class. Defines the contract every player must follow: `get_move(board) -> (row, col)`. |
| `CurrentState.py`   | The `CurrentState` class — owns the 3x3 grid and all board rules: validating moves, applying them, checking for a full board, and checking for a winner. |
| `Sudhanshu.py` / `Manglam.py` | Concrete `Player` subclasses, one per contributor. Each owns its symbol (`X` / `O`) and its own `get_move` implementation — this is the placeholder each of you fills in with your own move-picking logic (random, rule-based, minimax, whatever you like). |
| `TicTacToe.py`      | The `Game` class — orchestrates the match: alternates turns, asks the current player for a move, applies it to the board, and checks for a win/draw after every move. Also the entry point (`main()`). |

This mirrors a common LLD pattern: a **board/state** object that knows the rules,
an **abstract player** interface that decouples "who plays" from "how the game runs,"
and a **game/orchestrator** object that wires the two together. It lets each of you
work on your own `get_move` independently without touching shared code.

Right now `Sudhanshu.get_move` and `Manglam.get_move` are stubs that raise
`NotImplementedError` — the game runs and prints the board, but the first move
will raise until a player's logic is implemented.

## Board

`CurrentState.display()` prints the grid as a classic 3x3 tic-tac-toe board,
empty cells shown as spaces:

```
 X | O |  
-----------
   | X |  
-----------
 O |   | X
```

## Running the game

```
python TicTacToe.py
```

## Contributing

- Each player implements their move logic only in their own file (`Sudhanshu.py`
  or `Manglam.py`) — leave `Player.py`, `CurrentState.py`, and `TicTacToe.py` alone
  unless you're changing shared game rules.
- Work on a branch, open a PR, and review each other's changes before merging to `main`.
