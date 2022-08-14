# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

def removeNode(self, target):
    assert not self.isEmpty(), "cannot remove from an empty linked list"

    # given the head and tail references, remove a target from a linked list
    predNode = None
    curNode = self._head

    while curNode is not None and curNode.data != target:
        predNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode is self._head:
            head = curNode.next
        else:
            predNode.next = curNode.next

        if curNode is self._tail:
            self._tail = predNode
