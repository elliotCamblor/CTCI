from lib.HSTree import BinaryTreeNode
from lib.HSLinkedList import *
from queue import Queue

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

def createLevelLinkedListsBFS(root):
    q = Queue()
    q.put((root, 0))
    lists = []

    while not q.empty():
        cur, level = q.get()
        if level == len(lists):
            lists.append(Node(cur.key))
        else:
            lists[level].appendToTail(cur.key)

        if cur.left:
            q.put((cur.left, level + 1))
        if cur.right:
            q.put((cur.right, level + 1))

    return lists
        

