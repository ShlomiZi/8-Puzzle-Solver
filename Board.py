class Board:
    # constructor
    def __init__(self, brdArr, board_size, list = []):
        self.board = brdArr
        self.size = board_size
        self._checkForCellZero()
        self.path = list

    # get board
    def getBoard(self):
        return self.board

    # check if two boards are equals
    def equals(self, other):
        for i in range(self.size):
            for j in range(self.size):
                # if two non-equal elements found, return False
                if self.board[i][j] != other.board[i][j]:
                    return False

        return True

    # find the index of cell with value 0
    def _checkForCellZero(self):
        for i in range(self.size):
            for j in range(self.size):
                # if cell value is zero, save indices and return
                if (self.board[i][j] == 0):
                    self.zeroRow = i
                    self.zeroCol = j
                    return

    # make a move to a given direction
    def move(self, direction):
        zeroRow = self.zeroRow
        zeroCol = self.zeroCol
        # add the given direction to solution path
        self.path.append(direction)

        if direction == "D":
            self.board[zeroRow][zeroCol] = self.board[zeroRow - 1][zeroCol]
            zeroRow -= 1
            self.board[zeroRow][zeroCol] = 0
            self.zeroRow = zeroRow

        elif direction == "U":
            self.board[zeroRow][zeroCol] = self.board[zeroRow + 1][zeroCol]
            zeroRow += 1
            self.board[zeroRow][zeroCol] = 0
            self.zeroRow = zeroRow

        elif direction == "L":
            self.board[zeroRow][zeroCol] = self.board[zeroRow][zeroCol + 1]
            zeroCol += 1
            self.board[zeroRow][zeroCol] = 0
            self.zeroCol = zeroCol

        elif direction == "R":
            self.board[zeroRow][zeroCol] = self.board[zeroRow][zeroCol - 1]
            zeroCol -= 1
            self.board[zeroRow][zeroCol] = 0
            self.zeroCol = zeroCol

    # return size of board
    def getSize(self):
        return self.size

    # check if able to move towards a given direction
    def ableToMove(self, direction):
        if direction == "U":
            if self.zeroRow == self.size -1:
                return False
            return True

        elif direction == "D":
            if self.zeroRow == 0:
                return False
            return True

        elif direction == "L":
            if self.zeroCol == self.size -1:
                return False
            return True

        elif direction == "R":
            if self.zeroCol == 0:
                return False
            return True

    # return the path so far
    def getPath(self):
        return self.path

    # create a copy of the current (self) board
    def createCopy(self):
        arr = [[] for i in range(int(self.size))]
        for i in range(self.size):
            for j in range(self.size):
                arr[i].append(self.board[i][j])
        # create the path
        list = []
        for direction in self.path:
            list.append(direction)

        # return a new Board instance
        return Board(arr, self.size, list)