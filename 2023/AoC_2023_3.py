import pandas as pd

def partScan(targets, schematic):
    parts = ('+', '-', '*', '@', '=', '$', '%', '&', '#', '/')
    adjacent = [(0, -1), (0, +1),
                (+1, -1), (+1, 0), (+1, +1),
                (-1, -1), (-1, 0), (-1, +1)]
    for target in targets:
        for mod in adjacent:
            try:
                char = schematic.iloc[target[0] + mod[0], target[1] + mod[1]]
            except IndexError as e:
                pass
            if char in parts:
                return True
    return False        
    
def buildNum(targets, schematic):
    number = []
    for target in targets:
        digit = schematic.iloc[target[0], target[1]]
        number.append(digit)
    return ''.join(number)


def main():
    partNums = []
    with open ('AoC_2023_3.txt', 'r') as f:
        draft = f.read()
    blueprint = [list(line) for line in draft.split('\n')]
    schematic = pd.DataFrame(blueprint)
    yLimit = schematic.shape[0]
    xLimit = schematic.shape[1]
    x = 0
    y = 0
    while y < yLimit:
        targets = []
        while x <= xLimit:
            if x == xLimit:
                test = partScan(targets, schematic)
                if test:
                    partNums.append(buildNum(targets, schematic))
                targets = []
            elif str.isdigit(schematic.iloc[y, x]):
                targets.append((y, x))
            else:
                if len(targets) > 0:
                    test = partScan(targets, schematic)
                    if test:
                        partNums.append(buildNum(targets, schematic))
                targets = []
            x += 1
        x = 0
        y += 1
    partNums = [int(i) for i in partNums]
    print(sum(partNums))

if __name__ == "__main__":
    main()
    