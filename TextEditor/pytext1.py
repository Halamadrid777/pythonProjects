import tkinter as tk


class Menubar:

    def __init__(self, parent):
        fontSpecs = ('ubuntu', 15)

        menubar = tk.Menu(master, font=fontSpecs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(master, font=fontSpecs)
        file_dropdown.add_command(label="File Open", command=parent.open_file)

        file_dropdown1 = tk.Menu(master, font=fontSpecs)
        file_dropdown1.add_command(label="edit", command=parent.copy_)
        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="edit", menu=file_dropdown1)


class PyText:
    def __init__(self, master):
        font_specs = ('ubuntu', 18)
        master.title("untitled")
        master.geometry('1200x900')
        self.master = master
        self.Menubar = Menubar(self)

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)



    def set_window_title(self):
        pass

    def new_file(self):
        print("hello")

    def open_file(self):
        pass

    def copy_(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
