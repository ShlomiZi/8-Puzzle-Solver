from Algorithm import Algo
from queue import PriorityQueue
import functools
import math


class QueueItem:

    # constructor
    def __init__(self, valueOfBoard, brd, direc, nodesBefore):
        self.heuristicVal = valueOfBoard
        self.board = brd
        self.direction = direc
        self.evaluated = nodesBefore


    # comperator
    # compare by heuristic value, if equal, compare by insertion order
    # if still equal, compare by direction
    def __lt__(self, other):
        if self.heuristicVal == other.heuristicVal:

            if self.evaluated == other.evaluated:
                first = ["U", "D", "L", "R"].index(self.direction)
                second = ["U", "D", "L", "R"].index(other.direction)
                return first < second

            else:
                return self.evaluated < other.evaluated

        return self.heuristicVal < other.heuristicVal

class AStar(Algo):

    # constructor
    def __init__(self):
        Algo.__init__(self)
        # using priority queue for AStar algorithm
        self.queue = PriorityQueue()

    # printing solution to file
    def print(self, board):
        path = board.getPath()
        out = open("output.txt", 'w+')
        # writing the solution path
        for d in path:
            out.write(d, )
        # write the extra information
        out.write(" " + str(self.closedList) + " " + str(len(path)))
        out.close()

    # run the AStar algorithm
    def run(self, b):

        currNode = QueueItem(AStar.getHeuristic(b), b, None, self.closedList)
        self.solution = self.buildSolutionBoard(currNode.board)
        self.queue.put(currNode)

        while not self.queue.empty():
            # get the node with highest priority
            currNode = self.queue.get()
            # increase closed list
            self.increaseClosedList()
            # if solution found, print and return
            if (currNode.board.equals(self.solution)):
                self.print(currNode.board)
                return
            # check all directions
            if currNode.board.ableToMove("U"):
                board = currNode.board.createCopy()
                self.handleDircetion(board, "U")

            if currNode.board.ableToMove("D"):
                board = currNode.board.createCopy()
                self.handleDircetion(board, "D")

            if currNode.board.ableToMove("L"):
                board = currNode.board.createCopy()
                self.handleDircetion(board, "L")

            if currNode.board.ableToMove("R"):
                board = currNode.board.createCopy()
                self.handleDircetion(board, "R")


    # calculating heuristic for a given board
    def getHeuristic(b):

        board = b.getBoard()
        size = b.getSize()
        heuristic = 0
        # calculating manhattan distance
        for i in range(size):
            for j in range (size):
                val = board[i][j]
                # skipping the zero cell
                if (val != 0):
                    rightCol = ((val % size) + size - 1) % size
                    rightRow = math.ceil(val / size) - 1
                else:
                    continue
                heuristic += abs(i - rightRow) + abs(j - rightCol)
        return heuristic

    # handle a direction
    # calculate heuristic for given board, and add it to queue
    def handleDircetion(self, board, direc):
        board.move(direc)
        h4 = AStar.getHeuristic(board)
        h4 += len(board.getPath())
        item = QueueItem(h4, board, direc, self.closedList)
        self.queue.put(item)