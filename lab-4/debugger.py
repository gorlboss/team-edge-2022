import random

options = ["rock", "paper", "scissors"]

print("Let's play Rock, Paper, Scissors!\n")

# Challenge
# Find the bugs below:

while True:
    userInput = input("Do you want to play rock, paper, or scissors?\n\n")
    randomSelection = random.randint(0, 2)
    computerSelection = options[randomSelection]

    print(f"\nYou played: {userInput}\n\nThe computer played: {computerSelection}\n")
  
    if userInput == computerSelection:
        print("It's a tie!\n")
    elif (userInput == "rock" and computerSelection == "paper") or (userInput == "paper" and computerSelection == "scissors") or (userInput == "scissors" and computerSelection == "rock"):
        print("You Lose!\n")
    elif (userInput == "rock" and computerSelection == "scissors") or (userInput == "paper" and computerSelection == "rock") or (userInput == "scissors" and computerSelection == "paper"):
      print("You Win!\n")
    else:
        print("That's not an option. You Lose!\n")
    