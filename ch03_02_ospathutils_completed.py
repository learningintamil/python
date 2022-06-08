#
# Learning in Tamil - Python 
# Example file - os.path
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # get the name of the OS
    print (os.name)
    
    # Check for a file existence
    print ("Item exists: " + str(path.exists("textfile.txt")))
    print ("Item is a file: " + str(path.isfile("textfile.txt")))
    print ("Item is a directory: " + str(path.isdir("textfile.txt")))
    
    # file paths
    print ("Item's path: " + str(path.realpath("textfile.txt")))
    print ("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))
    
    # modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print (t)
    print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
    
    # get file modified date
    td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print ("It has been " + str(td) + " since the file was modified")
    print ("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
    main()
