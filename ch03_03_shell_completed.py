#
# Learning in Tamil - Python 
# Example file - filesystem shell methods
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # create duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path of the file in the current directory
        src = path.realpath("textfile.txt");
            
        # create a backup copy "bak" 
        dst = src + ".bak"
        # creates copy of the file
        shutil.copy(src,dst)
        
        # rename the original file
        os.rename("textfile.txt", "newfile.txt")
        
        # add files to ZIP archive
        root_dir,tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        # ZIP file handling
        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")
      
if __name__ == "__main__":
    main()
