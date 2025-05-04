import tkinter as tk
from tkinter import messagebox


def print_board(board):
    """Print the Tic-Tac-Toe board for debugging purposes."""
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---------")
    print()


def initialize_board():
    """Initialize the board with numbers 1 to 9."""
    return [str(i) for i in range(1, 10)]


def check_win(board, player):
    """Check if the player has won."""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return combo  # Return the winning combination
    return None


def check_tie(board):
    """Check if it's a tie."""
    return all(spot in ["X", "O"] for spot in board)


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#F8F9FA")  # Background color

        # Initialize the game
        self.board = initialize_board()
        self.current_player = "X"

        # Create UI elements
        self.buttons = []
        self.status_label = tk.Label(self.root, text="Player X's Turn", font=("Arial", 16), bg="#F8F9FA")
        self.status_label.grid(row=0, column=0, columnspan=3)

        # Create 9 buttons for the Tic-Tac-Toe grid
        for i in range(9):
            button = tk.Button(self.root, text=str(i + 1), font=("Arial", 20), width=5, height=2,
                               command=lambda i= i: self.player_input(i), relief="solid")
            button.grid(row=(i // 3) + 1, column=i % 3)
            self.buttons.append(button)

        # Create a button for starting a new game
        self.new_game_button = tk.Button(self.root, text="New Game", font=("Arial", 16), command=self.new_game)
        self.new_game_button.grid(row=4, column=0, columnspan=3)

        # Timer setup
        self.time_left = 10
        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.time_left}", font=("Arial", 14), bg="#F8F9FA")
        self.timer_label.grid(row=5, column=0, columnspan=3)
        self.timer_id = None
        self.start_timer()

    def print_board(self):
        """Print the current board state for debugging."""
        print_board(self.board)

    def highlight_winning_line(self, combo):
        """Highlight the winning line."""
        for i in combo:
            self.buttons[i].config(bg="green", fg="white")

    def start_timer(self):
        """Start the timer countdown."""
        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        """Update the timer and check if time runs out."""
        self.timer_label.config(text=f"Time Left: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.timer_up()

    def timer_up(self):
        """Handle when time is up."""
        messagebox.showinfo("Time's up", f"Player {self.current_player}'s time is up!")
        response = messagebox.askyesno("New Game", "Do you want to play a new game?")
        if response:
            self.reset_game()  # Start a new game round
        else:
            self.root.quit()  # Quit the game if no new game

    def stop_timer(self):
        """Stop the timer if needed."""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def switch_player(self):
        """Switch the current player."""
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"Player {self.current_player}'s Turn")
        self.stop_timer()
        self.start_timer()

    def player_input(self, position):
        """Handle player input and update the board."""
        if self.board[position] not in ["X", "O"]:
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            self.buttons[position].config(state="disabled")

            # Check if the current player wins
            winning_combo = check_win(self.board, self.current_player)
            if winning_combo:
                self.print_board()
                self.highlight_winning_line(winning_combo)
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.ask_for_new_game()
                return

            # Check if it's a tie
            if check_tie(self.board):
                self.print_board()
                messagebox.showinfo("Game Over", "It's a tie!")
                self.ask_for_new_game()
                return

            # Switch to the next player
            self.switch_player()

    def reset_game(self):
        """Reset the game for a new round."""
        self.board = initialize_board()
        for button in self.buttons:
            button.config(text="", state="normal", bg="#E9ECEF")
        self.current_player = "X"
        self.status_label.config(text="Player X's Turn")
        self.start_timer()

    def ask_for_new_game(self):
        """Ask the players if they want to play a new game."""
        response = messagebox.askyesno("New Game", "Do you want to play a new game?")
        if response:
            self.reset_game()  # Start a new game round
        else:
            self.root.quit()  # Quit the game if no new game

    def new_game(self):
        """Start a new game manually."""
        self.reset_game()


def main():
    # Set up the main window
    root = tk.Tk()
    app = TicTacToeApp(root)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
