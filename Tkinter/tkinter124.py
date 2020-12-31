# Create a window that will ask the user to enter their name. 
# When they click on a button it should display the message “Hello” and their name
#  and change the background colour and font colour of the message box. 


from tkinter import *


def call():
    name = entry_box.get()
    labelZ = str("hello "+name)
    # print(labelZ)
    display_name = Label(text=labelZ)
    display_name.place(x=30,y = 85, width=100, height=55)
    display_name["bg"]="red"


window = Tk()
window.title(string="Window")
xy = "300x300"
window.geometry(xy)


label = Label(text="Enter your name:")
label.place(x=30,y=30,)

name = StringVar()
entry_box = Entry(textvar = name)
entry_box.place(x=30, y=50,width=125,height=25)


click_button = Button(text="pressme",command = call)
click_button.place(x=30, y=75,width=55, height=25)
window.mainloop()