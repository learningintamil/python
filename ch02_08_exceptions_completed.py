#
# Learning in Tamil - Python 
# Example file - Exceptions
#

# How to handle error in a program
try:
    x = 8 / 0
except:
    print("This didn't work.")

# catching specific exceptions
try:
    inputNumber = input("Enter a number: ")
    num = int(inputNumber)
    print(100 / num)
except ZeroDivisionError as e:
    print("You can't divide by zero")
except ValueError as e:
    print("This is not a valid number.!")
    print(e)
finally:
    print("finally block always runs.")
