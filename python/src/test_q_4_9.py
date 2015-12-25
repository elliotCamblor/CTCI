import unittest
from q_4_9 import *
from lib.HSTree import BinaryTreeNode

class testcase1(unittest.TestCase):
    
    tests = [
        ([1, 2, 4, 3, 5], [4, 2, 1, 5, 3], 3, [[1, 2], [3]]),
    ]

    def test_1(self):
        for test in self.tests:
            t1 = BinaryTreeNode.buildTree(test[0], test[1])
            result = findSums(t1, test[2])
            self.assertEqual(result, test[3])

if __name__ == "__main__":
   unittest.main() 
