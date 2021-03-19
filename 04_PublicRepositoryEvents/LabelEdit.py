import tkinter as tk

SYMBOL_SIZE = 10

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
        super().__init__(master, textvariable=self.text, font="Fixedsys", takefocus=1,
                highlightthickness=1, anchor="w")
        self.focus()
        self.cursor_pos = 0
        self.cursor = tk.Frame(self, background="black", width=1)
        self.print_cursor()
        self.cursor.place(anchor=tk.CENTER, height=20)
        self.bind("<KeyPress>", self.button_clicked)
        self.bind("<Button-1>", self.mouse_clicked)
    
    def print_cursor(self):
        self.cursor.place(x = self.cursor_pos, y = 10)

    def button_clicked(self, event):
        if event.keysym == "BackSpace":
            self.text.set(self.text.get()[:-1])
            if self.cursor_pos > 0:
                self.cursor_pos -= SYMBOL_SIZE
            self.print_cursor()
        elif event.keysym == "Left":
            if self.cursor_pos > 0:
                self.cursor_pos -= SYMBOL_SIZE
            self.print_cursor()
        elif event.keysym == "Right":
            if self.cursor_pos < len(self.text.get()) * SYMBOL_SIZE:
                self.cursor_pos += SYMBOL_SIZE
            self.print_cursor()
        elif event.keysym == "Home":
            self.cursor_pos = 0
            self.print_cursor()
        elif event.keysym == "End":
            self.cursor_pos = len(self.text.get()) * SYMBOL_SIZE
            self.print_cursor()
        elif event.char.isprintable():
            self.text.set(self.text.get() + event.char)
            self.cursor_pos += SYMBOL_SIZE
            self.print_cursor()

    def mouse_clicked(self, event):
        self.focus()
        self.cursor_pos = event.x // SYMBOL_SIZE * SYMBOL_SIZE
        self.print_cursor()

app = Application(title="Sample application")
app.mainloop()
