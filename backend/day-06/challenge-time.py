'''
if a number is divisible by 3, print 'Fizz'
if a number is divisible by 5, print 'Buzz'
if a number is both divisible by 3 and 5, print 'FizzBuzz!'
'''
limit = int(input("Limit: "))

i = 1
while (i<=limit):
    if (i%3==0) and (i%5==0):
        print("FizzBuzz!")
    elif i % 3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
    i += 1