from HSLinkedList import Node

def partition(node, x):
    if not node:
        raise ValueError

    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None
    cur = node
    
    while cur:
        next = cur.next
        cur.next = None

        if cur.data < x:
            if not beforeStart:
                beforeStart = beforeEnd = cur
            else:
                beforeEnd.next = cur
                beforeEnd = beforeEnd.next
        else:
            if not afterStart:
                afterStart = afterEnd = cur
            else:
                afterEnd.next = cur
                afterEnd = afterEnd.next
        cur = next

    if not beforeEnd:
        return afterStart

    beforeEnd.next = afterStart
    return beforeStart

if __name__ == "__main__":
    a = Node(1)
    for i in range(2, 13):
        a.appendToTail(i % 4)
    
    print(a)
    partition(a, 2)
    print(a)
