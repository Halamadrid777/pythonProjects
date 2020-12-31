# 129 Create a window that will ask the user to enter a number in a text box. 
# When they click on a button it will use the code variable.isdigit() to check to see if it is a whole number. 
# If it is a whole number, add it to a list box, otherwise clear the entry box. Add another button that will clear the list. 

from tkinter import *

window = Tk()
window.geometry("500x500")
Listbox1= Listbox()
Listbox1.place(x=75,y=80,width=95,height=120)

def entry_to_listBox():
    if display1_entry.get().isdigit():
        Listbox1.insert(END,display1_entry.get())

display1_label= Label(text='Enter a number: ')
display1_label.place(x=30,y=30,width=120,height=25)

display1_entry=Entry(text=0)
display1_entry.place(x=160, y=30, width=80, height=25)

display1_button = Button(text="add nums only",command =entry_to_listBox )
display1_button.place(x=300,y=30,width=175, height=60)




window.mainloop()