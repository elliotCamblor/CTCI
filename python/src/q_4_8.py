def isSameTree(t1, t2):
    if t1 == None and t2 == None:
        return True
    if t1 == None or t2 == None:
        return False

    return t1.key == t2.key and isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

def __isSubtree(t1, t2):
    if t1 == None:
        return False

    if isSameTree(t1, t2):
        return True

    return __isSubtree(t1.left, t2) or __isSubtree(t1.right, t2)

def isSubtree(t1, t2):
    if t2 == None:
        return True

    return __isSubtree(t1, t2)
