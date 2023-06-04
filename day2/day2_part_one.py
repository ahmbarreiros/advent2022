with open("input.txt", "r") as f:
    total_score = 0
    for line in f:
        round_score = 0
        round = line.strip().split(" ")
        case_scores = {
            ('A', 'Y'): 6,
            ('B', 'Z'): 6,
            ('C', 'X'): 6,
            ('A', 'X'): 3,
            ('B', 'Y'): 3,
            ('C', 'Z'): 3
        }
        
        round_score += case_scores.get((round[0], round[1]), 0)
        
        if round[1] == 'X':
            round_score += 1
        elif round[1] == 'Y':
            round_score += 2
        else:
            round_score += 3
        
        print(round_score)
        total_score += round_score
            
    print(total_score)
        
# A = X = ROCK
# B = Y = PAPER
# C = Z = SCISSORS
