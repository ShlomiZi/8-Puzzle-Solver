from Board import Board

class Algo:

    # class attribute - final board state
    Sol = None

    def __init__(self):
        self.openList = []
        self.closedList = 0

    # creating the solution board
    # (once created, use that instance)
    def buildSolutionBoard(self,  board):
        # create the board once
        if Algo.Sol == None:
            size = board.getSize()
            solution = [[] for i in range(int(size))]
            values = 1
            for i in range(size):
                for j in range(size):
                    solution[i].append(values)
                    values+=1

            # add zero at the end
            solution[size - 1].pop(size - 1)
            solution[size - 1].append(0)

            Algo.Sol = Board(solution, size)

        return Algo.Sol

    # set a solution
    def setSolution(self, sol):
        Algo.Sol = sol

    # get the solution
    def getSolution(cls):
        return Algo.Sol

    # increase value of closedList by one.
    def increaseClosedList(self):
        self.closedList += 1

    # get closedList value
    def getClosedList(self):
        return self.closedList

    # set closedList value
    def setClosedList(self, num):
        self.closedList = num