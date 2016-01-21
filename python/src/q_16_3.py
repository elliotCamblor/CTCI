import time
from threading import Thread, RLock

class Chopstick:
    def __init__(self, name):
        self.lock = RLock()
        self.name = name

    def pickUp(self):
        return self.lock.acquire(blocking=False)

    def putDown(self):
        self.lock.release()

class Philosopher(Thread):
    def __init__(self, name, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.bites = 10
        self.success = False
        self.name = name

    def eat(self):
        while True:
            if self.pickUp():
                self.chew()
                self.putDown()
                break

    def pickUp(self):
        if not self.left.pickUp():
            return False
        
        if not self.right.pickUp():
            self.left.putDown()
            return False
        
        return True

    def chew(self):
        print("%s chews" % self.name)
        time.sleep(0.001)

    def putDown(self):
        self.left.putDown()
        self.right.putDown()

    def run(self):
        for i in range(self.bites):
            self.eat()

        self.success = True

    def isSuccess(self):
        return self.success

        return True
