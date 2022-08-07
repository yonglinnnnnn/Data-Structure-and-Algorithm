# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


# recursive function to arrange a sequence of integer values
# so that all the even values appear before all the odd values
def organize_recurse(data, low, high):
    if low < high:
        if data[high] % 2 == 0:
            # swapping of values without temp variable
            data[low], data[high] = data[high], data[low]

            # data[low] is known to be even
            organize_recurse(data, low+1, high)

        else:
            # data[high] is known to be odd
            organize_recurse(data, low, high-1)


def organize(data):
    organize_recurse(data, 0, len(data) - 1)


# test code
list_of_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Original list: \t\t', list_of_num)

organize(list_of_num)
print('Organized list: \t\t', list_of_num)
