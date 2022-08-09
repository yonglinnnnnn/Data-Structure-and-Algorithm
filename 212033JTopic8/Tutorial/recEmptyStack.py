# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

import pyliststack as stack


def recEmptyStack(S):
    if S.isEmpty():  # base case
        return S
    else:
        S.pop()
        recEmptyStack(S)


# test code
S = stack.Stack()

for i in range(10, 60, 10):
    S.push(i)

print('Before')
print('S: ', S._theItems)

recEmptyStack(S)

print('After')
print('S: ', S._theItems)
