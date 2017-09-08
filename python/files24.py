#!/usr/local/bin/python2.7
def main():
    """Program moves text files modified in previous 24hrs to another directory."""
        # **************************************************************************************
        # Python:   2.7.13
        # Filename: files24.py  Daily File Transfer scripting project
        # Author:   Laurette Roy
        # Purpose:  This program copies all .txt files that were modified within the
        #           previous 24 hrs from one folder to another (held in destination folder) where
        #           they are then transferred to the home office.
        #           You should create two folders; one to hold the files that get
        #           created or modified throughout the day, and another to receive
        #           the folders that your script determines should be copied over
        #           daily ('destination').
        #            To aid in your development efforts, you should create .txt files 
        #           to add to the first folder.  You should use files that you can
        #           edit, so that you can control whether they are meant to be detected
        #           as 'modified in the last 24 hours' by your program.
        #            Not working for case where file is in subdirectories.
        #            Assumptions: both folders are on desktop, & both directories exist.
        #           named Folder A, Folder B
        #            Use: 2.7.x, shutil module, run in shell, use IDLE
        # test platform: Win7
        #
        #           This program is an exercise for the python module of the Tech Academy
        #            bootcamp, Aug/Sep 2017.
        # ***************************************************************************************
    
    import shutil
    import os
    import glob
    import datetime
    import pytz

    def files24():
   
        status = 0
        
    source = 'c:/Users/Student/Desktop/Folder A'
    destination = 'c:/Users/Student/Desktop/Folder B'
    pacific = pytz.timezone("US/Pacific")
    dateformat = "%a %b %d %Y, %H:%M:%S, %Z "

    os.chdir(source)
    print "Source directory is: ", os.getcwd()   
    print "The contents of ", source, 'are: \n', os.listdir(source)
    print "The contents of ", destination, 'are: \n', os.listdir(destination)

    filenames_list = []
    subdirectories_list = []
    directories_list = []
    mdate_filenames_list = []
    mdate_filenames_tuple = {}
    last24 = []

    now = datetime.datetime.now(tz=pacific)
    file_age = datetime.timedelta(hours=24) # if want different age, change this line
    file_type = "*.txt"                     # and change this one for different file types

    for f in glob.iglob(os.path.join(source, file_type)):
        if os.path.isfile(f):
            filenames_list.append(f)
            lastmod_date = datetime.datetime.fromtimestamp(os.path.getmtime(f), tz=pacific)
            mdate_filenames_tuple = lastmod_date, f
            mdate_filenames_list.append(mdate_filenames_tuple)
            #print "lastmod_date:", lastmod_date
            if now - lastmod_date < file_age:
                print "{} was last modified on {:%a %b %d %Y, %H:%M:%S, %Z}. Moving to 'destinaiton' transfer folder.".format(f, lastmod_date)
                last24.append(f)
                shutil.copy2(f, destination)

        elif os.path.isdir(f):
            print 'in is dir'
            directories_list.append(f)
        #else: see if need to separate out subdirectories. if yeah, then if relative.startswith(os.pardir):or see ideasman42 is_subdir funct
    #print "The contents of ", source, 'are now: \n', os.listdir(source)
    print "The contents of ", destination, 'are now: \n', os.listdir(destination)

if __name__ == "__main__":
    main()
