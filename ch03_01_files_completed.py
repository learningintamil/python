#
# Learning in Tamil - Python 
# Example file - Files
#

def main():
    # Open file --> write data and create new if it doesn't exist
 
    myFile = open("newTextFile.txt","w+")
    
    # Open file --> append text to the end
    # myFile = open("newTextFile.txt","a+")

    # write lines of data to the file
    for i in range(10):
        myFile.write("This is appended line number %d\n" % (i+1))
    
    # close the file after completing IO operation
    myFile.close()
    
    # Open file --> read the contents
    myFile = open("newTextFile.txt","r")
    if myFile.mode == 'r': # to make sure that the file was opened in read mode
        
        # fileContents = myFile.read()
        # print (fileContents)
      
        allLines = myFile.readlines() # readlines reads the individual lines into a list
        for line in allLines:
            print (line)
    
if __name__ == "__main__":
    main()
