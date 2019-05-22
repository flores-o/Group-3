import unittest

from BinaryTree import BinaryTree
from Node import Node

class testBinaryTree(unittest.TestCase):

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
