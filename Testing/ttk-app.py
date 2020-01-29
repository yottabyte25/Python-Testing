from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

style = ttk.Style()

style.configure("BW.TLabel", foreground="white", background="black")

l1 = ttk.Label(text = "test label", style="BW.TLabel")
l1.grid()

mainloop()