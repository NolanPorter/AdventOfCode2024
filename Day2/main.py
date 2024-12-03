'''
Count how many lists are valid using helper function for simplicity.
'''
def part1() -> int:
    val = 0
    arr = []
    with open('input.txt') as f:
        for line in f.readlines():
            arr = list(map(int, line.split(" ")))
            if is_valid(arr):
                val += 1
    return val

'''
Check if a list is valid, if it isn't, split it into multiple lists where each number is removed once.
i.e. [1, 2, 3, 4] -> [[2,3,4],[1,3,4],[1,2,4],[1,2,3]]
Check if any of these are valid, if it is then the original counts as valid.
Add up standard valid and 1 removed valid occurances, and that's the answer.
'''
def part2() -> int:
    val = 0
    arr = []
    with open('input.txt') as f:
        for line in f.readlines():
            arr = list(map(int, line.split(" ")))
            if is_valid(arr):
                val += 1
            else:
                remove_one_lists = [arr[:i] + arr[i+1:] for i in range(len(arr))]
                for i in remove_one_lists:
                    if is_valid(i):
                        val += 1
                        break
    return val

'''
Helper function as the logic was kind of annoying to manage.
Checks if a list is valid or not by doing the following:
    If the first two values are increasing, say that the entire list is increasing. Then if it's found to not be increasing, not valid.
    If it is increasing, check that each adjacent pair of numbers is increasing by at least 1 and at most 3.
    If it is decreasing, check that each adjacent pair of numbers is decreasing by at least 1 and at most 3.
    If the entire list is iterated over and doesn't fail the above checks, it is valid (True)
'''
def is_valid(arr):
    increasing = False
    if arr[1] - arr[0] > 0:
        increasing = True

    for i in range(len(arr) - 1):
        if increasing:
            if arr[i + 1] - arr[i] > 0 and arr[i + 1] - arr[i] < 4:
                continue
            else:
                return False
        else:
            if arr[i] - arr[i + 1] > 0 and arr[i] - arr[i + 1] < 4:
                continue
            else:
                return False
    return True


print(part1())
print(part2())