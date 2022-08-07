# Xu Yong Lin
# 212033J
# IT2153 - 01


# The storage class for creating linked list nodes
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Implementation of the Singly Linked List
class SinglyLinkedList:
    # Constructs an empty linked list
    def __init__(self):
        self._head = None
        self._size = 0

    # Returns True if the linked list is empty.
    def isEmpty(self):
        return self._size == 0

    # Returns the total number of items in the linked list
    def __len__(self):
        return self._size

    # Prepend an item to the linked list

    def addFirst(self, data):
        # Create new node to be added
        newNode = ListNode(data)
        # Adjust linked list references
        newNode.next = self._head
        self._head = newNode
        # Adjust linked list size
        self._size += 1

    # Remove (and return) the first item from the linked list
    def removeFirst(self):
        assert not self.isEmpty(), "Cannot remove from an empty linked list."
        # Use tempNode to store the node to be removed
        # Adjust linked list references
        tempNode = self._head
        self._head = self._head.next
        tempNode.next = None
        # Adjust linked list size
        self._size -= 1
        # Return the removed node (or None if linked list is empty)
        return tempNode

    # Remove (and return) a target item from the linked list
    def removeNode(self, target):
        assert not self.isEmpty(), "Cannot remove from an empty linked list."

        # Initialise predNode and curNode pointers
        predNode = None
        curNode = self._head
        # Search for the target item
        while curNode is not None and curNode.data != target:
            predNode = curNode
            curNode = curNode.next

        # If target is found, curNode is pointing at node to be removed
        if curNode is not None:
            # If target is the head of the linked list
            if curNode is self._head:
                self._head = curNode.next
                curNode.next = None
            else:
                predNode.next = curNode.next
                curNode.next = None

            # Adjust linked list size
            self._size -= 1

            # Return the removed node (or None if target is not found)
            return curNode

    # Return the content of the linked list
    def __str__(self):
        outStr = ''
        curNode = self._head
        while curNode is not None:
            outStr += str(curNode.data) + " "
            curNode = curNode.next
        return outStr


# test code
if __name__ == '__main__':
    myLL = SinglyLinkedList()
    for i in range(10, 60, 10):
        myLL.addFirst(i)

    print("List content (F-->B): ", myLL, "\n")

    removedNode = myLL.removeFirst()
    if removedNode is None:
        print("No node removed from linked list!")
    else:
        print("Removed node: ", removedNode.data)

    print("List content (F-->B): ", myLL, "\n")

    removedNode = myLL.removeNode(30)

    if removedNode is None:
        print("No node removed from linked list!")
    else:
        print("Removed node: ", removedNode.data)

    print("List content (F-->B): ", myLL, "\n")
    removedNode = myLL.removeNode(100)

    if removedNode is None:
        print("No node removed from linked list!")
    else:
        print("Removed node: ", removedNode.data)

    print("List content (F-->B): ", myLL, "\n")
