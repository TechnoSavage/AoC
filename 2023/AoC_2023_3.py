import re
from pprint import pprint

#Misunderstood the problem and started finding all numbers following a part symbol
# total = 0
# partNumbers = []
# with open ('AoC_2023_3.txt', 'r') as f:
#     schematic = f.read().replace('\n', '')
#     parts = re.findall("([\+\-\*\@\=\$\/\%\&\#]\.*[0-9]+)", schematic)
#     print(parts)
#     for part in parts:
#         pNo = re.findall("[0-9]+", part)
#         partNumbers.append(int(pNo[0]))
# print(sum(partNumbers))

# partNos = []
# partChars = ('+', '-', '*', '@', '=', '$', '%', '&', '#')
# with open ('AoC_2023_3.txt', 'r') as f:
#     schematic = f.read().replace('\n', '')
#     #140 lines
#     #140 characters per line
#     loc = 0
#     for char in schematic:
#         quadrant = []
#         if char in partChars:
#             quadrant.append(schematic[loc - 143: loc -136])
#             quadrant.append(schematic[loc - 3: loc + 4])
#             quadrant.append(schematic[loc + 137: loc + 144])
#         loc += 1
#         if len(quadrant) > 0:
#             if quadrant[0][3] == '.':
#                 tleft = quadrant[0][0:4]
#                 tright = quadrant[0][3:7]
#                 match1 = re.match("([1-9]{1}[0-9]{1,2})\.", tleft)
#                 match2 = re.match("\.([1-9]{1}[0-9]{1,2})", tright)
#                 if match1 is not None:
#                     partNos.append(match1[1])
#                 if match2 is not None:
#                     partNos.append(match2[1])
#             else:
#                  topMatch = re.search("\.{1,3}([0-9]{0,3})\.{1,3}", quadrant[0])
#                  if topMatch is not None:
#                      partNos.append(topMatch[1])
#             midMatch = re.match("(\.?[0-9]+)[\+\-\*\@\=\$\/\%\&\#]([0-9]+)", quadrant[1])
#             if midMatch is not None:
#                 partNos.append(midMatch[1])
#                 partNos.append(midMatch[2])
#             if quadrant[2][3] == '.':
#                 bleft = quadrant[2][0:3]
#                 bright = quadrant[2][3:6]
#                 match3 = re.match("([1-9]{1}[0-9]{1,2})\.", bleft)
#                 match4 = re.match("\.([1-9]{1}[0-9]{1,2})", bright)
#                 if match3 is not None:
#                     partNos.append(match3[1])
#                 if match4 is not None:
#                     partNos.append(match4[1])
#             else:
#                  bottomMatch = re.search("\.{1,3}([0-9]{0,3})\.{1,3}", quadrant[2])
#                  if bottomMatch is not None:
#                      partNos.append(bottomMatch[1])
# partNos = [int(i.replace('.', '')) for i in partNos]           
# # partNos = [int(i) for i in partNos if i != '']
# #print(partNos)
# print(sum(partNos))

#Ugly but it works
def seek(col, row, number, partChars, schematic):
    numSize = len(str(number))
    if schematic[col][row] in partChars:
        return True
    if row - numSize - 1 >= 0: 
        if schematic[col][row - numSize - 1] in partChars:
            return True
    if col - 1 >= 0:
        if schematic[col - 1][row] in partChars:
            return True
        if schematic[col - 1][row - 1] in partChars:
            return True
        if schematic[col - 1][row - 2] in partChars:
            return True
        if numSize >= 2:
            if schematic[col - 1][row - 3] in partChars:
                return True
        if numSize == 3:
            if schematic[col - 1][row - 4] in partChars:
                return True
    if col + 1 <= 139:
        if schematic[col + 1][row] in partChars:
            return True
        if schematic[col + 1][row - 1] in partChars:
            return True
        if schematic[col + 1][row - 2] in partChars:
            return True
        if numSize >= 2:
            if schematic[col + 1][row - 3] in partChars:
                return True
        if numSize == 3:
            if schematic[col + 1][row - 4] in partChars:
                return True
    return False

if __name__ == "__main__":
    partChars = ('+', '-', '*', '@', '=', '$', '%', '&', '#')
    criteria = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    partNos = []
    with open ('AoC_2023_3.txt', 'r') as f:
        schematic = f.read()
    schematic = [list(line) for line in schematic.split('\n')]
    #pprint(schematic)
    col = 0
    row = 0
    buffer = []
    while col <= 139:
        cursor = schematic[col][row]
        if cursor in criteria:
            buffer.append(cursor)
        else:
            if len(buffer) > 0:
                number = ''.join(buffer)
                print(number)
                part = seek(col, row, number, partChars, schematic)
                if part == True:
                    partNos.append(number)
                buffer = []
        row += 1
        if row > 139:
            col += 1
            row = 0
    partNos = [int(i) for i in partNos]
    #print(partNos)
    print(sum(partNos))