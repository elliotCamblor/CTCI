class Queue:
    def __init__(self):
        self.stackNew = []
        self.stackOld = []

    def enqueue(self, n):
        self.stackNew.append(n)

    def __shiftStacks(self):
        if not self.stackOld:
            while self.stackNew:
                self.stackOld.append(self.stackNew.pop())

    def dequeue(self):
        self.__shiftStacks()
        return self.stackOld.pop()

    def peek(self):
        self.__shiftStacks()
        return self.stackOld[-1]

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert(q.dequeue() == 1)
    q.enqueue(3)
    assert(q.dequeue() == 2)
    assert(q.peek() == 3)
    assert(q.dequeue() == 3)
    print("success")

