from tkinter import * # import everything from tkinter

def call():
    msg = Label(window,text="you pressed the button")
    msg.place(x=30,y=50)
    button['bg']="blue"
    button["fg"]= "whilte"

window = Tk()
window.title("My first tkinter Programme")
window.geometry("200x110")
button = Button(text="Press Me",command=call)
button.place(x=30,y=20,width=120,height=25)
window.mainloop()