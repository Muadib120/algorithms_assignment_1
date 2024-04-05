# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', 'Benjamin Hatfield'
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        self.graph = None


    def addVertex(self, label:Coordinates):
        # Add vertex to vertices dictionary, value is the index to be used in the edge matrix 
        if label not in self.vertices:
            self.vertices[label] = self.numVertices
            self.numVertices += 1


    def addVertices(self, vertLabels:List[Coordinates]):
        # Add vertices to vertices dictionary, value is the index to be used in the edge matrix 
        for vertex in vertLabels:
            if vertex not in self.vertices:
                self.vertices[vertex] = self.numVertices
                self.numVertices += 1


    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        # If graph matrix has not been initialized, create matrix of numvertices by numvertices
        # initial value will be -1
        if self.graph == None:
            self.graph = [[-1 for val1 in range(self.numVertices)] for val2 in range(self.numVertices)]


        # Adds edge between vert1 and vert2 if vertices are adjacent and vertices exist and edge has not already been added
        if vert1 in self.vertices and vert2 in self.vertices and vert1.isAdjacent(vert2) and self.graph[self.vertices[vert1]][self.vertices[vert2]] == -1:
            self.graph[self.vertices[vert1]][self.vertices[vert2]] = addWall
            self.graph[self.vertices[vert2]][self.vertices[vert1]] = addWall
            return True
        else:
            return False
            
    
    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        # updates wall status of respective edge (both directions) if the edge already exists 
        if self.hasEdge(vert1,vert2):
            self.graph[self.vertices[vert1]][self.vertices[vert2]] = wallStatus
            self.graph[self.vertices[vert2]][self.vertices[vert1]] = wallStatus
            return True
        else:
            return False
    

    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # Removes respective edge (both directions) if the edge exists 
        # returns true if removed, false otherwise 
        if self.hasEdge(vert1,vert2):
            self.graph[self.vertices[vert1]][self.vertices[vert2]] = -1
            self.graph[self.vertices[vert2]][self.vertices[vert1]] = -1
            return True
        else:
            return False
        
        
    def hasVertex(self, label:Coordinates)->bool:
        # Returns whether vertex found in graph
        return label in self.vertices


    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # checks for matrix being initiated and if edge in both directions and returns result
        return self.graph != None and self.graph[self.vertices[vert1]][self.vertices[vert2]] != -1


    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # returns the status of the wall between the designated edge
        if self.hasEdge(vert1,vert2):
            return self.graph[self.vertices[vert1]][self.vertices[vert2]]
        else:
            return False


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        # return list of neighbours (current edges) to the provided label
        adjCoords = []
        for coord in self.vertices:
            if label.isAdjacent(coord):
                adjCoords.append(coord)

        return adjCoords
        