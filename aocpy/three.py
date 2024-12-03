
with open("../data/three.txt") as f:
    input_string = f.read()


def calc_mul(mul_string):
    numbers = [int(x) for x in mul_string.replace("mul(", "").replace(")", "").split(",")]
    if 0 <= numbers[0] <= 999 and 0 < numbers[1] <= 999:
        return numbers[0] * numbers[1]
    return 0


# returns true if its a full match, false if its not a match and None if its not full
def match_mul_pattern(group):
    pattern = ["m", "u", "l", "(", int, ",", int, ")"]
    i = 0
    offset = 0
    while i < len(pattern):
        if i+offset >= len(group):
            return None
    #    print(f"Debug: {pattern[i]} {group[i + offset]} {i} {offset}")
        if pattern[i] is int:
            if group[i + offset] in [str(x) for x in range(10)]:
                offset += 1
                continue
            elif group[i + offset] == pattern[i +1]:
                i += 1
                offset -= 1
                continue
            return False
        elif not pattern[i] == group[i + offset]:
            return False
        i += 1
    return True

def match_do_pattern(group):
    if len(group) == 1:
        return None if group[0] == "d" else False
    if len(group) == 2:
        return None if group == "do" else False
    if len(group) == 3:
        return None if group[2] in ["n", "("] else False
    if len(group) == 4:
        if group[2] == "(":
            return group[3] == ")"
        return None if group[3] == "'" else False
    if len(group) == 5:
        return None if group[4] == "t" else False
    if len(group) == 6:
        return None if group[5] == "(" else False
    if len(group) == 7:
        return True if group[6] == ")" else False
    return False

# Part 1:
total = 0
enabled = True
index = 0
group = ""
while index < len(input_string):
    group += input_string[index]
    index += 1
    if group.startswith("m"):
        result = match_mul_pattern(group)
        if result is None:
            continue
        if result is True:
            group_total = calc_mul(group)
            total += group_total
    group = ""
print(total)

# Part 2
total = 0
enabled = True
index = 0
group = ""
while index < len(input_string):
    group += input_string[index]
    index += 1
    if enabled and group.startswith("m"):
        result = match_mul_pattern(group)
        if result is None:
            continue
        if result is True:
            group_total = calc_mul(group)
            total += group_total
    if group.startswith("d"):
        result = match_do_pattern(group)
        if result is True:
            enabled = group=="do()"
        elif result is None:
            continue
    group = ""

print(total)
