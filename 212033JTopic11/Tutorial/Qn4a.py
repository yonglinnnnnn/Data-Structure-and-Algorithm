# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def addAtEnd(self, item):
    # given the head and tail pointers, add ad item to a linked list
    newNode = ListNode(item)

    if self._head is None:
        head = newNode
    else:
        self.tail.next(newNode)
        self.tail = newNode

