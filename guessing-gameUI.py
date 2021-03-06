# Fix the UI formating (Done)
# TODO Make a better menu (In progress)
# TODO Fix the exit game button and make it work(Done)
# TODO Fix the guess entry format and button
# TODO Implement a function that goes through a dictionary and displays hints 

# A required logic statement
'''
while E3 != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess_count +=1
        return use_input
'''

import tkinter as tk

root = tk.Tk()

def application():
    
    def new_game():
        # uses the input from the Entry box
        def use_input():
            guess_count = 0
            guess_limit = 3
            out_of_guesses = False
            retrieved_inp = E1.get()
            if retrieved_inp == "d":
                secret_word = "delta"
                Label_D = tk.Label(root, text="The word begins with the letter you typed", font=("Impact", 26), fg = "green", bg = "black")
                E3 = tk.Entry(root, bd = 5)
                guess_inp = E3.get()
                Button_0 = tk.Button(root, text = "Enter", font=("Impact", 8), padx = 10, pady = 10, bd = 3, command = guess_inp)

                E3.grid(row = 3, column = 1, columnspan = 1)
                Label_D.grid(row = 3, column = 0, columnspan = 1)
                Button_0.grid(row = 3, column = 2, columnspan = 1)
                while E3 != secret_word and not (out_of_guesses):
                    if guess_count < guess_limit:
                        guess_count +=1
                        guess_box = tk.Entry(root, bd = 5)
                        guess_label = tk.Label(root, text = "Guess", font=("Impact", 18), fg = "green", bg = "black")
                        inp = guess_box.get()
                        Button_1 = tk.Button(root, text = "Enter", font=("Impact", 8), padx = 10, pady = 10, bd = 3, command = inp)
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
        welcoming = tk.Label(root, text = "Welcome to the guessing Game!!!", font=("Impact", 22), fg = "green", bg = "black")
        prompt_E1 = tk.Label(root, text = "Type in one of the letters: d,s,a", font=("Impact", 20), fg = "green", bg = "black")
        E1 = tk.Entry(root, bd = 5)
        B1 = tk.Button(root, text="Enter", padx = 10, pady = 10, bd = 3, font=("Impact", 8), command = use_input)
        
        welcoming.grid(row = 1, column = 0, columnspan = 1)
        prompt_E1.grid(row = 2, column = 0, columnspan = 1)
        E1.grid(row = 2, column = 1)
        B1.grid(row = 2, column = 2)
        

    def game_credits():

        def game_credits_del():
            Credit_Label.destroy()
            Credit_Label2.destroy()
            Credit_Label3.destroy()
            Credit_Label4.destroy()
            Credit_Label5.destroy()
            Copyright_Label.destroy()
            Copyright_Label2.destroy()
            Back_Button.destroy()

            menu_welcoming = tk.Label(root, text="Welcome to the guessing game!!!", font=("Impact", 32), fg = "green", bg = "black")
            menu_welcoming2 = tk.Label(root, text="This game is still in devolpment so please beware of bugs.", font=("Impact", 26), fg = "green", bg = "black")
            menu_welcoming3 = tk.Label(root, text="This is in its Alpha stage.", font=("Impact", 26), fg = "green", bg = "black")
            Licence_Label = tk.Label(root, text="By: yottabyte25", font=("Impact", 32), fg = "green", bg = "black")
            menu_welcoming4 = tk.Label(root, text = "Press the 'begin' button below to begin", font=("Impact", 26), fg = "green", bg = "black")
            Licence_Label2 = tk.Label(root, text="If you wish too view the credits click the view button below", font=("Impact", 32), fg = "green", bg = "black")
            Licence_Button1 = tk.Button(root, text = "View", bd = 25, command = game_credits)
            begin_button = tk.Button(root, text = "Begin", bd = 25, command = new_game)
                
            menu_welcoming.grid(row = 1)
            menu_welcoming2.grid(row = 2)
            menu_welcoming3.grid(row = 3)
            menu_welcoming4.grid(row = 5)
            begin_button.grid(row = 7, column = 3, columnspan = 2)
            Licence_Label.grid(row = 4)
            Licence_Label2.grid(row = 6)
            Licence_Button1.grid(row = 8, column = 3)


        menu_welcoming.destroy()
        menu_welcoming2.destroy()
        menu_welcoming3.destroy()
        Licence_Label.destroy()
        menu_welcoming4.destroy()
        Licence_Label2.destroy()
        Licence_Button1.destroy()
        begin_button.destroy()
        

        Credit_Label = tk.Label(root, text = "Game Logic:", font=("Impact", 32), fg = "green", bg = "black")
        Credit_Label2 = tk.Label(root, text = "yottabyte25", font=("Impact", 32), fg = "green", bg = "black")
        Credit_Label3 = tk.Label(root, text = "Menu and Design:", font=("Impact", 32), fg = "green", bg = "black")
        Credit_Label4 = tk.Label(root, text = "yottabyte25", font=("Impact", 32), fg = "green", bg = "black")
        Copyright_Label = tk.Label(root, text = "Copyright © 2020 by yottabyte25", font=("Impact", 32), fg = "green", bg = "black")
        Copyright_Label2 = tk.Label(root, text = "All rights Reserved", font=("Impact", 32), fg = "green", bg = "black")
        Credit_Label5 = tk.Label(root, text = "To go back to the main menu click the back button below", font=("Impact", 32), fg = "green", bg = "black")
        Back_Button = tk.Button(root, text = "Back", bd = 25, command = game_credits_del)

        Credit_Label.grid(row = 1)
        Credit_Label2.grid(row = 2)
        Credit_Label3.grid(row = 3)
        Credit_Label4.grid(row = 4)
        Credit_Label5.grid(row = 5)
        Back_Button.grid(row = 6)
        Copyright_Label.grid()
        Copyright_Label2.grid()

    
    menu_welcoming = tk.Label(root, text="Welcome to the guessing game!!!", font=("Impact", 32), fg = "green", bg = "black")
    menu_welcoming2 = tk.Label(root, text="This game is still in devolpment so please beware of bugs.", font=("Impact", 26), fg = "green", bg = "black")
    menu_welcoming3 = tk.Label(root, text="This is in its Alpha stage.", font=("Impact", 26), fg = "green", bg = "black")
    Licence_Label = tk.Label(root, text="By: yottabyte25", font=("Impact", 32), fg = "green", bg = "black")
    menu_welcoming4 = tk.Label(root, text = "Press the 'begin' button below to begin", font=("Impact", 26), fg = "green", bg = "black")
    Licence_Label2 = tk.Label(root, text="If you wish too view the credits click the view button below", font=("Impact", 32), fg = "green", bg = "black")
    Licence_Button1 = tk.Button(root, text = "View", bd = 25, command = game_credits)
    begin_button = tk.Button(root, text = "Begin", bd = 25, command = new_game)
          
    menu_welcoming.grid(row = 1)
    menu_welcoming2.grid(row = 2)
    menu_welcoming3.grid(row = 3)
    menu_welcoming4.grid(row = 5)
    begin_button.grid(row = 7, column = 3, columnspan = 2)
    Licence_Label.grid(row = 4)
    Licence_Label2.grid(row = 6)
    Licence_Button1.grid(row = 8, column = 3)

    
def exitgame():
    root.destroy()

#title
root.title("Guessing game")

# The menu

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Quick Menu", menu=filemenu)
filemenu.add_command(label="New Game", command=application)
filemenu.add_command(label="Exit Game", command=exitgame)
root.config(menu=menubar)

#background
root.configure(background = "black")

root.mainloop()