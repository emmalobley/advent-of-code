import time
from itertools import islice


def get_seeds(filename):
    with open(filename, "r") as file:
        seeds = file.readlines()[0].split(": ")[1].rstrip('\n').split(" ")
    return [int(seed.strip()) for seed in seeds]


def get_new_seeds(start, count):
    return list(range(start, start + count))


def get_lines(filename, start, end):
    new_lines = []
    with open(filename, 'r') as file:
        lines = islice(file, start, end)
        lines = map(lambda s: s.strip(), lines)
        for line in lines:
            new_lines.append(line.split(" "))

    return new_lines


def get_map(lines, old):
    new = []
    for object in old:
        i = 0
        for line in lines:
            if int(line[1]) <= object < (int(line[1]) + int(line[2])):
                new_item = object - int(line[1]) + int(line[0])
                new.append(new_item)
                i += 1
                break
        if i == 0:
            new.append(object)
    return new


def get_min_loc(filename, file_lines, new_seeds):
    next = new_seeds
    for i in range(0, len(file_lines), 2):
        next = get_map(get_lines(filename, file_lines[i], file_lines[i+1]), next)
    return min(next)


def main(filename, file_lines):
    seeds = get_seeds(filename)
    ans = []
    # only pass first two args to func at time
    for i in range(0, len(seeds), 2):
        new_seeds = get_new_seeds(seeds[i], seeds[i + 1])
        ans.append(get_min_loc(filename, file_lines, new_seeds))

    return min(ans)


begin = time.time()
print(main("test_input.txt", [3, 5, 7, 10, 12, 16, 18, 20, 22, 25, 27, 29, 31, 33]))
print(time.time() - begin)


# print(main("puzzle_input.txt", [3, 36, 38, 62, 64, 86, 88, 107, 109, 120, 122, 131, 133, 165]))
