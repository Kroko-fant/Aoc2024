with open("../data/one-one.txt", "r") as f:
    data = f.readlines()

one = []
two = []
for line in data:
    split = line.replace('\n', '').split('   ')
    one.append(int(split[0]))
    two.append(int(split[1]))

one.sort()
two.sort()

print(sum([abs(one[x] - two[x]) for x in range(len(one))]))
print(sum([(two.count(one[x]) * one[x]) for x in range(len(one))]))
