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
