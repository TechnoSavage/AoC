def makeLists(start, end):
    start, end = int(start), int(end)
    if start != end:
        myList = list(range(start, end + 1))
    else:
        myList = [start]
    return myList

pairs = []
overlapping = 0
with open('AoC_2022_4.txt', 'r') as assignments:
    for pair in assignments:
        pairs.append(pair.strip('\n'))
for pair in pairs:
    div = pair.split(',')
    elf1, elf2 = div[0], div[1]
    elf1, elf2 = elf1.split('-'), elf2.split('-')
    elf1 = makeLists(elf1[0], elf1[1])
    elf2 = makeLists(elf2[0], elf2[1])
    if elf1[0] in elf2 or elf1[-1] in elf2:
        overlapping += 1
    elif elf2[0] in elf1 or elf2[-1] in elf1:
        overlapping += 1
    else:
        pass
print(overlapping)