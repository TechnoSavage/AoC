# A = Opponent Rock
# B = Opponent Paper
# C = Opponent Scissors
# X = Player loses
# Y = Player draws
# Z = Player wins

def judgement(opponent, player):
    """
    Determine winner of rock, paper, scissors and score

    :param opponent: A string, oppoents choice
    :param player: A string, players choice
    :returns: An integer, scoring for round """
    roundScore = 0
    scoring = {'A': 1, 'B': 2, 'C': 3}
    if player == 'X' and opponent == 'A':
        roundScore += 0 + 3
    elif player == 'X' and opponent != 'A':
        roundScore += 0 + scoring[opponent] - 1
    elif player == 'Y':
        roundScore += 3 + scoring[opponent]
    elif player == 'Z' and opponent != 'C':
        roundScore += 6 + scoring[opponent] + 1
    elif player == 'Z' and opponent == 'C':
        roundScore += 6 + 1
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