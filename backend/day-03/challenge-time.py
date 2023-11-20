#Welcome to the Game
print("Welcome to the Adventure Game!")


#Asking if the user want to proceed
print("Would you like to proceed? [(0) Yes: (1) No]")
proceed= int(input())

#Conditional Statements
if proceed == 0:
    print("A man is asking for a shelter. Will you let him in? [(0) Yes: (1) No]")
    man_ask= int(input())
    if man_ask == 0: 
        print("Police arrived and asked whether the thief is inside.")
        print("Will you tell the police about the man?  [(0) Yes: (1) No]")
        police_ask = input()
        if police_ask == 0:
            print("You Win!")
        elif police_ask==1:
            print("Game Over")
        else:
            print("Error")
    elif man_ask==1: 
        print("He attacked on you. Will you knock him down?  [(0) Yes: (1) No]")
        attack_you=input()
        if attack_you == 0:
            print("You Win!")
        elif attack_you==1:
            print("Game Over")
        else:
            print("Error")
    else:
        print("Error")
elif proceed == 1:
    print("Thank you!")
else:
    print("Error")
