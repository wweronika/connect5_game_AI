from tkinter import *

class GameLogic:
    def __init__(self, size):
        self.size = size
        self.matrix = [["" for j in range(self.size)] for i in range(self.size)]
        self.movesDict = {True : [], False : []} #True - Player 1, False - Player 2
        self.signDict = {True : 'o', False : "x"}
        self.isPlayer1 = True

    def singleMove(self, x,y):
        # append a coordinate pair to the current player's history
        if self.matrix[x][y] == "":    
            self.movesDict.get(self.isPlayer1).append([x,y]) 
            self.isPlayer1 = not self.isPlayer1
            self.matrix[x][y] = self.signDict.get(self.isPlayer1)
            return True
        else:
            return False

    def newGame(self):
        # reset game
        self.isPlayer1 = True
        self.matrix = [["" for j in range(self.size)] for i in range(self.size)]
        self.movesDict = {True : [], False : []} #True - Player 1, False - Player 2

    def winningPlayer(self, winLength): # winLength indicates how many signs in line indicate a win

        # winLength cannot exceed size
        if winLength > self.size: 
            return None

        # winning strings (e.g. "xxx" and "ooo" for winLength=3)
        winString1 = self.signDict.get(True) * winLength
        winString2 = self.signDict.get(False) * winLength

        # checking for winning strings in row
        for i in range(self.size):
            rowString = ''.join(self.matrix[i]) 
            if winString1 in rowString:
                return "o"
            elif winString2 in rowString:
                return "x"

        # checking for winning strings in column
        for j in range(self.size):
            columnString = ''.join(self.matrix[i][j] for i in range(self.size)) 
            if winString1 in columnString:
                return "o"
            elif winString2 in columnString:
                return "x"
        
        # checking for winning strings in diagonal
        for j in range(self.size - winLength + 1):
            diagonalString1 = ''.join(self.matrix[i+j][i] for i in range(self.size-j))
            diagonalString2 = ''.join(self.matrix[i][i+j] for i in range(self.size-j))

            if winString1 in diagonalString1 or winString1 in diagonalString2:
                return "o"
            elif winString2 in diagonalString1 or winString2 in diagonalString2:
                return "x"

        return ""

        #TODO undo, redo
