from MemoryEfficientBinaryTree import MemoryEfficientBinaryTree
import NodeWithParent

class TimeEfficientBinaryTree(MemoryEfficientBinaryTree):
    """A binary tree made up of NodeWithParents.

        See BinaryTree.

        Since this tree uses nodes which store their parent, it uses more
        memory than MemoryEfficientBinaryTree but is more efficient at find the
        parents and ancestors of nodes.

        Attributes:
            root: The root NodeWithParent of the tree, which has no parent.
    """

    # Do I have to do this or is it included automatically?
    def __init__(self, rootNode):
        """Inits TimeEfficientBinaryTree with a root Node."""
        MemoryEfficientBinaryTree.__init__(self,rootNode)

    def insert(self, childNode, parentNode, insertLeft):
        """Adds a NodeWithParent to the binary tree.

        Args:
            childNode: The NodeWithParent to be added to the tree.
            parentNode: The NodeWithParent which childNode will be a child of.
            insertLeft: A boolean indicating whether to make childNode the left
                or right child of parentNode.

        Raises:
            Exception: Tried to add a child to a reference that was not None.
        """

        if insertLeft and parentNode.left == None:
            parentNode.left = childNode
            childNode.parent = parentNode
        elif not(insertLeft) and parentNode.right == None:
            parentNode.right = childNode
            childNode.parent = parentNode
        else:
            raise Exception("Cannot insert where a child already exists.")

    def getParent(self, key, startingNode, parent):
        """Gets a reference to the parent of a NodeWithParent with a specific key.

        Args:
            key: A unique identifier of the NodeWithParent whose parent we are searching
                for. Can be any type.
            startingNode: This node and its left and right subtree will be
                searched; the rest of the binary tree is ignored.
            parent: The the key of the parent NodeWithParent of startingNode.

        Returns:
            The key of the NodeWithParent which is the parent of the NodeWithParent being searched
            for. This can be any type.
            None if there is no NodeWithParent with the searched for key or if this NodeWithParent
            has no parent.
        """
        childNode = self.getNodeWithKey(key, startingNode)
        if childNode is not None and childNode.parent is not None:
            parentKey = childNode.parent.key
        else:
            parentKey = None
        return parentKey
