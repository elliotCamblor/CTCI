import math

class TowerOfHanoi:
    def __init__(self, n):
        self.towers = [[],[], []]
        self.n = n
        for i in range(self.n - 1, -1, -1):
            self.towers[0].append(i)
    
    def solve(self):
        self.moveDisks(self.n, 0, 2, 1)

    def moveDisks(self, n, src, dest, buf):
        if n <= 0:
            return

        self.moveDisks(n-1, src, buf, dest)
        self.moveTop(src, dest)
        self.moveDisks(n-1, buf, dest, src)

    def moveTop(self, src, dest):
        srcTop = self.towers[src][-1] if self.towers[src] else math.inf
        destTop = self.towers[dest][-1] if self.towers[dest] else math.inf
        print("moving " + str(srcTop) + " from tower " + str(src) + " on top of "  + str(destTop) + " on tower " + str(dest))

        if srcTop >= destTop:
            raise InvalidMove()

        self.towers[dest].append(self.towers[src].pop())

class InvalidMove(Exception):
    pass

if __name__ == "__main__":
    hanoi = TowerOfHanoi(5)
    print(hanoi.towers)
    hanoi.solve()
    print(hanoi.towers)
    assert(not hanoi.towers[0])
    assert(not hanoi.towers[1])
    assert(len(hanoi.towers[2]) == 5)
    print("success")
    
        
