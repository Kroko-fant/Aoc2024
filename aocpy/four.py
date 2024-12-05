with open("../data/four.txt", "r") as f:
    lines = f.readlines()
    lines = [x.replace("\n", "") for x in lines]

lines_flipped = []
for i in range(len(lines[0])):
    temp = ""
    for j in range(len(lines)):
        temp += lines[j][i]
    lines_flipped.append(temp)


def get_diagonals(lines):
    lines_diagonal = []
    index_x = 0
    index_y = 0
    # increase x
    while index_x < len(lines):
        temp = ""
        for offset in range(0, len(lines) - index_x):
            if index_y + offset > len(lines[0]):
                break
            temp += lines[index_x + offset][index_y + offset]
        if temp != "":
            lines_diagonal.append(temp)
        index_x += 1
    # reset x to 0
    index_x = 0
    index_y = 1
    # increase y
    while index_y < len(lines[0]):
        temp = ""
        for offset in range(0, len(lines[0]) - index_y):
            if index_x + offset > len(lines):
                break
            temp += lines[index_x + offset][index_y + offset]
        if temp != "":
            lines_diagonal.append(temp)
        index_y += 1
    return lines_diagonal


lines_diagonal = get_diagonals(lines)
lines_diagonal_flipped = get_diagonals([line[::-1] for line in lines])

counter = 0
# count horizontal
for line in lines:
    counter += line.count("XMAS") + line.count("SAMX")

for line in lines_flipped:
    counter += line.count("XMAS") + line.count("SAMX")

for line in lines_diagonal:
    counter += line.count("XMAS") + line.count("SAMX")

for line in lines_diagonal_flipped:
    counter += line.count("XMAS") + line.count("SAMX")
print(counter)

# part 2
counter_two = 0
index_x = 0
while index_x + 2 < len(lines):
    index_y = 0
    while index_y + 2 < len(lines[0]):
        if lines[index_x + 1][index_y + 1] == "A":
            # 4 cases
            if lines[index_x][index_y] == "S" \
                    and lines[index_x + 2][index_y] == "S" \
                    and lines[index_x][index_y + 2] == "M" \
                    and lines[index_x + 2][index_y + 2] == "M":
                counter_two += 1
            elif lines[index_x][index_y] == "S" \
                    and lines[index_x + 2][index_y] == "M" \
                    and lines[index_x][index_y + 2] == "S" \
                    and lines[index_x + 2][index_y + 2] == "M":
                counter_two += 1
            elif lines[index_x][index_y] == "M" \
                    and lines[index_x + 2][index_y] == "S" \
                    and lines[index_x][index_y + 2] == "M" \
                    and lines[index_x + 2][index_y + 2] == "S":
                counter_two += 1
            elif lines[index_x][index_y] == "M" \
                    and lines[index_x + 2][index_y] == "M" \
                    and lines[index_x][index_y + 2] == "S" \
                    and lines[index_x + 2][index_y + 2] == "S":
                counter_two += 1
        index_y += 1
    index_x += 1
print(counter_two)
