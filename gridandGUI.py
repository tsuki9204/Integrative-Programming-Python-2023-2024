from tkinter import *
from tkinter.ttk import *
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
    TestLabel.config(text=" ")
    play_game() 

def scissors(event=None): # this happens when you choose scissors
    global userChoice
    userChoice = "scissors"
    print("Scissors")

def rock(event=None):     # this happens when you choose rock
    global userChoice
    userChoice = "rock"
    print("Rock")

def paper(event=None):    # this happens when you choose paper
    global userChoice
    userChoice = "paper"
    print("Paper")

def get_computer_choice(): # this makes the 'computer' choose randomly
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(computer_choice): # this determines whether the user or the computer wins
    global userChoice # referencing the actual variable in the program
    if userChoice == computer_choice:
        TestLabel.config(text="It's a tie")
    elif (userChoice == 'rock' and computer_choice == 'scissors') or \
         (userChoice == 'paper' and computer_choice == 'rock') or \
         (userChoice == 'scissors' and computer_choice == 'paper'):
        TestLabel.config(text="You win!")
    else:
        TestLabel.config(text="Computer wins!")

def play_game():
    global userChoice
    userChoice = "nothing yet"
    Player.config(text="The player chose " + userChoice)
    
    mainWindow.update()
    
    while userChoice == "nothing yet":
        mainWindow.update()
    ExitButton.grid(row=0, column=0, columnspan=8, sticky="ew")  # Centering the buttons

    computer_choice = get_computer_choice()
    determine_winner(computer_choice)
    Player.config(text="The player chose " + userChoice)
    Computer.config(text="The computer chose " + computer_choice)

if __name__ == "__main__":
    mainWindow = Tk()
    mainWindow.title('Main Window')

    button_font = ("Helvetica", 16)

    TestLabel = Label(text=" ", foreground="black", font=("Helvetica", 22))
    TestLabel.grid(row=1, column=0, columnspan=8, sticky="ew")  # Centering the label

    Player = Label(text="The player chose " + userChoice, foreground="black", font=("Helvetica", 22))
    Player.grid(row=2, column=0, columnspan=8, sticky="ew")  # Centering the label

    Computer = Label(text="The computer chose " + computerChoice, foreground="black", font=("Helvetica", 22))
    Computer.grid(row=3, column=0, columnspan=8, sticky="ew")  # Centering the label

    style = Style()
    style.configure('TButton', font=button_font)

    Scissors = Button(text="Scissors", style='TButton')
    Scissors.grid(row=4, column=4, columnspan=2, sticky="ew")  # Centering the buttons
    Scissors.bind('<Button-1>', scissors)

    Rock = Button(text="Rock", style='TButton')
    Rock.grid(row=4, column=2, columnspan=2, sticky="ew")  # Centering the buttons
    Rock.bind('<Button-1>', rock)

    Paper = Button(text="Paper", style='TButton')
    Paper.grid(row=4, column=0, columnspan=2, sticky="ew")  # Centering the buttons
    Paper.bind('<Button-1>', paper)

    ExitButton = Button(text="Terminate Program",padding=10)
    ExitButton.bind('<Button-1>', terminate)

    ResetButton = Button(text="Restart Program",padding=10, style='TButton')
    ResetButton.grid(row=0, column=7, columnspan=1, sticky="e")  # Aligning to the right
    ResetButton.config(command=reset_game)

    mainWindow.update_idletasks() # Update idle tasks to get correct frame size
    frame_width = mainWindow.winfo_width()
    frame_height = mainWindow.winfo_height()

    # Calculate the total width and height needed
    total_width = frame_width + 20
    total_height = frame_height + 20

    # Set geometry to fit all frames and buttons
    mainWindow.geometry(f"{total_width}x{total_height}")

    play_game()

    mainWindow.mainloop()
