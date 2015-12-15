class Node:
    def __init__(self, i):
        self.next = None
        self.data = i
    
    @classmethod
    def GetFromList(cls, lst):
        node = cls(lst[0])
        end = node
        for i in range(1, len(lst)):
            end.next = cls(lst[i])
            end = end.next

        return node

    def __len__(self):
        count = 0
        n = self
        
        while (n != None):
            count += 1
            n = n.next

        return count

    def __str__(self):
        l = []
        n = self
        while n != None:
            l.append(n.data)
            n = n.next
        return str(l)

    def appendToTail(self, d):
        end = Node(d)
        n = self
        while (n.next != None):
            n = n.next
        n.next = end
    
    @staticmethod
    def removeFromNode(head, d):
        n = head
        if (n.data == d):
            return head.next

        while (n.next != None):
            if (n.next.data == d):
                n.next = n.next.next
                return head
            n = n.next

        return head


