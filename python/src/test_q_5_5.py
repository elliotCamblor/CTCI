import unittest
from q_5_5 import *

class testcase1(unittest.TestCase):
    Tests = [
        (int('101', 2), int('010', 2), 3),
        (int('000', 2), int('000', 2), 0),
        (int('001', 2), int('000', 2), 1)
    ]
    
    def test1(self):
        for test in self.Tests:
            self.assertEqual(numBitSwapRequired(test[0], test[1]), test[2])

if __name__ == "__main__":
    unittest.main() 
