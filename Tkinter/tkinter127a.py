# Create a window that will ask the user to enter a name in a text box.
# When they click on a button it will add it to the end of the list that is displayed on the screen.
# Create another button which will clear the list.

from tkinter import *

window = Tk()
window.geometry("500x500")

#
lable1 = Label(text="Enter Name: ")
lable1.place(x=30, y=30, width=100, height=25)


def add_names():
    names1 = entry_name.get()
    Listbox1.insert(END,names1)

def remove_names():
    Listbox1.delete(0,END)


entry_name = Entry(text=0)
entry_name.place(x=140, y=30, width=150,height=25)

add_names = Button(text='add names',command=add_names)
add_names.place(x=300, y=30, width=75,height=25)

remove_names = Button(text="clear",command =remove_names)
remove_names.place(x=300, y=90, width=45,height=45)

Listbox1 = Listbox()
Listbox1.place(x=30,y=59,width=250,height=250)
window.mainloop()
