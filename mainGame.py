from tkinter import *
import gameGraphics

class Game:

    def __init__(self):

        self.root = Tk() # initialising the Tk object (graphics handler)
        self.gameGraphics = gameGraphics.GameGraphics(self.root)




if __name__ == "__main__":
    
    game = Game()
    game.gameGraphics.paintGrid()
    game.root.mainloop()



