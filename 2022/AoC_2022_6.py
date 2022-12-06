tran = []
with open('AoC_2022_6.txt', 'r') as transmission:
    for line in transmission:
        tran.append(line.strip('\n'))
tran = tran[0]
sliceStart, sliceEnd = 0, 4
answer = ''
while len(tran) > 0:
    init = tran[sliceStart:sliceEnd]
    if len(set(init)) == len(init):
        answer = sliceEnd
        break
    sliceStart += 1 
    sliceEnd += 1
print(answer) 
    