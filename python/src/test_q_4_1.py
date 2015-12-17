import unittest
from q_4_1 import *

class testcase1(unittest.TestCase):
    tests = [
        ([1, 2, 3], [2, 1, 3], True),
        ([1, 2, 3, 4], [2, 1, 4, 3], True),
        ([1, 2, 3, 4, 5], [2, 1, 4, 5, 3], False)
    ]

    def test1(self):
        for test in self.tests:
            btree = BinaryTreeNode.buildTree(test[0], test[1])
            self.assertEqual(isBalanced(btree), test[2])

if __name__ == "__main__":
   unittest.main() 
