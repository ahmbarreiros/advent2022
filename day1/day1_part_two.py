## PART ONE

with open("input.txt", "r") as f:
    max_calories = [0, 0, 0]
    temp = -1
    sum_of_calories = 0
    for line in f:
        max_calories.sort(reverse=True)
        if line.strip() == '':
            for i in range(len(max_calories)):
                if max_calories[i] < sum_of_calories and sum_of_calories not in max_calories:
                    temp = max_calories[i]
                    max_calories[i] = sum_of_calories
                    sum_of_calories = temp
            sum_of_calories = 0
        else:
            sum_of_calories += int(line)
            if int(line) > min(max_calories):
                lower = max_calories.index(min(max_calories))
                max_calories[lower] = int(line)
            
    print(sum_of_calories)
    print(max_calories)
    print(sum(max_calories))
