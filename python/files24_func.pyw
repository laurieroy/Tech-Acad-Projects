#!/usr/local/bin/python3
"""Function list to go with files24_main.py."""

import files24_gui, files24_main
from tkinter import filedialog, messagebox
from tkinter import Tk, Button, LEFT, YES, BOTH, Frame
import tkinter as tk
import shutil, os, glob, datetime

initial_dir =  'c:/Users/Student/Desktop/Folder A'  # change these paths to local dirs 
initial_dest = 'c:/Users/Student/Desktop/Folder B/'

def center_window(self, w, h):  # pass in the tkinter frame(master) ref and w & h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coords to paint the app centered on the user's screen
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}').format(w, h, x, y)
    return centerGeo
 
"""
cut this from main
    try:
        self.entry_from.insert(0, str(initial_dir)) # good to add in gets for these so if people type in instead of browse
        self.entry_to.insert(0, str(initial_dest))
    except IOError:
        print >> sys.stderr, "No such file" , x  # not really needed as only printing path on screen so no fail
"""        
def Get_fileInfo(self):
    """Get file type and age period."""
    global file_type, file_age
    hrs= int(self.txt_fileAge.get())
    file_age = datetime.timedelta(hours=hrs) 
    file_type = str(self.txt_fileType.get()) # not working for this. add in strip
    Get_Source(self)
   
def Get_Source(self): 
    """Gets path to source directory, generates filelist."""
    source_directory = filedialog.askdirectory(initialdir = initial_dir, title="Select source folder")
    global source
    source = source_directory 
    self.txt_srcPath.delete(0, 'end')
    self.txt_srcPath.insert(0, str(source_directory))
    global filenames_list
    filenames_list = []
    for f in glob.iglob(os.path.join(source, file_type)):
        if os.path.isfile(f):
            filenames_list.append(f)
    Get_Dest(self)
     
def Get_Dest(self):
    destination_directory  = filedialog.askdirectory(initialdir = initial_dest, title="Select destination folder")
    global destination
    destination = destination_directory
    self.txt_destPath.delete(0, 'end')
    self.txt_destPath.insert(0, str(destination_directory))
    checkFiles(self)

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
    for f in filenames_list:
        if os.path.isfile(f):
            lastmod_date = datetime.datetime.fromtimestamp(os.path.getmtime(f))
            mdate_filenames_tuple = lastmod_date, f
            mdate_filenames_list.append(mdate_filenames_tuple)
          
            if now - lastmod_date < file_age:
               
                #print ("{} was last modified on {:%a %b %d %Y, %H:%M:%S, %Z}. Moving to 'destinaiton' transfer folder.".format(f, lastmod_date))
                last24.append(f)
                shutil.copy2(f, destination)

    messagebox.showinfo(title="Files Transferred Confirmation", message="Files transferred to destination folder.")
    clear(self)
    ask_quit(self)
    
def clear(self):
    self.txt_srcPath.delete(0, 'end')
    self.txt_destPath.delete(0, 'end')
    self.txt_fileAge.delete(0, 'end')
    self.txt_fileType.delete(0, 'end')
    
if __name__ == "__main__":
    pass
