from threading import Thread, RLock

class Chopstick:
    def __init__(self):
        self.lock = RLock()

    def pickUp(self):
        return self.lock.acquire(blocking=False)

    def putDown(self):
        self.lock.release()

class Philosopher(Thread):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.bites = 10
        self.success = False

    def eat(self):
        if self.pickUp():
            self.chew()
            self.putDown()

    def pickUp(self):
        if not self.left.pickUp():
            return False
        
        if not self.right.pickUp():
            self.left.putDown()
            return False
        
        return True

    def chew(self):
        pass

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
