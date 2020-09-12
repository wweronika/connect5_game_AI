import random
import copy
from player import Player

ALPHA = 1
EPSILON = 0.3
GAMMA = 0.9

class QNetwork(Player):

    def __init__(self, sign, size):
        super().__init__(sign, size)
        self.alpha = ALPHA
        self.epsilon = EPSILON
        self.gamma = GAMMA
        self.QDict = {}
        self.type = "qnetwork"



    def bestNextState(self, matrix):
        availablePositions = self.getAvailablePositions(matrix)
        maxQuality = float("-inf")
        bestBoardHash = ""
        bestPosition = []
        for p in availablePositions:
            x = p[0]
            y = p[1]

            # create a new board with own symbol on next position
            newBoard = copy.deepcopy(matrix)
            newBoard[x][y] = self.sign
            # print("newboard")
            # print(newBoard)
            newBoardHash = self.getBoardHash(newBoard)
            
            # assign to value of newBoard max if known and better than max, instantiate as 0 if None
            if newBoardHash in self.QDict.keys():
                if self.QDict.get(newBoardHash) > maxQuality:
                    maxQuality = self.QDict.get(newBoardHash)
                    bestBoardHash = newBoardHash
                    bestPosition = [x,y]
            else:
                self.QDict[newBoardHash] = 0

        # return random available position if every move has equal quality
        if bestBoardHash == "":
            newBoard = copy.deepcopy(matrix)
            # print(availablePositions)
            p = random.choice(availablePositions)
            newBoard[p[0]][p[1]] = self.sign
            self.addMove(bestBoardHash)
            return newBoard

        else:
            self.addMove(bestBoardHash)
            newBoard[bestPosition[0]][bestPosition[1]] = self.sign
            return newBoard

    # returns next board hash after the player's move
    def move(self, matrix):

        # probablility epsilon of experimentation (random position choice)
        e = random.uniform(0,1)

        # random choice
        if e < self.epsilon:
            positions = self.getAvailablePositions(matrix)
            p = random.choice(positions)
            x = p[0]
            y = p[1]
            newBoard = copy.deepcopy(matrix)
            newBoard[x][y] = self.sign
            # print(self.sign + "  does random choice:  " +  str(x) + " , " + str(y))
            # append boardHash to board history
            self.addMove(self.getBoardHash(newBoard))
            return newBoard

        # greedy choice
        else:
            return self.bestNextState(matrix)

    # backpropagating - last move quality increases by reward, 2nd - gamma * reward etc
    # self.gamma = "discount factor"
    def giveReward(self, reward):

        r = reward * self.alpha

        for boardHash in reversed(self.boardHistory):

            if boardHash not in self.QDict.keys():
                self.QDict[boardHash] = 0

            self.QDict[boardHash] += r
            r *= self.gamma

        # clear board history
        self.boardHistory = []


