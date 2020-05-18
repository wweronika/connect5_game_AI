from tkinter import *

class GameGraphics:

    def __init__(self, root):

        self.root = root
        self.gridFrame = Frame(self.root)
        self.gridFrame.pack(side = LEFT) # align grid on the left
        self.width = 680
        self.height = 680
        self.sizeX = 8
        self.sizeY = 8
        self.canvas = Canvas(self.gridFrame, bg="white", width=self.width, height=self.height) #create canvas inside the frame
        self.canvas.pack() # binding it with the rest
        

    def paintGrid(self, matrix):
        
        for i in range(self.sizeX):
            for j in range(self.sizeY):

                # start coords of the first tile (square on the grid)
                xStart = (self.width - 60 * self.sizeX)/2 
                yStart = (self.height - 60 * self.sizeY)/2
                
                # creation of new tile with respect to the starting point
                # each tile 50x50, spacing 10 between each
                # format: (x_leftupper, y_leftupper, x_rightlower, y_rightlower, optionally: fill colour, outline etc)
                self.canvas.create_rectangle(xStart + i*60, yStart + j*60, xStart + 50 + i*60, yStart + 50 + j*60, fill="red", outline="")

                #create an x if denoted so in the matrix
                if matrix[i][j] == "x":

                     self.canvas.create_line(10 + xStart + i*60, 10 + yStart + j*60, xStart + 40 + i*60, yStart + 40 + j*60, width=4)
                     self.canvas.create_line(40 + xStart + i*60, 10 + yStart + j*60, xStart + 10 + i*60, yStart + 40 + j*60, width=4)
                
                #create a circle if denoted so in the matrix
                elif matrix[i][j] == "o":

                    self.canvas.create_oval(10 + xStart + i*60, 10 + yStart + j*60, xStart + 40 + i*60, yStart + 40 + j*60, fill="", outline="black", width=4)