#Welcome to the Game
print("Welcome to the Adventure Game!")


#Asking if the user want to proceed
proceed= input("Would you like to proceed? [Yes or No]: ").capitalize()

#Conditional Statements
if proceed == "Yes":
    man_ask= input("A man is asking for a shelter. Will you let him in? [Yes or No]: ").capitalize()
    if man_ask == "Yes": 
        print("Police arrived and asked whether the thief is inside.")
        police_ask = input("Will you tell the police about the man?  [Yes or No]: ")
        if police_ask == "Yes":
            print("You Win!")
        elif police_ask == "No":
            print("Game Over")
        else:
            print("Error")
    elif man_ask == "No": 
        attack_you=input("He attacked on you. Will you knock him down?  [Yes or No]: ").capitalize()
        if attack_you == "Yes":
            print("You Win!")
        elif attack_you=="No":
            print("Game Over")
        else:
            print("Error")
    else:
        print("Error")
elif proceed == "No":
    print("Thank you!")
else:
    print("Error")
