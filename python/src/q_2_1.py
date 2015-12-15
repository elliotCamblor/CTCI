from HSLinkedList import Node

def removeDuplicates(head):
    n = head
    d = {}
    
    p = None
    while n:
        if n.data in d:
            p.next = p.next.next
        else:
            d[n.data] = True
        
        p = n
        n = n.next

if __name__ == "__main__":
    n = Node(1)
    add = n.appendToTail
    add(1)
    add(2)
    add(3)
    add(3)
    add(4)
    add(5)
    add(5)
    print(n)
    removeDuplicates(n);
    print(n)
    assert(len(n) == 5)
    print("pass")
