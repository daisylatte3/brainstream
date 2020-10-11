from random import randint

options = ["Rock", "Paper", "Scissors"]

computer = options[randint(0,2)]

player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock" or "rock":
        if computer == "Paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Paper" or "paper":
        if computer == "Scissors":
            print("The computer wins!")
        else:
            print("You win!")
    elif player == "Scissors" or "scissors":
        if computer == "Rock":
            print("The computer wins")
        else:
            print("You win!")
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = options[randint(0,2)]