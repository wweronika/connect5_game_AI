class Game:

    def __init__(self, logic, graphics):
        self.logic = logic
        self.graphics = graphics

    def newGame(self):
        self.logic.newGame()
        self.graphics.newGame()

    def play(self):
                #TODO:
                # create a version with AI vs human
