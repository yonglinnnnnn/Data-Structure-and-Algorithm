# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


from Qn1 import Stack


def transfer(S, T):
    while not S.isEmpty():
        T.push(S.pop())


# test code
S = Stack()
T = Stack()

for i in range(10, 60, 10):
    S.push(i)

print('Before')
print('S: ', S)
print('T: ', T)

transfer(S)

print('After')
print('S: ', S)
print('T: ', T)
