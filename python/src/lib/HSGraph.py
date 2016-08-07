from enum import Enum

class Color(Enum):
    white = 0
    grey = 1
    black = 2

class Vertex:
    def __init__(self, pkey, pcolor, pdistance, pparent):
        self.key = pkey
        self.color = pcolor
        self.distance = pdistance
        self.parent = pparent
        self.adjacent = []

class Graph:
    
    #graph structure:
    #g = {'A': ['B', 'C'],
    #     'B': ['C'],
    #     'C': ['A']}
    def __init__(self, g_dict):
        self.graph = g_dict
        self.vertices = {}
        self.allVertices = []
        self.adjacent = {}

        for key, values in self.graph.items():
            if key not in self.vertices:
                self.vertices[key] = Vertex(key, Color.white, 0, None)
                self.allVertices.append(self.vertices[key])
            
            self.adjacent[key] = []
            
            for value in values:
                if value not in self.vertices:
                    self.vertices[value] = Vertex(value, Color.white, 0, None)
                    self.allVertices.append(self.vertices[value])
                
                self.adjacent[key].append(self.vertices[value])

#another one
class Node:
    def __init__(self, key):
        self.key = key
        self.visited = False
        self.adjacent = []
