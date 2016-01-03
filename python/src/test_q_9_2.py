import unittest
from q_9_2 import *

class testcase1(unittest.TestCase):
    countWaysTests = [
        (1, 1),
        (5, 6),
        (2, 9),
    ]
    
    def test1(self):
        for test in self.countWaysTests:
            self.assertEqual(countWaysDP(test[0], test[1]), countWaysBinomial(test[0], test[1]))

    getPathTests = [
        (7, 9, lambda x, y: y == 0 or x == 7, ['1, 0', '2, 0', '3, 0', '4, 0', '5, 0', '6, 0', '7, 0', '7, 1', '7, 2', '7, 3', '7, 4', '7, 5', '7, 6', '7, 7', '7, 8', '7, 9']),
        (7, 9, lambda x, y: x == 0 or y == 9, [ '0, 1', '0, 2', '0, 3', '0, 4', '0, 5', '0, 6', '0, 7', '0, 8', '0, 9', '1, 9', '2, 9', '3, 9', '4, 9', '5, 9', '6, 9', '7, 9',])
    ]

    def test2(self):
        for test in self.getPathTests:
            self.assertEquals(getPath(test[0], test[1], test[2]), test[3])

if __name__ == "__main__":
    unittest.main() 
