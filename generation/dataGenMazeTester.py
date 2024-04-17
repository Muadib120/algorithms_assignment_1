# -------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# This is the entry point to run the program.
# Refer to usage() for exact format of input expected to the program.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------


import sys
import time
import json
from typing import List

from maze.util import Coordinates
from maze.maze import Maze
from maze.arrayMaze import ArrayMaze
from maze.graphMaze import GraphMaze

from generation.mazeGenerator import MazeGenerator
from generation.recurBackGenerator import RecurBackMazeGenerator


# this checks if Visualizer has been imported properly.
# if not, likely missing some packages, e.g., matplotlib.
# in that case, regardless of visualisation flag, we should set the canVisualise flag to False which will not call the visuslisation part.
canVisualise = True
try:
	from maze.maze_viz import Visualizer
except:
	Visualizer = None
	canVisualise = False



def usage():
	"""
	Print help/usage message.
	"""

	# On Teaching servers, use 'python3'
	# On Windows, you may need to use 'python' instead of 'python3' to get this to work
	print('python3 mazeTester.py', '<configuration file>')
	sys.exit(1)


#
# Main.
#
if __name__ == '__main__':
	# Fetch the command line arguments
	args = sys.argv

	if len(args) != 2:
		print('Incorrect number of arguments.')
		usage()


	# open configuration file		
	fileName: str = args[1]
	with open(fileName,"r") as configFile:
		# use json parser
		configDict = json.load(configFile)

		# assign to variables storing various parameters
		dsApproach: str = configDict['dataStructure']
		rowNum: int = configDict['rowNum']
		colNum: int = configDict['colNum']
		entrances: List[List[int]] = configDict['entrances']
		exits: List[List[int]] = configDict['exits']
		genApproach: str = configDict['generator']
		bVisualise: bool = configDict['visualise']
		numPasses: int = configDict['numPasses']

		#
		# Initialise maze object (which also selects which data structure implementation is used).

		#           10x10   5x20    4x25    2x50    1x100   20x5    25x4    50x2   100x1    1x1    5x5  10x10  20x20   30x30   40x40   50x50   75x75  100x100
		iterList = [[9,9],[-5,10],[-1, 5],[-2,25],[-1,50],[19,-95],[5,-1],[25,-2],[50,-1],[-99,0],[4,4],[5,5],[10,10],[10,10],[10,10],[10,10],[25,25],[25,25]]

		for value in iterList:
			print("########################################################################################") #line to separate each set of results
			rowNum += value[0]
			colNum += value[1]
			for x in range(3):
				if x == 0:
					dsApproach = 'array'
				if x == 1:
					dsApproach = 'adjlist'
				if x == 2:
					dsApproach = 'adjmat'
				
				totalTime = 0.0
				if rowNum == 100 and colNum == 100:
					numPasses = 3
				for i in range(numPasses):

					maze: Maze = None
					if dsApproach == 'array':
						maze = ArrayMaze(rowNum, colNum)
					elif dsApproach == 'adjlist':
						maze = GraphMaze(rowNum, colNum, dsApproach)
					elif dsApproach == 'adjmat':
						maze = GraphMaze(rowNum, colNum, dsApproach)
					else:
						print('Unknown data structure approach specified.')
						usage()

					# add the entraces and exits
					for [r,c] in entrances:
						maze.addEntrance(Coordinates(r, c))
					for [r,c] in exits:
						maze.addExit(Coordinates(r, c))

					
					#
					# Generate maze
					#
					generator: MazeGenerator = None
					if genApproach == 'recur':
						generator = RecurBackMazeGenerator()
					else:
						print('Unknown generator approach specified.')
						usage()


					# timer for generation
					startGenTime : float = time.perf_counter()

					generator.generateMaze(maze)

					# stop timer
					endGenTime: float = time.perf_counter()

					#print(f'Generation took {endGenTime - startGenTime:0.4f} seconds')
					totalTime += endGenTime - startGenTime
					# add/generate the entrances and exits
					generator.addEntrances(maze)
					generator.addExits(maze)

					#
					# Display maze.
					#
					if bVisualise and canVisualise:
						cellSize = 1
						visualiser = Visualizer(maze, cellSize) 
						visualiser.show_maze()
					
				print(f'Type: {dsApproach}:\n\tPasses: {numPasses}\n\tDimensions: {rowNum},{colNum}\n\tTotal time: {totalTime:0.4f}seconds\n\tAverage time: {totalTime/numPasses:0.4f}\n\n')