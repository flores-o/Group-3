import Node

class BinaryTree:

    def __init__(self, rootNode):
        self.root = rootNode

    def insert(self, childNode, parentNode, insertLeft):
        # TODO: Check if childNode.key is already in tree

        if insertLeft and parentNode.left == None:
            parentNode.left = childNode
        elif not(insertLeft) and parentNode.right == None:
            parentNode.right = childNode
        else:
            raise Exception("Cannot insert where a child already exists.")

    # https://www.tutorialspoint.com/python/python_tree_traversal_algorithms.htm
    # Using pre-order traversal
    def getNodeWithKey(self, key):
        # traverse tree until you find the key
        pass
