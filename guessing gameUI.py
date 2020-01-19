# TODO Fix the UI formating
# TODO Make a better menu (Fix the UI)
# TODO Fix the exit game button and make it work
# TODO Implement a function that goes through a dictionary and displays hints 

from tkinter import *

root = Tk()
def newgame():
    # uses the input from the Entry box
    
    def use_input():
        retrieved_inp = E1.get()
        if retrieved_inp == "d":
            secret_word = "delta"
            Label_D = Label(root, text="The word begins with the letter you typed", font=("Courier", 12), bg = "Black", fg = "white")
            E3 = Entry(root, bd = 5)
            guess_inp = E3.get()
            Button_1 = Button(root, text = "Enter", font=("Courier", 8), bg = "black", fg = "white", command = guess_inp)
            Label_D.grid(row = 3)
            E3.grid(row = 4, column = 1)
            Button_1.grid(row = 4)
            if guess_inp == secret_word:
                winLabel = Label(root, text="You won the game!!!", font=("Courier", 8), bg = "black", fg = "white")
                winLabel2 = Label(root, text="This game is a work in progress and is not finished.", font=("Courier", 8), bg = "black", fg = "white")
                winLabel3 = Label(root, text="Thank you for playing!!!", font=("Courier", 8), bg = "black", fg = "white")
                winLabel.grid()
                winLabel2.grid()
                winLabel3.grid()
            elif guess_inp != secret_word:
                loseLabel = Label(root, text="You lost", font=("Courier", 8), bg = "black", fg = "white")
                loseLabel2 = Label(root, text="Click on the menu and then click New Game", font=("Courier", 8), bg = "black", fg = "white")
                loseLabel.grid()
                loseLabel2.grid()
        elif retrieved_inp == "s":
            Label_S = Label(root, text="The word begins with the letter you typed", font=("Courier", 12), bg = "black", fg = "white")
            E4 = Entry(root, bd = 5)
            guess_inp2 = E4.get()
            Button_2 = Button(root, text = "Enter", font=("Courier", 8), bg = "black", fg = "white", command = guess_inp)
            Label_S.grid(row = 3)
            E4.grid(row = 4, column = 1)
            Button_2.grid(row = 4, column = 2)
            if guess_inp2 == secret_word:
                winLabel4 = Label(root, text="You won the game!!!", font=("Courier", 8))
                winLabel5 = Label(root, text="This game is still a work and progress", font=("Courier", 8))
        elif retrieved_inp == "a":
            Label_A = Label(root, text="The word begins with the letter you typed", font=("Courier", 12), bg = "black", fg = "white")
            E5 = Entry(root, bd = 5)
            Button_3 = Button(root, text = "Enter", font=("Courier", 8), bg = "black", fg = "white")
            Label_A.grid(row = 3, column = 3)
            E5.grid(row = 4)
            Button_3.grid(row = 4)
    
    #The welcoming and prompt to start the game
    welcoming = Label(root, text = "Welcome to the guessing Game!!!", font=("Courier", 22), bg = "black", fg = "white")
    prompt_E1 = Label(root, text = "Type in one of the letters: d,s,a", font=("Courier", 18), bg = "black", fg = "white")
    E1 = Entry(root, bd = 5)
    B1 = Button(root, text="Enter", padx = 10, pady = 10, bd = 3, command = use_input)
    welcoming.grid(row = 1)
    prompt_E1.grid(row = 2)
    E1.grid(row = 2, column = 2)
    B1.grid(row = 2, column = 3)

def exitgame():
    pass

#title
root.title("Guessing game")

# The menu
menubar = Menu(root, bg = "black", fg = "white")
filemenu = Menu(menubar, tearoff=0, bg = "black", fg = "white")
menubar.add_cascade(label="Quick Menu", menu=filemenu)
filemenu.add_command(label="New Game", command=newgame)
filemenu.add_command(label="Exit Game", command=exitgame)
root.config(menu=menubar)

root.mainloop()