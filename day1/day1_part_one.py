## PART ONE

with open("input.txt", "r") as f:
    max_calories = 0
    sum_of_calories = 0
    for line in f:
        if line.strip() != "":
            sum_of_calories += int(line)
        else:
            sum_of_calories = 0
        if max_calories < sum_of_calories:
            max_calories = sum_of_calories
    print(max_calories)
