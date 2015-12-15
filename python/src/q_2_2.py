from HSLinkedList import Node
from queue import *

def kthLastRecursive(node, k, result):
    if node == None:
        return 0

    i = kthLastRecursive(node.next, k, result) + 1

    if i == k:
        result.node = node

    return i

def kthLastRecursiveContainer(node, k):
    class resultContainer:
        pass
    
    r = resultContainer()
    kthLastRecursive(node, k, r)
    return r.node

def kthLast(node, k):
    q = Queue()
    count = 0
    while node != None:
        q.put(node)
        count += 1
        if (count > k):
            q.get(False)
            count -= 1
        node = node.next
    return q.get(False)

if __name__ == "__main__":
    n = Node(0)
    n.appendToTail(2)
    n.appendToTail(3)
    n.appendToTail(4)
    n.appendToTail(5)
    n.appendToTail(6)
    n.appendToTail(7)
    n.appendToTail(8)
    n.appendToTail(9)
    
    r = kthLastRecursiveContainer(n, 3)
    assert(r.data == 7)
    r = kthLast(n, 4)
    assert(r.data == 6)

    print("success")
