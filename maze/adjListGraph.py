# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
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
        ### Implement me! ###
        self.graph = {}


        
    def addVertex(self, label:Coordinates):
        ### Implement me! ###
        if label not in self.graph:
            self.graph[label] = list()


    def addVertices(self, vertLabels:List[Coordinates]):
        ### Implement me! ###
        for label in vertLabels:
            if label not in self.graph:
                self.graph[label] = list()



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        # remember to return booleans
        edgeNotValid = False

        for edge in self.graph[vert1]:
            if vert2 in edge:
                edgeNotValid = True

        for edge in self.graph[vert2]:
            if vert1 in edge:
                edgeNotValid = True
        
        if not edgeNotValid and vert1.isAdjacent(vert2):
            self.graph[vert1].append({vert2:addWall})
            self.graph[vert2].append({vert1:addWall})
        
        return not edgeNotValid
        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        edgeFound = False
        if vert1.isAdjacent(vert2):
            for edge in self.graph[vert1]:
                if vert2 in edge:
                    edge[vert2] = wallStatus
                    print("edge updated 1"+ str(edge[vert2]) + " " + str(wallStatus))
                    edgeFound = True

            for edge in self.graph[vert2]:
                if vert1 in edge:
                    edge[vert1] = wallStatus
                    print("edge updated 2"+ str(edge[vert1]) + " " + str(wallStatus))

                    edgeFound = True

        return edgeFound


    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        edgeRemoved = False
        if vert1.isAdjacent(vert2):
            for edge in self.graph[vert1]:
                if vert2 in edge:
                    del edge
                    edgeRemoved = True
            for edge in self.graph[vert2]:
                if vert1 in edge:
                    del edge
                    edgeRemoved = True
                    
        return edgeRemoved 


    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return label in self.graph



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        #
        hasEdge = False
        for edge in self.graph[vert1]:
            if vert2 in edge:
                hasEdge = True

        return hasEdge



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        # returns the status of the designated edge
        for edge in self.graph[vert1]:
            if vert2 in edge:
                return edge[vert2]
       
        return False
    

    def neighbours(self, label:Coordinates)->List[Coordinates]:
        # returns a list of coordinates that are neighbours to the label coordinate
        coords = list()
        for edge in self.graph[label]:
            for coordinate in edge:              
                coords.append(coordinate)

        return coords
        