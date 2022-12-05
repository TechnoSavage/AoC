# [W] [V]     [P]                    
# [B] [T]     [C] [B]     [G]        
# [G] [S]     [V] [H] [N] [T]        
# [Z] [B] [W] [J] [D] [M] [S]        
# [R] [C] [N] [N] [F] [W] [C]     [W]
# [D] [F] [S] [M] [L] [T] [L] [Z] [Z]
# [C] [W] [B] [G] [S] [V] [F] [D] [N]
# [V] [G] [C] [Q] [T] [J] [P] [B] [M]
#  1   2   3   4   5   6   7   8   9 

import re

one = ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W']
two = ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V']
three = ['C', 'B', 'S', 'N', 'W']
four = ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P']
five = ['T', 'S', 'L', 'F', 'D', 'H', 'B']
six = ['J', 'V', 'T', 'W', 'M', 'N']
seven = ['P', 'F', 'L', 'C', 'S', 'T', 'G']
eight = ['B', 'D', 'Z']
nine = ['M', 'N', 'Z', 'W']

map = {'1': one,
       '2': two,
       '3': three,
       '4': four,
       '5': five,
       '6': six,
       '7': seven,
       '8': eight,
       '9': nine}

inst = []
with open('AoC_2022_5.txt', 'r') as instructions:
    for instruction in instructions:
        inst.append(instruction.strip('\n'))
for order in inst:
    mv = re.match('move ([0-9]+) from ([1-9]) to ([1-9])', order)
    count = int(mv.group(1))
    while count > 0:
        item = map[mv.group(2)].pop()
        map[mv.group(3)].append(item)
        count -= 1
print(one[-1], two[-1], three[-1], four[-1], five[-1], six[-1], seven[-1], eight[-1], nine[-1])
#T B V F V D Z P N