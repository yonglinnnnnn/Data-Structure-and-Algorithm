# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# concatenate 2 lsits, L and M, given the first node of each list
# assuming L and M are not empty
def concatTwoLists(firstNodeOfL, firstNodeOfM):
    # initialise curNode to first node of L
    curNode = firstNodeOfL

    # find the last node in list L
    while curNode.next is not None:
        curNode = curNode.next

    # link the last node in list L to first node in list M
    curNode.next = firstNodeOfM

    # return the first node of L + M
    return firstNodeOfL
