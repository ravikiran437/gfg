#User function Template for python3

def fizzBuzz(number):
    if  number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 :
        print("Fizz")
    else:
        print(number)