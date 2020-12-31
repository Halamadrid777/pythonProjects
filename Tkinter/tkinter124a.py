# Create a window that will ask the user to enter their name. 
# When they click on a button it should display the message “Hello” and their name
#  and change the background colour and font colour of the message box. 

from tkinter import *

geo = "600x500"

def call():
    name = input1.get()
    name_hello = str("Hello "+name)
    label2 = Message(text=name_hello)
    label2.place(x=30, y=85,width=125, height=45)
    label2["bg"]="blue" # background colour
    label2["fg"] = "white" #font colour


window = Tk()
window.title("window")
window.geometry(geo)

label1 = Label(text="Enter your name: ")
label1.place(x=30,y=25)

name = StringVar()
input1 = Entry(textvar=name)
input1.place(x=30, y=45,width=125,height=25)

press_button = Button(text="press  me!",command=call)
press_button.place(x=30,y=75, width=75, height=25)


window.mainloop()