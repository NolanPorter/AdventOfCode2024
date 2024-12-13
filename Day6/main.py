from pprint import pprint
import time
import copy
def part1() -> int:
    val = 0

    while(get_guard_position() is not None):
        guard = get_guard_position()
        if(guard[2] == "^"):
            if (guard[0]-1 >= 0 and input_rows[guard[0]-1][guard[1]] == "#"):
                input_rows[guard[0]][guard[1]] = ">"
                continue
            elif (guard[0]-1 >= 0 and input_rows[guard[0]-1][guard[1]] == "."):
                input_rows[guard[0]-1][guard[1]] = "^"
                input_rows[guard[0]][guard[1]] = "."
                if (guard[0], guard[1]) not in seen_spots:
                    seen_spots.append((guard[0], guard[1]))
                    val += 1
            else:
                val += 1
                break
        elif(guard[2] == "<"):
            if (guard[1]-1 >= 0 and input_rows[guard[0]][guard[1]-1] == "#"):
                input_rows[guard[0]][guard[1]] = "^"
            elif (guard[1]-1 >= 0 and input_rows[guard[0]][guard[1]-1] == "."):
                input_rows[guard[0]][guard[1]-1] = "<"
                input_rows[guard[0]][guard[1]] = "."
                if (guard[0], guard[1]) not in seen_spots:
                    seen_spots.append((guard[0], guard[1]))
                    val += 1
            else:
                val += 1
                break
        elif(guard[2] == ">"):
            if (guard[1]+1 < len(input_rows[0]) and input_rows[guard[0]][guard[1]+1] == "#"):
                input_rows[guard[0]][guard[1]] = "v"
            elif (guard[1]+1 < len(input_rows[0]) and input_rows[guard[0]][guard[1]+1] == "."):
                input_rows[guard[0]][guard[1]+1] = ">"
                input_rows[guard[0]][guard[1]] = "."
                if (guard[0], guard[1]) not in seen_spots:
                    seen_spots.append((guard[0], guard[1]))
                    val += 1
            else:
                val += 1
                break
        elif(guard[2] == "v"):
            if (guard[0]+1 < len(input_rows) and input_rows[guard[0]+1][guard[1]] == "#"):
                input_rows[guard[0]][guard[1]] = "<"
            elif (guard[0]+1 < len(input_rows) and input_rows[guard[0]+1][guard[1]] == "."):
                input_rows[guard[0]+1][guard[1]] = "v"
                input_rows[guard[0]][guard[1]] = "."
                if (guard[0], guard[1]) not in seen_spots:
                    seen_spots.append((guard[0], guard[1]))
                    val += 1
            else:
                val += 1
                break

    return val

