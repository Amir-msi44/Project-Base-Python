import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10  # Initialize the board with empty spaces.
        self.player_turn = 'X'  # Start with player X.

    def show_board(self):
        """Displays the current state of the board."""
        print('\n')
        print(self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('---------')
        print(self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('---------')
        print(self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('\n')

    def swap_player_turn(self):
        """Switches the player turn."""
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'

    def is_board_filled(self):
        """Checks if the board is full."""
        return ' ' not in self.board[1:]

    def fix_spot(self, cell, player):
        """Places a player's mark on the board."""
        self.board[cell] = player

    def is_valid_move(self, cell):
        """Checks if a move is valid (spot is free and within the board)."""
        return self.board[cell] == ' ' and 1 <= cell <= 9

    def win(self, player):
        """Checks if the given player has won."""
        win_combos = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        for combo in win_combos:
            if all(self.board[cell] == player for cell in combo):
                return True
        return False

    def player_input(self):
        """Manages the player's input, ensuring it is valid."""
        while True:
            try:
                position = int(input(f"Player {self.player_turn}, enter the position (1-9): "))
                if self.is_valid_move(position):
                    return position
                else:
                    print("This position is already taken or out of range. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def computer_move(self):
        """Determines and executes the computer's move based on a basic strategy."""
        # Placeholder for the strategy implementation
        # Check for a winning move first
        for i in range(1, 10):
            if self.is_valid_move(i):
                self.board[i] = 'O'
                if self.win('O'):
                    return
                else:
                    self.board[i] = ' '

        # Block player's winning move
        for i in range(1, 10):
            if self.is_valid_move(i):
                self.board[i] = 'X'
                if self.win('X'):
                    self.board[i] = 'O'
                    return
                else:
                    self.board[i] = ' '

        # Take the center if available
        if self.is_valid_move(5):
            self.board[5] = 'O'
            return

        # Take any corner if available
        for i in [1, 3, 7, 9]:
            if self.is_valid_move(i):
                self.board[i] = 'O'
                return

        # Take any side
        for i in [2, 4, 6, 8]:
            if self.is_valid_move(i):
                self.board[i] = 'O'
                return

    def play_game(self, against_ai=False):
        """The main game loop, with an option to play against AI."""
        while True:
            self.show_board()
            if self.player_turn == 'X' or not against_ai:
                position = self.player_input()
                self.fix_spot(position, self.player_turn)
            else:
                print("Computer's turn:")
                self.computer_move()

            if self.win(self.player_turn):
                self.show_board()
                winner = "Computer" if against_ai and self.player_turn == 'O' else f'Player {self.player_turn}'
                print(f'{winner} wins!')
                break
            if self.is_board_filled():
                print('Draw! Game ends.')
                break
            self.swap_player_turn()

        # Ask if players want to play again
        self.ask_replay(against_ai)

    def ask_replay(self, against_ai):
        """Asks the players if they want to play again."""
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            self.__init__()  # Reset the game
            self.play_game(against_ai)

if __name__ == "__main__":
    game = TicTacToe()
    against_ai = input("Do you want to play against the computer? (yes/no): ").lower() == 'yes'
    game.play_game(against_ai)
