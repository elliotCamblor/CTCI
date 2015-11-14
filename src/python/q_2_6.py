from HSLinkedList import *

def getFirstNodeInLoop(n):
    a = b = n

    while True:
        a = a.next
        b = b.next.next
        if a is b:
            break

    a = n
    while True:
        a = a.next
        b = b.next
        if a is b:
            return a

if __name__ == "__main__":
    start = Node(0)
    end = start
    for i in range(1, 10):
        end.next = Node(i)
        end = end.next
    loopStart = start.next.next
    end.next = loopStart

    result = getFirstNodeInLoop(start)
    assert(result is loopStart)
    print("success")
