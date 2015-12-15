from HSLinkedList import *

def deleteNode(node):
    if not node and not node.next:
        raise ValueError

    node.data = node.next.data
    node.next = node.next.next

if __name__ == '__main__':
    n = Node(1)
    for i in range(2, 10):
        n.appendToTail(i)

    b = Node(1)
    for i in range(2, 10):
        if i == 5:
            continue

        b.appendToTail(i)

    c = n
    for i in range(4):
        c = c.next
    
    print(n)
    deleteNode(c)
    print(n)
    assert(str(b) == str(n))
    print("success")

