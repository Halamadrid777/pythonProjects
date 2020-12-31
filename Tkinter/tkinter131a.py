# 131 Create a program that will allow the user to create a new .csv file.
# It should ask them to enter the name and age of a person and then allow 
# them to add this to the end of the file they have just created.

from tkinter import *
import csv


def createFile():
    add_csv_name = name_entry.get()+".csv"
    csvfile = open(add_csv_name,'w')
    csvfile.write("Name: "+name_entry.get()+"  "+'Age: '+age_entry.get())
    csvfile.close()

    


window = Tk()
window.title("CSV file")
window.geometry("600x600")

name_label =Label(text="Enter your name:  ")
name_label.place(x=30,y=30,width=95,height=25)
name_entry = Entry(text=0)
name_entry.place(x=135, y=30, width=125, height=25)


age_label =Label(text="Enter your age:  ")
age_label.place(x=30,y=60,width=95,height=25)
age_entry = Entry(text=1)
age_entry.place(x=135, y=60, width=125, height=25)

add_csv = Button(text="add csv",command=createFile)
add_csv.place(x=295, y=30,width=45, height=45)


window.mainloop()