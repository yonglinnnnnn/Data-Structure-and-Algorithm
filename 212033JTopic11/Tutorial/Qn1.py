# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# find second last node in the linked list
def findSecondLastNode(self):
    # initialise curNode pointer
    curNode = self.head

    # if the list is empty or contains less than 2 nodes
    if curNode is None or curNode.next is None:
        return None

    # traverse the linked list
    while curNode is not None:
        # if the current node is the second to last node, return current node
        if curNode.next.next is None:
            return curNode

        # if not, move to the next node
        curNode = curNode.next

