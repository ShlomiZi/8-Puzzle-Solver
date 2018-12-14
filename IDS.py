from Algorithm import Algo

class IDS(Algo):

    # constructor
    def __init__(self):
        super().__init__()
        self.pathDepth = 0

    # printing solution to file
    def print(self, board):
        path = board.getPath()
        out = open("output.txt", 'w+')
        # writing the solution path
        for d in path:
            out.write(d, )
        # write the extra information
        out.write(" " + str(self.closedList) + " " + str(self.pathDepth))
        out.close()

    # run the IDS algorithm
    def run(self, board):
        self.setSolution(self.buildSolutionBoard(board))
        self._IDDFS(board)


    def _IDDFS(self, root):

        # as long as solution not found, increase the depth
        while not self._DLS(root, self.pathDepth):
            self.closedList = 1
            self.pathDepth += 1

    # depth-limited DFS function
    def _DLS(self, current, currDepth):

        if (currDepth == 0):
            if (current.equals(Algo.getSolution(self))):
                self.print(current)
                return True

        else:
            # look for solution
            for d in ["U", "D", "L", "R"]:
                copiedBoard = current.createCopy()
                # check the above direction
                if d == "U":
                    if copiedBoard.ableToMove("U"):
                        self.operateOnDirection(copiedBoard, "U")
                        if self._DLS(copiedBoard, currDepth - 1):
                            return True
                # check below direction
                elif d == "D":
                    if copiedBoard.ableToMove("D"):
                        self.operateOnDirection(copiedBoard, "D")
                        if self._DLS(copiedBoard, currDepth - 1):
                            return True
                # check left direction
                elif d == "L":
                    if copiedBoard.ableToMove("L"):
                        self.operateOnDirection(copiedBoard, "L")
                        if self._DLS(copiedBoard, currDepth - 1):
                            return True
                # check right direction
                else:
                    if copiedBoard.ableToMove("R"):
                        self.operateOnDirection(copiedBoard, "R")
                        if self._DLS(copiedBoard, currDepth - 1):
                            return True

        return False

    # operate on given board and direction
    def operateOnDirection(self, board, direc):
        self.increaseClosedList()
        board.move(direc)

