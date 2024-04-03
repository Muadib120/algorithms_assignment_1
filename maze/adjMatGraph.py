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
        self.vertices = []
        self.numVertices = 0
        self.graphSetup = False
        self.graph = []



    def addVertex(self, label:Coordinates):
        ### Implement me! ###
        if label not in self.vertices:
            self.vertices.append(label)
            self.numVertices += 1

            # if self.numVertices > 1:
            #         for edge in self.graph:
            #             edge.append(-1)

            # temp = []

            # for vert in range(self.numVertices):
            #     temp.append(-1)
            
            # self.graph.append(temp)


    def addVertices(self, vertLabels:List[Coordinates]):
        ### Implement me! ###
        for vertex in vertLabels:
            if vertex not in self.vertices:
                self.vertices.append(vertex)
                self.numVertices += 1

                # if self.numVertices > 1:
                #     for edge in self.graph:
                #         edge.append(-1)

                # temp = []

                # for vert in range(self.numVertices):
                #     temp.append(-1)
                
                # self.graph.append(temp)



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        # remember to return booleans
        if not self.graphSetup:
            self.graph = [[-1 for val1 in range(self.numVertices)] for val2 in range(self.numVertices)]
            self.graphSetup = True
                
        if self.graph[self.vertices.index(vert1)][self.vertices.index(vert2)] == -1:
            self.graph[self.vertices.index(vert1)][self.vertices.index(vert2)] = addWall
            self.graph[self.vertices.index(vert2)][self.vertices.index(vert1)] = addWall
            return True
        else:
            return False
            
    

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        if vert1 in self.vertices and vert2 in self.vertices:
            self.graph[self.vertices.index(vert1)][self.vertices.index(vert2)] = wallStatus
            self.graph[self.vertices.index(vert2)][self.vertices.index(vert1)] = wallStatus
            return True
        else:
            return False
    


    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        if vert1 in self.vertices and vert2 in self.vertices:
            self.graph[self.vertices.index(vert1)][self.vertices.index(vert2)] = -1
            self.graph[self.vertices.index(vert2)][self.vertices.index(vert1)] = -1
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
        return vert1 in self.vertices and vert2 in self.vertices



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        if vert1 in self.vertices and vert2 in self.vertices:
            return self.graph[self.vertices.index(vert1)][self.vertices.index(vert2)]
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
        