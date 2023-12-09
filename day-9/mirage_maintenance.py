
import numpy as np

def get_sequences(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.rstrip().split() for line in lines]


def calc_next(sequence):
    nums = [int(item) for item in sequence]
    n = len(nums)
    if n < 2:
        return None  # Sequence is too short to predict the next value

    x_values = np.arange(1, n + 1)  # Generate x values from 1 to n

    # Fit a polynomial of degree n-1 to the sequence
    coeffs = np.polyfit(x_values, nums, n - 1)

    # Predict the next value in the sequence
    next_value = np.polyval(coeffs, n + 1)
    return round(next_value)


sequences = get_sequences("test_input.txt")
next_sum = 0
for sequence in sequences:
    print(calc_next(sequence))
    next_sum = next_sum + calc_next(sequence)

print(next_sum)


sequences = get_sequences("puzzle_input.txt")
next_sum = 0
for sequence in sequences:
    print(calc_next(sequence))
    next_sum = next_sum + calc_next(sequence)

print(next_sum)