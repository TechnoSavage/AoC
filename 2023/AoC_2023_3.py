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
    partNos = []
    with open ('AoC_2023_3.txt', 'r') as f:
        schematic = f.read()
    schematic = [list(line) for line in schematic.split('\n')]
    col = 0
    row = 0
    buffer = []
    while col <= 139:
        cursor = schematic[col][row]
        if str.isdigit(cursor):
            buffer.append(cursor)
        else:
            if len(buffer) > 0:
                number = ''.join(buffer)
                part = seek(col, row, number, partChars, schematic)
                if part == True:
                    partNos.append(number)
                buffer = []
        row += 1
        if row > 139:
            col += 1
            row = 0
    partNos = [int(i) for i in partNos]
    print(sum(partNos))