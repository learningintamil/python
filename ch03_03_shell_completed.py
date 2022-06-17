#
# Learning in Tamil - Python 
# Example file - filesystem shell methods
#

import shutil
from shutil import make_archive
from zipfile import ZipFile
import os
from os import path

def main():
    # How to duplicate an existing file
    if path.exists("newTextFile.txt"):
        # current directory path of the file
        sourceFile = path.realpath("newTextFile.txt")
            
        # append "bak" to the source file name
        destinationFile = sourceFile + ".bak" 
        print(sourceFile)
        print(destinationFile)
        # make a copy using the shutil
        shutil.copy(sourceFile,destinationFile)

        # rename the source file
        if not os.path.exists("newTextFileRenamed.txt") :
            os.rename("newTextFile.txt", "newTextFileRenamed.txt")

        shutil.copy(destinationFile,sourceFile)
        
        # add files to a ZIP archive
        source_directory,filename = path.split(sourceFile)
        print(source_directory)
        print(filename)
        shutil.make_archive("archive", "zip", source_directory)

        with ZipFile("customZip.zip","w") as newzip:
             newzip.write("newTextFile.txt.bak")
             newzip.write("newTextFileRenamed.txt")
      
if __name__ == "__main__":
    main()
