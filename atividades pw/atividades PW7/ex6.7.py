import shutil
import os

def filerename():

    myfile = input("Write the file name:")

    base, extension = os.path.splitext(myfile)
    newfile = base + ".copy"

    shutil.copyfile(myfile, newfile)



filerename()