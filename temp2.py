# without recursion
# def SumEvenWORecur(n):
#     total = 0
#     for i in range(n):      # change this part to recursion
#         if i % 2 == 0:
#             total += i
#     return total

# def SumEven(n):
#     if n == 0:
#         return 0
#     else:
#         if n % 2 == 0:
#             return n + SumEven(n-1)
#         else:
#             return SumEven(n - 1)

# print(SumEven(9))

def numPalindrome(x):
    x = str(x)
    if len(x) < 2:
        return True
    else:
        return x[0] == x[-1] and numPalindrome(x[1: len(x) - 1])

# print(numPalindrome(1324231))


def numPalindrome2(n):
    # print(n)
    if n < 10:
        return True

    last = n % 10
    first = n
    places = 0
    while first >= 10:
        places += 1
        first = first // 10
        # print(first)

    if first == last:
        new_num = (n - first * 10 ** places) // 10
        return numPalindrome2(new_num)

    return False


print(numPalindrome2(-1221))
print(numPalindrome2(-131))
print(numPalindrome(-132))

# tut qn1


def fib(n):
    # base case
    if n == 1 or n == 0:
        return n

    else:
        return fib(n - 1) + fib(n - 2)


for i in range(12):
    print(fib(i), end=' ')

# tut qn1
# def main():
#     # computer and print the sum of (1 + 2 + ... + 10)
#     print()
#     print(sum(10))

# def sum(x):
#     # base case
#     if x == 1:
#         return 1
#     # assuming x >= 1
#     else:
#         return x + sum(x - 1)

# main()


# tut qn2
# def sumDigits(n):
#     # base case
#     if n < 10:
#         return int(n)
#     else:
#         return n % 10 + int(sumDigits(n / 10))

# print(sumDigits(368))

# tut qn3
# def main():
#     y = foo(4)
#     bar(2)

# def foo(x):
#     if x % 2 != 0:
#         return 0
#     else:
#         return x + foo(x - 1)

# def bar(n):
#     if n > 0:
#         bar(n - 1)
#         print(n)
# main()


# qn 4
def isPalindrome(aStr):
    if len(aStr) <= 1:
        return True
    else:
        return aStr[0] == aStr[-1] and isPalindrome(aStr[1:-1])


print(isPalindrome('madam'))

# tut qn 5


def exp(x, n):
    total = 1
    for i in range(n):
        total = total * x
    return total


def exp_recursive(x, n):
    # base case:
    if n == 1:
        return x
    else:
        # x * (x * (x * x))
        return x * exp_recursive(x, n-1)


# practice qn

def SumEven(n):
    # 2 + 4 + 6 + 8
    if n <= 1:
        return 0
    else:
        if n % 2 == 0:  # if n is even
            return n + SumEven(n - 2)
        else:  # if n is odd
            return SumEven(n - 1)


# print(SumEven(9))


# n (n-1) (n-2) (n-3)... 0... (n-3) (n-2) (n-1)

def Sequence(x):
    if x == 0:
        return str(0)
    else:
        return str(x) + ' ' + Sequence(x-1) + ' ' + str(x)


print(Sequence(3))


def pattern(num):
    if num == 1:
        return '*'
    else:
        return (pattern(num-1)) + '\n' + '*' * num + '\n*'


print(pattern(2))

# def take2(n):
#     if n == 0:
#         return str(0)
#     else:
#         return take2(n - 1) + ' ' + str(n) + ' ' + take2(n - 1)

# print(take2(3))
