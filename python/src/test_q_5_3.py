import unittest
from q_5_3 import *

class testcase1(unittest.TestCase):
    getNextTests = [
        ( int('101100', 2), int('110001', 2)),
        (0, -1)
    ]
    
    getPrevTests = [
        (int('110011', 2), int('101110', 2)),
        (0, -1),
        (1, -1)
    ]

    def test1(self):
        for test in self.getNextTests:
            self.assertEquals(getNext(test[0]), test[1])

        for test in self.getPrevTests:
            self.assertEquals(getPrev(test[0]), test[1])

if __name__ == "__main__":
    unittest.main() 
