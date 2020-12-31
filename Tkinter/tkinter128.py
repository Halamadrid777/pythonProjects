# 128 1 kilometre = 0.6214 miles and 1 mile = 1.6093 kilometres. 
# Using these figures, make a program that will allow the user to convert between miles and kilometres. 

from tkinter import *

window = Tk()
window.geometry("500x500")


mile = 0
def convert_toMile():
    inKM = float(convert_toMile_entry.get())
    global mile
    mile = inKM / 1.6093
    convert_toMile_message = Message(text=mile)
    convert_toMile_message.place(x=250,y=120,width=259,height=200)
    convert_toMile_message["justify"]='centere'


KM = 0
def convert_toKM():
    inMile = float(convert_toKM_entry.get())
    global KM
    KM = inMile*1.6093
    convert_toKM_Message = Message(text=KM)
    convert_toKM_Message.place(x=10,y=120,width=259,height=25)
    convert_toKM_Message["justify"]="centere"
    



convert_toKM_label = Label(text="Enter amount of mile:  ")
convert_toKM_label.place(x=30,y=30,width=120,height=25)
convert_toKM_entry = Entry(text=0)
convert_toKM_entry.place(x=30,y=55, width=150, height=25)
convert_toKM_button = Button(text="convert to km",command = convert_toKM)
convert_toKM_button.place(x=30,y=80,width=125, height=25)



convert_toMile_label = Label(text="Enter amount of KM:  ")
convert_toMile_label.place(x=250,y=30,width=120, height=25)
convert_toMile_entry = Entry(text=1)
convert_toMile_entry.place(x=250,y=55, width=120, height=25)
convert_toMile_BUtton = Button(text="convert to mile",command=convert_toMile)
convert_toMile_BUtton.place(x=250,y=80,width=125, height=25)


window.mainloop()