import unittest

from TimeEfficientBinaryTree import TimeEfficientBinaryTree
from MemoryEfficientBinaryTree import MemoryEfficientBinaryTree
from Node import Node
from NodeWithParent import NodeWithParent

class TestBinaryTree(object):

    def createExampleTree(self):
        binaryTree = self.getBinaryTree(self.getNode(7))

        binaryTree.insert(self.getNode(3), binaryTree.root, True)
        binaryTree.insert(self.getNode(4), binaryTree.root, False)
        binaryTree.insert(self.getNode(2), binaryTree.root.left, True)
        binaryTree.insert(self.getNode(5), binaryTree.root.left, False)
        binaryTree.insert(self.getNode(8), binaryTree.root.right, False)
        binaryTree.insert(self.getNode(1), binaryTree.root.left.left, True)
        binaryTree.insert(self.getNode(6), binaryTree.root.left.left, False)

        return binaryTree

    ###
    # insert tests
    ###
    def test_insertLeft(self):
        node1 = self.getNode(1)
        binaryTree = self.getBinaryTree(node1)

        # Node is inserted successfully
        node2 = self.getNode(2)
        binaryTree.insert(node2, binaryTree.root, True)
        self.assertEqual(binaryTree.root.left, node2)
        self.assertEqual(binaryTree.root.right, None)

        # Node cannot be inserted where one already exists
        node3 = self.getNode(3)
        with self.assertRaises(Exception):
            binaryTree.insert(node3, binaryTree.root, True)

    def test_insertRight(self):
        node1 = self.getNode(1)
        binaryTree = self.getBinaryTree(node1)

        # Node is inserted successfully
        node2 = self.getNode(2)
        binaryTree.insert(node2, binaryTree.root, False)
        self.assertEqual(binaryTree.root.right, node2)
        self.assertEqual(binaryTree.root.left, None)

        # Node cannot be inserted where one already exists
        node3 = self.getNode(3)
        with self.assertRaises(Exception):
            binaryTree.insert(node3, binaryTree.root, False)

    def test_insertDuplicate(self):
        pass

    ###
    # getNodeWithKey tests
    ###
    def test_getNodeWithKey(self):
        exampleTree = self.createExampleTree()
        self.assertEqual(exampleTree.getNodeWithKey(7, exampleTree.root), exampleTree.root)
        self.assertEqual(exampleTree.getNodeWithKey(3, exampleTree.root), exampleTree.root.left)
        self.assertEqual(exampleTree.getNodeWithKey(4, exampleTree.root), exampleTree.root.right)
        self.assertEqual(exampleTree.getNodeWithKey(2, exampleTree.root), exampleTree.root.left.left)
        self.assertEqual(exampleTree.getNodeWithKey(5, exampleTree.root), exampleTree.root.left.right)
        self.assertEqual(exampleTree.getNodeWithKey(8, exampleTree.root), exampleTree.root.right.right)
        self.assertEqual(exampleTree.getNodeWithKey(1, exampleTree.root), exampleTree.root.left.left.left)
        self.assertEqual(exampleTree.getNodeWithKey(6, exampleTree.root), exampleTree.root.left.left.right)

        # Non-existing key
        self.assertEqual(exampleTree.getNodeWithKey(9, exampleTree.root), None)

    ###
    # getParent tests
    ###
    def test_getParent(self):

        exampleTree = self.createExampleTree()
        self.assertEqual(exampleTree.getParent(exampleTree.root.key, exampleTree.root, None), None)
        self.assertEqual(exampleTree.getParent(exampleTree.root.left.key, exampleTree.root, None), exampleTree.root.key)
        self.assertEqual(exampleTree.getParent(exampleTree.root.right.key, exampleTree.root, None), exampleTree.root.key)
        self.assertEqual(exampleTree.getParent(exampleTree.root.left.left.key, exampleTree.root, None), exampleTree.root.left.key)
        self.assertEqual(exampleTree.getParent(exampleTree.root.left.right.key, exampleTree.root, None), exampleTree.root.left.key)
        self.assertEqual(exampleTree.getParent(exampleTree.root.right.right.key, exampleTree.root, None), exampleTree.root.right.key)
        self.assertEqual(exampleTree.getParent(exampleTree.root.left.left.left.key, exampleTree.root, None), exampleTree.root.left.left.key)
        self.assertEqual(exampleTree.getParent(exampleTree.root.left.left.right.key, exampleTree.root, None), exampleTree.root.left.left.key)

        self.assertEqual(exampleTree.getParent(9, exampleTree.root, None), None)

    ###
    # getAncestors tests
    ###
    def test_getAncestors(self):
        exampleTree = self.createExampleTree()

        self.assertEqual(exampleTree.getAncestors(exampleTree.root.key), [7])

        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.key), [3, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.right.key), [4, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.left.key), [2, 3, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.right.key), [5, 3, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.right.right.key), [8, 4, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.left.left.key), [1,2, 3, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.left.right.key), [6, 2, 3, 7])

        self.assertEqual(exampleTree.getAncestors(9), [9])

    def test_getLowestCommonAncestor(self):
        exampleTree = self.createExampleTree()

        self.assertEqual(exampleTree.getLowestCommonAncestor(exampleTree.root.left.left.right, exampleTree.root.left.right), 3)
        # One node is root
        self.assertEqual(exampleTree.getLowestCommonAncestor(exampleTree.root, exampleTree.root.right), exampleTree.root.key)
        # One ancestor is parent of another
        self.assertEqual(exampleTree.getLowestCommonAncestor(exampleTree.root.left, exampleTree.root.left.left), exampleTree.root.left.key)
        # Both nodes are the same
        self.assertEqual(exampleTree.getLowestCommonAncestor(exampleTree.root.right.right, exampleTree.root.right.right), exampleTree.root.right.right.key)

class TestTimeEfficientBinaryTree(TestBinaryTree, unittest.TestCase):
    getNode = staticmethod(NodeWithParent)
    getBinaryTree = staticmethod(TimeEfficientBinaryTree)

class TestMemoryEfficientBinaryTree(TestBinaryTree, unittest.TestCase):
    getNode = staticmethod(Node)
    getBinaryTree = staticmethod(MemoryEfficientBinaryTree)
