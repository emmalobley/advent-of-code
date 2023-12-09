from collections import Counter

card_rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def file_to_dict(filename):
    play_dict = {}
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            new_line = line.rstrip('\n').split(" ")
            play_dict[new_line[0]] = new_line[1]
    return play_dict

print(file_to_dict("test_input.txt"))
