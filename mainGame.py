from tkinter import *
import gameGraphics

class Game:

    def __init__(self):

        self.root = Tk() # initialising the Tk object (graphics handler)
        self.gameGraphics = gameGraphics.GameGraphics(self.root)




if __name__ == "__main__":
    
    game = Game()

    #temporary matrix for showcasing the x and o graphics 
    # TODELETE later

    m = [[0 for i in range(8)] for j in range(8)]
    m[0][0] = "x"
    m[0][1] = "o"

    
    game.gameGraphics.paintGrid(m)
    game.root.mainloop()



