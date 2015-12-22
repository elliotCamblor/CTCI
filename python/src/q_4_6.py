def __leftMost(node):
    while node.left:
        node = node.left
 
    return node

def inOrderSuccessor(node):
    if node == None:
        return None
    elif node.right:
        return __leftMost(node.right)
    else:
        while node.parent and node == node.parent.right:
            node = node.parent

        return node.parent
