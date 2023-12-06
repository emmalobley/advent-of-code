from collections import deque

def get_time(filename):
    with open(filename, "r") as file:
        times = file.readlines()[0].split(": ")[1].rstrip('\n').split()
    return [int(t) for t in times]

def get_win_distance(filename):
    with open(filename, "r") as file:
        distance = file.readlines()[1].split(": ")[1].rstrip('\n').split()
    return [int(d) for d in distance]

def get_time_held(time):
    return list(range(1, time))
def player_distance(time):
    play_dist = []
    held = deque(get_time_held(time))
    while 0 < len(held):
        new = 0
        if len(held) == 1:
            new = held.pop()
            play_dist.append(new*new)
        else:
            new = held.pop()*held.popleft()
            play_dist.append(new)
            play_dist.append(new)
    return play_dist

def get_scorebreakers(play_dist, max_dist):
    return [p for p in play_dist if p > max_dist]

def get_sum(filename):
    num = 1
    for index, time in enumerate(get_time(filename)):
        max_dist = get_win_distance(filename)[index]
        num = num * len(get_scorebreakers(player_distance(time), max_dist))

    return num


print(get_sum("test_input.txt"))
print(get_sum("puzzle_input.txt"))

# part 2

def new_time(filename):
    with open(filename, "r") as file:
        times = file.readlines()[0].split(": ")[1].rstrip('\n').split()
    return int("".join(times))


def new_win_distance(filename):
    with open(filename, "r") as file:
        distance = file.readlines()[1].split(": ")[1].rstrip('\n').split()
    return int("".join(distance))


def get_new_sum(filename):
    max_dist = new_win_distance(filename)
    return len(get_scorebreakers(player_distance(new_time(filename)), max_dist))

print(get_new_sum("test_input.txt"))
print(get_new_sum("puzzle_input.txt"))