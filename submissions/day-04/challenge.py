#Rock Paper Scissors Game
#Welcome to the game
print("Welcome to this simple rock-paper-scissor console game!")

#Player Input
player_1= input("Player 1: ")
player_2= input("Player 2: ")

#Conditional Statements
if player_1== "Rock":
    if player_2 == "Scissors":
        print("Player1 Wins!")
    elif player_2 == "Paper":
        print("Player2 Wins!")
    elif player_1==player_2:
        print("Draw!")
    else:
        print("Error")

elif player_1 == "Paper":
    if player_2 == "Rock":
        print("Player1 Wins!")
    elif player_2 == "Scissors":
        print("Player2 Wins!")
    elif player_1==player_2:
        print("Draw!")

elif player_1 == "Scissors":
    if player_2=="Paper":
        print("Player1 Wins!")
    elif player_2=="Rock":
        print("Player2 Wins!")
    elif player_1==player_2:
        print("Draw!")
    else:
        print("Error")

else:
    print("Error")