'''
Sort the numbers, then sequentially compare the distance between left[i] and right[i]
Add up those distances and that's the answer.
'''
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

'''
Map the values of the right list to the number of times they appear, i.e. {1: 12, 2: 3}...
Loop over every value in left list, multiply left value by the number of times it appears in the right
Add up those multiplied values and that is the answer.
'''
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