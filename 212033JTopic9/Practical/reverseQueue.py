# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

import pylistqueue as queue


# Implementation of the Queue ADT using a circular array.
class Queue:
    # Creates an empty queue.
    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = [None] * maxSize

    # Returns True if the queue is empty.
    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return len(self._qArray) == self._count

    # Returns the number of items in the queue.
    def __len__(self):
        return self._count

    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue."
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        item = self._qArray[0]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item
        # Return the content of the queue (with array index in square

    # brackets].
    def __str__(self):
        maxSize = len(self._qArray)
        outStr = ''
        for i in range(self._count):
            outStr += ('[' + str((self._front + i) % maxSize) + ']:')
            outStr += (str(self._qArray[(self._front + i) % maxSize]) + ' ')
        return outStr


q = Queue(10)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(q)

q.dequeue()
q.dequeue()

print(q)

q.enqueue(60)
q.enqueue(70)
print(q)

# test code
myQueue = queue.Queue()
for i in range(10, 60, 10):
    myQueue.enqueue(i)

print('The contents of the queue (BEFORE REVERSING): ')
print(myQueue)
