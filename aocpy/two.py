from copy import copy

with open("../data/two-one.txt", "r") as f:
    lines = f.readlines()

lines = [([int(x) for x in l.replace("\n", "").split(" ")]) for l in lines]


def sorted_copy(x, reverse=False):
    y = copy(x)
    y.sort(reverse=reverse)
    return y


all_inc_or_dec = lambda x: (sorted_copy(x) == x or sorted_copy(x, True) == x)
adjacent_levels = lambda x: not any([abs(x[index] - x[(index + 1)] if index +1 != len(x) else 1) not in [1, 2, 3]for index in range(len(x))])

print(sum(all_inc_or_dec(line) and adjacent_levels(line) for line in lines))


def two(x):
    if all_inc_or_dec(x) and adjacent_levels(x):
        return True
    for index in range(len(x)):
        temp = [y for y in x]
        temp.pop(index)
        if all_inc_or_dec(temp) and adjacent_levels(temp):
            return True
    return False


print(sum([two(line) for line in lines]))
