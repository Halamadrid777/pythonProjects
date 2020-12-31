# 129 Create a window that will ask the user to enter a number in a text box.
# When they click on a button it will use the code variable.isdigit() to check to see if it is a whole number.
# If it is a whole number, add it to a list box, otherwise clear the entry box. Add another button that will clear the list.
# 130 Alter program 129 to add a third button that will save the list to a .csv file. The code tmp_list = num_list.get(0,END)
# can be used to save the contents of a list box as a tuple called tmp_list.

import atexit
from tkinter import *
import csv
import time

window = Tk()
window.geometry("500x500")
listofbox = Listbox()
listofbox.place(x=75, y=80, width=95, height=120)
tuple_of_box = ()
def entry_to_listBox():
    global tuple_of_box
    if display1_entry.get().isdigit():
        listofbox.insert(END, display1_entry.get())
        tuple_of_box = listofbox.get(0, END)



display1_label = Label(text='Enter a number: ')
display1_label.place(x=30, y=30, width=120, height=25)

display1_entry = Entry(text=0)
display1_entry.place(x=160, y=30, width=80, height=25)

display1_button = Button(text="add nums only", command=entry_to_listBox)
display1_button.place(x=300, y=30, width=175, height=60)








def wirte_csv():
    digits = open('C:/Users/X/Desktop/pythonProjects/Tkinter/tkinter130.csv','w')
    for char in tuple_of_box:
        digits.write(str(char)+'\n')
    digits.close()
    


window.mainloop()
atexit.register(wirte_csv)

# create_csv()