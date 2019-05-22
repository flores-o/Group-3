import Node

class BinaryTree:

    def __init__(self, rootNode):
        self.root = rootNode

    def insert(self, childNode, parentNode, insertLeft):
        # TODO: Check if childNode.key is already in tree

        if insertLeft && parentNode.left = None:
            parentNode.left = childNode
        elif insertRight && parentNode.right = None:
            parentNode.right = childNode
        else:
            # TODO: throw an exception
            print("Error: Cannot insert where a child already exists.")
