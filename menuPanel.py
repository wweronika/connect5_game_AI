from tkinter import *

class MenuPanel:

    def __init__(self, root, graphics):
        self.root = root
        self.buttonNames = ["newgame", "undo", "redo"]
        self.buttons = {name: Button(master=self.root, text=name, command=(lambda n=name : self.onClickButton(n))) for name in self.buttonNames}
        self.graphics = graphics

    def paintMenu(self):

        for (buttonKey, buttonValue) in self.buttons.items():
            buttonValue.config(bg="white", text=buttonKey)
            buttonValue.pack(side=TOP)

    def onClickButton(self, name):
        if name == "newgame":
            self.graphics.newGame()

