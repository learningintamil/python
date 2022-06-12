#
# Learning in Tamil - Python 
# Example file - functions
#


# new function definition 
def functionA():
    print("I am functionA")

# How to use arguments in a function
def functionB(arg1, arg2):
    print(arg1, " ", arg2)

# How to return a value from a function
def functionSquare(x):
    return x*x

# How to give default value to an argument in a function
def functionPower(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# How to create a function with variable number of arguments
def multiArgFunction(*args):
    result = 0
    for x in args:
        result = result + x
    return result


functionA()
print(functionA())
print(functionA)
functionB(20, 30)
print(functionB(20, 30))
print(functionSquare(5))
print(functionPower(2))
print(functionPower(2, 3))
print(functionPower(x=3, num=2))
print(multiArgFunction(3, 3, 5, 5, 4))
print(multiArgFunction(3, 3, 5, 5, 4, 10))
