import string

alpha = list(string.ascii_letters)
packs = []
totalScore = 0
with open('AoC_2022_3.txt', 'r') as rucks:
    for line in rucks:
        packs.append(line.strip('\n'))
for item in packs:
    comp1, comp2 = item[0:len(item)//2], item[len(item)//2:]
    comp1, comp2 = list(dict.fromkeys(comp1)), list(dict.fromkeys(comp2))
    for item in comp1:
        if item in comp2:
            priority = alpha.index(item) + 1
            totalScore += priority
print(totalScore)