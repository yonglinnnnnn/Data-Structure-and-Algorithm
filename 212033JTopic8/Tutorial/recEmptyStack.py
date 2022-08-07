# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

from Qn1 import Stack


def recEmptyStack(S):
    if S.isempty():  # base case
        return S
    else:
        S.pop()
        recEmptyStack(S)


# test code
S = Stack()

for i in range(10, 60, 10):
    S.push(i)

print('Before')
print('S: ', S)

recEmptyStack(S)

print('After')
print('S: ', S)
