def convert_digits(line):
    # credit to Laura for the keeping edge letters - i couldn't crack it :(
    # come back and figure out another way!!!
    number_dict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for x in number_dict:
        if x in line:
            line = line.replace(x, number_dict[x])
    return line


def convert_file(filename):
    with open(filename, "r") as file:
        data = file.readlines()

    data = [convert_digits(line) for line in data]

    with open(filename, "w") as file:
        file.writelines(data)

    return

def get_digits(input):
    num = ""
    for i in input:
        if i.isdigit():
            num = num + i
    return int(num[0] + num[-1])

def sum_from_file(filename):
    f = open(filename, "r")
    sum = 0
    for line in f.readlines():
        sum = sum + get_digits(line)
    f.close()
    return sum

def main():
    convert_file("puzzle_input.txt")
    print(sum_from_file("puzzle_input.txt"))


if __name__ == "__main__":
    main()

