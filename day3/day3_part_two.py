#PART TWO

with open("input.txt", "r") as f:
    list_of_lines = []
    group_of_lines = []
    group_count = 1
    
    ## separate groups of elves
    for line in f:
        if line != '':
            group_of_lines.append([*line])
            if group_count % 3 == 0:
                list_of_lines.append(group_of_lines)
                group_of_lines = []
            group_count = group_count + 1
    
    ## iterate through them to get item type badge
    list_of_keys = []
    char_dict = {}
    for group in list_of_lines:
        char_dict = {}
        for j in range(len(group)):
            for k in range(len(group[j])):
                if group[j][k] != '\n':
                    if ((group[j][k] in group[0]) and (group[j][k] in group[1]) and (group[j][k] in group[2]) and (group[j][k] not in char_dict)):
                        ascii_num = ord(group[j][k])
                        if ascii_num - 96 > 0 and ascii_num - 96 < 27:
                            ascii_num = int(ascii_num - 96)
                        else:
                            if ascii_num - 38 < 53:
                                ascii_num = int(ascii_num - 38)
                        char_dict[group[j][k]] = ascii_num
        list_of_keys += char_dict.values()
    print(sum(list_of_keys))