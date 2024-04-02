import tkinter as tk
from tkinter import ttk
import random

userChoice = "nothing yet"
computerChoice = "nothing yet"

def terminate(event=None): # exiting program
    exit()

def reset_game(): # resetting the game
    global userChoice, computerChoice
    userChoice = "nothing yet"
    computerChoice = "nothing yet"
    Player.config(text="The player chose " + userChoice)
    Computer.config(text="The computer chose " + computerChoice)
    Results.config(text=" ")
    play_game() 

def scissors(event=None): #this happens when you choose scissors
    global userChoice
    userChoice = "scissors"
    print("Scissors")

def rock(event=None):     #this haappens when you choose rock
    global userChoice
    userChoice = "rock"
    print("Rock")

def paper(event=None):    #this happens when you choose paper
    global userChoice
    userChoice = "paper"
    print("Paper")

def get_computer_choice(): #this makes the 'computer' choose randomly
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(computer_choice): #this determines whether the user or the computer wins
    global userChoice #referencing the actual variable in the program
    if userChoice == computer_choice:
        Results.config(text="It's a tie")
    elif (userChoice == 'rock' and computer_choice == 'scissors') or \
         (userChoice == 'paper' and computer_choice == 'rock') or \
         (userChoice == 'scissors' and computer_choice == 'paper'):
        Results.config(text="You win!")
    else:
        Results.config(text="Computer wins!")

def play_game():
    global userChoice
    userChoice = "nothing yet"
    Player.config(text="The player chose " + userChoice)
    
    main.update()
    
    while userChoice == "nothing yet":
        main.update()

    computer_choice = get_computer_choice()
    determine_winner(computer_choice)
    Player.config(text="The player chose " + userChoice)
    Computer.config(text="The computer chose " + computer_choice)

main = tk.Tk()

content = ttk.Frame(main)
mainframe = ttk.Frame(content, borderwidth=8, relief="ridge", width=1280, height=720)
debug = ttk.Frame(mainframe, borderwidth=2,relief="sunken")
PlayerFrame = ttk.Frame(mainframe,borderwidth=1)
ComputerFrame = ttk.Frame(mainframe,borderwidth=1)
ResultFrame = ttk.Frame(mainframe,borderwidth=4)
ButtonsFrame = ttk.Frame(mainframe,borderwidth=6,relief="raise")

restartButton = ttk.Button(debug,text="Restart Program",command=reset_game) #reset
terminateButton = ttk.Button(debug,text="Terminate Program",command=terminate) #exit
Player = ttk.Label(PlayerFrame,text="The player chose " + userChoice, foreground="black", font=("Helvetica",22))
Computer = ttk.Label(ComputerFrame,text="The computer chose " + computerChoice , foreground="black", font=("Helvetica",22))
Results = ttk.Label(ResultFrame,text=" ", foreground="black", font=("Helvetica", 22))
Rock = ttk.Button(ButtonsFrame,text="Rock", style='TButton',command=rock)
Paper = ttk.Button(ButtonsFrame,text="Paper", style='TButton',command=paper)
Scissors = ttk.Button(ButtonsFrame,text="Scissors", style='TButton',command=scissors)



content.grid(column=0, row=0)
mainframe.grid(column=0,row=0)

#remmove these frames in final
debug.grid(column=0,row=0)
restartButton.grid(column=0,row=0)
terminateButton.grid(column=1,row=0)

PlayerFrame.grid(column=0,row=1)
Player.grid(column=0,row=0)

ComputerFrame.grid(column=0,row=2)
Computer.grid(column=0,row=0)

ResultFrame.grid(column=0,row=3)
Results.grid(column=0,row=0)

ButtonsFrame.grid(column=0,row=4)
Rock.grid(column=0,row=0,columnspan=2)
Paper.grid(column=2,row=0,columnspan=2)
Scissors.grid(column=4,row=0,columnspan=2)

play_game()

main.mainloop()
