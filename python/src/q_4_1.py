from lib.HSTree import BinaryTreeNode

def depth(x):
    if x == None:
        return 0

    leftDepth = depth(x.left)
    rightDepth = depth(x.right)
    diff = abs(leftDepth - rightDepth)
    diff2 = -1 if diff > 1 else diff

    if any(x == -1 for x in [leftDepth, rightDepth, diff2]):
        return -1
    else:
        return max(leftDepth, rightDepth) + 1


def isBalanced(x):
    return depth(x) != -1
