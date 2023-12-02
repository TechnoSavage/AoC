coordinates = []
total = 0
with open ('AoC_2023_1.txt', 'r') as f:
    for line in f.readlines():
        tens = ''
        ones = ''
        for char in line:
            if str.isdigit(char) and tens == '':
                tens = char
            if str.isdigit(char):
                ones = char
        coordinates.append(tens + ones)
for coordinate in coordinates:
    total += int(coordinate)
print(total)
#part 2
coordinates = []
total = 0
num_strings = {'zero': '0', 
               'one': '1', 
               'two': '2', 
               'three': '3', 
               'four': '4', 
               'five': '5', 
               'six': '6', 
               'seven': '7', 
               'eight': '8', 
               'nine': '9'}
with open ('AoC_2023_1.txt', 'r') as f:
    for line in f.readlines():
        chars = []
        first = ''
        last = ''
        for char in line.strip():
            chars.append(char)
        queue = []
        for char in chars:
            if not str.isdigit(char):
                queue.append(char)
                for k,v in num_strings.items():
                        if k in ''.join(queue) and first == '':
                            first = v
            else:
                if first == '':
                    first = char
                last = char
                queue = []
        if len(queue) >= 3:
            while len(queue) > 2:
                    for k,v in num_strings.items():
                        if k in ''.join(queue):
                            last = v
                    queue.pop(0)
        coordinates.append(first + last)
for coordinate in coordinates:
    total += int(coordinate)
print(total)