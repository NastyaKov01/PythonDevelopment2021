import tkinter as tk
from itertools import product

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''
        self.Lab = InputLabel(self)
        self.Lab.grid(sticky = "we")
        self.Quit = tk.Button(self, text="Quit", command=self.master.quit)
        self.Quit.grid()


class InputLabel(tk.Label):
    def __init__(self, master=None):
        self.text = tk.StringVar()
        super().__init__(master, textvariable=self.text, font="fixed", padx=20, pady=10, takefocus=1,
                highlightthickness=1)
        self.focus()
        self.cursor_pos = 0
        self.cursor = tk.Frame(self, background="black", width=1)
        self.cursor.place(anchor=tk.CENTER, height=35)
        self.bind("<KeyPress>", self.button_clicked)
        self.bind("<Button-1>", self.mouse_clicked)
    
    def move_cursor(self):
        

    def button_clicked(self, event):
        print(event)
        if event.keysym == "BackSpace":
            self.text.set(self.text.get()[:-1])
        elif event.keysym == "Left":
            pass
        elif event.keysym == "Right":
            pass
        elif event.keysym == "Home":
            pass
        elif event.keysym == "End":
            pass
        elif event.char.isprintable():
            self.text.set(self.text.get() + event.char)
            #print(self.winfo_reqwidth())

    def mouse_clicked(self, event):
        pass

app = Application(title="Sample application")
app.mainloop()
