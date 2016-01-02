import unittest
from q_9_1 import *

class testcase1(unittest.TestCase):
    Tests = [
        (2, 2),
        (5, 13),
        (10, 274),
        (20, 121415),
    ]
    
    def test1(self):
        for test in self.Tests:
            self.assertEqual(countWays(test[0]), test[1])

if __name__ == "__main__":
    unittest.main() 
