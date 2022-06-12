#
# Learning in Tamil - Python 
# Example file - loops
#

def main():
    x = 0
    
    # while loop
    while (x < 8):
        print(x)
        x = x + 1

    # for loop
    for x in range(8,12):
        print (x)
      
    # using for loop with a collection
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    for month in months:
        print (month)
    
    # break and continue statements usage in loops
    for x in range(8,12):
        #if (x == 10): break
        if (x == 10): continue
        print (x)
    
    # enumerate() function usage to get index 
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    for index, month in enumerate( months):
        print (index, month)    
  
if __name__ == "__main__":
    main()
