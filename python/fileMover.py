# fileMover.py
"""Program copies text files to another directory."""
# **************************************************************************************
# Python:   2.7.13
# Author:   Laurette Roy
# Purpose:  This program moves all .txt files from one folder to another
#           with the click of a button. The filepath is printed
#           to the shell after move. Files are removed from A after move.            
#            Assumptions: both files are on desktop, both directories exist.
#           named Folder A, Folder B
#           Use: 2.7.x, shutil module, run in shell, use IDLE
# test platform: Win7
#
#           This program is an exercise for the python module of the Tech Academy bootcamp, Aug 2017.
# ***************************************************************************************
import tkinter
import shutil
import os

# display in gui files in dir A, dir B.
# move file xyz
# make GUI with button to move files or
# Ask user if ready to move files from Folder A to Fodler B 'y'<enter>

source = 'c:/Users/Student/Desktop/Folder A'
destination = 'c:/Users/Student/Desktop/Folder B'

print os.getcwd()
os.chdir(source)
print os.getcwd()
# moveFiles = confirm()
print("Type confirm() <enter> to start dialogue.")
def confirm():
    print("Are you sure you'd like to move the contents of Folder A to Folder B?")
    answer= raw_input("\n y/n ")
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
        print("The contents of ", source, 'are: \n', os.listdir(source))
        for files in source:
            if files.endswith(".txt"):
                shutil.move(files,destination)
    except:
        print(shutil.Error)
