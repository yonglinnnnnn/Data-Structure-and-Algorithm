# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# using both stack and queue to reverse the queue.

import pylistqueue as queue
import pyliststack as stack

def reverseQueue(Q):
    S = stack.Stack()
    while not Q.isEmpty():
        S.push(Q.dequeue())
    while not S.isEmpty():
        Q.enqueue(S.pop())

# test code
myQueue = queue.Queue()
for i in range(10,60,10):
    myQueue.enqueue(i)

# print('The contents of the queue (BEFORE REVERSING): ')
# while not myQueue.isEmpty():
#     value = myQueue.dequeue()
#     print(value)

print('Contents of the queue (AFTER REVERSING):')
reverseQueue(myQueue)
while not myQueue.isEmpty():
    value = myQueue.dequeue()
    print(value)
