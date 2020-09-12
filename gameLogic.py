from tkinter import *
from QNetwork import QNetwork

class GameLogic:
    def __init__(self, size, player1, player2):
        self.size = size
        self.matrix = [["" for j in range(self.size)] for i in range(self.size)]
        self.movesDict = {True : [], False : []} #True - Player 1, False - Player 2
        self.signDict = {True : 'o', False : "x"}
        self.isPlayer1 = True
        self.player1 = player1
        self.player2 = player2
        self.scores = {player1.sign : 0, player2.sign : 0, "tie" : 0}

    def placeAvailable(self,x,y):
        if self.matrix[x][y] == "":
            return True
        return False

        
    def clearBoard(self):
        self.matrix = [["" for j in range(self.size)] for i in range(self.size)]

    def singleMove(self, x,y):   

        self.movesDict.get(self.isPlayer1).append([x,y]) 
        self.isPlayer1 = not self.isPlayer1
        self.matrix[x][y] = self.signDict.get(self.isPlayer1)

    def newGame(self):
        # reset game
        self.isPlayer1 = True
        self.matrix = [["" for j in range(self.size)] for i in range(self.size)]
        self.movesDict = {True : [], False : []} #True - Player 1, False - Player 2

    def winningPlayer(self, winLength): # winLength indicates how many signs in line indicate a win

        # winLength cannot exceed size
        if winLength > self.size: 
            return ""

        # winning strings (e.g. "xxx" and "ooo" for winLength=3)
        winString1 = self.player1.sign * winLength
        winString2 = self.player2.sign * winLength

        # checking for winning strings in row
        for i in range(self.size):
            rowString = ''.join(self.matrix[i]) 
            if winString1 in rowString:
                # print(winString1 + "  " + rowString)
                # print("row won")
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

        for row in self.matrix:
            if "" in row:
                return ""

        return "tie"

    def evaluate(self, winner):
        self.scores[winner] = self.scores.get(winner) + 1
        if winner == self.player1.sign:
            self.player1.giveReward(10)
        elif winner == self.player2.sign:
            self.player2.giveReward(10)
        elif winner == "tie":
            self.player2.giveReward(5)
    
    def autoPlay(self):

        for i in range(1000):
            while self.winningPlayer(self.size) == "":
                # print("printing matrix 1")
                # print(self.matrix)
                self.matrix = self.player1.move(self.matrix)
                # print("printing matrix 2")
                # print(self.matrix)
                if self.winningPlayer(self.size) == "":
                    self.matrix = self.player2.move(self.matrix)

            winner = self.winningPlayer(self.size)
            self.evaluate(winner)
            print("winner  " + str(winner))
            # print(self.matrix)
            # print(self.player2.QDict)
            self.clearBoard()
            #TODO undo, redo


q1 = QNetwork("o", 3)
q2 = QNetwork("x", 3)
game = GameLogic(3,q1,q2)
game.autoPlay()
print(game.scores)