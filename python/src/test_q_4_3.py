import unittest
from q_4_3 import *
from lib.HSTree import BinaryTreeNode

class testcase1(unittest.TestCase):
    tests = [
        ([3, 7, 9], [7, 3, 9]),
        ([1, 2, 3, 4], [2, 1, 3, 4])
    ]

    def test1(self):
        i = 0
        for test in self.tests:
            node = createBSTWrapper(test[0])
            self.assertTrue(list(BinaryTreeNode.getInOrderGenerator(node)) == test[0] and list(BinaryTreeNode.getPreOrderGenerator(node)) == test[1] , '%i failed' %i)
            i += 1

if __name__ == "__main__":
   unittest.main() 
