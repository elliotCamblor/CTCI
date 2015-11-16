class SetOfStacks:
    def __init__(self, capacity):
        self.buf = []
        self.buf.append([])
        self.capacity = capacity

    def push(self, i):
        self.buf[-1].append(i)
        if len(self.buf[-1]) >= self.capacity:
            self.buf.append([])
        

    def pop(self):
        self.buf[-1].pop()
        if len(self.buf[-1]) == 0:
            self.buf.pop()

    def popAt(self, i):
        return self.__leftShift(i, True)

    def __leftShift(self, i, removeTop):
        v = self.buf[i].pop(-1 if removeTop else 0)

        if len(self.buf[i]) == 0:
            self.buf.pop(i)
        elif i+1 < len(self.buf) :
            v = self.__leftShift(i+1, False)
            self.buf[i].append(v)

        return v


#TODO: implement test for this class

if __name__ == "__main__":
    ss = SetOfStacks(2)
    for i in range(5):
        ss.push(i)

    r0 = [
        [0, 1],
        [2, 3],
        [4],
        ]

    assert(r0 == ss.buf)

    ss.pop()

    r1 = [
        [0, 1],
        [2, 3]
        ]

    assert(r1 == ss.buf)

    ss.popAt(0)

    r2 = [
        [0, 2],
        [3]
        ]

    assert(r2 == ss.buf)
    
    print("success")
