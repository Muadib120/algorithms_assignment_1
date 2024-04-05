# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
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
        ### Implement me! ###
        self.vertices = {}
        self.numVertices = 0
        self.graphSetup = False
        self.graph = []



    def addVertex(self, label:Coordinates):
        ### Implement me! ###
        if label not in self.vertices:
            self.vertices[label] = self.numVertices
            self.numVertices += 1



    def addVertices(self, vertLabels:List[Coordinates]):
        ### Implement me! ###
        for vertex in vertLabels:
            if vertex not in self.vertices:
                self.vertices[vertex] = self.numVertices
                self.numVertices += 1



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        # remember to return booleans
        if not self.graphSetup:
            self.graph = [[-1 for val1 in range(self.numVertices)] for val2 in range(self.numVertices)]
            self.graphSetup = True

        if vert1 in self.vertices and vert2 in self.vertices and vert1.isAdjacent(vert2):
            vert1Index = self.vertices[vert1]
            vert2Index = self.vertices[vert2]
            
            if self.graph[vert1Index][vert2Index] == -1:
                self.graph[vert1Index][vert2Index] = addWall
                self.graph[vert2Index][vert1Index] = addWall
                return True
            else:
                return False
            
    

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        if self.hasEdge(vert1,vert2):
            vert1Index = self.vertices[vert1]
            vert2Index = self.vertices[vert2]


            self.graph[vert1Index][vert2Index] = wallStatus
            self.graph[vert2Index][vert1Index] = wallStatus
            return True
        else:
            return False
    


    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        if self.hasEdge(vert1,vert2):
            vert1Index = self.vertices[vert1]
            vert2Index = self.vertices[vert2]


            self.graph[vert1Index][vert2Index] = -1
            self.graph[vert2Index][vert1Index] = -1
            return True
        else:
            return False
        
        

    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return label in self.vertices



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return self.graphSetup and self.graph[self.vertices[vert1]][self.vertices[vert2]] != -1



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        if self.hasEdge(vert1,vert2):
            return self.graph[self.vertices[vert1]][self.vertices[vert2]]
        else:
            return False



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        ### Implement me! ###
        # remember to return list of coordinates
        adjCoords = list()
        for coord in self.vertices:
            if coord.isAdjacent(label):
                adjCoords.append(coord)

        return adjCoords
        