# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


# in class
def fib(n):
    assert n >= 0, "Fibonacci not defined for n < 0"

    if n == 0 or n == 1:  # base case
        return n

    else:  # recursion case n>1, recursion method must work towards its base case
        return fib(n - 1) + fib(n - 2)
    # if the program does not work towards the base?
    #     - stack memory will be out (memory overflow)


# test code
print(fib(12))
for i in range(12):
    print(fib(i), end=" ")
