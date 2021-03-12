
def combine(list_one, list_two):
    new_list = []
    count = 0

    if len(list_one) >= len(list_two):
        for i in list_one:
            new_list.append(i)
            if count <= len(list_two) - 1:
                new_list.append(list_two[count])
            count += 1
        print(new_list)
    else:
        for i in list_two:
            new_list.append(i)
            if count <= len(list_one) - 1:
                new_list.append(list_one[count])
            count += 1
        print(new_list)

combine([11, 22, 33, 44, 55], [1, 2, 3])

