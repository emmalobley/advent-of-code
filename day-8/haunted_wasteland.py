from itertools import islice
from collections import deque
from math import gcd

# Function to find LCM
def lcm(a, b):
    return a * b // gcd(a, b)

def file_to_dict(filename, last):
    moves_dict = {}
    with open(filename, "r") as file:
        lines = islice(file, 2, last)
        lines = map(lambda s: s.strip(), lines)
        for line in lines:
            new_line = line.split(" = ")
            moves_dict[new_line[0]] = new_line[1]
    return moves_dict

def get_moves(filename):
    with open(filename, "r") as file:
        first_line = file.readline().strip()
    return deque([item for item in first_line])


def get_steps(filename, moves_dict, moves):
    position = "AAA"
    steps = 0
    while position != "ZZZ":
        steps += 1
        if len(moves) == 0:
            moves = get_moves(filename)
        next_move = moves.popleft()
        if next_move == "L":
            position = moves_dict[position].split(", ")[0].strip("(")
        elif next_move == "R":
            position = moves_dict[position].split(", ")[1].strip(")")
    return steps

moves_dict = file_to_dict("test_input.txt", 9)
moves = get_moves("test_input.txt")
print(get_steps("test_input.txt", moves_dict, moves))

moves_dict = file_to_dict("puzzle_input.txt", 704)
moves = get_moves("puzzle_input.txt")
print(get_steps("puzzle_input.txt", moves_dict, moves))

## part 2

def get_start_a(moves_dict):
    start = []
    for key, item in moves_dict.items():
        if key[-1] == "A":
            start.append(key)
    return start

def get_steps(filename, start, moves_dict, moves):
    steps_count = []
    for item in start:
        position = item
        steps = 0
        while position[-1] != "Z":
            steps += 1
            if len(moves) == 0:
                moves = get_moves(filename)
            next_move = moves.popleft()
            if next_move == "L":
                position = moves_dict[position].split(", ")[0].strip("(")
            elif next_move == "R":
                position = moves_dict[position].split(", ")[1].strip(")")
        steps_count.append(steps)

    numbers = steps_count

    # Calculate LCM iteratively
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])

    return result


moves_dict = file_to_dict("test_part2.txt", 9)
moves = get_moves("test_part2.txt")
print(get_steps("test_part2.txt", get_start_a(moves_dict), moves_dict, moves))

moves_dict = file_to_dict("puzzle_input.txt", 704)
moves = get_moves("puzzle_input.txt")
print(get_steps("puzzle_input.txt", get_start_a(moves_dict), moves_dict, moves))






