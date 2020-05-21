from tkinter import *

class GameLogic:
    def __init__(self, size):
        self.size = size
        self.matrix = [["" for j in range(self.size)] for i in range(self.size)]
        self.movesDict = {"x" : [], "o" : []}
        self.isPlayer1 = True
