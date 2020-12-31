# 125 Write a program that can be used instead of rolling a six-sided die in a board game.
# When the user clicks a button it should display a random whole number between 1 to 6 (inclusive).


from tkinter import *
import random


def roll():
    ramdom_num=random.randint(1,6)
    message1  = Message(text=ramdom_num)
    message1.place(x=30,y=80,width=100,height=100)

window = Tk()
window.geometry("500x500")
window["bg"] = "blue"


# display1 = Label(text="")

pressme_button = Button(text="press me to roll the dice", command=roll)
pressme_button.place(x=30, y=30, width=175, height=35)
pressme_button["bg"] = 'red'


window.mainloop()
