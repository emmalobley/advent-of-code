
import numpy as np

def get_sequences(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    sequences = []
    for line in lines:
        new_line = []
        for item in line.rstrip().split():
            new_line.append(int(item))
        sequences.append(new_line)
    return sequences

def next_sequence(line):
    new_sequence = []
    for i in range(len(line)-1):
        new_sequence.append(int(line[i+1]) - int(line[i]))
    return new_sequence

def get_next_item(line):
    matrix = []
    matrix.append(line)
    while set(next_sequence(line)) != {0}:
        line = next_sequence(line)
        matrix.append(line)
    new_num = 0
    for line in matrix[::-1]:
        line.append(line[-1] + new_num)
        new_num = line[-1]
    # print(matrix)
    return matrix[0][-1]


sequences = get_sequences("test_input.txt")
sum = 0
for line in sequences:
    sum = sum + get_next_item(line)

print(sum)

# part 2
from collections import deque

def get_prev_item(line):
    matrix = []
    matrix.append(line)
    while set(next_sequence(line)) != {0}:
        line = next_sequence(line)
        matrix.append(line)
    new_num = 0
    for line in matrix[::-1]:
        line = deque(line)
        line.appendleft(line[0] - new_num)
        line = list(line)
        new_num = line[0]
    return new_num


sequences = get_sequences("puzzle_input.txt")
sum = 0
for line in sequences:
    sum = sum + get_prev_item(line)

print(sum)