def part2() -> int:

    global input_rows
    global seen_spots   
    original_path = []
    while(get_guard_position() is not None):
        guard = get_guard_position()
        if(guard[2] == "^"):
            if (guard[0]-1 >= 0 and input_rows[guard[0]-1][guard[1]] == "#"):
                input_rows[guard[0]][guard[1]] = ">"
                continue
            elif (guard[0]-1 >= 0 and input_rows[guard[0]-1][guard[1]] == "."):
                input_rows[guard[0]-1][guard[1]] = "^"
                input_rows[guard[0]][guard[1]] = "."
                if (guard[0], guard[1]) not in original_path:
                    original_path.append((guard[0], guard[1]))
            else:
                original_path.append((guard[0], guard[1]))
                break
        elif(guard[2] == "<"):
            if (guard[1]-1 >= 0 and input_rows[guard[0]][guard[1]-1] == "#"):
                input_rows[guard[0]][guard[1]] = "^"
            elif (guard[1]-1 >= 0 and input_rows[guard[0]][guard[1]-1] == "."):
                input_rows[guard[0]][guard[1]-1] = "<"
                input_rows[guard[0]][guard[1]] = "."
                if (guard[0], guard[1]) not in original_path:
                    original_path.append((guard[0], guard[1]))
            else:
                original_path.append((guard[0], guard[1]))
                break
        elif(guard[2] == ">"):
            if (guard[1]+1 < len(input_rows[0]) and input_rows[guard[0]][guard[1]+1] == "#"):
                input_rows[guard[0]][guard[1]] = "v"
            elif (guard[1]+1 < len(input_rows[0]) and input_rows[guard[0]][guard[1]+1] == "."):
                input_rows[guard[0]][guard[1]+1] = ">"
                input_rows[guard[0]][guard[1]] = "."
                if (guard[0], guard[1]) not in original_path:
                    original_path.append((guard[0], guard[1]))
            else:
                original_path.append((guard[0], guard[1]))
                break
        elif(guard[2] == "v"):
            if (guard[0]+1 < len(input_rows) and input_rows[guard[0]+1][guard[1]] == "#"):
                input_rows[guard[0]][guard[1]] = "<"
            elif (guard[0]+1 < len(input_rows) and input_rows[guard[0]+1][guard[1]] == "."):
                input_rows[guard[0]+1][guard[1]] = "v"
                input_rows[guard[0]][guard[1]] = "."
                if (guard[0], guard[1]) not in original_path:
                    original_path.append((guard[0], guard[1]))
            else:
                original_path.append((guard[0], guard[1]))
                break






    val = 0
    input_rows = copy.deepcopy(original_rows)
    # original_rows = copy.deepcopy(input_rows)
    num_boards_to_check = len(original_path)
    num_checked = 0
    total_time = 0
    for input_row_row_idx, input_row_row in enumerate(input_rows):
        for input_row_column_idx, input_row_column in enumerate(input_row_row):
            start_time = time.time()
            if((input_row_row_idx, input_row_column_idx) not in original_path):
               continue
            if (input_row_row_idx < len(input_rows) and input_row_column_idx < len(input_rows[0])) and ((input_rows[input_row_row_idx][input_row_column_idx] == "#") or (input_rows[input_row_row_idx][input_row_column_idx] in possible_guards)):
                # print(f"{input_row_row_idx},{input_row_column_idx} already set with # or char")
                continue
            elif input_row_row_idx < len(input_rows) and input_row_column_idx < len(input_rows[0]):
                input_rows[input_row_row_idx][input_row_column_idx] = "#"
                # print("Trying new obstacle:", input_row_row_idx, input_row_column_idx)
                # pprint(input_rows)
            else:
                continue

            while(get_guard_position() is not None):
                guard = get_guard_position()
                # pprint(input_rows)
                # print(len(seen_spots))
                # print(guard)
                if(guard[2] == "^"):
                    if (guard[0]-1 >= 0 and input_rows[guard[0]-1][guard[1]] == "#"):
                        input_rows[guard[0]][guard[1]] = ">"
                    elif (guard[0]-1 >= 0 and input_rows[guard[0]-1][guard[1]] == "."):
                        input_rows[guard[0]-1][guard[1]] = "^"
                        input_rows[guard[0]][guard[1]] = "."
                        if (guard[0], guard[1], guard[2]) in seen_spots:
                            val += 1
                            break
                        else:
                            seen_spots.append((guard[0], guard[1], guard[2]))
                    else:
                        break
                elif(guard[2] == "<"):
                    if (guard[1]-1 >= 0 and input_rows[guard[0]][guard[1]-1] == "#"):
                        input_rows[guard[0]][guard[1]] = "^"
                    elif (guard[1]-1 >= 0 and input_rows[guard[0]][guard[1]-1] == "."):
                        input_rows[guard[0]][guard[1]-1] = "<"
                        input_rows[guard[0]][guard[1]] = "."
                        if (guard[0], guard[1], guard[2]) in seen_spots:
                            val += 1
                            break
                        else:
                            seen_spots.append((guard[0], guard[1], guard[2]))
                    else:
                        break
                elif(guard[2] == ">"):
                    if (guard[1]+1 < len(input_rows[0]) and input_rows[guard[0]][guard[1]+1] == "#"):
                        input_rows[guard[0]][guard[1]] = "v"
                    elif (guard[1]+1 < len(input_rows[0]) and input_rows[guard[0]][guard[1]+1] == "."):
                        input_rows[guard[0]][guard[1]+1] = ">"
                        input_rows[guard[0]][guard[1]] = "."
                        if (guard[0], guard[1], guard[2]) in seen_spots:
                            val += 1
                            break
                        else:
                            seen_spots.append((guard[0], guard[1], guard[2]))
                    else:
                        break
                elif(guard[2] == "v"):
                    if (guard[0]+1 < len(input_rows) and input_rows[guard[0]+1][guard[1]] == "#"):
                        input_rows[guard[0]][guard[1]] = "<"
                    elif (guard[0]+1 < len(input_rows) and input_rows[guard[0]+1][guard[1]] == "."):
                        input_rows[guard[0]+1][guard[1]] = "v"
                        input_rows[guard[0]][guard[1]] = "."
                        if (guard[0], guard[1], guard[2]) in seen_spots:
                            val += 1
                            break
                        else:
                            seen_spots.append((guard[0], guard[1], guard[2]))
                    else:
                        break
                guard = get_guard_position()
                # print("new guard")
                # time.sleep(0.5)
            
            input_rows = copy.deepcopy(original_rows)
            seen_spots = []
            num_checked += 1
            elapsed_time = time.time() - start_time
            total_time += elapsed_time
            print(f"Boards checked: {num_checked}/{num_boards_to_check}, done in {elapsed_time}, for a total time taken of {total_time}, average time of {total_time / num_checked}, and an estimated {((total_time / num_checked) * (num_boards_to_check - num_checked))/60/60} hours left!")
            # pprint(original_rows)
            # time.sleep(1000)

    return val

