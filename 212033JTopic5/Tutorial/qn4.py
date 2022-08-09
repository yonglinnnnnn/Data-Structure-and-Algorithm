# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# enhancement: checks a number if it is a palindrome recursively


def isPalindrone(aStr):
    if len(aStr) <= 1:
        return True
    else:
        return aStr[0] == aStr[-1] and isPalindrone(aStr[1: len(aStr) - 1])


print('madam: ', isPalindrone('madam'))

print('===Enhancement===')


def check_palindrome(n):
    # print(f'checking: {n}')

    # base case
    if n < 10:
        return True

    last = n % 10  # returns last digit in the number
    first = n
    places = 0
    # if n is larger than 10
    while first >= 10:
        places += 1
        # floor division of 10 => eg 121 // 10 = 12
        first = first // 10

    if first == last:
        new_num = (n - first * 10 ** places) // 10
        return check_palindrome(new_num)
    return False


print('1221: ', check_palindrome(1221))
print('131: ', check_palindrome(131))
print('132: ', check_palindrome(132))
