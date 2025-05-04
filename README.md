# Tic-Tac-Toe Game (with Timer)

A simple and interactive **Tic-Tac-Toe** game built using **Python** and the **Tkinter** library. This project features a timer for each player, a clear visual representation of the game board, and automatic checks for a winner or tie. The game also prompts players to start a new game after a win, tie, or when the time runs out.

## Features

- **2-player game**: Players alternate between "X" and "O".
- **Timer**: Each player has a limited time to make a move (e.g., 15 seconds).
- **Winner detection**: The game detects and announces the winner or if there's a tie.
- **Restart game**: Players can start a new game after the game is over or the time runs out.
- **UI**: A clean graphical interface built with **Tkinter**.

## Requirements

To run this game, you need Python installed on your system along with the **Tkinter** library, which is included by default with Python.

- **Python 3.x**: Download it from [python.org](https://www.python.org/).
- **Tkinter**: Tkinter is bundled with Python by default, so you don't need to install it separately.

## How to Run

1. **Clone the repository** or **download the files**.

    ```bash
    git clone https://github.com/yourusername/tic-tac-toe.git
    ```

2. **Navigate to the project directory**.

    ```bash
    cd tic-tac-toe
    ```

3. **Run the Python file**.

    ```bash
    python3 main.py
    ```

4. **Play the game**: The game window will appear. Players alternate turns. When the time runs out, the game will ask if they want to play a new game.

## Game Rules

1. The game board consists of a 3x3 grid.
2. Players take turns marking a spot on the grid with either an "X" or an "O".
3. The player who places three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
4. If all spots are filled and no player has won, the game ends in a tie.
5. Each player has a limited amount of time (e.g., 15 seconds) to make their move.
6. Once a player wins or the game ends in a tie, the game will prompt the players to start a new game.

## Game Interface

The game interface includes the following elements:

- **Game Board**: A 3x3 grid of buttons representing the Tic-Tac-Toe board.
- **Status Label**: Displays the current player's turn (Player X or Player O).
- **Timer**: Shows the remaining time for the current player to make a move.
- **New Game Button**: Starts a new game manually at any time.

## Contributing

Feel free to fork the repository and submit a pull request with your changes.

---

Enjoy playing Tic-Tac-Toe! 🎮
