import unittest
from q_9_5 import *

class testcase1(unittest.TestCase):
    tests = [
        ['', ['']],
        ['a', ['a']],
        ['ab', ['ba', 'ab']],
        ['abc', ['cba', 'bca','bac', 'cab','acb','abc',]],
    ]

    def test(self):
        for test in self.tests:
            self.assertEqual(set(getPerms(test[0])), set(test[1]))

if __name__ == "__main__":
    unittest.main() 
