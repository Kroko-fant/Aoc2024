with open("../data/five.txt", "r") as f:
    lines = f.readlines()

rules = {}
orders = []
for line in lines:
    if "|" in line:
        if (key := int(line.split("|")[0])) not in rules:
            rules[key] = []
        rules[key].append(int(line.split("|")[1].replace("\n", "")))
    elif "," in line:
        orders.append([int(x) for x in line.split(",")])
# part 1
correct = 0
incorrect = []
for order in orders:
    for index, order_element in enumerate(order):
        if order_element not in rules:
            continue
        indexes = [order.index(x) for x in rules[order_element] if x in order]
        if len(indexes) != 0 and index > min(indexes):
            # collect for part 2
            incorrect.append(order)
            break
    else:
        correct += order[len(order) // 2]

print(correct)

# part 2
def ordered(order):
    for index, order_element in enumerate(order):
        if order_element not in rules:
            continue
        indexes = [order.index(x) for x in rules[order_element] if x in order]
        if len(indexes) != 0 and index > min(indexes):
            return False, index
    return True, order[len(order) // 2]


incorrect_index = -1
result_two = 0
while (incorrect_index := incorrect_index + 1) < len(incorrect):
    element = incorrect[incorrect_index]
    while True:
        status, result = ordered(element)
        if status:
            result_two += result
            break
        entry = element.pop(result)
        element.insert(result-1, entry)
print(result_two)
