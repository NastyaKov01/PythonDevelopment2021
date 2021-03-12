import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.nextButton = tk.Button(self, text='Next')
        self.quitButton.grid()
        self.nextButton.grid()
        but= "Button"
        for i in range(1, 16):
            name = but + str(i)
            self.name = tk.Button(self, text=str(i))
            self.name.grid()

app = Application()
app.master.title('15')
app.mainloop()
