from lib.HSTree import BinaryTreeNode

def isBST(root):
    inOrderList = list(BinaryTreeNode.getInOrderGenerator(root))
    return inOrderList == sorted(inOrderList)

