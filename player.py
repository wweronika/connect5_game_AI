class Player:

    def __init__(self, sign, size):
        self.sign = sign
        self.boardHistory = []
        self.size = size
        self.isAwaitHuman = False
        self.type = ""

    # gets hash of a board
    def getBoardHash(self, matrix):
        matrixFlat = []
        for row in matrix:
            for item in row:
                matrixFlat.append(item)
        boardHash = str(matrixFlat)
        return boardHash

        # returns all free positions in [x,y] format
    def getAvailablePositions(self, matrix):

        positions = []

        for i in range(self.size):
            for j in range(self.size):
                if matrix[i][j] == "":
                    positions.append([i,j])
        return positions

    # append move to board history
            
    def addMove(self, board):
        self.boardHistory.append(board)