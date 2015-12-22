import unittest
from q_4_6 import *
from lib.HSTree import BinaryTreeNode

class testcase1(unittest.TestCase):

    def test_1(self):
        root = BinaryTreeNode.buildTree([1, 2, 3], [2, 1, 3])
        self.assertEqual(inOrderSuccessor(root.left).key, 1) 

    def test_2(self):
        root = BinaryTreeNode.buildTree([1, 2, 3], [2, 1, 3])
        self.assertEqual(inOrderSuccessor(root).key, 3) 

    def test_3(self):
        root = BinaryTreeNode.buildTree([1, 2, 3], [2, 1, 3])
        self.assertEqual(inOrderSuccessor(root.right), None) 

if __name__ == "__main__":
   unittest.main() 
