import unittest
from q_16_3 import *

class testcase1(unittest.TestCase):

    def test(self):
        num = 5
        chopSticks = []
        for i in range(num):
            chopSticks.append(Chopstick())

        philosophers = []
        for i in range(num):
            j = i + 1 if i + 1< len(chopSticks) else 0
            philosophers.append(Philosopher(chopSticks[i], chopSticks[j]))

        for i in range(num): 
            philosophers[i].start()
       
        for i in range(num):
            philosophers[i].join()
            self.assertTrue(philosophers[i].isSuccess())

if __name__ == "__main__":
    unittest.main() 
