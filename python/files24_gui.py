#!/usr/local/bin/python3
"""THIS IS THE GUI SETUP for use with files24_main.py """

from tkinter import *
import tkinter as tk

import files24_func, files24_main

def load_gui(self):

    initial_dir =  'c:/Users/Student/Desktop/Folder A'  
    initial_dest = 'c:/Users/Student/Desktop/Folder B/'
    fileage = '24'
    filetype ='*.txt'
    """
    self.lbl_header = tk.Label(self.master, font = 'bold', text = "Select files for transfer to HQ!")
    self.lbl_header.grid(row=0, column=0, columnspan=2) 
    self.lbl_subheadertk.Label(self.master, "Fill in all blanks before pressing button.")
    self.lbl_subheader.grid(row = 1, column =0, pady=(10))
    """
    # create labels
    self.lbl_srcPath = tk.Label(self.master, text='Source Path:')
    self.lbl_srcPath.grid(row=2, column=1, padx=(15), pady=(10), sticky=N + W)
    self.lbl_destPath = tk.Label(self.master, text='Destination Path:')
    self.lbl_destPath.grid(row=5, column=1, padx=(15), pady=(10), sticky=N + W)
    self.lbl_fileAge = tk.Label(self.master, text='File Age (hours):')
    self.lbl_fileAge.grid(row=6, column=1, padx=(15), pady=(10), sticky=N + W)
    self.lbl_fileType = tk.Label(self.master, text='File Type: (*. for all files) ')
    self.lbl_fileType.grid(row=7, column=1, padx=(15), pady=(10), sticky=N + W)
    
    # create and place one line entry
    self.txt_srcPath = tk.Entry(self.master, width= 40, text='')
    self.txt_srcPath.grid(row=2, column=1, rowspan=1, columnspan=3, padx=(30,40), pady=(30), sticky=N + E + W)
    self.txt_destPath = tk.Entry(self.master, text='')
    self.txt_destPath.grid(row=5, column=1, rowspan=1, columnspan=3,padx=(30,40), pady=(30), sticky=N + E + W)
    self.txt_fileAge = tk.Entry(self.master, width=5, text='')
    self.txt_fileAge.grid(row=6, column=1, padx=(30, 10), pady=(30), sticky=N + E + W)
    self.txt_fileType = tk.Entry(self.master, width=5, text='')
    self.txt_fileType.grid(row=7, column=1, padx=(30, 10), pady=(30), sticky=N + E + W)
    
    # insert defaults
    self.txt_srcPath.insert(0, str(initial_dir)) 
    self.txt_destPath.insert(0, str(initial_dest))
    self.txt_fileAge.insert(0, str(fileage))
    self.txt_fileType.insert(0, str(filetype))

    # create and place buttons
    """
    self.btn_checkFiles = tk.Button(self.master, width=14, height=2, bg='green', text='Check Files',
                             command=lambda: files24_func.checkFiles(self))
    self.btn_checkFiles.grid(row=4, column=0, padx=(15, 0),  rowspan=2, sticky=W)
    self.btn_selectSource = tk.Button(self.master, width=14, height=2,
                                text='Select Source', command=lambda: files24_func.Get_Source(self))
    self.btn_selectSource.grid(row=0, column=0, padx=(15, 0), pady=(15, 10), sticky=W)
    self.btn_selectDest = tk.Button(self.master, width=14, height=2,text='Select Destination', command=lambda: files24_func.Get_Dest(self))
    self.btn_selectDest.grid(row=3, column=0, padx=(15, 0), pady=(25, 10), sticky=W)

    self.btn_close = tk.Button(self.master, width=14, height=2, text='Close', bg='red', command=lambda: files24_func.ask_quit(self)) #rowspan=2,
    self.btn_close.grid(row=4, column=3, padx=(15, 0), pady=(15, 10), rowspan=2, sticky=E)
    
    self.btn_clear =tk.Button(self.master, text='Clear', command= files24_func.clear(self))
    self.btn_clear.grid(row=6, column=1, padx=5, pady=5, sticky='se') 
    """
    self.btn_xferFiles = tk.Button(self.master, width=14, height=2,text='Transfer Files', bg='green', command=lambda: files24_func.Get_fileInfo(self))
    self.btn_xferFiles.grid(row=6, column=0, padx=(15, 0), pady =(15, 10),rowspan=2, sticky=W)
    self.btn_close = tk.Button(self.master, width=14, height=2, text='Close', bg='red', command=lambda: files24_func.ask_quit(self)) #rowspan=2,
    self.btn_close.grid(row=6, column=3, padx=(15, 0), pady=(15, 10), rowspan=2, sticky=E)


    if __name__ == "__main__":
          pass
