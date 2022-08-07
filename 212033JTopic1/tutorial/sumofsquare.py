# question 2
def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        # print(i)
        total += i ** 2
    return total


# number of arguments must be equal to the number of parameters
print('question2',sum_of_squares(4))


# question 3, dont use the modulus operator in implementing your solution
def sum_of_squares2(k):
    total = 0
    for i in range(1, k+1):
        # if int(i/2) * 2 != i:
        #     print(i)
        #     total += i*i
        if i in range(1, k+1, 2):
            # print(i)
            total += i*i
    return total


print(sum_of_squares2(4))
