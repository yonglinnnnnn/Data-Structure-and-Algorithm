# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

class Stack:
    def __init__(self):
        self._theItems = list()

    # returns true if the stack is empty or false otherwise
    def isEmpty(self):
        return True if len(self._theItems) == 0 else False

    #   return len(self) == 0

    # returns the number of items in the stack
    def __len__(self):
        return len(self._theItems)

    # returns the top item on the stack without removing it
    def peek(self):
        assert not self.isEmpty(), 'Cannot peek at an empty stack'
        return self._theItems[-1]

    # removes and returns the top item on the stack
    def pop(self):
        assert not self.isEmpty(), 'Cannot pop from an empty stack'
        return self._theItems.pop()

    # push an item onto the top of the stack
    def push(self, item):
        self._theItems.append(item)


# test code
if __name__ == '__main__':
    myStack = Stack()  # need to create instance of object
    try:
        while True:
            user_input = input('Enter a line (ctrl-D to stop): ')
            myStack.push(user_input)
    except EOFError:
        print('The contents of the stack:')
        while (myStack.isEmpty()) is False:
            print(myStack.peek())
            myStack.pop()
