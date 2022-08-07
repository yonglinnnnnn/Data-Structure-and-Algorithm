# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


# non recursive
def exp(x, n):
    total = 1
    for i in range(n):
        total = total * x
    return total


print('non-recursive: ', exp(2, 8))


# recursive
def exp_recursive(x, n):
    # base case: n == 0
    if n == 0:
        return 1
    else:
        # x * (x * x) ...
        return x * exp_recursive(x, n-1)


print('recursive: ', exp_recursive(2, 8))
