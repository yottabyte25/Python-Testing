from tkinter import *

root = Tk()

e = Entry(root, width=100)
e.pack()

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButon = Button(root, text="Click Me!", padx=50, pady=50, command=myClick)
myButon.pack()


root.mainloop()