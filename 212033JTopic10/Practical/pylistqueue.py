# implement of the Queue ADT using Python list


class Queue:
    # creates an empty list
    def __init__(self):
        self._qList = list()

    # returns True if the queue is empty
    def isEmpty(self):
        return len(self._qList) == 0

    # returns the number of items in the queue
    def __len__(self):
        return len(self._qList)

    # adds the given item to the queue
    def enqueue(self, item):
        self._qList.append(item)

    # removes and returns the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        return self._qList.pop(0)


# test code
if __name__ == '__main__':
    PROMPT = "Enter a number (ctrl-D to end): "
    myQueue = Queue()

    value = int(input(PROMPT))
    while True:
        try:
            myQueue.enqueue(value)
            value = int(input(PROMPT))
        except EOFError:
            break

    print('\nThe contents of the queue: ')
    while not myQueue.isEmpty():
        value = myQueue.dequeue()
        print(value, end=" ")
