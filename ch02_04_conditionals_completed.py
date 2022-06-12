#
# Learning in Tamil - Python 
# Example file - conditional statements
#

def start():
    x, y = 20, 200

    # How to use if, elif and else 
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x equals to y"
    else:
        result = "x is greater than y"
    print(result)

    # How to use conditional statement
    result = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(result)

    # How match-case helps for multiple comparisons
    caseNumber  = 1
    match caseNumber:
        case 1:
            result = "one"
        case 2:
            result = "two"
        case 3 | 4:
            result = "three or four"
        case _:
            result = "default"
    print(result)

if __name__ == "__main__":
    start()
