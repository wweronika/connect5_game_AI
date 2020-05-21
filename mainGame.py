from tkinter import *
import gameGraphics
import menuPanel

class Game:

    def __init__(self):

        self.root = Tk() # initialising the Tk object (graphics handler)

        self.graphicsFrame = Frame(self.root)
        self.menuFrame = Frame(self.root)

        self.graphicsFrame.pack(side=LEFT)
        self.menuFrame.pack(side=RIGHT)

        self.graphics = gameGraphics.GameGraphics(self.graphicsFrame)
        self.menu = menuPanel.MenuPanel(self.menuFrame, self.graphics)

        self.graphics.paintGrid()
        self.menu.paintMenu()



if __name__ == "__main__":
    
    game = Game()
    game.root.mainloop()



