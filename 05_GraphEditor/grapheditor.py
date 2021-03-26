import tkinter as tk


class Application(tk.Frame):
    """Sample tkinter application class"""

    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize"""
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
        """Create all the widgets"""


class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.Textwidg = tk.Text(self, padx=10, pady=10)
        self.strings = [""]
        self.shapes = ["oval", "rectangle", "line"]
        self.cur_id = 0
        self.coords = [0, 0, 0, 0]
        self.newfig = False
        self.ids = []
        self.Canv = tk.Canvas(self)
        self.Labvar = tk.StringVar()
        #self.Help = tk.Label(self, textvariable=self.Labvar)
        self.Draw = tk.Button(self, text="DRAW", command=self.draw_handler)
        self.Write = tk.Button(self, text="WRITE", command=self.write_handler)
        self.Q = tk.Button(self, text="QUIT", command=self.master.quit)

        self.Textwidg.grid(row=0, column=0)
        self.Canv.grid(row=0, column=1, sticky="news")
        #self.Help.grid(row=1, column=1)
        self.Draw.grid(row=2, column=1)
        self.Write.grid(row=2, column=0)
        self.Q.grid(row=3, column=1)

        self.Textwidg.tag_config("incorrect", foreground="red")
        self.Textwidg.tag_config("correct", foreground="green")

        self.Canv.bind("<Button-1>", self.click_handler)
        self.Canv.bind("<Motion>", self.move_handler)
        self.Canv.bind("<ButtonRelease>", self.release_handler)

    def click_handler(self, event):
        self.coords = [event.x, event.y] * 2
        #print(self.coords)
        #print(self.Canv.find_overlapping(*self.coords))
        #print(self.cur_id)
        if len(self.Canv.find_overlapping(*self.coords)) == 0:
            self.cur_id = self.Canv.create_oval(*self.coords)
            self.newfig = True
        else:
            self.cur_id = self.Canv.find_overlapping(*self.coords)[-1]
            self.newfig = False

    def move_handler(self, event):
        if event.state == 0x0100:
            if self.newfig:
                self.coords[2] = event.x
                self.coords[3] = event.y
                self.Canv.delete(self.cur_id)
                self.cur_id = self.Canv.create_oval(*self.coords, width=2, fill='green')
            else:
                self.Canv.move(self.cur_id, event.x-self.coords[0], event.y-self.coords[1])
                self.coords = [event.x, event.y] * 2

    def release_handler(self, event):
        if self.newfig:
            self.ids.append(self.cur_id)
        index = self.ids.index(self.cur_id)
        options = self.Canv.itemconfigure(self.cur_id)
        coords = self.Canv.coords(self.cur_id)
        filling, width, outline = options['fill'][-1], options['width'][-1], options['outline'][-1]
        string = f"oval {coords[0]} {coords[1]} {coords[2]} {coords[3]} " \
                        f"width='{width}' outline='{outline}' fill='{filling}'"
        self.Textwidg.delete(str(index + 1) + ".0", str(index + 1) + ".0 lineend")
        self.Textwidg.insert(str(index + 1) + ".0", string)
        if self.newfig:
            self.Textwidg.insert(tk.END, "\n")

    def set_tag(self, tag_rem, tag_set, ind):
        self.Textwidg.tag_remove(tag_rem, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")
        self.Textwidg.tag_add(tag_set, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")

    def draw_shapes(self):
        self.strings = self.Textwidg.get("1.0", tk.END).split("\n")
        self.ids.clear()
        for i, s in enumerate(self.strings):
            words = s.split(" ")
            if words[0] in self.shapes:
                try:
                    fid = eval(f"self.Canv.create_{words[0]}({','.join(words[1:])})")
                    self.ids.append(fid)
                    self.set_tag("incorrect", "correct", i)
                except:
                    self.set_tag("correct", "incorrect", i)
            else:
                self.set_tag("correct", "incorrect", i)

    def draw_handler(self):
        for fid in self.Canv.find_all():
            self.Canv.delete(fid)
        self.draw_shapes()

    def write_handler(self):
        pass

app = App(title="Simple Graphic Editor")
app.mainloop()
