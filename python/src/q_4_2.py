from lib.HSGraph import *
from queue import Queue

#g is Graph, start and end are Vertex
def isConnected(g, start, end):
    for v in g.allVertices:
        v.color = Color.white

    q = Queue()
    start.color = Color.grey
    q.put(start)

    while not q.empty():
        v = q.get()

        if v.key == end.key:
            return True
        
        for adj in g.adjacent[v.key]:
            if adj.color == Color.white:
                adj.color = Color.grey
                q.put(adj)
       
    return False
