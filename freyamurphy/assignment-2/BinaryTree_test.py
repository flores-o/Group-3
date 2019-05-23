import unittest

from BinaryTree import BinaryTree
from Node import Node

class testBinaryTree(unittest.TestCase):

    def createExampleTree(self):
        binaryTree = BinaryTree(Node(7))

        binaryTree.insert(Node(3), binaryTree.root, True)
        binaryTree.insert(Node(4), binaryTree.root, False)
        binaryTree.insert(Node(2), binaryTree.root.left, True)
        binaryTree.insert(Node(5), binaryTree.root.left, False)
        binaryTree.insert(Node(8), binaryTree.root.right, False)
        binaryTree.insert(Node(1), binaryTree.root.left.left, True)
        binaryTree.insert(Node(6), binaryTree.root.left.left, False)

        return binaryTree

    ###
    # insert tests
    ###
    def test_insertLeft(self):
        node1 = Node(1)
        binaryTree = BinaryTree(node1)

        # Node is inserted successfully
        node2 = Node(2)
        binaryTree.insert(node2, binaryTree.root, True)
        self.assertEqual(binaryTree.root.left, node2)
        self.assertEqual(binaryTree.root.right, None)

        # Node cannot be inserted where one already exists
        node3 = Node(3)
        with self.assertRaises(Exception):
            binaryTree.insert(node3, binaryTree.root, True)

    def test_insertRight(self):
        node1 = Node(1)
        binaryTree = BinaryTree(node1)

        # Node is inserted successfully
        node2 = Node(2)
        binaryTree.insert(node2, binaryTree.root, False)
        self.assertEqual(binaryTree.root.right, node2)
        self.assertEqual(binaryTree.root.left, None)

        # Node cannot be inserted where one already exists
        node3 = Node(3)
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

        self.assertEqual(exampleTree.getAncestors(exampleTree.root.key), [])

        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.key), [7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.right.key), [7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.left.key), [3, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.right.key), [3, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.right.right.key), [4, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.left.left.key), [2, 3, 7])
        self.assertEqual(exampleTree.getAncestors(exampleTree.root.left.left.right.key), [2, 3, 7])

        self.assertEqual(exampleTree.getAncestors(9), [])

        # Example from brief
        self.assertEqual(exampleTree.getAncestors(6), [2, 3, 7])
