# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# enhancement: expanding the queue via multiplying the maxSize by 2

# Implementation of the Queue ADT using a circular array.
class Queue:
    # Creates an empty queue.
    def __init__(self, maxSize):
        self._limit = maxSize
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

    # enhancement: expanding the array
    def resize(self):
        # doubling the size of the array
        new_q = [None] * (self._limit * 2)
        old_q = self._qArray
        for i in range(len(old_q)):
            new_q[i] = old_q[i]
        # doubling the size of the array
        self._limit = self._limit * 2
        self._qArray = new_q

    def enqueue(self, item):
        # enhancement: expanding the circular array if full
        if self._count == self._limit:
            print("Cannot enqueue to a full queue. Expanding array now!")
            Queue.resize(self)

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

    # brackets[].
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

# more data inputs to implement enhancement code
q.enqueue(60)
q.enqueue(70)
q.enqueue(80)
q.enqueue(90)
q.enqueue(100)
q.enqueue(110)

print(q)

q.dequeue()
q.dequeue()

print(q)

q.enqueue(60)
q.enqueue(70)
print(q)


