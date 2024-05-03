import random

PUZZLE_SIZE = 5


def number_placement_game():
    # random.sample ensures no duplicates.
    puzzle_nums = random.sample(range(100), PUZZLE_SIZE)
    puzzle = []

    for i in range(PUZZLE_SIZE - 1):
        puzzle.append("?")
        puzzle.append(">" if random.random() < .5 else "<")
    puzzle.append("?")

    print("### Number Placement Puzzle ###")
    print("Arrange the puzzle numbers so that the puzzle statement is true.\n")
    print("Puzzle numbers:", *puzzle_nums)  # Nifty unpacking operator
    print("Puzzle statement:", " ".join(puzzle)) # ?<?<?<?

    players_numbers = get_player_input(puzzle_nums)
    number_positions = list(range(0, 2 * PUZZLE_SIZE -1, 2))
    for i in range(PUZZLE_SIZE):
        puzzle[number_positions[i]] = str(players_numbers[i])
    print("You answered:", " ".join(puzzle))

number_placement_game()