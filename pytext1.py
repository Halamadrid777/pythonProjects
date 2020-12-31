import tkinter as tk


class Menubar:
    def __init__(self,parent):
        fontSpecs = ('ubuntu',18)
        menubar = tk.Menu(master,font=fontSpecs,tearoff=0)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(master,font=fontSpecs,tearoff=0)
        file_dropdown.add_command(label='New',command=parent.Open_file)


        menubar.add_cascade(label="file",menu=file_dropdown)
class PyText:
    def __init__(self,master):
        fontSpecs = ('ubuntu',15)
        master.title("untitled")
        master.geometry('1200x700')
        self.master = master

        self.textarea = tk.Text(master,font=fontSpecs)
        self.scroll = tk.Scrollbar(master,command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        


        self.Menubar = Menubar(self)

    def Open_file(self):
        print("hello world")


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()