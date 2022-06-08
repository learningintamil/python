#
# Learning in Tamil - Python 
# Example file - Files
#

def main():  
    # Open a file for writing (it will be created when not exists)
    f = open("textfile.txt","w+")
    
    # Open the file to append text to the end
    # f = open("textfile.txt","a+")

    # write data to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    
    # finally close the file.
    f.close()
    
    # Open the file and read the contents
    f = open("textfile.txt","r")
    if f.mode == 'r': # check the file was opened
        # read() function can read the entire file
        # contents = f.read()
        # print (contents)
      
        fl = f.readlines() # readlines --> individual lines into a list
        for x in fl:
            print (x)
    
if __name__ == "__main__":
    main()
