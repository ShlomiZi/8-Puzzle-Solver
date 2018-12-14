from Algorithm import Algo

class BFS(Algo):

    def __init__(self):
        # call parent constructor
        Algo.__init__(self)

    # printing solution to file
    def print(self, board):
        # get the solution path
        path = board.getPath()
        out = open("output.txt", 'w+')
        # writing the solution path
        for d in path:
            out.write(d,)

        out.write(" ",)
        # write number of closed list nodes
        out.write(str(self.closedList),)
        out.write(" 0")
        out.close()


    # run the algorithm
    def run(self, board):
        workingBoard = board
        self.solution = self.buildSolutionBoard(workingBoard)
        self.openList.append(workingBoard.createCopy())

        # run as long as there are nodes in open list
        while not len(self.openList) == 0:

            workingBoard = self.openList.pop(0)
            self.increaseClosedList()
            # if solution found - print and return
            if workingBoard.equals(self.getSolution()):
                self.print(workingBoard)
                return

            # move up if possible
            if workingBoard.ableToMove("U"):
                copy = workingBoard.createCopy()
                copy.move("U")
                self.openList.append(copy)

            # move down if possible
            if workingBoard.ableToMove("D"):
                copy = workingBoard.createCopy()
                copy.move("D")
                self.openList.append(copy)

            # move left if possible
            if (workingBoard.ableToMove("L")):
                copy = workingBoard.createCopy()
                copy.move("L")
                self.openList.append(copy)

            # move right if possible
            if workingBoard.ableToMove("R"):
                copy = workingBoard.createCopy()
                copy.move("R")
                self.openList.append(copy)