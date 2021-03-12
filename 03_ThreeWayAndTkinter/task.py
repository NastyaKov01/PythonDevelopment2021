import tkinter as tk
from random import shuffle

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky="nsew")
        self.createWidgets()

    def randHandler(self):
        shuffle(self.numList)
        for i in range(15):
            b, k = self.buttons[i], self.numList.index(i)
            b.grid(row = 1 + k//4, column = k%4, sticky = "nsew")


    def createWidgets(self):
        toplevel = self.winfo_toplevel()
        toplevel.rowconfigure(0, weight=1)
        toplevel.columnconfigure(0, weight=1)

        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.numList, self.buttons = [], []
        self.quitButton = tk.Button(self, text = 'Quit', command = self.quit)
        self.newButton = tk.Button(self, text = 'New', command = self.randHandler)
        for i in range(15):
            self.numList.append(i)
            name = "Button" + str(i+1)
            self.name = tk.Button(self, text=str(i+1))
            self.buttons.append(self.name)
        self.numList.append(15)

        self.quitButton.grid(row = 0, column = 2, columnspan = 2, sticky = "EW")
        self.newButton.grid(row = 0, column = 0, columnspan = 2, sticky = "EW")
        self.randHandler()


app = Application()
app.master.title('15')
app.mainloop()
