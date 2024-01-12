#Import randomization
import random

#Welcome to the game
print("Welcome to this simple rock-paper-scissor console game!")

#Player Input
player_1= input("Player 1: ").lower()
choices=["rock", "paper", "scissors"]
player_2= random.choice(choices)
print(player_2)

#Conditional Statements
if player_1== "rock":
    if player_2 == "scissors":
        print("Player1 Wins!")
    elif player_2 == "paper":
        print("Player2 Wins!")
    elif player_1==player_2:
        print("Draw!")
    else:
        print("Error")

elif player_1 == "paper":
    if player_2 == "rock":
        print("Player1 Wins!")
    elif player_2 == "scissors":
        print("Player2 Wins!")
    elif player_1==player_2:
        print("Draw!")

elif player_1 == "scissors":
    if player_2=="paper":
        print("Player1 Wins!")
    elif player_2=="rock":
        print("Player2 Wins!")
    elif player_1==player_2:
        print("Draw!")
    else:
        print("Error")

else:
    print("Error")