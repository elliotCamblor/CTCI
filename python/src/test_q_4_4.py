import unittest
from q_4_4 import *
from lib.HSTree import BinaryTreeNode
from lib.HSLinkedList import *

class testcase1(unittest.TestCase):
    tests = [
        ([1, 2, 3], [2, 1, 3], [[1], [2, 3]]),
        ([1, 2, 3, 4], [2, 1, 4, 3], [[1], [2, 3], [4]])
    ]

    def test_1(self):
        for test in self.tests:
            treeRoot = BinaryTreeNode.buildTree(test[0], test[1])
            levelLists = createLevelLinkedLists(treeRoot)
            levelLists2 = createLevelLinkedListsBFS(treeRoot)

            for i in range(len(test[2])):
                self.assertEqual(str(test[2][i]), str(levelLists[i]))
                self.assertEqual(str(test[2][i]), str(levelLists2[i]))

if __name__ == "__main__":
   unittest.main() 
