letters = []

def part1() -> int:
    val = 0
    with open('input.txt') as f:
        for line in f.readlines():
            letters.append(list(line.strip()))
        
        for row_index, row in enumerate(letters):
            for letter_index, letter in enumerate(row):
                if letter == "X":
                    val += find_nearby_character("X", "left", letter_index, row_index)
                    val += find_nearby_character("X", "upleft", letter_index, row_index)
                    val += find_nearby_character("X", "up", letter_index, row_index)
                    val += find_nearby_character("X", "upright", letter_index, row_index)
                    val += find_nearby_character("X", "right", letter_index, row_index)
                    val += find_nearby_character("X", "downright", letter_index, row_index)
                    val += find_nearby_character("X", "down", letter_index, row_index)
                    val += find_nearby_character("X", "downleft", letter_index, row_index)
                
    return val

def part2() -> int:
    val = 0
    with open('input.txt') as f:
        for line in f.readlines():
            letters.append(list(line.strip()))

        for row_index, row in enumerate(letters):
                for letter_index, letter in enumerate(row):
                    if letter == "A":
                        val += xmas(letter_index, row_index)
    return val


def find_nearby_character(current_string, direction, x, y):
    if current_string == "XMAS":
        return 1
    
    if len(current_string) >= 4:
        return 0

    if(x < 0 or x > len(letters[0]) or y < 0 or y > len(letters)):
        return 0

    val = 0
    
    if current_string == "X" or current_string == "XM" or current_string == "XMA":
        if direction == "left":
            if(x-1 < 0):
                return 0
            if(letters[y][x-1] and valid_character(letters[y][x-1])):
                val += find_nearby_character(current_string + letters[y][x-1], "left", x-1, y)
        elif direction == "upleft":
            if(x-1 < 0 or y-1 < 0):
                return 0
            if(valid_character(letters[y-1][x-1])):
                val += find_nearby_character(current_string + letters[y-1][x-1], "upleft", x-1, y-1)
        elif direction == "up":
            if(y-1 < 0):
                return 0
            if(valid_character(letters[y-1][x])):
                val += find_nearby_character(current_string + letters[y-1][x], "up", x, y-1)
        elif direction == "upright":
            if(x+1 > len(letters[0])-1 or y-1 < 0):
                return 0
            if(valid_character(letters[y-1][x+1])):
                val += find_nearby_character(current_string + letters[y-1][x+1], "upright", x+1, y-1)
        elif direction == "right":
            if(x+1 > len(letters[0])-1):
                return 0
            if(valid_character(letters[y][x+1])):
                val += find_nearby_character(current_string + letters[y][x+1], "right", x+1, y)
        elif direction == "downright":
            if(x+1 > len(letters[0])-1 or y+1 > len(letters)-1):
                return 0
            if(valid_character(letters[y+1][x+1])):
                val += find_nearby_character(current_string + letters[y+1][x+1], "downright", x+1, y+1)
        elif direction == "down":
            if(y+1 > len(letters)-1):
                return 0
            if(valid_character(letters[y+1][x])):
                val += find_nearby_character(current_string + letters[y+1][x], "down", x, y+1)
        elif direction == "downleft":
            if(x-1 < 0 or y+1 > len(letters)-1):
                return 0
            if(valid_character(letters[y+1][x-1])):
                val += find_nearby_character(current_string + letters[y+1][x-1], "downleft", x-1, y+1)

    return val

def valid_character(letter):
    if letter in ["M", "A", "S"]:
        return True
    return False

def xmas(x, y):
    if (y-1 < 0 or x-1 < 0 or y+1 > len(letters)-1 or x+1 > len(letters[0])-1):
        return 0
    if(
        (letters[y-1][x-1] == "M" and letters[y+1][x+1] == "S" and letters[y-1][x+1] == "M" and letters[y+1][x-1] == "S")
        or (letters[y-1][x-1] == "S" and letters[y+1][x+1] == "M" and letters[y-1][x+1] == "S" and letters[y+1][x-1] == "M")
        or (letters[y-1][x-1] == "M" and letters[y+1][x+1] == "S" and letters[y-1][x+1] == "S" and letters[y+1][x-1] == "M")
        or (letters[y-1][x-1] == "S" and letters[y+1][x+1] == "M" and letters[y-1][x+1] == "M" and letters[y+1][x-1] == "S")
        ):
       return 1

    return 0

print(part1())
letters = []
print(part2())