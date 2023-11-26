def divide(a, b):
    return a / b

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    quotient = divide(a, b)
except ValueError as e:
    print(e)
    print("Enter only a number pls")
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero lol ")
except Exception as e:
    print(f"Invalid input: {e}")

else:
    print(f"The quotient is {quotient}")