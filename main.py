from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def msg():
    messagebox.showwarning("Alert","Stop! Virus Found. ")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=200, y=200)

root.mainloop()