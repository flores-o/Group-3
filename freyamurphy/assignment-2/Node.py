# Based on tutorial from:
# https://www.tutorialspoint.com/python/python_binary_tree.htm

class Node:
    """A node in a BinaryTree.

    Attributes:
        left: The Node which is the left child of this Node. Can be None.
        right: The Node which is the right child of this Node. Can be None.
        key: A unique identifier of any type for the Node.
    """

    def __init__(self, key):
        """Inits Node with key.

        Initially a Node has no children.
        """
        self.left = None
        self.right = None
        self.key = key
