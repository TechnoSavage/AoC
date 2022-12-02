calories = []
with open('AoC_2022_1.txt', 'r') as food:
    for line in food:
        calories.append(line)
elves = {}
tally = 1
pack = []
for item in calories:
    if item != '\n':
        pack.append(int(item.strip('\n')))
    else:
        elves[tally] = pack
        pack = []
        tally += 1
totals = []
for item in elves:
    total = sum(elves[item])
    totals.append(total)
totals.sort()
print(totals[-1])
#Part 2 answer
topThree = sum(totals[-3:])
print(topThree)
