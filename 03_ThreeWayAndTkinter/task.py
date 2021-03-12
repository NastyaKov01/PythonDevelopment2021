import tkinter as tk
from random import shuffle
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky = "nsew")
        self.createWidgets()

    def randHandler(self):
        shuffle(self.numList)
        for i in range(15):
            b, k = self.buttons[i], self.numList.index(i)
            b.grid(row = 1 + k//4, column = k%4, sticky = "nsew")

    def move(self, i):
        pos15 = self.numList.index(15)
        pos = self.numList.index(i)
        row15, col15 = pos15 // 4, pos15 % 4
        rowb, colb = pos // 4, pos % 4
        if (col15 == colb and (row15 - 1 == rowb or row15 + 1 == rowb) or
            row15 == rowb and (col15 - 1 == colb or col15 + 1 == colb)):
            num = int(self.numList[pos])
            self.numList[pos15], self.numList[pos] = self.numList[pos], self.numList[pos15]
            self.buttons[num].grid(row = 1 + row15, column = col15, sticky = "nsew")
            win = True
            for i in range(15):
                if self.numList.index(i) != i:
                    win = False
            if win:
                messagebox.showinfo(title = None, message = "YOU WIN!")
                self.randHandler()
        

    def createWidgets(self):
        toplevel = self.winfo_toplevel()
        toplevel.rowconfigure(0, weight=1)
        toplevel.columnconfigure(0, weight=1)

        for i in range(5):
            if i == 0:
                self.columnconfigure(i, weight = 1)
            elif i == 4:
                self.rowconfigure(i, weight = 1)
            else:
                self.rowconfigure(i, weight=1)
                self.columnconfigure(i, weight=1)

        self.numList, self.buttons = [], []
        self.quitButton = tk.Button(self, text = 'Quit', command = self.quit)
        self.newButton = tk.Button(self, text = 'New', command = self.randHandler)
        for i in range(15):
            self.numList.append(i)
            name = "Button" + str(i+1)
            def catch(j = i):
                self.move(j)
            self.name = tk.Button(self, text=str(i+1), command = catch)
            self.buttons.append(self.name)
        self.numList.append(15)

        self.quitButton.grid(row = 0, column = 2, columnspan = 2, sticky = "EW")
        self.newButton.grid(row = 0, column = 0, columnspan = 2, sticky = "EW")
        self.randHandler()


app = Application()
app.master.title('15')
app.mainloop()
