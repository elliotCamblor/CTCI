from HSLinkedList import *

def getFirstNodeInLoop(n):
    a = b = n

    while (b is not None) and (b.next is not None):
        a = a.next
        b = b.next.next
        if a is b:
            break

    if (b is None) or (b.next is None):
        return None

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
