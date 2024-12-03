import re

def part1() -> int:
    val = 0
    pattern = r"mul\((\d+),(\d+)\)"
    with open('input.txt') as f:
        for line in f.readlines():
            matches = re.findall(pattern, line)
            numbers = [(int(a), int(b)) for a, b in matches]
            for pair in numbers:
                val += pair[0]*pair[1]

    return val

'''
NOT DONE YET
'''
def part2() -> int:
    val = 0
    with open('input.txt') as f:
        for line in f.readlines():
            val += 1
    return val


print(part1())
print(part2())