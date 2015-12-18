import unittest
from q_4_2 import *
from lib.HSGraph import *

class testcase1(unittest.TestCase):
    tests = [
        ({
            0: [1],
            1: [2],
            2: []
         }, 0, 2, True),
        ({
            0: [],
            1: [2],
            2: []
         }, 0, 2, False),
    ]

    def test1(self):
        i = 0
        for test in self.tests:
            g = Graph(test[0])
            self.assertEqual(isConnected(g, g.vertices[test[1]], g.vertices[test[2]]), test[3], '%i failed' %i)
            i += 1

if __name__ == "__main__":
   unittest.main() 