def part2_2() -> int:
    guard = get_guard_position()
    res = 0
    global input_rows
    num_checked = 0
    total_time = 0

    pre_calc_seen = calculate_all_seen(guard[1], guard[0], guard[2], input_rows)
    num_boards_to_check = len(pre_calc_seen)

    for input_row_row_idx, input_row_row in enumerate(input_rows):
        for input_row_column_idx, input_row_column in enumerate(input_row_row):
            start_time = time.time()
            # if((input_row_row_idx, input_row_column_idx) not in pre_calc_seen):
            #    continue
            if (input_row_row_idx < len(input_rows) and input_row_column_idx < len(input_rows[0])) and ((input_rows[input_row_row_idx][input_row_column_idx] == "#") or (input_rows[input_row_row_idx][input_row_column_idx] in possible_guards)):
                # print(f"{input_row_row_idx},{input_row_column_idx} already set with # or char")
                continue
            elif input_row_row_idx < len(input_rows) and input_row_column_idx < len(input_rows[0]):
                input_rows[input_row_row_idx][input_row_column_idx] = "#"
                # print("Trying new obstacle:", input_row_row_idx, input_row_column_idx)
                # pprint(input_rows)
            else:
                continue

            res += calculate_path(guard[1], guard[0], guard[2], input_rows)
            num_checked += 1
            input_rows = copy.deepcopy(original_rows)
            elapsed_time = time.time() - start_time
            total_time += elapsed_time
            print(f"Boards checked: {num_checked}/{num_boards_to_check}, done in {elapsed_time}, for a total time taken of {total_time}, average time of {total_time / num_checked}, and an estimated {((total_time / num_checked) * (num_boards_to_check - num_checked))/60/60} hours left!")

    return res

def calculate_path(guard_x, guard_y, starting_guard_direction, board):
    seen = []
    x = copy.copy(guard_x)
    y = copy.copy(guard_y)
    guard = starting_guard_direction
    # pprint(board)
    while x >= 0 and x < len(board[0]) and y >= 0 and y < len(board):
        if (x,y,guard) in seen:
            return 1
        seen.append((x,y,guard))
        # pprint(seen)
        if guard == "^":
            if (y-1 < 0):
                break
            elif (board[y-1][x] == "#"):
                guard = ">"
                continue
            else:
                y -= 1
                continue
        elif guard == ">":
            if (x+1 >= len(board[0])):
                break
            elif (board[y][x+1] == "#"):
                guard = "v"
                continue
            else:
                x += 1
                continue
        elif guard == "v":
            if (y+1 >= len(board)):
                break
            elif (board[y+1][x] == "#"):
                guard = "<"
                continue
            else:
                y += 1
                continue
        elif guard == "<":
            if (x-1 < 0):
                break
            elif (board[y][x-1] == "#"):
                guard = "^"
                continue
            else:
                x -= 1
                continue

    if has_duplicate(seen):
        return 1
    return 0

def has_duplicate(arr):
    seen = set()  # This set will store unique elements
    while True:
        for num in arr:
            if num in seen:  # Check if the number has already been encountered
                return True  # A duplicate exists
            seen.add(num)  # Add the number to the set if it's not a duplicate
        break  # This break is just to prevent an infinite loop for demonstration purposes
    return False

def calculate_all_seen(guard_x, guard_y, starting_guard_direction, board):
    seen = []
    x = copy.copy(guard_x)
    y = copy.copy(guard_y)
    guard = starting_guard_direction
    # pprint(board)
    while x >= 0 and x < len(board[0]) and y >= 0 and y < len(board):
        if guard == "^":
            seen.append((x, y-1))
            if (y-1 < 0):
                break
            elif (board[y-1][x] == "#"):
                guard = ">"
                continue
            else:
                y -= 1
                continue
        elif guard == ">":
            seen.append((x+1, y))
            if (x+1 >= len(board[0])):
                break
            elif (board[y][x+1] == "#"):
                guard = "v"
                continue
            else:
                x += 1
                continue
        elif guard == "v":
            seen.append((x, y+1))
            if (y+1 >= len(board)):
                break
            elif (board[y+1][x] == "#"):
                guard = "<"
                continue
            else:
                y += 1
                continue
        elif guard == "<":
            seen.append((x-1, y))
            if (x-1 < 0):
                break
            elif (board[y][x-1] == "#"):
                guard = "^"
                continue
            else:
                x -= 1
                continue

    return seen

def parse_input(value):
    global input_rows
    with open(f"input{value}.txt") as f:
        for line in f.readlines():
            input_rows.append(list(line.strip()))

def get_guard_position() -> tuple[int, int, str]:
    global possible_guards
    for possible_guard in possible_guards:
        for row_idx, row in enumerate(input_rows):
            for col_idx, char in enumerate(row):
                if char == possible_guard:
                    return (row_idx, col_idx, possible_guard)
            else:
                continue
    return None

# def guard_is_present():
    possible_guards = ["^", "<", ">", "v"]
    for possible_guard in possible_guards:
        if any(possible_guard in string for string in input_rows):
            return True
    return False

input_rows = []
possible_guards = ["^", "<", ">", "v"]
seen_spots = []
parse_input(2)
# print(part1())

input_rows = []
seen_spots = []
parse_input(1)
# p = calculate_path(4, 6, "^", input_rows)
# print(p)
original_rows = copy.deepcopy(input_rows)
print(part2_2())