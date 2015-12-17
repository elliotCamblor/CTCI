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

if __name__ == "__main__":
    tests = [
        (0, [1, 2, 3], [2, 1, 3], True),
        (1, [1, 2, 3, 4], [2, 1, 4, 3], True),
        (2, [1, 2, 3, 4, 5], [2, 1, 4, 5, 3], False)
    ]

    for test in tests:
        testTree = BinaryTreeNode.buildTree(test[1], test[2])
        assert isBalanced(testTree) == test[3], "test %i failed" % test[0]

    print("success")
            
