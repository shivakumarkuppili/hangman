from os import system
import random
import time
import tkinter as tk


def cls():
    system ('cls')

def hangman_game():
    cls()
    
    print("\nWelcome")
    print("Lets play Hangman\n")

    name = input("What is your name?\n")
    name = name.capitalize()
    print("\nHello " + name + ", It is time to play HamgMan")
    print("\nStart Guessing...\n")
    guessed_word = []

    # Creats a variable with an empty value
    guesses = ""

    # Determine the Number of turns
    turns = 10                                  #ToDo : Change the turns that you want to give the player

    # Here we set the Secret
    words = [
        "Forrest Gump",
        "Hangman Project",
        "The Godfather",
        "The Green Mile",
        "Hotel Rwanda",
        "Goodfellas",
        "Scarface",
        "The Terminal",
        "Million Dollar Baby",
        "Driving Miss Daisy",
        "Catch Me If You Can",
        "Chinatown",
        "The Departed",
        "Dances with Wolves",
        "Ford v Ferrari",
        "Little Women",
        "A Star Is Born",
        "Dear Basketball",
        "pawan kalyan",
        "ratan tata",
        "ms dhoni"
    ]

    word = random.choice(words)
    word = word.upper()

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=" ")

            elif char == " ":
                print(' / ', end=" ")
                
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            note_input1 ="\n\n\n"+name + """\n\n\nYOU WON!!\n :) GAME IS OVER U ROCKED IT"""
            print("\nyou won!!")
            note1 =  note_input1
            time.sleep(1)
        
            root = tk.Tk()
            root.title("Pin Your Note")
            root.geometry("300x300")

            
        
            tk.Label(root, text=note1).pack()

            root.mainloop()
          
            break

        guess = input("\n\nGuess a Character : ")
        guess = guess.upper()

        if len(guess) > 1:
            break

        guesses += guess
        if (guess not in word) and (guess not in guessed_word):
            turns -= 1
            guessed_word.append(guess)
            print("\nWrong Guess :/")
        cls()

        print("\nYou have ", + turns, "more guesses")
        print("\nWrong Character's Entered : ", guessed_word)
        print('\n')

        if turns == 0:
          
            note_input ="\n\n\n"+name+ "\n\n\nGAME IS OVER,YOU LOST!!  \nTRY AGAIN LATER :("
            print("\nyou loose!!")
            note =  note_input
            time.sleep(1)
        
            root = tk.Tk()
            root.title("Pin Your Note")
            root.geometry("300x300")

            
        
            tk.Label(root, text=note).pack()

            root.mainloop()

    check = input("\nDo you want to play again Y/N?")

    if check == "Y" or check == "y" :
        hangman_game()


hangman_game()