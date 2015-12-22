from lib.HSTree import BinaryTreeNode

def __commonAncestorHelper(n, p, q):
    if n == None:
        return None, False
    elif n == p and n == q:
        return n, True
    
    leftNode, isAncestor = __commonAncestorHelper(n.left, p, q)
    if isAncestor:
        return leftNode, isAncestor

    rightNode, isAncestor = __commonAncestorHelper(n.right, p, q)
    if isAncestor:
        return rightNode, isAncestor

    if leftNode != None and rightNode != None:
        return n, True
    if n == p or n == q:
        isAncestor = leftNode or rightNode
        return n, isAncestor
    else:
        return leftNode if leftNode else rightNode, False

def commonAncestor(n, p, q):
    ancestor, isAncestor = __commonAncestorHelper(n, p, q)
    if isAncestor:
        return ancestor
    else:
        return None
