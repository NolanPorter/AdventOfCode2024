def part1() -> int:
    val = 0
    arr = []
    with open('input.txt') as f:
        for line in f.readlines():
            arr = list(map(int, line.split(" ")))
            if is_valid(arr):
                val += 1
    return val

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