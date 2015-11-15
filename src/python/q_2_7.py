from HSLinkedList import *

def isPalindromeRecursive(node, length):
    if length == 1:
        return node.next, True
    elif length == 2:
        return node.next.next, node.data == node.next.data

    back, isPalindrome = isPalindromeRecursive(node.next, length - 2)
    return back.next, isPalindrome and node.data == back.data

if __name__ == "__main__":
    n0 = Node.GetFromList([0, 1, 2, 3, 2, 1, 0])    
    _, result = isPalindromeRecursive(n0, 7)
    assert(result == True)
    n1 = Node.GetFromList([0, 1, 2, 2, 1, 0])
    _, result = isPalindromeRecursive(n1, 6)
    assert(result == True)
    n2 = Node.GetFromList([0, 3, 2, 1, 0])
    _, result = isPalindromeRecursive(n2, 5)
    assert(result == False)
    print("success")


