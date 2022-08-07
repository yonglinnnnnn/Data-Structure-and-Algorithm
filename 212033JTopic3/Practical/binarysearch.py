# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# part a
def BinarySearchPartA(theValues, target):
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (high + low) // 2
        if theValues[mid] == target:
            return mid
        elif theValues[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "not found"


# part b
def BinarySearchPartB(theValues, target):
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (high + low) // 2
        # changed this part from part a
        if theValues[mid] == target:
            # decrease the mid value to check if it is the same as target
            while theValues[mid - 1] == target:
                mid -= 1
            return mid

        # smaller
        elif theValues[mid] < target:
            low = mid + 1

        # larger
        else:       #theValues[mid] > target
            high = mid - 1
    return "not found"


# test code
l = [-1, 2, 3, 4, 4, 4, 5, 6, 6, 7]

# part a
print(BinarySearchPartA(l, -1))

# part b
target = 4
index = BinarySearchPartB(l, target)
if index != -1:
    print(f'first occurrence of {target} is {index}')
else:
    print('not found')
