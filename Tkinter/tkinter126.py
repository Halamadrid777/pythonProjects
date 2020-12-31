# 126 Create a program that will ask the user to enter a number in a box.
#  When they click on a button it will add that number to a total and display it in another box.
#  This can be repeated as many times as they want and keep adding to the total.
# There should be another button that resets the total back to 0 and empties the original text box, ready for them to start again

from tkinter import *


number=0

window = Tk()
window.geometry("500x500")
window["bg"] = "blue"
total = 0
def add():
    global total
    number_to_add = int(enter_number.get())
    total+=number_to_add
    message = Message(text=total)
    message.place(x=30, y=55, width=125, height=125)
    message['bg'] = "red"
enter_number = Entry(textvar=number)
enter_number.place(x=30, y=30, width=35, height=25)
enter_number['bg'] = "white"

add_buton = Button(text="add number", command=add)
add_buton.place(x=100, y=30, width=100, height=25)
window.mainloop()


