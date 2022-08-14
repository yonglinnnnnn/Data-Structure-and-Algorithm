# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


def sequentialSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
        elif theValues[i] > target:
            return False
    return False  # If not found, return False

# test code
l = [-1, 2, 3, 4, 5, 6, 7, 11, 15, 19]
l2 = [9, 2, 3, 4, 5, 6, 7, 11, 9, 19]


# part a
print(sequentialSearch(l, 3))
print(sequentialSearch(l2, 3))

