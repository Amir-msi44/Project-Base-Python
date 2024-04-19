import random


class RockPaperScissor():
    """Main class for Rock Paper Scissors game."""
    def __init__(self):
        self.choices = ['ROCK', 'PAPER', 'SCISSORS']

    def get_player_choice(self):
        player_choice = input(f'Please choose between {self.choices}:')
        if player_choice.upper() in self.choices:
            return player_choice.upper()
        print('Not VALID choice! Try Again!')
        return self.get_player_choice()

    def get_computer_choice(self):
        """Get computer choice randomly from choices: Rock, Paper, Scissors"""
        return random.choice(self.choices)

    def decide_winner(self, player_choice: str, computer_choice: str) -> str:
        if player_choice == computer_choice:
            return "It's a TIE!"

        win_combos = [('ROCK' , 'SCISSORS'), ('SCISSORS', 'PAPER'), ('PAPER', 'ROCK')]
        for i in win_combos:
            if (player_choice == i[0]) & (computer_choice == i[1]):
                return "You Won!:))"
        return "You Lost!:(("

    def play(self):
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner = self.decide_winner(player_choice, computer_choice)
        print(f'Computer Choice is {computer_choice}:')
        print(winner)


if __name__ == "__main__":
    game = RockPaperScissor()

    while True:
        game.play()
        continue_game = input('Do you want to continue? (Enter any Key to continue or enter Q/q to quit)')
        if continue_game.lower() == 'q':
            break