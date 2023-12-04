def file_to_list(filename):
    with open(filename, "r") as file:
        games = file.readlines()
    return games

def get_card(card):
    play = card.split(": ")[1].rstrip('\n').split(" | ")

    # print(play[0])
    return play

def check_wins(plays):
    winning = plays[0].split(" ")
    player = plays[1].split(" ")

    while '' in winning:
        winning.remove('')

    win = [play for play in player if play in winning]
    return win

# my attempt at recursion!
def get_score(wins):
    if wins == 0:
        return 0
    elif wins == 1:
        return 1
    else:
        return get_score(wins - 1) * 2


cards = file_to_list("puzzle_input.txt")
wins_list = []
total_score = 0
for card in cards:
    count = 0
    play = get_card(card)
    wins = check_wins(play)
    # print(wins)

    for win in wins:
        count += 1

    total_score = total_score + get_score(count)

    wins_list.append(count)

    card_num = int(card.split(": ")[0].split(" ")[-1])
    # print("Card", card_num, "wins", count, "new cards")

print("Points total:", total_score)

# part 2

# initialise list with one copy of each to begin
copies_list = [1 for win in wins_list]

for index, win in enumerate(wins_list):
    counter = win
    i = index
    while counter > 0:
        copies_list[i+1] += copies_list[index]
        i = i + 1
        counter -= 1

# print("Number of wins:", wins_list)
# print("Number of copies", copies_list)
total_cards = sum(copies_list)
print("Total number of cards is", total_cards)
