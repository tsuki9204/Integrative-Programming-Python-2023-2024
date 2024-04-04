import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import requests
from io import BytesIO

# Define global variables
userChoice = "nothing yet"
computerChoice = "nothing yet"

# Function to terminate the program
def terminate(event=None):
    exit()

# Function to reset the game
def reset_game():
    global userChoice, computerChoice
    userChoice = "nothing yet"
    computerChoice = "nothing yet"
    Player.config(text="The player chose " + userChoice)
    Computer.config(text="The computer chose " + computerChoice)
    Results.config(text=" ")
    play_game() 

# Function for when the user chooses scissors
def scissors(event=None):
    global userChoice
    userChoice = "scissors"
    print("Scissors")

# Function for when the user chooses rock
def rock(event=None):
    global userChoice
    userChoice = "rock"
    print("Rock")

# Function for when the user chooses paper
def paper(event=None):
    global userChoice
    userChoice = "paper"
    print("Paper")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(computer_choice):
    global userChoice
    if userChoice == computer_choice:
        Results.config(text="It's a tie")
    elif (userChoice == 'rock' and computer_choice == 'scissors') or \
         (userChoice == 'paper' and computer_choice == 'rock') or \
         (userChoice == 'scissors' and computer_choice == 'paper'):
        Results.config(text="You win!")
    else:
        Results.config(text="Computer wins!")

# Function to play the game
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

# Initialize the main window
main = tk.Tk()

# Fetch and load images from URLs
response_scissors = requests.get("https://i.ibb.co/2YRpmQZ/scissors.jpg?fbclid=IwAR1uymGwX1SEm8C8ItqGr8EYLM9B-tqig78Xwoz-nioHmZaK11qvAyT-xuk_aem_ASstGA4HTtagBGfjSKernvyjmA0h6KLLhzbN2AVaKcu1jJEWJeMeL5DLvBacvxehjlKEzN9I2FxJgtdLQQBw3_Yy")
image_scissors = Image.open(BytesIO(response_scissors.content))
image_scissors = image_scissors.resize((50, 50), Image.LANCZOS)
image_scissors = ImageTk.PhotoImage(image_scissors)

response_paper = requests.get("https://i.ibb.co/vLxPDX2/paper.jpg?fbclid=IwAR1DZw6Kl_iCF6PPB5j7FSQd9Z366X-yyToslNWs3jvsEkNri1p4r5aOxpE_aem_AStIHxyJEJwfEg2YU0z-MUS5sxnVEY8xTtl-rvPtrd-oA_PU-d58X0symGhSEgT1mxc9ZWj9Vp4j37Qvt63n04fh")
image_paper = Image.open(BytesIO(response_paper.content))
image_paper = image_paper.resize((50, 50), Image.LANCZOS)
image_paper = ImageTk.PhotoImage(image_paper)

response_rock = requests.get("https://i.ibb.co/RvPfHZy/rock.jpg?fbclid=IwAR0QD23ZGEPu0g-ml0qc48BtmlzuJVZ-aiFk5QaPWKgFQB1BftC_XrVDzeA_aem_ASvXMWXYP8VHPpgewt1gDNzMTunmaoAcKyUzpHlZJBjUHRQpQ6XbyMVNOf5rOyR8AUU6qR5Wz7AXNBJZ7BBLUC58")
image_rock = Image.open(BytesIO(response_rock.content))
image_rock = image_rock.resize((50, 50), Image.LANCZOS)
image_rock = ImageTk.PhotoImage(image_rock)

# Create GUI elements
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
Rock = ttk.Button(ButtonsFrame, image=image_rock, style='TButton', command=rock)
Paper = ttk.Button(ButtonsFrame, image=image_paper, style='TButton', command=paper)
Scissors = ttk.Button(ButtonsFrame, image=image_scissors, style='TButton', command=scissors)

# Grid layout
content.grid(column=0, row=0)
mainframe.grid(column=0,row=0)

# Debug frame
debug.grid(column=0,row=0)
restartButton.grid(column=0,row=0)
terminateButton.grid(column=1,row=0)

# Player frame
PlayerFrame.grid(column=0,row=1)
Player.grid(column=0,row=0)

# Computer frame
ComputerFrame.grid(column=0,row=2)
Computer.grid(column=0,row=0)

# Result frame
ResultFrame.grid(column=0,row=3)
Results.grid(column=0,row=0)

# Buttons frame
ButtonsFrame.grid(column=0,row=4)
Rock.grid(column=0,row=0)
Paper.grid(column=1,row=0)
Scissors.grid(column=2,row=0)

play_game()

main.mainloop()
