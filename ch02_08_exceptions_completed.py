#
# Learning in Tamil - Python 
# Example file - Exceptions
#


try:
    x = 10 / 0
except:
    print("Well that didn't work!")

# how to catch specific exceptions
try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10 / num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
finally:
    print("The finally section always runs")

