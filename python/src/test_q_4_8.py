import unittest
from q_4_8 import *
from lib.HSTree import BinaryTreeNode

class testcase1(unittest.TestCase):
    
    tests = [
        #t1 pre, t1 inorder, t2 pre, t2 inorder
        ([1, 2, 4, 3, 5], [4, 2, 1, 5, 3], [2, 4], [4, 2], True),
        ([1, 2, 4, 3, 5], [4, 2, 1, 5, 3], [2, 4], [2, 4], False)
    ]

    def test_1(self):
        for test in self.tests:
            t1 = BinaryTreeNode.buildTree(test[0], test[1])
            t2 = BinaryTreeNode.buildTree(test[2], test[3])
            self.assertEquals(isSubtree(t1, t2), test[4])
if __name__ == "__main__":
   unittest.main() 
