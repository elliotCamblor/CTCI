import math

class BinaryTreeNode:
    def __init__(self, k=0, right=None, left=None, parent=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.key = k
    
    def __eq__(self, other):
        return self.key == other.key if other else False

    @classmethod
    def __printInOrder(cls, root):
        if root == None:
            return

        cls.__printInOrder(root.left)
        print(root.key, end=', ')
        cls.__printInOrder(root.right)

    @classmethod
    def printInOrder(cls, root):
        cls.__printInOrder(root)
        print()

    @classmethod
    def getInOrderGenerator(cls, root):
        if root == None:
            return

        yield from cls.getInOrderGenerator(root.left)
        yield root.key
        yield from cls.getInOrderGenerator(root.right)

    @classmethod
    def __printPreOrder(cls, root):
        if root == None:
            return

        print(root.key, end=', ')
        cls.__printPreOrder(root.left)
        cls.__printPreOrder(root.right)

    @classmethod
    def printPreOrder(cls, root):
        cls.__printPreOrder(root)
        print()

    @classmethod
    def getPreOrderGenerator(cls, root):
        if root == None:
            return

        yield root.key
        yield from cls.getPreOrderGenerator(root.left)
        yield from cls.getPreOrderGenerator(root.right)
    
    @classmethod
    def __printPostOrder(cls, root):
        if root == None:
            return
        
        cls.__printPostOrder(root.left)
        cls.__printPostOrder(root.right)
        print(root.key, end=', ')

    @classmethod
    def printPostOrder(cls, root):
        cls.__printPostOrder(root)
        print()

    @classmethod
    def getPostOrderGenerator(cls, root):
        if root == None:
            return

        yield from cls.getPostOrderGenerator(root.left)
        yield from cls.getPostOrderGenerator(root.right)
        yield root.key

    @classmethod
    def __buildTree(cls, preOrder, inOrder, inStart, inEnd):
        if inStart > inEnd:
            return None

        node = cls(preOrder[cls.i])
        cls.i += 1
        k = inOrder.index(node.key)

        node.left = cls.__buildTree(preOrder, inOrder, inStart, k - 1)
        if node.left:
            node.left.parent = node
        node.right = cls.__buildTree(preOrder, inOrder, k + 1, inEnd)
        if node.right:
            node.right.parent = node
        return node

    @classmethod
    def buildTree(cls, preOrder, inOrder):
        cls.i = 0
        return cls.__buildTree(preOrder, inOrder, 0, len(inOrder) - 1)
