import unittest
from q_9_4 import *

class testcase1(unittest.TestCase):
    allTestSets = [
        [],
        [2],
        [2, 4],
        [1, 2, 5],
        [1, 8, 2, 3, 4, 5, 6, 7]
    ]

    def test(self):
        for testSet in self.allTestSets:
            subsets = getSubsets(testSet)
            subsets2 = getSubsets2(testSet)

            mergedSet = set()
            for subset in subsets:
                mergedSet |= set(subset)
            
            mergedSet2 = set()
            for subset in subsets2:
                mergedSet2 |= set(subset)

            self.assertTrue(mergedSet == set(testSet))
            self.assertTrue(mergedSet2 == set(testSet))

if __name__ == "__main__":
    unittest.main() 
