# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

import pyliststack as stack


def transfer(S, T):
    while not S.isEmpty():
        T.push(S.pop())


# test code
S = stack.Stack()
T = stack.Stack()

for i in range(10, 60, 10):
    S.push(i)

print('Before')
print('S: ', S._theItems)
print('T: ', T._theItems)

transfer(S, T)

print('After')
print('S: ', S._theItems)
print('T: ', T._theItems)
