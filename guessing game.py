guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

key = input("Welcome to the Guessing game! \n Type in one of the letters: d,a,s: ")
if key.lower() == "d" : 
    secret_word = "delta"
    print("The word you are trying to guess is apart of the military alphabet\nThe first letter begins with d")
elif key.lower() == "a" :
    secret_word = "alpha"
    print("The word begins with an a and is mentioned in the military alphabet")
else:
    if key.lower() == "s" :
        secret_word = "santa"
        print ("It is apart of christmas.")
while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count +=1
    else: 
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, you lose.")
else:
    print("You win!")
print("You have reached the end of the game so far.")
print("I am planning to add more gamemodes later on in the future as well along with other things.")
print("Thank you for playing!!!")

def replay_function():
    pass

# replay = input("Do you want to play again?\nY/N: ")
#if replay.upper() or replay.lower() == "N" :
#    pass
#elif replay.upper() or replay.lower() == "Y" :
#    replay_function()