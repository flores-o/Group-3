import Node

class BinaryTree:
    """A binary tree made up of Nodes.

    Each Node has up to two children.

    Attributes:
        root: The root Node of the tree, which has no parent.
    """

    def __init__(self, rootNode):
        """Inits BinaryTree with a root Node."""
        self.root = rootNode

    def insert(self, childNode, parentNode, insertLeft):
        """Adds a Node to the binary tree.

        Args:
            childNode: The Node to be added to the tree.
            parentNode: The Node which childNode will be a child of.
            insertLeft: A boolean indicating whether to make childNode the left
                or right child of parentNode.

        Raises:
            Exception: Tried to add a child to a reference that was not None.
        """
        # TODO: Check if childNode.key is already in tree.
        # TODO: Check if parentNode is actually part of the tree.

        if insertLeft and parentNode.left == None:
            parentNode.left = childNode
        elif not(insertLeft) and parentNode.right == None:
            parentNode.right = childNode
        else:
            raise Exception("Cannot insert where a child already exists.")

    def getNodeWithKey(self, key, startingNode):
        """Gets a reference to the Node with a specific key.

        Based on pre-order traversal algorithm from:
        https://www.tutorialspoint.com/python/python_tree_traversal_algorithms.htm

        Args:
            key: The unique Node identifier to search for. Can be any type.
            startingNode: This Node and its left and right subtree will be
                searched; the rest of the binary tree is ignored.

        Returns:
            A reference to the Node with attribute key equal to parameter key.
            None if there is no suitable Node is found.
        """

        if startingNode is not None:
            if startingNode.key == key:
                return startingNode
            else:
                leftSubtree = self.getNodeWithKey(key, startingNode.left)
                if leftSubtree is not None:
                    return leftSubtree
                else:
                    return self.getNodeWithKey(key, startingNode.right)

    def getParent(self, key, startingNode, parent):
        """Gets a reference to the parent of a Node with a specific key.

        Args:
            key: A unique identifier of the Node whose parent we are searching
                for. Can be any type.
            startingNode: This node and its left and right subtree will be
                searched; the rest of the binary tree is ignored.
            parent: The parent Node of startingNode.

        Returns:
            A reference to a Node which is the parent of the Node with attribute
            key equal to parameter key.
            None if there is no Node with the searched for key or if this Node
            has no parent.
        """

        if startingNode is not None:
            if startingNode.key == key:
                if parent is not None:
                    return parent.key
                else:
                    return None
            else:
                leftSubtree = self.getParent(key, startingNode.left, startingNode)
                if leftSubtree is not None:
                    return leftSubtree
                else:
                    parent = startingNode
                    return self.getParent(key, startingNode.right, startingNode)


    def getAncestors(self, key):
        """ Gets a list containing all ancestors of the Node with a specified
            key.

        Args:
            key: The key of the Node to get the ancestors of. Can be any type.

        Returns:
            A list of keys of the ancestors of the Node with attribute key equal
            to parameter key.
        """

        parent = self.getParent(key, self.root, None)

        if parent is None:
            return []
        else:
            parentAncestors = self.getAncestors(parent)
            myAncestors = [parent] + parentAncestors

            return myAncestors
