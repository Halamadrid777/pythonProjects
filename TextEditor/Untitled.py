import tkinter as tk
# Hello world
class  Menubar:
    def __init__(self,parent):
        FontSpecs = ('ubuntu',18)
        menubar = tk.Menu(master,font=FontSpecs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(master,font=FontSpecs,tearoff=0)
        file_dropdown.add_command(label="New",accelerator="ctrl+N",command=parent.New)


        menubar.add_cascade(label="file",menu=file_dropdown)
        
class PyText:
    def __init__(self,master):
        FontSpecs = ('ubuntu',18)
        self.master = master
        master.title('Untitled')
        master.geometry("1200x700")

        self.Menubar = Menubar(self)


        self.textarea = tk.Text(master,font=FontSpecs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
    def New(self):
        print("hello")

if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()