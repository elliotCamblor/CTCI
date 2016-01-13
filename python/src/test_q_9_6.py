import unittest
from q_9_6 import *

class testcase1(unittest.TestCase):
    tests = [
        [2, ['()()', '(())']],
        [3, ['(()())', '((()))', '()(())', '(())()', '()()()']]
    ]

    def test(self):
        for test in self.tests:
            self.assertEqual(set(generateParen(test[0])), set(test[1]))

if __name__ == "__main__":
    unittest.main() 
