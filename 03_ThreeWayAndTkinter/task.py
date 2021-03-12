import tkinter as tk
from random import shuffle

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def randHandler(self):
        shuffle(self.numList)
        for i in range(15):
            b, k = self.buttons[i], self.numList.index(i)
            b.grid(row = 1 + k//4, column = k%4, sticky = "nsew")


    def createWidgets(self):
        self.numList, self.buttons = [], []
        self.quitButton = tk.Button(self, text = 'Quit', command = self.quit)
        self.newButton = tk.Button(self, text = 'New', command = self.randHandler)
        for i in range(15):
            self.numList.append(i)
            name = "Button" + str(i+1)
            self.name = tk.Button(self, text=str(i+1))
            self.buttons.append(self.name)
        self.numList.append(15)

        self.quitButton.grid(row = 0, column = 2, columnspan = 2)
        self.newButton.grid(row = 0, column = 0, columnspan = 2)
        self.randHandler()


app = Application()
app.master.title('15')
app.mainloop()
