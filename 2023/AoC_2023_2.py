import re

limit = {'red': 12,
         'green': 13,
         'blue': 14}
possible = []
with open ('AoC_2023_2.txt', 'r') as f:
    for line in f.readlines():
        game = True
        gid = re.findall("Game ([0-9]+):" , line)
        gid = gid[0]
        red = re.findall("([0-9]+) red" , line)
        green = re.findall("([0-9]+) green" , line)
        blue = re.findall("([0-9+]+) blue" , line)
        for cubes in red:
            if int(cubes) > limit['red']:
                game = False
        for cubes in green:
            if int(cubes) > limit['green']:
                game = False
        for cubes in blue:
            if int(cubes) > limit['blue']:
                game = False
        if game:
            possible.append(int(gid))
print(sum(possible))
#part 2
powers = []
with open ('AoC_2023_2.txt', 'r') as f:
    for line in f.readlines():
        red = re.findall("([0-9]+) red" , line)
        red = [int(i) for i in red]
        r = max(red)
        green = re.findall("([0-9]+) green" , line)
        green = [int(i) for i in green]
        g = max(green)
        blue = re.findall("([0-9+]+) blue" , line)
        blue = [int(i) for i in blue]
        b = max(blue)
        power = r * g * b
        powers.append(power)
print(sum(powers))
