#
# Learning in Tamil - Python 
# Example file - functions
#


# define a  function
def func1():
    print("I am a function")

# function that has arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with an argument has default value
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function has variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


func1()
print(func1())
print(func1)
func2(10, 20)
print(func2(10, 20))
print(cube(3))
print(power(2))
print(power(2, 3))
print(power(x=3, num=2))
print(multi_add(4, 5, 10, 4))
