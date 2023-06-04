with open("input.txt", "r") as f:
    total_score = 0
    for line in f:
        round_score = 0
        round = line.strip().split(" ")
        case_score = {
            ('A', 'X'): 3,
            ('B', 'X'): 1,
            ('C', 'X'): 2,
            ('A', 'Y'): 4,
            ('B', 'Y'): 5,
            ('C', 'Y'): 6,
            ('A', 'Z'): 8,
            ('B', 'Z'): 9,
            ('C', 'Z'): 7
        }
        
        round_score += case_score.get((round[0], round[1]), 0)
        
        print(round_score)
        total_score += round_score
            
    print(total_score)
        