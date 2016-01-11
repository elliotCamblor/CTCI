import unittest
from q_9_3 import *

class testcase1(unittest.TestCase):
    tests = [
        ([-20, 0, 2, 5, 7, 8, 20], 2),
        ([0], 0)
    ]
    
    def test(self):
        for test in self.tests:
            self.assertEqual(magicBrute(test[0]), test[1])
            self.assertEqual(magicFast(test[0]), test[1])

if __name__ == "__main__":
    unittest.main() 
