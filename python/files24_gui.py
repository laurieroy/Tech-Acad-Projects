#!/usr/local/bin/python3
"""THIS IS THE GUI SETUP for use with files24_main.py """

from tkinter import *
import tkinter as tk
import sqlite3
import files24_func, files24_main

def load_gui(self):

    initial_dir =  'c:/Users/Student/Desktop/Folder A'  
    initial_dest = 'c:/Users/Student/Desktop/Folder B/'
    fileage = '24'
    filetype ='*.txt'

    # create labels
    self.lbl_srcPath = tk.Label(self.master, text='Source Path:')
    self.lbl_srcPath.grid(row=4, column=1, padx=(15), pady=(10), sticky=N + W)
    self.lbl_destPath = tk.Label(self.master, text='Destination Path:')
    self.lbl_destPath.grid(row=5, column=1, padx=(15), pady=(10), sticky=N + W)
    self.lbl_fileAge = tk.Label(self.master, text='File Age (hours):')
    self.lbl_fileAge.grid(row=2, column=1, padx=(15), pady=(10), sticky=N + W)
    self.lbl_fileType = tk.Label(self.master, text='File Type: (*.txt for all text files) ')
    self.lbl_fileType.grid(row=1, column=1, padx=(15), pady=(10), sticky=N + W)
    self.lbl_lastRun = tk.Label(self.master, text='Time of Previous Transfer: ')
    self.lbl_lastRun.grid(row=0, column=1, padx=(15), pady=(10), sticky=N + W)
    # create and place one line entry
    self.txt_srcPath = tk.Entry(self.master, width= 40, text= '')
    self.txt_srcPath.grid(row=4, column=1, rowspan=1, columnspan=3, padx=(30,40), pady=(30), sticky=N + E + W)
    self.txt_destPath = tk.Entry(self.master, text= '')
    self.txt_destPath.grid(row=5, column=1, rowspan=1, columnspan=3,padx=(30,40), pady=(30), sticky=N + E + W)
    self.txt_fileAge = tk.Entry(self.master, width=5, text= '')
    self.txt_fileAge.grid(row=2, column=1, padx=(30, 10), pady=(30), sticky=N + E + W)
    self.txt_fileType = tk.Entry(self.master, width=5, text= '')
    self.txt_fileType.grid(row=1, column=1, padx=(30, 10), pady=(30), sticky=N + E + W)
    self.txt_lastRun = tk.Entry(self.master, width=20, text='')
    self.txt_lastRun.grid(row=0, column=1, padx=(30, 10), pady=(30), sticky=N + E + W)
    

    # create and place buttons # need to change order if want tab to work load_defaults(self)
    self.btn_lastXfer = tk.Button(self.master, width=14, height=2,text='See Time', command=lambda: files24_func.last_run(self))
    self.btn_lastXfer.grid(row=0, column=0, padx=(15, 0), pady=(25, 10), sticky=W)

    self.btn_help =tk.Button(self.master, width=14, height=2, text='Help', command= lambda: files24_func.help(self))
    self.btn_help.grid(row=0, column=2, padx=(15, 0), pady=(15, 10), sticky='se')

    self.btn_clear =tk.Button(self.master, width=14, height=2,text='Clear', command= lambda: files24_func.clear(self))
    self.btn_clear.grid(row=1, column=2, padx=(15, 0), pady=(15, 10), sticky='se')

    self.btn_updateInfo = tk.Button(self.master, width=14, height=2,text='Update File Info', command=lambda: files24_func.Get_fileInfo(self))
    self.btn_updateInfo.grid(row=1, column=0, padx=(15, 0), pady=(15, 10), sticky=W)

    self.btn_loadDefaults = tk.Button(self.master, width=14, height=2,text='Load Defaults', command=lambda: files24_func.load_defaults(self))
    self.btn_loadDefaults.grid(row=2, column=2, padx=(15, 0), pady=(15, 10), sticky=W)   

    self.btn_selectSource = tk.Button(self.master, width=14, height=2,
                                text='Select Source', command=lambda: files24_func.Get_Source(self))
    self.btn_selectSource.grid(row=4, column=0, padx=(15, 0), pady=(15, 10), sticky=W)

    self.btn_selectDest = tk.Button(self.master, width=14, height=2,text='Select Destination', command=lambda: files24_func.Get_Dest(self))
    self.btn_selectDest.grid(row=5, column=0, padx=(15, 0), pady=(25, 10), sticky=W)

    self.btn_checkFiles = tk.Button(self.master, width=14, height=2, bg='green', text='Check Files',
                             command=lambda: files24_func.checkFiles(self))
    self.btn_checkFiles.grid(row=7, column=0, padx=(15, 0), pady=(15, 10), sticky=W), 
    
    self.btn_close = tk.Button(self.master, width=14, height=2, text='Close', bg='red', command=lambda: files24_func.ask_quit(self)) 
    self.btn_close.grid(row=7, column=2, padx=(15, 0), pady=(15, 10), rowspan=2, sticky=E)
   
    
    

    if __name__ == "__main__":
        pass
