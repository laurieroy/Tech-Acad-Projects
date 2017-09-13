#!/usr/local/bin/python3

# *******************************************************************************
# Python:   3.6.2
# Filename: UI_xferFiles24.py  Daily File Transfer scripting project
# Author:   Laurette Roy
# Purpose: Drill 6, PyDrill_gui_34_idle
#           Title: UI for File Transfer project - Python 3.4 - IDLE
#       Scenario: You recently created a script that will check a folder for new or modified files,
#       and then copy those new or modified files to another location.
#       Users are asking for a user interface to make using the script easier and more versatile.
#       Desired features of the UI:
#       - Allow the user to browse to and choose a specific folder that will contain the
#       files to be checked daily.
#       - Allow the user to browse to and choose a specific folder that will receive the
#       copied files.
#       - Allow the user to manually initiate the 'file check' process that is performed by
#       the script.
#       You have been asked to create this UI.
#       Guidelines:
#       - Use Python 3.4 for this drill.
#       - Use tkinter to create the UI.
#       - The layout of the UI is up to you.
#       - You should use IDLE for this Drill.
# ******************************************************************************
from tkinter import *
from tkinter import ttk, messagebox, filedialog, constants
import shutil, os, glob, datetime
import tkinter as tk
import files24_func
import files24_gui as gui


class ParentWindow(Frame):
    """Create GUI structure. """

    def __init__(self, master):
        Frame.__init__(self, master)
        # Create the GUI:
        self.master = master
        self.master.minsize(500,400) #(Height, Width)
        self.master.maxsize(500,400)
        
        #files24_func.center_window(self, 500, 400)
        
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on windows OS. Maybe do an if or something.
        self.master.protocol("WM_DELETE_WINDOW", lambda: files24_func.ask_quit(self))

        self.master.title('File Transfer Browser')
        self.master.resizable(False, False)

        gui.load_gui(self)
         
if __name__ == "__main__":
    
    root = Tk()
    browse = ParentWindow(root)
    root.mainloop()
