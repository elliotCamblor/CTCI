import unittest
from q_5_6 import *

class testcase1(unittest.TestCase):
    Tests = [
        (int('1100110', 2), int('10011001', 2)),
    ]
    
    def test1(self):
        for test in self.Tests:
            self.assertEqual(swapOddEvenBits(test[0]), test[1])

if __name__ == "__main__":
    unittest.main() 
