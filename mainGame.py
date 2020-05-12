from tkinter import *

class Game:

    def __init__(self):

        self.root = Tk() # initiallising the Tk object (graphics handler)

        self.gridFrame = Frame(self.root)
        self.gridFrame.pack(side = LEFT) # align grid on the left
        self.canvas = Canvas(root, bg="blue", width=600, height=600)
        self.canvas.pack()
        self.root.mainloop()



if __name__ == "__main__":
    
    game = Game()



