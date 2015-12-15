from HSLinkedList import *

def addLinkedLists(num0, num1):
    sum = None
    carry = 0
    while num0 or num1 or carry:
        c0 = num0.data if num0 else 0
        c1 = num1.data if num1 else 0
        
        v = c0 + c1 + carry
        c = v % 10
        carry = v//10

        if sum:
            sum.appendToTail(c)
        else:
            sum = Node(c)

        if num0:
            num0 = num0.next
        if num1:
            num1 = num1.next

    return sum

def addLinkedListRecursive(n0, n1, carry):
    
    if (not n0) and (not n1) and (not carry):
        return None

    c0 = n0.data if n0 else 0
    c1 = n1.data if n1 else 0
    val = c0 + c1 + carry
    s = val % 10
    c = val // 10

    sum = Node(s)
    sum.next = addLinkedListRecursive(n0.next if n0 else None, n1.next if n1 else None, c)
    
    return sum


if __name__ == "__main__":
    num0 = Node(8)
    num0.appendToTail(9)
    num0.appendToTail(2)

    num1 = Node(5)
    num1.appendToTail(5)

    result = Node(3)
    result.appendToTail(5)
    result.appendToTail(3)

    assert(str(addLinkedLists(num0, num1)) == str(result))
    assert(str(addLinkedListRecursive(num0, num1, 0)) == str(result))
    print("success")
