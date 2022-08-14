# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

import pylistqueue as queue

# qn 1a
myQueue = queue.Queue()
for i in range(16):
    if i % 3 == 0:
        myQueue.enqueue(i)

print('qn 1a: ', myQueue._qList)

# qn 1b
q2 = queue.Queue()
for i in range(16):
    if i % 3 == 0:
        q2.enqueue(i)
    elif i % 4 == 0:
        q2.dequeue()
print('qn 1b: ',q2._qList)

# qn 1c:
queue3 = queue.Queue()
for i in range(16):
    if i % 3 == 0:
        queue3.enqueue(i)
        queue3.enqueue(i + 1)
    elif i % 4 ==0:
        queue3.dequeue()

print('qn 1c: ', queue3._qList)


# qn 1d
q4 = queue.Queue()
for i in range(16):
    if i % 4 == 0:
        q4.dequeue()
    elif i % 3 == 0:
        q4.enqueue(i)
print('qn 1d:', q4._qList)
#  >>> assertion error: cannot dequeue from empty queue

