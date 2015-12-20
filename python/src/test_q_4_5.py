import unittest
from q_4_5 import *
from lib.HSTree import BinaryTreeNode

class testcase1(unittest.TestCase):
    tests = [
        ([1, 2, 3], [2, 1, 3], True),
        ([1, 2, 5, 3], [2, 1, 5, 3], False),
    ]

    def test_1(self):
        for test in self.tests:
            root = BinaryTreeNode.buildTree(test[1], test[0])
            self.assertEqual(isBST(root), test[2])
            self.assertEqual(isBST2(root), test[2])

if __name__ == "__main__":
   unittest.main() 
