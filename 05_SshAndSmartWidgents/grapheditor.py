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
        self.shapes = ["oval", "rectangle"]
        self.cur_id, self.coords = 0, [0, 0, 0, 0]
        self.newfig, self.isoval = False, True
        self.ids = []
        self.Canv = tk.Canvas(self)
        self.Draw = tk.Button(self, text="DRAW", command=self.draw_handler)
        self.Write = tk.Button(self, text="WRITE", command=self.write_handler)
        self.Q = tk.Button(self, text="QUIT", command=self.master.quit)

        self.Shape = tk.Label(self, text="shape")
        self.Width = tk.Label(self, text="width")
        self.Fill = tk.Label(self, text="fill")
        self.Outline = tk.Label(self, text="outline")
        self.Woptlist = ['1.0', '2.0', '3.0', '4.0', '5.0']
        self.Foptlist = ['green', 'blue', 'red', 'yellow', 
                                'black', 'white', 'cyan', 'magenta']
        self.Outlist = ['black', 'blue', 'red', 'green', 'yellow', 
                                'white', 'cyan', 'magenta']
        self.Shvar = tk.StringVar()
        self.Shvar.set(self.shapes[0])
        self.Wvar = tk.StringVar()
        self.Wvar.set(self.Woptlist[0])
        self.Fvar = tk.StringVar()
        self.Fvar.set(self.Foptlist[0])
        self.Ovar = tk.StringVar()
        self.Ovar.set(self.Outlist[0])
        self.Shmenu = tk.OptionMenu(self, self.Shvar, *self.shapes)
        self.Wmenu = tk.OptionMenu(self, self.Wvar, *self.Woptlist)
        self.Fmenu = tk.OptionMenu(self, self.Fvar, *self.Foptlist)
        self.Omenu = tk.OptionMenu(self, self.Ovar, *self.Outlist)

        self.Shape.grid(row=0, column=1, sticky="news")
        self.Width.grid(row=0, column=2, sticky="news")
        self.Outline.grid(row=0, column=3, sticky="news")
        self.Fill.grid(row=0, column=4, sticky="news")
        self.Shmenu.grid(row=1, column=1, sticky="news")
        self.Wmenu.grid(row=1, column=2, sticky="news")
        self.Omenu.grid(row=1, column=3, sticky="news")
        self.Fmenu.grid(row=1, column=4, sticky="news")
        self.Textwidg.grid(row=2, column=0)
        self.Canv.grid(row=2, column=1, columnspan=4, sticky="news")
        self.Draw.grid(row=3, column=2, columnspan=2)
        self.Write.grid(row=3, column=0)
        self.Q.grid(row=4, column=3)

        self.Textwidg.tag_config("incorrect", background="red")
        self.Textwidg.tag_config("correct", background="white")

        self.Canv.bind("<Button-1>", self.click_handler)
        self.Canv.bind("<Motion>", self.move_handler)
        self.Canv.bind("<ButtonRelease>", self.release_handler)

    def click_handler(self, event):
        self.coords = [event.x, event.y] * 2
        if len(self.Canv.find_overlapping(*self.coords)) == 0:
            self.cur_id = self.Canv.create_oval(*self.coords)
            self.newfig = True
        else:
            self.cur_id = self.Canv.find_overlapping(*self.coords)[-1]
            self.newfig = False

    def move_handler(self, event):
        if event.state == 0x0100:
            if self.newfig:
                self.coords[2], self.coords[3] = event.x, event.y
                self.Canv.delete(self.cur_id)
                s, w, f, o = self.Shvar.get(), self.Wvar.get(), self.Fvar.get(), self.Ovar.get()
                if s == "oval":
                    self.isoval = True
                    self.cur_id = self.Canv.create_oval(*self.coords, width=w, fill=f, outline=o)
                else:
                    self.isoval = False
                    self.cur_id = self.Canv.create_rectangle(*self.coords, width=w, fill=f, outline=o)
            else:
                self.Canv.move(self.cur_id, event.x-self.coords[0], event.y-self.coords[1])
                self.coords = [event.x, event.y] * 2
    
    def release_handler(self, event):
        if self.newfig:
            self.ids.append((self.cur_id, self.isoval))
        coords = self.Canv.coords(self.cur_id)
        s, w, f, o = self.Shvar.get(), self.Wvar.get(), self.Fvar.get(), self.Ovar.get()
        for i, obj in enumerate(self.ids):
            if obj[0] == self.cur_id:
                index = i
        self.Canv.delete(self.cur_id)
        if s == "oval":
            self.isoval = True
            self.cur_id = self.Canv.create_oval(*coords, width=w, fill=f, outline=o)
        else:
            self.isoval = False
            self.cur_id = self.Canv.create_rectangle(*coords, width=w, fill=f, outline=o)
        self.ids[index] = (self.cur_id, self.isoval)
        self.write_info((self.cur_id, self.isoval))

    def get_config(self, fid):
        options = self.Canv.itemconfigure(fid)
        coords = self.Canv.coords(fid)
        width, filling, outline = options['width'][-1], options['fill'][-1], options['outline'][-1]
        return width, filling, outline, coords

    def write_info(self, obj):
        index = self.ids.index(obj)
        fid = obj[0]
        width, filling, outline, coords = self.get_config(fid)
        string = f" {coords[0]} {coords[1]} {coords[2]} {coords[3]} " \
                 f"width='{width}' outline='{outline}' fill='{filling}'"
        self.Textwidg.delete(str(index + 1) + ".0", str(index + 1) + ".0 lineend")
        if self.ids[index][1]:
            self.Textwidg.insert(str(index + 1) + ".0", "oval")
        else:
            self.Textwidg.insert(str(index + 1) + ".0", "rectangle")
        self.Textwidg.insert(str(index + 1) + ".0 lineend", string)
        if len(self.Textwidg.get("1.0", tk.END).split("\n")) == index + 2:
            self.Textwidg.insert(tk.END, "\n")
    
    def set_tag(self, tag_rem, tag_set, ind):
        self.Textwidg.tag_remove(tag_rem, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")
        self.Textwidg.tag_add(tag_set, str(ind + 1) + ".0", str(ind + 1) + ".0 lineend")

    def draw_shapes(self):
        strings = self.Textwidg.get("1.0", tk.END).split("\n")
        self.ids.clear()
        for i, s in enumerate(strings):
            words = s.split(" ")
            if words[0] in self.shapes:
                try:
                    fid = eval(f"self.Canv.create_{words[0]}({','.join(words[1:])})")
                    if words[0] == "oval":
                        obj = (fid, True)
                    else:
                        obj = (fid, False)
                    self.ids.append(obj)
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
        self.Textwidg.delete('1.0', tk.END)
        for obj in self.ids:
            self.write_info(obj)


app = App(title="Simple Graphic Editor")
app.mainloop()
