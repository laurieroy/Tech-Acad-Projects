#!/usr/local/bin/python3
"""Function list to go with files24_main.py."""

import files24_gui, files24_main
from tkinter import filedialog, messagebox
import tkinter as tk
import shutil, os, glob, datetime, sqlite3, time

initial_dir =  'c:/Users/Student/Desktop/Folder A'  
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
        create_db(self)
    except NameError:
        #messagebox(title='', text='')
        pass
    
def help(self):
    messagebox.showinfo(title="Files Transfer Browser Information", message="To see time of last "
                        "file transfer, press 'See Time'\n Buttons must be pressed in the order: "
                        "Update info/ Source / Destination / Check. Select Source and Destination "
                        "buttons to browse to a new folder (directory) location. Note: subdirectories"
                        "must be done separately.\n 'Update info' adds in the the time period in hours "
                        " and filetype that is being searched.\n 'Clear' will reset the fields, which "
                        "can then be re-entered. \nYou may close out the app by selecting 'close' or the window's x. ")
    
def Get_fileInfo(self):
    """Get file type and age period."""
    global file_age, file_type, hrs
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
    global files_list
    files_list = []
    global ft_list
    ft_list = []
    for f in glob.iglob(os.path.join(source, file_type)):
        files_list = [os.path.splitext(f)[0]]
        filenames_list.append(f) 
       
def clean_file(filesnames_list, file_type):  # so now not needed.
    """Clean out char from s."""
    global files_list
    files_list = []
    global ft_list
    ft_list = []
    for line in filesnames_list:
        s, fileType = line.split('.') # split off file_type here
        print(s)
        files_list.append(s)
        ft_list.append(fileType)
    print(files_list)
    return (files_list)   
     
def Get_Dest(self):
    destination_directory  = filedialog.askdirectory(initialdir = initial_dest, title="Select destination folder")
    global destination
    destination = destination_directory
    self.txt_destPath.delete(0, 'end')
    self.txt_destPath.insert(0, str(destination_directory))

def create_db(self):
    with sqlite3.connect('fileTransfer.db') as connection:
        c=connection.cursor() # This assume time has been converted to seconds since epoch
        c.execute('CREATE TABLE if not exists tbl_lastRun( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_timestamp INT, \
                col_source TEXT, \
                col_destination TEXT, \
                col_file_type TEXT, \
                col_file_age INT \
                );')
        # You must commit() to save changes & close the database connection
        connection.commit()
    connection.close()
    test_run(self)
# *************************
# from Dan's code:
def test_run(self):
    data=('145123542'), ('initial_dir'), ('initial_dest'), ('initial_filetype'), ('hrs')
    with sqlite3.connect('fileTransfer.db') as connection:
        c=connection.cursor()
        c, count=count_records(cur)
        if count < 1:
            c.execute(
                '''INSERT INTO tbl_lastRun (col_timestamp, col_source, col_destination, col_file_type, col_file_age) VALUES (?,?,?,?,?)''',  ('145123542', 'source', 'destination', 'file_type', 'hrs'))
            connection.commit()
        connection.close
# from Dan's code:
def count_records(cur):
        count=''
        c.execute('''SELECT COUNT(*) FROM tbl_lastRun''')
        count=c.fetchone()[0]
        return c, count

def last_run(self):
    """Get time of last file backup."""
    with sqlite3.connect('fileTransfer.db') as connection:
        c = connection.cursor()
        cursor = c.execute('SELECT max(id) FROM tbl_lastRun')    
        max_id = cursor.fetchone()[0]
        cursor = c.execute('SELECT col_timestamp FROM tbl_lastRun')
        #timeLastRun = cursor.fetchone()[0]
        tLR_str = time.strftime('%Y-%m-%d %H:%M %z', time.localtime(cursor.fetchone()[0])) 
        self.txt_lastRun.delete(0, 'end')
        self.txt_lastRun.insert(0, tLR_str)

  

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
    noise,ft = file_type.split('.')
    ## note can do an entry bg color stoplight thing >24 hrs = red,  12-24 hrs = yellow < 12 = green nice little if loop
    for f in filenames_list:
        if os.path.isfile(f):
            lastmod_date = datetime.datetime.fromtimestamp(os.path.getmtime(f))
            mdate_filenames_tuple = lastmod_date, f
            mdate_filenames_list.append(mdate_filenames_tuple)
          
            if now - lastmod_date < file_age:
                
                #print ("{} was last modified on {:%a %b %d %Y, %H:%M:%S, %Z}. Moving to 'destinaiton' transfer folder.".format(f, lastmod_date))
                last24.append(f)
                shutil.copy2(f, destination)
                xferTime=time.time()
                
                fa = str(file_age) 
                with sqlite3.connect('fileTransfer.db') as connection:
                    c = connection.cursor()
                    c.execute("INSERT INTO tbl_lastRun(col_timestamp, col_source, col_destination, col_file_type, col_file_age) VALUES (?,?,?,?,?)",(xferTime, source, destination, ft, hrs))
                    connection.commit()
                connection.close   

    clear(self)
    ask_quit(self)
    
def clear(self):
    self.txt_lastRun.delete(0, 'end')
    self.txt_srcPath.delete(0, 'end')
    self.txt_destPath.delete(0, 'end')
    self.txt_fileAge.delete(0, 'end')
    self.txt_fileType.delete(0, 'end')
    
if __name__ == "__main__":
    pass
