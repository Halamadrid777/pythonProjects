# Create a window that will ask the user to enter a name in a text box.
# When they click on a button it will add it to the end of the list that is displayed on the screen.
# Create another button which will clear the list.

from tkinter import *

window = Tk()
window.geometry("500x500")
# window["bg"] = "blue"

# entername
# name1 = StringVar()

entername = Entry(text=0)
entername.place(x=30, y=30, width=125, height=25)
entername.focus()


# add to list button
def add_list():
    names = entername.get()
    Listbox1.insert(END,names)
    print(Listbox1)


add_button = Button(text="add",command=add_list)
add_button.place(x=165, y=30, width=85, height=25)


# display list to screen
Listbox1 = Listbox()
Listbox1.place(x=30, y=60, width=200, height=200)

# clear the list button


def clear_list():
    Listbox1.delete(0,END)


clear_button = Button(text="clear", command=clear_list)
clear_button.place(x=300, y=45, width=65, height=65)

window.mainloop()
# while clear_list():
#     print("Hello")
