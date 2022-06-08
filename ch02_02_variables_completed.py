#
# Learning in Tamil - Python 
# Example file - Variables
#

# Basic data types: Numbers, Strings, Booleans, Sequences, Dictionaries
integerVar = 5
floatVar = 13.2
stringVar = "This is a string variable"
booleanVar = True
list = [0, 1, "two", 3.2, False]
tuple = (0, 1, 2)
dictionary = {"one" : 1, "two" : 2}

print(integerVar)
print(floatVar)
print(stringVar)
print(booleanVar)
print(list)
print(tuple)
print(dictionary)

# What happens when we re-declare an integer variable to String
integerVar = "change"
print (integerVar)

# How to access a member of Sequence
print(list[2])
print(tuple[1])
# How to get the parts of a sequence using slices
print(list[1:4:2])
# How to reverse a sequence using slices
print(list[::-1])

# How to access dictionaries with keys
print(dictionary["one"]) 

# NOTE: cannot combine variables of different types
#print ("string type " + 123)
print ("string type " + str(123))

# Understanding GLOBAL vs local variables in functions
def newFunction():
    #global stringVar
    stringVar = "def"
    print (stringVar)

newFunction()
print (stringVar) 

#del stringVar
print (stringVar)

