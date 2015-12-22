import unittest
from q_4_7 import *
from lib.HSTree import BinaryTreeNode

class testcase1(unittest.TestCase):

    def test_1(self):
        root = BinaryTreeNode.buildTree([1, 2, 3], [2, 1, 3])
        self.assertEqual(commonAncestor(root, root.left, root.right), root) 

    def test_2(self):
        root = BinaryTreeNode.buildTree([1, 2, 3], [3, 2, 1])
        self.assertEqual(commonAncestor(root, root.left, root.left.left), root.left) 

    def test_3(self):
        root = BinaryTreeNode.buildTree([1, 2, 3], [3, 2, 1])
        self.assertEqual(commonAncestor(root, root.left, root.left), root.left) 

    def test_4(self):
        root = BinaryTreeNode.buildTree([1, 2, 3], [2, 1, 3])
        self.assertEqual(commonAncestor(root, BinaryTreeNode(7), root.right), None) 

if __name__ == "__main__":
   unittest.main() 
