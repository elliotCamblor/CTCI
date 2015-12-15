from HSTree import BinaryTreeNode

def depth(x):
    if x == None:
        return 0

    return max(depth(x.left), depth(x.right)) + 1

def isBalanced(x):
    if x == None:
        return True
    elif abs(depth(x.left) - depth(x.right)) > 1:
        return False
    else:
        return isBalanced(x.left) and isBalanced(x.right)

if __name__ == "__main__":
    x = BinaryTreeNode.createBinaryTreeQuick(0, 0, 0, 0, 0)

    
