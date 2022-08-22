#
# Learning in Tamil - Python 
# Example file - os.path
#

import os
from os import path
import datetime
import platform
from datetime import date, time, timedelta
import time

def main():
    # get the name of the OS
    print (os.name)
    print(platform.system() )
    
    # Check for a file existence
    print ("File exists?: " + str(path.exists("newTextFile.txt")))
    print ("Is it a file?: " + str(path.isfile("newTextFile.txt")))
    print ("Is it a directory?: " + str(path.isdir("newTextFile.txt")))
    
    # file paths
    print ("Path of the File: " + str(path.realpath("newTextFile.txt")))
    filepath, filename = path.split(path.realpath("newTextFile.txt"))
    print ("Filepath: " + filepath + " Filename: " + filename)
    
    # modification time
    timestamp = path.getmtime("newTextFile.txt")
    print(timestamp)
    convertedTime = time.ctime(timestamp)
    print(convertedTime)
    
    print (datetime.datetime.fromtimestamp(path.getmtime("newTextFile.txt")))
    
    # get file modified date
    timeDifference= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("newTextFile.txt"))
    print ("It has been " + str(timeDifference) + " since the file was modified")
    print ("Or, " + str(timeDifference.total_seconds()) + " seconds")

if __name__ == "__main__":
    main()
