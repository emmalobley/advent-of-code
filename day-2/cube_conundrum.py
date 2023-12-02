def file_to_list(filename):
    with open(filename, "r") as file:
        games = file.readlines()
    return games

def get_games_dict(filename):
    games = file_to_list(filename)
    games_dict = {}
    for line in games:
        play = line.split(": ")[1].rstrip('\n').split("; ")
        # print(play)

        draw_dict = {}
        for draw in play:
            for item in draw.split(", "):
                colour = item.split(" ")[1]
                num = int(item.split(" ")[0])
                if colour not in draw_dict or draw_dict[colour] < num:
                    draw_dict[colour] = num
        games_dict[line.split(": ")[0]] = dict(sorted(draw_dict.items()))
    return games_dict

def valid_game(game, max):
    if game["blue"] <= max[0] and game["green"] <= max[1] and game["red"] <= max[2]:
        return True
    return False

games_dict = get_games_dict("puzzle_input.txt")
print(games_dict)

max = [14, 13, 12]

valid_game_sum = 0

for game in games_dict:
    # print(games_dict[game])
    if valid_game(games_dict[game], max):
        valid_game_sum += int(game.split(" ")[-1])

print("Sum of valid game ID's:",valid_game_sum)

# part 2

fewest_cubes = {}  # dictionary for game number and power ( product of red, blue, green)
for game in games_dict:
    # already have the minimum sets in games_dict[game]
    fewest_cubes[game] = games_dict[game]["blue"] * games_dict[game]["red"] * games_dict[game]["green"]

print(sum(fewest_cubes.values()))

