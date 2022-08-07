# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


def isPalindrone(aStr):
    if len(aStr) <= 1:
        return True
    else:
        return aStr[0] == aStr[-1] and isPalindrone(aStr[1: len(aStr) - 1])


print(isPalindrone('madam'))
