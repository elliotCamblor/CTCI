import math
from lib.HSTree import BinaryTreeNode

def isBST(root):
    inOrderList = list(BinaryTreeNode.getInOrderGenerator(root))
    return inOrderList == sorted(inOrderList)

def __isBST2(root, minimum, maximum):
    if root == None:
        return True

    if root.key < minimum or root.key > maximum:
        return False

    if not __isBST2(root.left, minimum, root.key) or not __isBST2(root.right, root.key, maximum):
        return False

    return True

#get actual minimum and maximum int when you have access to internet
def isBST2(root):
    return __isBST2(root, -math.inf, math.inf) 
