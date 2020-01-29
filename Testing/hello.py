from tkinter import *

root = Tk()

# Creating a Label widget
myLabel = Label(root, text="Hola comos ta?")
myLabel1 = Label(root, text="This a thing")
# Making the label appear onto the screen

myLabel.grid(row=0, column=0)
myLabel1.grid(row=1, column=0)


root.mainloop()
