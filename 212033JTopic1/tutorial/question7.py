def num_check(input_num):
    list = []
    for i in range(len(input_num)):
        if input_num[i] not in list:
            list.append(input_num[i])
        else:
            return "numbers are not distinct!"
            break
    return f'numbers are distinct!'


# alternative method - Ashlee method
def checker(list):
    pop = []  # list to store in unique numbers
    i = 0
    for i in range(len(list)):
        # print(f'line 16: {i}')
        for j in range(i + 1, len(list)):
            if i == j:
                pop.append(i)
                print(pop)
    if len(pop) == len(list):
        return 'the numbers are not distinct!'
    else:
        return 'the numbers are distinct'


num_list = [2, 3, 4, 5, 3, 23, 10]
print(num_check(num_list))

print(checker([2, 3, 4, 5, 23, 10]))
