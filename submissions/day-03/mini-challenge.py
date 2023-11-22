#Entering a number
num= int(input("Enter a number: "))

#Conditional Staement
if num>0:
    print(f"{num} is a Positive number!")
elif num<0:
    print(f"{num} is a Negative number!")
else:
    print("That number is a Zero!")