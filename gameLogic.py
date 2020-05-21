from tkinter import *

class GameLogic:
    def __init__(self, size):
        self.size = size
        self.matrix = [["" for j in range(self.size)] for i in range(self.size)]
        self.movesDict = {True : [], False : []} #True - Player 1, False - Player 2
        self.isPlayer1 = True

    def singleMove(self, x,y):
        # append a coordinate pair to the current player's history
        self.movesDict.get(self.isPlayer1).append([x,y]) 
        self.isPlayer1 = not self.isPlayer1

    def newGame(self):
        # reset game
        self.isPlayer1 = True
        self.matrix = [["" for j in range(self.size)] for i in range(self.size)]
        self.movesDict = {True : [], False : []} #True - Player 1, False - Player 2