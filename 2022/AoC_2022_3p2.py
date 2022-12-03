import string

alpha = list(string.ascii_letters)
elves = []
totalScore = 0
with open('AoC_2022_3.txt', 'r') as packs:
    for line in packs:
        elves.append(line.strip('\n'))
while len(elves) > 0:
    group = elves[0:3]
    del elves[0:3]
    elf1, elf2, elf3 = group[0], group[1], group[2]
    elf1, elf2, elf3 = list(dict.fromkeys(elf1)), list(dict.fromkeys(elf2)), list(dict.fromkeys(elf3))
    for item in elf1:
        if item in elf2 and item in elf3:
            priority = alpha.index(item) + 1
            totalScore += priority
print(totalScore)