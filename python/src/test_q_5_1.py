import unittest
from q_5_1 import *

class testcase1(unittest.TestCase):
    tests = [
        (int('0000000000', 2), int('1111', 2), 2, 5, int('0000111100', 2)),
        (int('0000000000', 2), int('1111', 2), 0, 3, int('0000001111', 2)),
    ]

    def test1(self):
        for test in self.tests:
            self.assertEquals(updateBits(test[0], test[1], test[2], test[3]), test[4])

if __name__ == "__main__":
    unittest.main() 
