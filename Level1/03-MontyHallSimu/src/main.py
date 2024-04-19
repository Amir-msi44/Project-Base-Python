import random

def monty_hall(switch_doors):
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    if switch_doors:
        doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        door_revealed = random.choice(doors_revealed)
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'

def simulate_game(num_games):
    num_wins_with_switching = sum([monty_hall(True) for _ in range(num_games)])
    num_wins_without_switching = sum([monty_hall(False) for _ in range(num_games)])
    return num_wins_without_switching, num_wins_with_switching


if __name__ == '__main__':
    print(simulate_game(10000))