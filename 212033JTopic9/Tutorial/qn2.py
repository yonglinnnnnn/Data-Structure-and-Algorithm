# NAME: XU YONG LIN
# ADMIN NO: 212033J
# IT2154-01

import pylistqueue as queue
import pyliststack as stack

def reverseQueue(Q):
    S = stack.Stack()
    while not Q.isEmpty():
        S.push(Q.dequeue())
    while not S.isEmpty():
        Q.enqueue(S.pop())
