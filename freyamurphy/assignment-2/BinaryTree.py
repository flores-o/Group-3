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

    # Return reference to Node with key
    # If key does not exist, return None
    # Based on pre-order traversal algorithm from:
    # https://www.tutorialspoint.com/python/python_tree_traversal_algorithms.htm
    def getNodeWithKey(self, key, startingNode):

        if startingNode is not None:
            if startingNode.key == key:
                return startingNode
            else:
                leftSubtree = self.getNodeWithKey(key, startingNode.left)
                if leftSubtree is not None:
                    return leftSubtree
                else:
                    return self.getNodeWithKey(key, startingNode.right)
