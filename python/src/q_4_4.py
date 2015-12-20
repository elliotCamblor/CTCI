from lib.HSTree import BinaryTreeNode
from lib.HSLinkedList import *

#list: array of linkedlists
def __createLevelLinkedLists(root, lists, level):
    if root == None:
        return

    if len(lists) <= level:
        lists.append(Node(root.key))
    else:
        lists[level].appendToTail(root.key) 

    __createLevelLinkedLists(root.left, lists, level + 1)
    __createLevelLinkedLists(root.right, lists, level + 1)

def createLevelLinkedLists(root):
    lists = []
    __createLevelLinkedLists(root, lists, 0)
    return lists
