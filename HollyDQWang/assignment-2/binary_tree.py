
class BinaryTreeNode(object):
    """
    Represent a node in Binary Tree.

    This class provides properties for current node instance, and the binary 
    tree in which the node is the root of. 
    When a docstring in this class mentions “binary tree”, it is referring to
    the current node and its descendants

    Attributes:
    val: the key carried by this node
    left: left subtree of this node. None if such left subtree doesn't exist.
    right: right subtree of this node. None if such right subtree doesn't exist.
    """

    # Constructor to create a new tree node
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def find_node(btree, key):
    """
    Given a binary tree and a key, returns a reference to the node with
    that key in the tree.

    Args:
        btree: a binary tree instance
        key: the specific key to look for within btree.

    Returns:
        a reference to the node with key in btree. Each reference is an instance
        of a BinaryTreeNode object.
        For example: for the given btree
                                    10
                                   /   \
                                  5     40
                                /  \      \
                               1    7      50
        find_node(btree, 1) would return a reference to the node on lower left.
        Return None if given key is not presented in the tree.
    """
    if btree is None:
        return None
    if btree.val == key:
        return btree

    left_ans = find_node(btree.left, key)
    right_ans = find_node(btree.right, key)

    return left_ans if left_ans is not None else right_ans


def in_tree(btree, key):
    """
    Helper Function: for a binary tree and a key, returns True if the node with 
    that key is presented in the tree, return False otherwise.

    Args:
        btree: a binary tree instance
        key: the specific key to look for within btree.

    Returns:
        a reference to the node with key in btree. Each reference is an instance
        of a BinaryTreeNode object.
        For example: for the given btree
                                    10
                                   /   \
                                  5     40
                                /  \      \
                               1    7      50
        in_tree(btree, 1) would return True
        in_tree(btree, 20) would return False
    """
    if btree is None:
        return False
    if btree.val == key:
        return True
    return in_tree(btree.left, key) or in_tree(btree.right, key)


def find_ancestor(btree, key):
    """
    Given a binary tree and a key, returns all the ancestors of the node with
    that key in the given binary tree.

    Args:
        btree: a binary tree instance
        key: the specific key to look for within btree.

    Returns:
        a list of all the ancestors of the node with that key in the
        given binary tree. In other words, return a list of chosen keys.
        For example: for the given btree
                                    10
                                   /   \
                                  5     40
                                /  \      \
                               1    7      50
        find_ancestor(btree, 1) would return [5, 10]
        Return [] if given key is not presented in the tree.
    """
    if not in_tree(btree, key):
        return []
    if btree.val == key:
        return []

    left_ans = find_ancestor(btree.left, key)
    right_ans = find_ancestor(btree.right, key)
    return left_ans + [btree.val] if left_ans != [] else right_ans + [btree.val]


def find_lc_ancestor(btree, key1, key2):
    """
    Given a binary tree and 2 keys, find their lowest common ancestor.
    Args:
        btree: a binary tree instance
        key1: one of the keys to look for within btree.
        key2: another keys to look for within btree.

    Returns:
        a reference to the lowest ancestor shared by the two nodes with specified
        key1 and key2.
                                    10
                                   /   \
                                  5     40
                                /  \      \
                               1    7      50
        find_ancestor(btree, 1, 7) would return the reference to node 5
        find_ancestor(btree, 10, 10) would return the reference to node 10
        find_ancestor(btree, 1, 10) would return the reference to node 10
        find_ancestor(btree, 5, 50) would return the reference to node 10

        return None if either of the keys is not in btree.
    """
    if btree is None:
        return None

    if btree.val == key1 or btree.val == key2:
        return btree

    left_lca = find_lc_ancestor(btree.left, key1, key2)
    right_lca = find_lc_ancestor(btree.right, key1, key2)

    if left_lca and right_lca:
        return btree

    return left_lca if left_lca is not None else right_lca


def main():
    """
    Construct a binary tree for testing
    For reference: 
             20
            /  \
           8    22
          / \   
         4  12 
            / \
           10 14
    """
    root = BinaryTreeNode(20)

    root.left = BinaryTreeNode(8)
    root.right = BinaryTreeNode(22)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(12)
    root.left.right.left = BinaryTreeNode(10)
    root.left.right.right = BinaryTreeNode(14)

    # find_node tests
    key1 = 8
    node1 = find_node(root, key1)
    assert node1.val == 8

    key2 = 50
    node2 = find_node(root, key2)
    assert node2 is None

    key3 = 14
    node3 = find_node(root, key3)
    assert node3.val == 14

    # find_ancestor tests
    ance1 = find_ancestor(root, 8)
    assert ance1 == [20]

    ance2 = find_ancestor(root, 14)
    assert ance2 == [12, 8, 20]

    ance3 = find_ancestor(root, 50)
    assert ance3 == []

    ance4 = find_ancestor(root, 20)
    assert ance4 == []

    # find_lc_ancestor tests
    key1 = 10
    key2 = 14
    t = find_lc_ancestor(root, key1, key2)
    assert t.val == 12

    key1 = 14
    key2 = 8
    t = find_lc_ancestor(root, key1, key2)
    assert t.val == 8

    key1 = 10
    key2 = 22
    t = find_lc_ancestor(root, key1, key2)
    assert t.val == 20


if __name__ == "__main__":
    main()
