
def file_to_list(filename):
    lines = []
    count = 0
    with open(filename, "r") as file:
        for line in file.readlines():
            lines.append("."+line.strip('\n')+".")
            count += 1

    list_of_items = []
    boarder = []  # make a boarder of dots to check the surrounding space of all digits
    for i in range(count + 2):
        boarder.append(".")

    list_of_items.append(boarder)
    for items in lines:
        list_of_items.append([*items])

    list_of_items.append(boarder)
    # print(list_of_items)
    return list_of_items

def loop_list(list):
    sum = 0
    # loop rows
    for index, row in enumerate(list):
        num = ""
        row_index = int(index)

        # loop columns
        # by far the most disgusting brain boggling piece of code ive ever written
        # point is i got there and can come back to tidy when i figure out how
        for index, char in enumerate(row):
            col_index = int(index)
            if char.isdigit() and not list[row_index][col_index-1].isdigit():
                around_cells = [list[row_index - 1][col_index - 1], list[row_index - 1][col_index],
                                list[row_index - 1][col_index + 1], list[row_index][col_index - 1],
                                list[row_index][col_index + 1], list[row_index - 1][col_index - 1],
                                list[row_index - 1][col_index], list[row_index - 1][col_index + 1]]

                if list[row_index][col_index + 1].isdigit():
                    around_cells = [list[row_index - 1][col_index - 1], list[row_index - 1][col_index],
                                    list[row_index - 1][col_index + 1], list[row_index - 1][col_index + 2],
                                    list[row_index + 1][col_index - 1], list[row_index + 1][col_index],
                                    list[row_index + 1][col_index + 1], list[row_index + 1][col_index + 2],
                                    list[row_index][col_index - 1], list[row_index][col_index + 2]]

                    if list[row_index][col_index + 2].isdigit():
                        around_cells = [list[row_index - 1][col_index - 1], list[row_index - 1][col_index],
                                        list[row_index - 1][col_index + 1], list[row_index - 1][col_index + 2],
                                        list[row_index - 1][col_index + 3], list[row_index + 1][col_index - 1],
                                        list[row_index + 1][col_index], list[row_index + 1][col_index + 1],
                                        list[row_index + 1][col_index + 2], list[row_index + 1][col_index + 3],
                                        list[row_index][col_index - 1], list[row_index][col_index + 3]]

                        if contains_special(around_cells):
                            num = char + list[row_index][col_index + 1] + list[row_index][col_index + 2]
                            sum = sum + int(num)

                    elif contains_special(around_cells):
                        num = char + list[row_index][col_index + 1]
                        sum = sum + int(num)

                elif contains_special(around_cells):
                    sum = sum + int(char)

    return sum

def contains_special(list):
    special_characters = "@$%&*+=-/#"
    special = []
    for item in list:
        if item in special_characters:
            special.append(True)
        else:
            special.append(False)
    if sum(special) > 0:
        return True
    return False

list = file_to_list("puzzle_input.txt")
print(loop_list(list))

