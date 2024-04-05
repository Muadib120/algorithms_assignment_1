# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', 'Benjamin Hatfield'
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class AdjListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        # Empty Dictionary for adding vertices and their respective edges
        self.graph = {}


        
    def addVertex(self, label:Coordinates):
        # Adds a vertex to the graph
        if label not in self.graph:
            self.graph[label] = {}


    def addVertices(self, vertLabels:List[Coordinates]):
        # Adds multiple Vertices to the graph, each dictionary value is another dictionary to be filled with edges 
        for label in vertLabels:
            if label not in self.graph:
                self.graph[label] = {}



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        # Adds edges in the form of dictionary keys with wall status being the value 
        # Checks if each vertex is adjacent so only adjacent vertices are added 
        if vert1 not in self.graph[vert2] and vert2 not in self.graph[vert1] and vert1.isAdjacent(vert2):
            self.graph[vert1][vert2] = addWall
            self.graph[vert2][vert1] = addWall
            return True
        
        return False
        

    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        # updates wall status of respective edge (both directions) if the edge already exists 
        if self.hasEdge(vert1,vert2):
            self.graph[vert1][vert2] = wallStatus
            self.graph[vert2][vert1] = wallStatus
            return True
        return False


    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # Removes respective edge (both directions) if the edge exists 
        # returns true if removed, false otherwise 
        if self.hasEdge(vert1,vert2):
            del self.graph[vert1][vert2]
            del self.graph[vert2][vert1]
            return True
                    
        return False


    def hasVertex(self, label:Coordinates)->bool:
        # Returns whether vertex found in graph
        return label in self.graph


    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # checks for edge in both directions and returns result
        return vert1 in self.graph[vert2] and vert2 in self.graph[vert1]


    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # returns the status of the wall between the designated edge
        if self.hasEdge(vert1,vert2):
            return self.graph[vert1][vert2]
        return False
    

    def neighbours(self, label:Coordinates)->List[Coordinates]:
        # returns a list of coordinates that are neighbours to the label coordinate
        coords = []
        for edge in self.graph[label]:             
                coords.append(edge)

        return coords
        