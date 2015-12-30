import unittest
from q_5_2 import *

class testcase1(unittest.TestCase):
    tests = [
        (0.75, '.11'),
        (0.5 + 0.125, '.101')
    ]

    def test1(self):
        for test in self.tests:
            self.assertEquals(getBinaryString(test[0]), test[1])

if __name__ == "__main__":
    unittest.main() 
