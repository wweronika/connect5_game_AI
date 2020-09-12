import copy
from player import Player

class HumanPlayer(Player):
    def __init__(self, sign):
        super().__init__()
        self.boardHistory = []
        self.sign = sign
        self.type = "human"

    def move(self, matrix, x, y):

        newBoard = copy.deepcopy(matrix)
        newBoard[x][y] = self.sign
        self.addMove(self.getBoardHash(newBoard))
        return newBoard