import tkinter as tk

root = tk.Tk()

def app():
    menu_welcoming = tk.Label(root, text="Welcome to the guessing game!!!", font=("Impact", 32), fg = "green", bg = "black")
    menu_welcoming2 = tk.Label(root, text="This game is still in devolpment so please beware of bugs.", font=("Impact", 26))
    menu_welcoming3 = tk.Label(root, text="This is in its Alpha stage.", font=("Impact", 26))
    menu_welcoming4 = tk.Label(root, text = "Press the button below to begin", font=("Impact", 26))
    begin_button = tk.Button(root, text = "Begin", bd = 25, command = new_game)
    
    menu_welcoming.grid(row = 1, column = 1)
    menu_welcoming2.grid(row = 2, column = 1)
    menu_welcoming3.grid(row = 3, column = 1)
    menu_welcoming4.grid(row = 4, column = 1)
    begin_button.grid(row = 5, column = 3)

def new_game():
    # uses the input from the Entry box
    def create_window():
        window = tk.Toplevel(root)

        def use_input():
            guess_count = 0
            guess_limit = 3
            out_of_guesses = False
            retrieved_inp = E1.get()
            if retrieved_inp == "d":
                secret_word = "delta"
                Label_D = tk.Label(root, text="The word begins with the letter you typed", font=("Impact", 16), fg = "green", bg = "black")
                E3 = tk.Entry(root, bd = 5)
                guess_inp = E3.get()
                Button_0 = tk.Button(root, text = "Enter", font=("Courier", 8), padx = 10, pady = 10, bd = 3, command = guess_inp, fg = "green", bg = "black")

                E3.grid(row = 3, column = 1, columnspan = 1)
                Label_D.grid(row = 3, column = 0, columnspan = 1)
                Button_0.grid(row = 3, column = 2, columnspan = 1)
                while E3 != secret_word and not (out_of_guesses):
                    if guess_count < guess_limit:
                        guess_count +=1
                        guess_box = tk.Entry(root, bd = 5)
                        guess_label = tk.Label(root, text = "Guess", font=("Courier", 18))
                        inp = guess_box.get()
                        Button_1 = tk.Button(root, text = "Enter", font=("Courier", 8), padx = 10, pady = 10, bd = 3, command = inp)
                        guess_box.grid(row = 4, column = 1)
                        Button_1.grid(row = 4, column = 2)
                        guess_label.grid(row = 4, column = 0, columnspan = 1)
                        if inp != secret_word and not (out_of_guesses):
                            return
                        else:
                            winLabel = tk.Label(root, text = "You win!!!")
                            winLabel.grid(row = 5, column = 0, columnspan = 1)
                            break
                    else:
                        out_of_guesses = True
                if out_of_guesses == True:
                    loseLabel = tk.Label(root, text="You lost")
                    loseLabel.grid(row = 5, column = 0)
            elif retrieved_inp == "s":
                secret_word = "Santa"
                Label_S = tk.Label(root, text="The word begins with the letter you typed", font=("Courier", 12))
                E4 = tk.Entry(root, bd = 5)
                guess_inp2 = E4.get()
                Button_2 = tk.Button(root, text = "Enter", font=("Courier", 8), command = guess_inp)
                
                Label_S.grid(row = 3)
                E4.grid(row = 4, column = 1)
                Button_2.grid(row = 4, column = 2)
                while E3 != secret_word and not (out_of_guesses):
                    if guess_count < guess_limit:
                        guess_box = tk.Entry(root, bd = 5)
                        guess_box.grid(row = 6, column =1)
                        guess_count +=1
                    else:
                        out_of_guesses = True
                if out_of_guesses == True:
                    lose_label = tk.Label(root, text="You lost")
                    lose_label.grid(row = 7, column = 1)
            elif retrieved_inp == "a":
                secret_word = "Alpha"
                Label_A = tk.Label(root, text="The word begins with the letter you typed", font=("Courier", 12))
                E5 = tk.Entry(root, bd = 5)
                Button_3 = tk.Button(root, text = "Enter", font=("Courier", 8))
                
                Label_A.grid(row = 3, column = 3)
                E5.grid(row = 4)
                Button_3.grid(row = 4)
                while E3 != secret_word and not (out_of_guesses):
                    if guess_count < guess_limit:
                        guess_box = tk.Entry(root, bd = 5)
                        guess_box.grid(row = 6, column =1)
                        guess_count +=1
                    else:
                        out_of_guesses = True
                if out_of_guesses == True:
                    lose_label = tk.Label(root, text="You lost")
                    lose_label.grid(row = 7, column = 1)
        
        #The welcoming and prompt to start the game
    
    
    welcoming = tk.Label(root, text = "Welcome to the guessing Game!!!", font=("Courier", 22))
    prompt_E1 = tk.Label(root, text = "Type in one of the letters: d,s,a", font=("Courier", 20))
    E1 = tk.Entry(root, bd = 5)
    B1 = tk.Button(root, text="Enter", padx = 10, pady = 10, bd = 3, font=("Courier", 8), command = create_window)
          
    welcoming.grid(row = 1, column = 0, columnspan = 1)
    prompt_E1.grid(row = 2, column = 0, columnspan = 1)
    E1.grid(row = 2, column = 1)
    B1.grid(row = 2, column = 2)

def exitgame():
    pass

#title
root.title("Guessing game")

# The menu

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Quick Menu", menu=filemenu)
filemenu.add_command(label="New Game", command=app)
filemenu.add_command(label="Exit Game", command=exitgame)
root.config(menu=menubar)

#background
root.configure(background = "black")

root.mainloop()