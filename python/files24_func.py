#!/usr/local/bin/python3
"""Function list to go with files24_main.py."""

import files24_gui, files24_main
from tkinter import filedialog, messagebox
from tkinter import Tk, Button, LEFT, YES, BOTH, Frame
import tkinter as tk
import shutil, os, glob, datetime, sqlite3

initial_dir =  'c:/Users/Student/Desktop/Folder A'  # change these paths to local dirs 
initial_dest = 'c:/Users/Student/Desktop/Folder B/'
initial_fileage = 24
initial_filetype = '*.txt'

def load_defaults(self):
    """load default values."""
    try:
        self.txt_srcPath.insert(0, str(initial_dir)) 
        self.txt_destPath.insert(0, str(initial_dest))
        self.txt_fileAge.insert(0, str(initial_fileage))
        self.txt_fileType.insert(0, str(initial_filetype))
    except NameError:
        messagebox(title='', text='')

def help(self):
    messagebox.showinfo(title="Files Transfer Browser Information", message="To see time of last file transfer, press 'Check Time'\n"
                        "Select Source and Destination buttons to browse to a new folder (directory) location. Note: subdirectories"
                        "must be done separately.\n 'Update info' adds in the the time period in hours and filetype"
                        "that is being searched.\n 'Clear' will reset the fields, which can then be re-entered. \nYou may close out the "
                        "app by selecting 'close' or the window's x. ")
    
def Get_fileInfo(self):
    """Get file type and age period."""
    global file_age, file_type
    hrs= int(self.txt_fileAge.get())
    file_age = datetime.timedelta(hours=hrs)
    file_type = self.txt_fileType.get()
    messagebox.showinfo(title="Run select source again.", message = "After updating file type or hours, please select source again to update file selection.")
 
   
def Get_Source(self): 
    """Get path to source directory, generate filelist."""
    source_directory = filedialog.askdirectory(initialdir = initial_dir, title="Select source folder")
    global source
    source = source_directory 
    self.txt_srcPath.delete(0, 'end')
    self.txt_srcPath.insert(0, str(source_directory))
    file_type = self.txt_fileType.get()
    hrs= int(self.txt_fileAge.get())
    file_age = datetime.timedelta(hours=hrs)
    global filenames_list
    filenames_list = []
    for f in glob.iglob(os.path.join(source, file_type)):
        if os.path.isfile(f):
            filenames_list.append(f)
    
     
def Get_Dest(self):
    destination_directory  = filedialog.askdirectory(initialdir = initial_dest, title="Select destination folder")
    global destination
    destination = destination_directory
    self.txt_destPath.delete(0, 'end')
    self.txt_destPath.insert(0, str(destination_directory))
   

# from Dan's code:    
# FOR MS: catch if the user's click on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)  # clears all widgets out of memory


def checkFiles(self):
    """Check age of selected file types in selected dir. Transfer to destination, and blank fields.""" 
    mdate_filenames_list = []
    mdate_filenames_tuple = {}
    last24 = []
    now = datetime.datetime.now()
    # add in last run time (now)
    for f in filenames_list:
        if os.path.isfile(f):
            lastmod_date = datetime.datetime.fromtimestamp(os.path.getmtime(f))
            mdate_filenames_tuple = lastmod_date, f
            mdate_filenames_list.append(mdate_filenames_tuple)
          
            if now - lastmod_date < file_age:
                #print ("{} was last modified on {:%a %b %d %Y, %H:%M:%S, %Z}. Moving to 'destinaiton' transfer folder.".format(f, lastmod_date))
                last24.append(f)
                shutil.copy2(f, destination)


    clear(self)
    ask_quit(self)
    
def clear(self):
    self.txt_srcPath.delete(0, 'end')
    self.txt_destPath.delete(0, 'end')
    self.txt_fileAge.delete(0, 'end')
    self.txt_fileType.delete(0, 'end')
    
if __name__ == "__main__":
    pass
