# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


class Queue:
    # Creates an empty queue.
    def __init__(self):
        self._qList = list()

    # Returns True if the queue is empty.

    def isEmpty(self):
        return len(self._qList) == 0

    # Returns the number of items in the queue.

    def __len__(self):
        return len(self._qList)

    # Adds the given item to the queue.

    def enqueue(self, item):
        self._qList.append(item)

    # Removes and returns the first item in the queue.

    def dequeue(self):
        assert not self.isEmpty(), \
            "Cannot dequeue from an empty queue."
        return self._qList.pop(0)


# test code
if __name__ == '__main__':
    myQueue = Queue()  # need to create instance of object
    PROMPT = 'Enter a line (ctrl-D to stop): '
    value = int(input(PROMPT))

    while True:
        try:
            myQueue.enqueue(value)
            value = int(input(PROMPT))
        except EOFError:
            break

    print('\nThe contents of the queue:')
    while not myQueue.isEmpty():
        value = myQueue.dequeue()
        print(value)
