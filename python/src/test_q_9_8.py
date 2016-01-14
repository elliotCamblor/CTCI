import unittest
from q_9_8 import *

class testcase1(unittest.TestCase):
    tests = [
        [2, 1],
        [8, 2]
    ]

    def test(self):
        for test in self.tests:
            self.assertEqual(makeChange(test[0]), test[1])

if __name__ == "__main__":
    unittest.main() 
