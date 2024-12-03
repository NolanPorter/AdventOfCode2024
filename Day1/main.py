def part1() -> int:
    val = 0
    left = []
    right = []
    with open('input.txt') as f:
        for line in f.readlines():
            left_val, right_val = map(int, line.split("   "))
            left.append(left_val)
            right.append(right_val)

    left.sort()
    right.sort()

    for i in range(len(left)):
        val += abs(left[i] - right[i])

    return val

def part2() -> int:
    val = 0
    left = []
    right = {}
    with open('input.txt') as f:
        for line in f.readlines():
            left_val, right_val = map(int, line.split("   "))
            left.append(left_val)
            right[right_val] = right.get(right_val, 0) + 1

    for i in range(len(left)):
        if(left[i] in right):
            val += left[i] * right[left[i]]

    return val


print(part1())
print(part2())