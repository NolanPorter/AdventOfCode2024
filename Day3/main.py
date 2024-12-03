import re

pattern_mul = r"mul\((\d+),(\d+)\)"
pattern_program = r"mul\(\d+,\d+\)|do\(\)|don['’]t\(\)"
pattern_nums = r"\d+"

'''
Simple regex pattern match to get all of the mul instructions, then iterate over them
'''
def part1() -> int:
    val = 0
    with open('input.txt') as f:
        for line in f.readlines():
            numbers = [(int(a), int(b)) for a, b in re.findall(pattern_mul, line)]
            print(numbers)
            for pair in numbers:
                val += pair[0]*pair[1]

    return val

'''
Another simple regex pattern match with a changing boolean based on instruction.
'''
def part2() -> int:
    val = 0
    with open('input.txt') as f:
        do_mult = True
        for line in f.readlines():
            for i in re.findall(pattern_program, line):
                if i == "do()":
                    do_mult = True
                elif i == "don't()":
                    do_mult = False
                else:
                    if do_mult:
                        pair1, pair2 = [int(num) for num in re.findall(pattern_nums, i)]
                        val += pair1*pair2
    return val

print(part1())
print(part2())