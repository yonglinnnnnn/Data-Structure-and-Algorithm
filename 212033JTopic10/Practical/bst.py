# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


import pylistqueue as queue


# the storage class for creating binary tree nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# implement of the Binary Search Tree
class BinarySearchTree:
    # creates an initially empty BST
    def __init__(self):
        self._root = None
        self._size = 0

    # returns the total no of elements in BST
    def __len__(self):
        return self._size

    # insert new node into the BST
    def insertNode(self, new_node):
        if self._root is None:
            self._root = new_node
            self._size += 1
        else:
            self._recInsertNode(self._root, new_node)

    # helper method to insert new_node into the BST recursively from start_node
    def _recInsertNode(self, start_node, new_node):
        if start_node.data < new_node.data:
            if start_node.right is None:
                start_node.right = new_node
            else:
                self._recInsertNode(start_node.right, new_node)
        else:
            if start_node.left is None:
                start_node.left = new_node
                self._size += 1
            else:
                self._recInsertNode(start_node.left, new_node)

    # pre-order traversal of BST
    def preorderTrav(self):
        if self._root is None:
            print("Tree is empty")
        else:
            self._recPreorderTrav(self._root)

    # helper method to perform pre-order traversal of the given subtree recursively
    def _recPreorderTrav(self, subtree):
        if subtree is not None:
            print(subtree.data, end=" ")
            self._recPreorderTrav(subtree.left)
            self._recPreorderTrav(subtree.right)

    # in-order traversal of BST
    def inorderTrav(self):
        if self._root is None:
            print("Tree is empty")
        else:
            self._recInorderTrav(self._root)

    # helper method to perform in-order traversal of the given subtree recursively
    def _recInorderTrav(self, subtree):
        if subtree is not None:
            self._recPreorderTrav(subtree.left)
            print(subtree.data, end=" ")
            self._recPreorderTrav(subtree.right)

    # post-order traversal of the BST
    def postorderTrav(self):
        if self._root is None:
            print("Tree is empty")
        else:
            self._recPostorderTrav(self._root)

    # helper method to perform post-order traversal of the given subtree recursively
    def _recPostorderTrav(self, subtree):
        if subtree is not None:
            self._recPreorderTrav(subtree.left)
            self._recPreorderTrav(subtree.right)
            print(subtree.data, end=" ")

    # breadth-first traversal of BST
    def breadthfirstTrav(self):
        # create a queue and add the root node to it
        myQueue = queue.Queue()
        myQueue.enqueue(self._root)

        # visit each node in the tree
        while not myQueue.isEmpty():
            # remove the next node from the queue and visit it
            node = myQueue.dequeue()
            print(node.data, end=" ")

            # add the two children to the queue
            if node.left is not None:
                myQueue.enqueue(node.left)
            if node.right is not None:
                myQueue.enqueue(node.right)


# test code
if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insertNode(Node(60))
    bst.insertNode(Node(12))
    bst.insertNode(Node(90))
    bst.insertNode(Node(4))
    bst.insertNode(Node(41))
    bst.insertNode(Node(1))
    bst.insertNode(Node(100))
    bst.insertNode(Node(71))
    bst.insertNode(Node(29))
    bst.insertNode(Node(37))
    bst.insertNode(Node(84))
    bst.insertNode(Node(23))

    print(f'Size of BST: {len(bst)}')

    # pre-order
    print('\nPre-order Traversal of BST: ')
    print('==============================')
    bst.preorderTrav()

    # in-order
    print('\n\nIn-order Traversal of BST: ')
    print('==============================')
    bst.inorderTrav()

    # post-order
    print('\n\nPost-order Traversal of BST: ')
    print('==============================')
    bst.postorderTrav()

    # breadth-first traversal of BST
    print('\n\nBreadth-first Traversal of BST: ')
    print('==============================')
    bst.breadthfirstTrav()
