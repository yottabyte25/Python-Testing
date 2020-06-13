import School_1 as s1
import School_2 as s2
import tkinter as tk

root = tk.Tk()
root.geometry("325x250")

def use_e1():
    if e1 == "School 1":
        s1.s.add()
        print(s1.s.total) 

question = tk.Label(root, text = "What school do you want to join?")
option1 = tk.Label(root, text = "School 1")
option2 = tk.Label(root, text = "School 2")
e1 = tk.Entry(root, bd = 3)
b1 = tk.Button(root, command = use_e1, text = "Enter", bd = 3)

question.grid(row = 0, column = 0)
option1.grid(row = 1, column = 0)
option2.grid(row = 2, column = 0)
e1.grid(row = 2, column = 1)
b1.grid(row = 2, column = 2)

root.mainloop()