from tkinter import *
import gameLogic

class GameGraphics:

    def __init__(self, root):

        self.root = root
        self.gridFrame = Frame(self.root)
        self.gridFrame.pack(side = LEFT) # align grid on the left
        self.width = 680
        self.height = 680
        self.size = 3
        self.canvas = Canvas(self.gridFrame, bg="white", width=self.width, height=self.height) #create canvas inside the frame
        self.canvas.pack() # binding it with the rest
        self.logic = gameLogic.GameLogic(self.size)

    def paintGrid(self):
        
        for i in range(self.size):
            for j in range(self.size):

                # start coords of the first tile (square on the grid)
                xStart = (self.width - 60 * self.size)/2 
                yStart = (self.height - 60 * self.size)/2
                
                # creation of new tile with respect to the starting point
                # each tile 50x50, spacing 10 between each
                # format: (x_leftupper, y_leftupper, x_rightlower, y_rightlower, optionally: fill colour, outline etc)
                self.canvas.create_rectangle(xStart + i*60, yStart + j*60, xStart + 50 + i*60, yStart + 50 + j*60, fill="red", outline="", tag="tile")
                
                self.canvas.tag_bind("tile", '<ButtonPress-1>', lambda e: self.paintSign(e))
  
    def paintSign(self, event):

        # retrieve ID of current tile
        currentID = self.canvas.find_withtag("current")[0]
        print(currentID)
        x = (currentID - 1) // self.size
        y = (currentID - 1) % self.size

        if self.logic.singleMove(x,y):
            # player 1 move
            if self.logic.isPlayer1:
                self.paintO(x,y)
            # player 2 move
            else:
                self.paintX(x,y)

        if self.logic.winningPlayer(self.size) != "":
            print(self.logic.winningPlayer(self.size))
            self.newGame()
   
    # paints an X in tile given coordinates
    def paintX(self,i,j):

        xStart = (self.width - 60 * self.size)/2 
        yStart = (self.height - 60 * self.size)/2
        self.canvas.create_line(10 + xStart + i*60, 10 + yStart + j*60, xStart + 40 + i*60, yStart + 40 + j*60, width=4, tag="x")
        self.canvas.create_line(40 + xStart + i*60, 10 + yStart + j*60, xStart + 10 + i*60, yStart + 40 + j*60, width=4, tag="x")
    
    # paints an O in tile given coordinates
    def paintO(self,i,j):
        xStart = (self.width - 60 * self.size)/2 
        yStart = (self.height - 60 * self.size)/2
        self.canvas.create_oval(10 + xStart + i*60, 10 + yStart + j*60, xStart + 40 + i*60, yStart + 40 + j*60, fill="", outline="black", width=4, tag="o")
        
    def newGame(self):
        print(self.canvas.find_withtag("x"))
        print(self.canvas.find_withtag("o"))
        self.canvas.delete("x")
        self.canvas.delete("o")
        self.logic.newGame()
