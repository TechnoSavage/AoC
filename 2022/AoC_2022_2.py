# A = Opponent Rock
# B = Opponent Paper
# C = Opponent Scissors
# X = Player Rock
# Y = Player Paper
# Z = Player Scissors

def judgement(opponent, player):
    """
    Determine winner of rock, paper, scissors and score

    :param opponent: A string, oppoents choice
    :param player: A string, players choice
    :returns: An integer, scoring for round """
    roundScore = 0
    rock = ('A', 'X', 1)
    paper = ('B', 'Y', 2)
    scissors = ('C', 'Z', 3)
    loss = ('BX', 'CY', 'AZ', 0)
    draw = ('AX', 'BY', 'CZ', 3)
    win = ('CX', 'AY', 'BZ', 6)
    if player in rock:
        roundScore += rock[-1]
    elif player in paper:
        roundScore += paper[-1]
    elif player in scissors:
        roundScore += scissors[-1]
    else:
        pass
    if opponent + player in loss:
        roundScore += loss[-1]
    elif opponent + player in draw:
        roundScore += draw[-1]
    elif opponent + player in win:
        roundScore += win[-1]
    else:
        pass
    return roundScore


playerScore = 0
rounds = []
with open('AoC_2022_2.txt', 'r') as bouts:
    for line in bouts:
        rounds.append(line.strip('\n'))
for item in rounds:
    sep = item.split()
    opponent = sep[0]
    player = sep[1]
    result = judgement(opponent, player)
    playerScore += result
print(playerScore)

    
    