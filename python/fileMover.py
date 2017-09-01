# def fileMover():
"""Program moves text files to another directory."""
    # **************************************************************************************
    # Python:   2.7.13
    # Filename: fileMover.py
    # Author:   Laurette Roy
    # Purpose:  This program moves all .txt files from one folder to another
    #           with the click of a button (F5). The filepath is printed
    #           to the shell after move. Files are removed from A after move.            
    #            Assumptions: both folders are on desktop, & both directories exist.
    #           named Folder A, Folder B
    #            Use: 2.7.x, shutil module, run in shell, use IDLE
    # test platform: Win7
    #
    #           This program is an exercise for the python module of the Tech Academy bootcamp, Aug 2017.
    # ***************************************************************************************
import shutil
import os
import glob
source = 'c:/Users/Student/Desktop/Folder A'
destination = 'c:/Users/Student/Desktop/Folder B'
def start():
    os.chdir(source)
    print "Source directory is: ", os.getcwd()   # Would you like to change directories?"
    print "The contents of ", source, 'are: \n', os.listdir(source)
    print "The contents of ", destination, 'are: \n', os.listdir(destination)
    confirm()

def confirm():
    print("Are you sure you'd like to move the contents of Folder A to Folder B?")
    answer = raw_input("\n y/n ")
    choice(answer)
    
def choice(answer):
    if answer == 'y':   # if choose to copy files, proceed
        fileMove()      
    elif answer == 'n':     #if they choose no, quit program
        pass
    else:
        print("\nYour choices are 'y' for 'YES', or 'n' for 'NO'. ")
        confirm()

def fileMove():
    try:
        files = os.listdir(source)
        print "The contents of ", source, 'are: \n', files 
        for f in glob.iglob(os.path.join(source, "*.txt")):
            if os.path.isfile(f):
                print f
                shutil.copy2(f, destination)
                os.remove(f)
        print "The contents of ", source, 'are now: \n', os.listdir(source)
        print "The contents of ", destination, 'are now: \n', os.listdir(destination)
    except Exception, e:
        print repr(e)

        
if __name__=='__main__':
    start()
