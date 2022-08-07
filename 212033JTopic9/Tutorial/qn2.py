# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# import pylistqueue as queue
# import pyliststack as stack

def reverseQueue(Q):
    S = stack.Stack()
    while not Q.isEmpty():
        S.push(Q.dequeue())
    while not S.isEmpty():
        Q.enqueue(S.pop())
