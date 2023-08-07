#PART ONE

with open("input.txt", "r") as f:
    half = 0
    num_of_items = []
    line_items = []
    for line in f:
        line_items = []
        half = len(line) // 2
        if line != "":
            for i in range(half):
                for j in range(half, len(line)):
                    if line[i] == line[j]:
                        if line[j] not in line_items:
                            line_items.append(line[j])
            num_of_items += line_items
    for i in range(len(num_of_items)):
        if ord(num_of_items[i]) - 96 > 0 and ord(num_of_items[i]) - 96 < 27:
            num_of_items[i] = int(ord(num_of_items[i]) - 96)
        else:
            if ord(num_of_items[i]) - 38 < 53:
                num_of_items[i] = int(ord(num_of_items[i]) - 38)
    print(sum(num_of_items))