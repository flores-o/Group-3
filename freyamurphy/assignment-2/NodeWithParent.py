from Node import Node

class NodeWithParent(Node):
    """A binary tree node with an additional attribute for parent.

    Attributes:
        left: The Node which is the left child of this Node. Can be None.
        right: The Node which is the right child of this Node. Can be None.
        key: A unique identifier of any type for the Node.
        parent: The Node which is the parent of this Node.
    """

    def __init__(self, key):
        """Inits node with a key.

            Initially a NodeWithParent has no parent or children.
        """
        Node.__init__(self, key)
        self.parent = None
