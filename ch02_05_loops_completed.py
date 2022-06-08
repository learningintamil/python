#
# Learning in Tamil - Python 
# Example file - loops
#

def main():
    x = 0
    
    # while loop
    while (x < 5):
        print(x)
        x = x + 1

    # for loop
    for x in range(5,10):
        print (x)
      
    # using for loop with a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print (d)
    
    # break and continue statements usage
    for x in range(5,10):
        #if (x == 7): break
        #if (x % 2 == 0): continue
        print (x)
    
    # enumerate() function usage to get index 
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i, d in enumerate(days):
        print (i, d)
  
if __name__ == "__main__":
    main()
