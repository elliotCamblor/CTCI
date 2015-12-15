import math

class BinaryTreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.key = 0

    def __init__(self, k):
        self.right = None
        self.left = None
        self.key = k

    @staticmethod
    def getInOrder(root, outList):
        if root == None:
            return

        getInOrder(root.left, outList)
        outList.append(root.key)
        getInOrder(root.left, outList)

    @staticmethod
    def getPreOrder(root, outList):
        if root == None:
            return

        outList.append(root.key)
        getPreOrder(root.left, outList)
        getPreOrder(root.right, outList)

    @staticmethod
    def getPostOrder(root, outList):
        if root == None:
            return

       getPostOrder(root.left, outList)
       getPostOrder(root.right, outList)
       outList.append(root.key)
    
    @classmethod
    def buildTree(inOrderList, preOrderList):
        assert(len(inOrderList) == len(preOrderList))





