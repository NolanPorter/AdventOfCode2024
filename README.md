# AdventOfCode2024

I'm going to try my best to go as far as I can in Advent of Code 2024!


## Code file format
```
def part1() -> int:
    val = 0
    return val

def part2() -> int:
    val = 0
    return val

def parse_input(value):
    global input_rows
    with open(f"input{value}.txt") as f:
        for line in f.readlines():
            input_rows.append(line.strip())


input_rows = []
parse_input(2)
print(part1())
print(part2())
```

## README file format
```
## Thoughts

## Total time spent

### Part 1
#### Time spent:

### Part 2
#### Time spent: 
```