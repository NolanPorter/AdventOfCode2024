import itertools

def part1() -> int:
    val = 0
    valid_updates = save_relevant_updates(True)
    for update in valid_updates:
        val += int(update[len(update) // 2])

    return val

def part2() -> int:
    val = 0
    invalid_updates = save_relevant_updates(False)
    fixed_updates = []
    print(invalid_updates)
    for update in invalid_updates:
        temp = []
        for page in update:
            inserted = False
            it = len(temp)
            print(temp)
            for j in range(it):
                if temp[j] in rules_map and page in rules_map[temp[j]]:
                    # print("New temp:", temp[:j] + [page] + temp[j:])
                    temp.insert(j, page)
                    inserted = True
                    break
            if not inserted:
                temp.append(page)
        fixed_updates.append(temp)
        
    print(fixed_updates)

    for fix in fixed_updates:
        if not check_update_validity(fix):
            print("failed")

    for update in fixed_updates:
        val += int(update[len(update) // 2])

    return val

def parse_input(value):
    rows = []
    rules = []
    global updates
    with open(f"input{value}.txt") as f:
        for line in f.readlines():
            rows.append(line.strip())

    passedRules = False
    for row in rows:
        if row == "":
            passedRules = True

        if not passedRules:
            rules.append(row)
        else:
            updates.append(row)

    updates = updates[1:]

    for rule in rules:
        value,key = rule.split("|")
        if key in rules_map:
            rules_map[key].append(value)
        else:
            rules_map[key] = [value]

def save_relevant_updates(save_valid):
    relevant_updates = []
    for update in updates:
        if save_valid and check_update_validity(update):
            relevant_updates.append(update.split(","))
        elif not save_valid and not check_update_validity(update):
            relevant_updates.append(update.split(","))
    return relevant_updates

def check_update_validity(update):
    if type(update) is str:
        page_order = update.split(",")
    else:
        page_order = update
    valid = True
    for i, page in enumerate(page_order):
        before_list = []
        if page in rules_map:
            before_list = rules_map[page]
        for prev_page in page_order[:i]:
            if prev_page not in before_list and page in rules_map[prev_page]:
                valid = False
                break
            if not valid:
                break
        if not valid:
            break
    return valid

rules_map = {}
updates = []
parse_input(1)

print(part1())
print(part2())