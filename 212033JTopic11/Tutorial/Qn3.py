# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# counts the number of nodes in linked list recursively
# given 'node' as starting node
def getCountRec(self, node):
    if (node is None):  # base case
        return 0
    else:
        return 1 + self.getCountRec(node.next)


# a wrapper over getCountRec()
def getCount(self):
    return self.getCountRec(self._head)
