from lib.HSTree import BinaryTreeNode

def createBST(sortedList, start, end):
    if start > end:
        return None

    middle = (start + end)//2

    node = BinaryTreeNode(sortedList[middle])
    node.left = createBST(sortedList, start, middle - 1)
    node.right = createBST(sortedList, middle + 1, end)

    return node

def createBSTWrapper(sortedList):
    return createBST(sortedList, 0, len(sortedList) - 1)
